"""The relaunch format (strategy/RELAUNCH.md): host voice, subtitles, and older Shorts kept out of the test."""

import json
import os
import subprocess
import sys
from pathlib import Path

import yaml

from ytc import auto, captions, studio, tts
from ytc.spec import CaptionStyle, ShortSpec

FONTS = Path(__file__).resolve().parents[1] / "assets" / "fonts"
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
    _episode(tmp_path, "ep002", studio.FORMAT)
    monkeypatch.setattr(auto, "EPISODES", tmp_path)
    states = {e["id"]: e["state"] for e in auto.episodes()}
    assert states == {"ep001": "shelved", "ep002": "waiting"}
    assert auto.inventory()["total"] == 1


def test_a_new_spec_carries_the_format_voice_and_subtitles():
    research = {"claims": [{"sources": ["A"]}], "sources": [{"label": "A", "url": "https://a"}],
                "series": "Scale Breaker"}
    script = {"title": "T", "description": "D", "hashtags": ["#space"], "tags": [],
              "beats": [{"text": "One line.", "emphasis": [], "claims": [1]}]}
    spec = ShortSpec.model_validate(studio.spec_from(script, [{"source": "color"}], research, "ep009"))
    assert spec.format == studio.FORMAT
    assert spec.voice.engine == "gemini" and spec.voice.voice != "af_heart"
    assert not spec.captions.karaoke and not spec.captions.uppercase


def test_gemini_never_reads_kokoro_markup():
    assert tts.plain("The moon [Io](/ˈaɪoʊ/) erupts.") == "The moon Io erupts."


def test_subtitles_show_a_phrase_at_a_time_without_lighting_each_word(tmp_path):
    words = [tts.Word(t, i * 0.4, i * 0.4 + 0.35, 0) for i, t in enumerate("Saturn would float in a bathtub.".split())]
    style = CaptionStyle(**studio.CAPTIONS)
    path = tmp_path / "c.ass"
    captions.write_ass(words, style, path, 3.0, {0: {"float"}}, FONTS)
    events = [l for l in path.read_text(encoding="utf-8").splitlines() if l.startswith("Dialogue")]
    assert len(events) < len(words)
    assert "Saturn" in events[0] and "SATURN" not in events[0]


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
