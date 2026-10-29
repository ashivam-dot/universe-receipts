"""The relaunch format (strategy/RELAUNCH.md): Days of Odd's format 2, and older Shorts kept out of the test."""

import json
import os
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest
import yaml
from PIL import Image

from ytc import auto, bed, check, plates, studio, tts, writer
from ytc.spec import ShortSpec

GATE = Path(__file__).resolve().parents[2] / ".github" / "backup_gate.py"


def _episode(root: Path, name: str, fmt: str | None) -> None:
    folder = root / name
    folder.mkdir(parents=True)
    spec = {"id": name, "title": name, "series": "Scale Breaker", "beats": [{"text": "A line."}]}
    if fmt is not None:
        spec["format"] = fmt
    (folder / "short.yaml").write_text(yaml.safe_dump(spec), encoding="utf-8")
    (folder / "hold.json").write_text('{"media_url": "https://example.org/v.mp4"}', encoding="utf-8")


def test_older_finished_shorts_are_shelved_not_ready(monkeypatch, tmp_path):
    _episode(tmp_path, "ep001", None)
    _episode(tmp_path, "ep002", "v2")
    _episode(tmp_path, "ep003", studio.FORMAT)
    monkeypatch.setattr(auto, "EPISODES", tmp_path)
    states = {e["id"]: e["state"] for e in auto.episodes()}
    assert states == {"ep001": "shelved", "ep002": "shelved", "ep003": "waiting"}
    assert auto.inventory()["total"] == 1


def _spec(meta: dict | None = None, series: str = "Mission Files") -> ShortSpec:
    research = {"claims": [{"sources": ["A"]}], "sources": [{"label": "A", "url": "https://a"}], "series": series}
    script = {"title": "T", "description": "D", "hashtags": ["#space"], "tags": [],
              "beats": [{"text": "One line.", "emphasis": [], "claims": [1]}]}
    return ShortSpec.model_validate(studio.spec_from(script, [{"source": "color"}], research, "ep009",
                                                     studio._voice(meta or {})))


def test_a_new_spec_is_days_of_odds_format_2():
    spec = _spec()
    assert spec.format == studio.FORMAT
    assert (spec.voice.engine, spec.voice.voice, spec.voice.speed, spec.voice.max_pause) == \
        ("gemini", "Zubenelgenubi", 1.05, 0.25)
    assert spec.look == "bold" and spec.music.path == "bed:chase" and spec.music.fade_out == 1.0
    assert spec.captions.hook_size == 150 and spec.captions.karaoke


def test_every_series_has_a_bed_mood():
    assert set(studio.MOODS) == set(auto.SERIES)
    assert set(studio.MOODS.values()) <= set(bed.MOODS)


def test_a_mispronounced_word_is_respelled_for_the_voice_only():
    spec = _spec({"say": {"Io": "eye oh"}})
    assert spec.voice.say == {"Io": "eye oh"} and spec.beats[0].text == "One line."


def test_shorts_are_about_thirty_seconds():
    assert (writer.MIN_WORDS, writer.MAX_WORDS) == (65, 95) and check.DURATION == (20, 40)
    beats = [{"text": " ".join(["word"] * 12), "claims": [1], "emphasis": []} for _ in range(4)]
    assert any("65 to 95 spoken words" in p for p in writer.problems({"beats": beats}, {"claims": []}))


def test_the_script_rules_of_format_2():
    beats = [{"text": "In 1970 an oxygen tank blew up on the way to the Moon.", "claims": [1], "emphasis": []},
             {"text": " ".join(["word"] * 15) + ".", "claims": [1], "emphasis": []}]
    found = writer.problems({"beats": beats}, {"claims": []})
    assert any("The hook (beat 1) must be 10 words or fewer" in p for p in found)
    assert any("Beat 1 starts with a year or date" in p for p in found)
    assert any("Beat 2 must be 14 words or fewer" in p for p in found)


def test_gemini_never_reads_kokoro_markup():
    assert tts.plain("The moon [Io](/ˈaɪoʊ/) erupts.") == "The moon Io erupts."


def test_the_bold_look_fills_the_screen_only_from_a_sharp_picture():
    sharp, soft = Image.new("RGB", (2400, 1600), "gray"), Image.new("RGB", (900, 600), "gray")
    filled = plates.fill(sharp, (0.5, 0.5), [0.4, 0.3, 0.6, 0.7])
    assert filled is not None and filled.size == (plates.PW, plates.PH)
    assert plates.fill(soft, (0.5, 0.5), [0.4, 0.3, 0.6, 0.7]) is None
    assert plates.fill(sharp, (0.5, 0.5), []) is None


def test_a_bed_is_composed_for_each_short(tmp_path):
    import soundfile as sf

    path = bed.compose("ep009", 12.0, tmp_path / "bed.wav", "wonder")
    audio, rate = sf.read(path)
    assert abs(len(audio) / rate - 12.0) < 0.5 and np.abs(audio).max() > 0.01


def test_famous_topics_go_first(monkeypatch):
    topics = [{"topic": t, "series": s, "kind": "backlog", "date": None, "status": None}
              for t, s in (("Obscure void", "Scale Breaker"), ("Apollo 13 filter", "Mission Files"))]
    monkeypatch.setattr(auto, "calendar_topics", lambda today=None: topics)
    monkeypatch.setattr(auto, "_available", lambda t, today: True)
    monkeypatch.setattr(auto, "demand", lambda ts: {"Obscure void": 2000, "Apollo 13 filter": 90000})
    monkeypatch.setattr(auto, "_series_shares", lambda: None)
    assert auto.choose_topics(1, [{"id": "ep001", "series": "Scale Breaker"}])[0]["topic"] == "Apollo 13 filter"
    assert auto.choose_topics(1, [{"id": "ep001", "series": "Mission Files"}])[0]["topic"] == "Apollo 13 filter"


def _gate(tmp_path: Path, status: dict) -> str:
    (tmp_path / "status").mkdir(parents=True)
    (tmp_path / "status" / "status.json").write_text(json.dumps(status), encoding="utf-8")
    out = tmp_path / "out"
    subprocess.run([sys.executable, str(GATE)], cwd=tmp_path, env={**os.environ, "GITHUB_OUTPUT": str(out)},
                   check=True, capture_output=True)
    return out.read_text()


def test_the_backup_makes_what_modal_had_no_credit_for(tmp_path):
    from datetime import datetime, timezone

    now = datetime.now(timezone.utc).isoformat()
    fresh = {"updated_at": now, "result": "ok", "run": {"host": "modal"}, "starved": 0}
    assert "skip=true" in _gate(tmp_path / "a", fresh)
    assert "skip=false" in _gate(tmp_path / "b", {**fresh, "starved": 4})
