from ytc import auto


def _setup(monkeypatch, key: str | None):
    monkeypatch.setattr(auto, "ON_MODAL", True)
    monkeypatch.setattr(auto, "MODAL_CREDIT", 30.0)
    monkeypatch.setattr(auto, "_modal_cost", lambda: {"metered": 0.0})
    monkeypatch.setattr(auto, "inventory", lambda *a: {"total": 0, "remote": []})
    monkeypatch.setattr(auto, "_spawn", lambda run, jobs: (_ for _ in ()).throw(AssertionError("spawned")))
    monkeypatch.delenv("YTC_STUDIO_HERE", raising=False)
    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)
    if key:
        monkeypatch.setenv("YTC_GEMINI_API_KEY", key)
    else:
        monkeypatch.delenv("YTC_GEMINI_API_KEY", raising=False)


def test_a_run_on_modal_without_the_voice_key_starts_no_workers(monkeypatch):
    _setup(monkeypatch, None)
    assert auto.capacity()["cloud"] == 0


def test_a_run_on_modal_with_the_voice_key_starts_workers(monkeypatch):
    _setup(monkeypatch, "test")
    assert auto.capacity()["cloud"] > 0


def test_shorts_it_cannot_start_are_left_to_the_github_backup(monkeypatch):
    _setup(monkeypatch, None)
    monkeypatch.setattr(auto, "_jobs", lambda n: [{"id": f"ep{i}"} for i in range(n)])
    run = auto.Run("schedule")
    auto.produce(run, 4)
    assert run.starved == 4
