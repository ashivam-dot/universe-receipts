import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from ytc import auto, publish, youtube


def _waiting(n, series=("A", "B", "C")):
    return [{"id": f"ep{900 + i}", "folder": Path(f"/x/ep{900 + i}"), "state": "waiting", "title": f"T{i}",
             "series": series[i % len(series)], "record": None, "held": {"media_url": "u"}, "topic": {}, "remote": None}
            for i in range(n)]


@pytest.fixture
def busy(monkeypatch):
    def set_until(hours):
        monkeypatch.setattr(publish, "_busy_until", datetime.now(timezone.utc) + timedelta(hours=hours))
    yield set_until
    publish._busy_until = None


def test_direct_publishing_only_when_buffer_is_refused_for_long(busy):
    assert not auto.direct_publishing()
    busy(2)
    assert not auto.direct_publishing()
    busy(24 * 4)
    assert auto.direct_publishing()


def test_direct_publish_books_the_next_slots_on_youtube_without_buffer(monkeypatch):
    eps = _waiting(6)
    monkeypatch.setattr(auto, "episodes", lambda: eps)
    monkeypatch.setattr(auto, "slots_per_day", lambda today=None: 2)
    monkeypatch.setattr(publish, "posts", lambda *a, **k: pytest.fail("Buffer was read"))
    monkeypatch.setattr(publish, "schedule", lambda *a, **k: pytest.fail("Buffer was asked to schedule"))
    booked = []

    def direct(spec_path, when):
        booked.append(when)
        return {"due_at": when.isoformat()}

    monkeypatch.setattr(publish, "schedule_direct", direct)
    run = auto.Run("test")
    auto.publish_waiting(run, direct=True)
    now = datetime.now(publish.AUDIENCE_TZ)
    assert 2 <= len(booked) <= 4
    assert len(set(booked)) == len(booked)
    assert all(now < when <= now + auto.DIRECT_AHEAD for when in booked)
    assert all(when.timetz().replace(tzinfo=None) in publish.SLOTS[:2] for when in booked)
    assert all(s["name"].startswith("upload ") and s["ok"] for s in run.stages)


def test_buffer_scheduling_keeps_off_slots_a_direct_upload_holds(monkeypatch):
    now = datetime.now(publish.AUDIENCE_TZ)
    held = publish.next_slots(1, set())[0]
    eps = _waiting(1) + [{"id": "ep899", "folder": Path("/x/ep899"), "state": "scheduled", "title": "D", "series": "A",
                          "record": {"buffer_post_id": None, "direct": True, "due_at": held.isoformat(), "status": "scheduled"},
                          "held": None, "topic": {}, "remote": None}]
    monkeypatch.setattr(auto, "episodes", lambda: eps)
    monkeypatch.setattr(auto, "slots_per_day", lambda today=None: 2)
    monkeypatch.setattr(publish, "posts", lambda *a, **k: [])
    booked = []
    monkeypatch.setattr(publish, "schedule", lambda spec_path, when: booked.append(when) or {"due_at": when.isoformat()})
    auto.publish_waiting(auto.Run("test"))
    assert booked and booked[0] != held and booked[0] > now


def test_settle_direct_marks_public_uploads_sent(monkeypatch, tmp_path):
    past = (datetime.now(timezone.utc) - timedelta(hours=1)).isoformat()
    future = (datetime.now(timezone.utc) + timedelta(hours=5)).isoformat()
    for name, due, vid in (("ep901", past, "aaaaaaaaaaa"), ("ep902", future, "bbbbbbbbbbb"), ("ep903", past, "ccccccccccc")):
        (tmp_path / name).mkdir()
        (tmp_path / name / "publish.json").write_text(json.dumps({
            "id": name, "direct": True, "status": "scheduled", "due_at": due,
            "youtube_url": f"https://www.youtube.com/shorts/{vid}"}))

    class Videos:
        def list(self, part, id):
            assert "bbbbbbbbbbb" not in id
            return type("R", (), {"execute": lambda self: {"items": [{"id": "aaaaaaaaaaa", "status": {"privacyStatus": "public"}}]}})()

    monkeypatch.setattr(youtube, "_credentials", lambda: None)
    monkeypatch.setattr(youtube, "build", lambda *a, **k: type("Y", (), {"videos": lambda self: Videos()})())
    changes = youtube.settle_direct(tmp_path)
    assert changes == ["ep901 sent", "ep903 error"]
    assert json.loads((tmp_path / "ep901" / "publish.json").read_text())["sent_at"]
    assert json.loads((tmp_path / "ep902" / "publish.json").read_text())["status"] == "scheduled"


def test_a_run_reads_buffers_queue_once(monkeypatch):
    reads = []
    monkeypatch.setattr(publish, "youtube_channel_id", lambda: "ch")
    monkeypatch.setattr(publish, "_read_posts", lambda since, channel: reads.append(since) or [
        {"id": "p", "dueAt": datetime.now(publish.AUDIENCE_TZ).isoformat(), "status": "scheduled"}])
    publish.forget_posts()
    now = datetime.now(publish.AUDIENCE_TZ)
    publish.posts(since=now - timedelta(days=30))
    publish.posts(since=now - timedelta(days=3))
    publish.posts(since=now - timedelta(days=30))
    assert len(reads) == 1
    publish.forget_posts()
    publish.posts(since=now - timedelta(hours=1))
    assert len(reads) == 2 and reads[1] > now - timedelta(hours=2)
    publish.forget_posts()


def test_slot_watch_checks_once_after_each_slot_in_use():
    from ytc import cloud

    assert cloud.WATCH_SCHEDULE == "40 19,21 * * *"


def test_buffer_busy_says_the_day():
    assert "Nov 28 18:52" in str(publish.BufferBusy(datetime(2026, 11, 28, 18, 52, tzinfo=timezone.utc)))
