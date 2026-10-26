import json
from datetime import datetime, timedelta, timezone
from types import SimpleNamespace

from ytc import youtube


def _record(folder, short_id, video_id, **extra):
    sent = (datetime.now(timezone.utc) - timedelta(hours=5)).isoformat()
    (folder / short_id).mkdir()
    (folder / short_id / "publish.json").write_text(json.dumps(
        {"id": short_id, "status": "sent", "sent_at": sent, "youtube_url": f"https://www.youtube.com/shorts/{video_id}", **extra}))


def test_a_replaced_short_made_private_is_not_a_problem(tmp_path, monkeypatch):
    _record(tmp_path, "ep001", "AAAAAAAAAAA", replaced_by="BBBBBBBBBBB")
    _record(tmp_path, "ep002", "CCCCCCCCCCC")
    asked = []

    def videos_list(part, id):
        asked.append(id)
        return SimpleNamespace(execute=lambda: {"items": [
            {"id": "CCCCCCCCCCC", "status": {"uploadStatus": "processed", "privacyStatus": "private"}}]})

    monkeypatch.setattr(youtube, "_credentials", lambda: None)
    monkeypatch.setattr(youtube, "build", lambda *a, **k: SimpleNamespace(videos=lambda: SimpleNamespace(list=videos_list)))
    problems = youtube.check_live(tmp_path)
    assert asked == ["CCCCCCCCCCC"]
    assert problems == [{"id": "ep002", "problem": "upload processed, private"}]
