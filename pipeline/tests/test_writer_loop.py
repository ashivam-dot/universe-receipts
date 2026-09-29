from ytc import writer


def _script(last: str) -> dict:
    beats = [{"text": "A Soviet lander kept talking from Venus for 127 minutes.", "claims": [1], "emphasis": ["127 minutes"],
              "queries": ["Venera 13"], "sfx": "none"}]
    beats += [{"text": "It sat on the surface.", "claims": [1], "emphasis": ["surface"], "queries": ["Venus"], "sfx": "none"}] * 5
    beats.append({"text": last, "claims": [], "emphasis": [last.split()[0]], "queries": ["Venera 13"], "sfx": "none"})
    return {"beats": beats, "title": "t", "hashtags": ["#space", "#venus", "#nasa"], "tags": ["a", "b", "c", "d"],
            "description": "One."}


def _loop_problems(last: str) -> list[str]:
    return [p for p in writer.problems(_script(last), {"claims": [{}]}) if "last beat" in p]


def test_dangling_loop_endings_are_rejected():
    for last in ("This saved the program, which began because...", "And it all started when", "It lasted until"):
        assert _loop_problems(last), last


def test_complete_loop_sentence_passes():
    for last in ("It was built to last 32 minutes.", "Nobody expected it to survive."):
        assert not _loop_problems(last), last
