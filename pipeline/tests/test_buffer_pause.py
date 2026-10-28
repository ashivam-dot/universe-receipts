from datetime import datetime, timedelta

from ytc import auto


def test_buffer_is_paused_until_the_direct_uploads_are_out(monkeypatch):
    monkeypatch.setattr(auto, "_now", lambda: auto.BUFFER_PAUSED_UNTIL - timedelta(minutes=1))
    assert auto.buffer_paused()
    monkeypatch.setattr(auto, "_now", lambda: auto.BUFFER_PAUSED_UNTIL)
    assert not auto.buffer_paused()


def test_the_daily_cap_holds_even_when_the_numbers_earn_more(monkeypatch):
    monkeypatch.setattr(auto, "day_number", lambda today=None: 55)
    monkeypatch.setattr(auto, "_pace_numbers", lambda: ([1000.0] * 10 + [1200.0] * 10, [0.6] * 20))
    monkeypatch.setattr(auto, "_reach_numbers", lambda: [1000.0] * 10 + [1200.0] * 10)
    assert auto.slots_per_day() == 1
    monkeypatch.setattr(auto, "DAILY_CAP", None)
    assert auto.slots_per_day() > 1


def test_a_paused_run_never_touches_buffer(monkeypatch, tmp_path):
    touched = []
    monkeypatch.setattr(auto, "_now", lambda: datetime(2026, 10, 29, 12, 0, tzinfo=auto.IST))
    monkeypatch.setattr(auto, "STATUS", tmp_path)
    for name in ("check_channel", "repair_posts", "preflight_posts", "release_anniversaries", "publish_waiting",
                 "crosspost_scheduled"):
        monkeypatch.setattr(auto, name, lambda *a, _n=name, **k: touched.append(_n))
    run = auto.Run("test")
    monkeypatch.setattr(auto, "Run", lambda trigger: run)

    class Stop(Exception):
        pass

    def stop(*a, **k):
        raise Stop

    monkeypatch.delenv("MODAL_TOKEN_ID", raising=False)
    monkeypatch.setattr(auto, "ON_MODAL", False)
    monkeypatch.setattr(auto, "inventory", lambda eps=None: {"total": 25, "remote": [], "making": []})
    monkeypatch.setattr(auto, "_session_note", stop)
    from ytc import publish, youtube
    monkeypatch.setattr(publish, "sync", lambda content: [])
    monkeypatch.setattr(youtube, "file_into_playlists", lambda content: [])
    monkeypatch.setattr(youtube, "fix_languages", lambda content: [])
    monkeypatch.setattr(youtube, "check_live", lambda content: [])
    monkeypatch.setattr(auto, "review_shorts", lambda run: [])
    monkeypatch.setattr(auto, "daily", lambda *a, **k: None)
    try:
        auto.main(produce_count=0, daily_mode="no")
    except Stop:
        pass
    assert touched == []
    assert any("Buffer is paused" in note for note in run.notes)
