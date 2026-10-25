from ytc import auto

RISING = [1000.0] * 10 + [1200.0] * 10


def _setup(monkeypatch, day, engaged, share=None, reach=RISING):
    monkeypatch.setattr(auto, "day_number", lambda today=None: day)
    monkeypatch.setattr(auto, "_pace_numbers", lambda: (engaged, share or [0.6] * len(engaged)))
    monkeypatch.setattr(auto, "_reach_numbers", lambda: reach)


def test_first_two_weeks_post_two_a_day(monkeypatch):
    _setup(monkeypatch, 3, [])
    assert auto.slots_per_day() == 2


def test_before_launch_posts_two(monkeypatch):
    _setup(monkeypatch, -1, [])
    assert auto.slots_per_day() == 2


def test_without_twenty_shorts_of_numbers_the_pace_stops_at_three(monkeypatch):
    _setup(monkeypatch, 55, [1000.0] * 12)
    assert auto.slots_per_day() == 3


def test_holding_numbers_earn_the_planned_pace(monkeypatch):
    _setup(monkeypatch, 35, [1000.0] * 10 + [1000.0] * 10)
    assert auto.slots_per_day() == 4
    _setup(monkeypatch, 55, [1000.0] * 10 + [1200.0] * 10)
    assert auto.slots_per_day() == 5


def test_flat_reach_per_short_holds_the_pace_at_three(monkeypatch):
    # The channel on Day 25: engagement holds, but each Short reaches about as many people as before.
    _setup(monkeypatch, 35, [520.0] * 20, reach=[950.0] * 10 + [1000.0] * 10)
    assert auto.slots_per_day() == 3


def test_rising_reach_under_a_thousand_holds_the_pace_at_three(monkeypatch):
    _setup(monkeypatch, 35, [520.0] * 20, reach=[600.0] * 10 + [900.0] * 10)
    assert auto.slots_per_day() == 3


def test_too_few_measured_shorts_hold_the_pace_at_three(monkeypatch):
    _setup(monkeypatch, 35, [520.0] * 20, reach=[2000.0] * 12)
    assert auto.slots_per_day() == 3


def test_slipping_views_per_short_hold_the_pace_at_three(monkeypatch):
    _setup(monkeypatch, 55, [1000.0] * 10 + [850.0] * 10)
    assert auto.slots_per_day() == 3


def test_a_big_drop_steps_back_to_two(monkeypatch):
    _setup(monkeypatch, 55, [1000.0] * 10 + [600.0] * 10)
    assert auto.slots_per_day() == 2


def test_unreadable_numbers_post_two(monkeypatch):
    monkeypatch.setattr(auto, "day_number", lambda today=None: 40)

    def broken():
        raise ValueError("bad file")

    monkeypatch.setattr(auto, "_pace_numbers", broken)
    assert auto.slots_per_day() == 2
