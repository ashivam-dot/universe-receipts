"""The Day 21/30 decisions and reach levers: series shares, rising Shorts, stalled Shorts, the slot test."""

from datetime import date, datetime, timedelta, timezone

from ytc import auto, growth, publish

NOW = datetime(2026, 10, 20, 9, 0, tzinfo=timezone.utc)


def _row(series, views, published="2026-10-10T23:00:00+00:00"):
    return {"series": series, "early_reach": {"hours": 25, "views": views}, "published": published}


def _ranked_rows():
    medians = {"Space Myths, Busted": 1167, "Mission Files": 1033, "Scale Breaker": 948, "Near Misses": 829,
               "Space Got Weird": 708, "The Universe Is Terrifying": 637}
    return [_row(s, v) for s, v in medians.items() for _ in range(auto.SERIES_MEASURED)]


def test_series_reach_ranks_only_series_with_enough_measured_shorts():
    rows = _ranked_rows() + [_row("Space Got Weird", 5000)] + [{"series": "Scale Breaker", "early_reach": None}]
    reach = auto.series_reach(rows[: auto.SERIES_MEASURED * 2] + [_row("Near Misses", 900)])
    assert set(reach) == {"Space Myths, Busted", "Mission Files"}
    assert auto.series_reach(_ranked_rows())["Space Myths, Busted"] == 1167


def test_series_shares_give_the_top_three_seventy_percent_and_keep_the_rest_alive():
    shares = auto.series_shares(auto.series_reach(_ranked_rows()))
    top = ("Space Myths, Busted", "Mission Files", "Scale Breaker")
    assert round(sum(shares[s] for s in top), 3) == auto.TOP_SHARE
    assert all(shares[s] > 0 for s in auto.SERIES)
    assert round(sum(shares.values()), 6) == 1
    # With too few ranked series the plain rotation stays.
    assert auto.series_shares({"Mission Files": 1000, "Scale Breaker": 900}) is None


def _backlog(per_series=6):
    return [{"kind": "backlog", "topic": f"{s} topic {i}", "series": s, "date": None, "status": "", "episode": ""}
            for s in auto.SERIES for i in range(per_series)]


def test_choose_topics_follows_the_shares_without_back_to_back_series(monkeypatch):
    monkeypatch.setattr(auto, "_now", lambda: NOW)
    monkeypatch.setattr(auto, "calendar_topics", lambda today=None: _backlog())
    monkeypatch.setattr(auto, "_available", lambda t, today: True)
    monkeypatch.setattr(auto, "demand", lambda topics: {})
    monkeypatch.setattr(auto, "_series_shares", lambda: auto.series_shares(auto.series_reach(_ranked_rows())))
    chosen = auto.choose_topics(20, [])
    series = [t["series"] for t in chosen]
    top = sum(s in ("Space Myths, Busted", "Mission Files", "Scale Breaker") for s in series)
    assert 13 <= top <= 15  # about 70% of 20
    assert all(series.count(s) >= 1 for s in auto.SERIES)  # every series still gets re-tested
    assert all(a != b for a, b in zip(series, series[1:]))


def test_choose_topics_rotates_evenly_without_numbers(monkeypatch):
    monkeypatch.setattr(auto, "_now", lambda: NOW)
    monkeypatch.setattr(auto, "calendar_topics", lambda today=None: _backlog())
    monkeypatch.setattr(auto, "_available", lambda t, today: True)
    monkeypatch.setattr(auto, "demand", lambda topics: {})
    monkeypatch.setattr(auto, "_series_shares", lambda: None)
    series = [t["series"] for t in auto.choose_topics(12, [])]
    assert all(series.count(s) == 2 for s in auto.SERIES)


def _video(vid, published, views):
    return {"id": vid, "title": f"Short {vid}", "published": published.isoformat().replace("+00:00", "Z"), "views": views}


def _history(candidate_views, candidate_hours=24, peer_views=900, peers=6):
    snapshots = []
    for n in range(peers):
        taken = NOW - timedelta(days=peers - n)
        snapshots.append({"date": taken.date().isoformat(), "taken_at": taken.isoformat(),
                          "videos": [_video(f"peer{n}", taken - timedelta(hours=30), peer_views)]})
    snapshots.append({"date": NOW.date().isoformat(), "taken_at": NOW.isoformat(),
                      "videos": [_video("hit", NOW - timedelta(hours=candidate_hours), candidate_views)]})
    return snapshots


def test_a_short_well_above_its_peers_is_rising_not_a_breakout():
    found = growth.breakouts(_history(1500))
    assert [(b["video"], b["tier"]) for b in found] == [("hit", "rising")]
    assert growth.breakouts(_history(1200)) == []  # under RISING_MIN_VIEWS
    assert growth.breakouts(_history(1500, peer_views=1100)) == []  # only 1.4x
    assert growth.breakouts(_history(1500, candidate_hours=10)) == []  # too early to tell
    assert growth.breakouts(_history(3000))[0]["tier"] == "breakout"


def test_stalled_finds_old_shorts_that_never_got_an_audience():
    analytics = {"taken_at": NOW.isoformat(), "videos": [
        _video("stuck", NOW - timedelta(days=6), 11), _video("young", NOW - timedelta(hours=10), 5),
        _video("fine", NOW - timedelta(days=3), 900)]}
    assert [s["video"] for s in auto.stalled(analytics)] == ["stuck"]
    assert auto.stalled(analytics, {"stuck"}) == []


def test_the_third_slot_alternates_only_during_the_test():
    before, first = publish.SLOT_TEST[0] - timedelta(days=1), publish.SLOT_TEST[0]
    days = [first + timedelta(days=i) for i in range(20)]
    thirds = [publish.slots_on(d)[2] for d in days]
    assert set(thirds) == set(publish.SLOT_TEST_TIMES)
    assert thirds.count(publish.SLOT_TEST_TIMES[0]) == thirds.count(publish.SLOT_TEST_TIMES[1]) == 10
    assert publish.slots_on(before) == publish.SLOTS
    assert publish.slots_on(publish.SLOT_TEST[1]) == publish.SLOTS
    assert all(publish.slots_on(d)[:2] == publish.SLOTS[:2] for d in days)


def test_next_slots_uses_the_days_test_slot():
    odd = next(publish.SLOT_TEST[0] + timedelta(days=i) for i in range(2)
               if (publish.SLOT_TEST[0] + timedelta(days=i)).toordinal() % 2)
    start = datetime.combine(odd, datetime.min.time(), publish.AUDIENCE_TZ)
    times = {t.time() for t in publish.next_slots(3, set(), start=start, per_day=3) if t.date() == odd}
    assert publish.SLOT_TEST_TIMES[1] in times and publish.SLOT_TEST_TIMES[0] not in times


def test_slot_test_counts_only_each_days_test_slot():
    tz = publish.AUDIENCE_TZ
    days = [publish.SLOT_TEST[0] + timedelta(days=i) for i in range(2)]
    slot = {d: publish.slots_on(d)[2] for d in days}
    other = {d: next(t for t in publish.SLOT_TEST_TIMES if t != slot[d]) for d in days}

    def at(d, t, minutes=0):
        return (datetime.combine(d, t, tz) + timedelta(minutes=minutes)).isoformat()

    rows = [dict(_row("x", 700, at(days[0], slot[days[0]])), short="a"),
            dict(_row("x", 1100, at(days[1], slot[days[1]], 50)), short="b"),  # resent by slot_watch
            dict(_row("x", 9000, at(days[0], other[days[0]])), short="c"),  # a slot over the pace
            dict(_row("x", 8000, at(days[1], slot[days[1]])), short="timely"),
            dict(_row("x", 5000, at(days[0] - timedelta(days=3), slot[days[0]])), short="d")]
    line = auto.slot_test(rows, {"timely"})
    assert f"{slot[days[0]]:%H:%M} ET: 1 Shorts, median 700" in line
    assert f"{slot[days[1]]:%H:%M} ET: 1 Shorts, median 1,100" in line
    assert auto.slot_test([]) is None


def test_a_rising_short_that_breaks_out_gets_the_rest_of_its_follow_ups(monkeypatch, tmp_path):
    state = {"breakouts": {"hit": {"on": "2026-10-19", "short": "ep300", "added": 1, "tier": "rising"}}}
    ep = {"id": "ep300", "title": "Hit", "series": "Mission Files", "topic": {"topic": "t"}, "folder": tmp_path, "video_id": "hit"}
    asked = []
    monkeypatch.setattr(auto, "STATUS", tmp_path)
    monkeypatch.setattr(auto, "ANALYTICS", tmp_path)
    monkeypatch.setattr(auto, "episodes", lambda: [ep])
    monkeypatch.setattr(auto, "_by_video", lambda eps: {"hit": ep})
    monkeypatch.setattr(auto, "calendar_topics", lambda today=None: [])
    monkeypatch.setattr(auto, "_known_topics", lambda topics, eps: [])
    monkeypatch.setattr(auto, "_verified", lambda items, known, limit: items[:limit])
    monkeypatch.setattr(auto, "_write_timely", lambda rows: None)
    monkeypatch.setattr(growth, "propose_followups", lambda short, known, count: asked.append(count) or
                        [{"topic": f"f{i}", "wikipedia": "x"} for i in range(count)])
    monkeypatch.setattr(growth, "breakouts", lambda snaps, done: [] if "hit" in done else
                        [{"video": "hit", "title": "Hit", "views": 4000, "median": 900, "ratio": 4.4, "hours": 40,
                          "tier": "breakout"}])
    auto.breakout_topics(None, state)
    assert asked == [auto.FOLLOW_UPS - 1]
    assert state["breakouts"]["hit"]["tier"] == "breakout" and state["breakouts"]["hit"]["added"] == auto.FOLLOW_UPS
    # Once a breakout, it is done for good.
    asked.clear()
    auto.breakout_topics(None, state)
    assert asked == []
