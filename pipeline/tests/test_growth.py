"""Offline checks of growth.py's pure functions: trending filters, NASA's feed, and breakout detection."""

from datetime import datetime, timedelta, timezone

from ytc import growth

NOW = datetime(2026, 10, 20, 9, 0, tzinfo=timezone.utc)


def test_merge_top_drops_non_articles_and_keeps_best_day():
    day1 = {"items": [{"articles": [{"article": "Main_Page", "views": 6_000_000}, {"article": "Special:Search", "views": 900_000},
                                    {"article": "Voyager_1", "views": 50_000}, {"article": "Wikipedia:Featured_pictures", "views": 5}]}]}
    day2 = {"items": [{"articles": [{"article": "Voyager_1", "views": 80_000}, {"article": "Betelgeuse", "views": 30_000}]}]}
    views = growth.merge_top(growth.merge_top({}, day1), day2)
    assert views == {"Voyager 1": 80_000, "Betelgeuse": 30_000}


def test_space_articles_keeps_space_descriptions_most_read_first():
    views = {"Pac (wrestler)": 800_000, "Voyager 1": 50_000, "Betelgeuse": 90_000, "Jessica Watkins": 20_000, "Lizzie Borden": 300_000}
    described = {"Pac (wrestler)": "English professional wrestler (1986–2026)", "Voyager 1": "NASA space probe launched in 1977",
                 "Betelgeuse": "Red supergiant star in the constellation Orion", "Jessica Watkins": "American astronaut (born 1988)",
                 "Lizzie Borden": "American woman acquitted of murder"}
    assert [a["title"] for a in growth.space_articles(views, described)] == ["Betelgeuse", "Voyager 1", "Jessica Watkins"]


FEED = """<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>NASA</title>
<item><title>Crew-13 Rocket and Spacecraft at Launch Pad</title><link>https://www.nasa.gov/image-article/crew-13/</link>
<pubDate>Tue, 20 Oct 2026 03:31:56 +0000</pubDate>
<description><![CDATA[<p>Ahead of NASA’s SpaceX Crew-13 mission launch, a Falcon 9 stands at the pad [&#8230;]</p>]]></description></item>
<item><title>Europa Clipper Sees Jupiter</title><link>https://www.nasa.gov/news-release/europa/</link>
<pubDate>Mon, 19 Oct 2026 12:00:00 +0000</pubDate><description>First look.</description></item>
<item><title>Old News</title><link>https://www.nasa.gov/old/</link>
<pubDate>Wed, 14 Oct 2026 12:00:00 +0000</pubDate><description>Stale.</description></item>
<item><title>No Date</title><link>https://www.nasa.gov/x/</link></item>
</channel></rss>"""


def test_nasa_news_keeps_recent_items_newest_first():
    items = growth.nasa_news(FEED, NOW, hours=48)
    assert [i["title"] for i in items] == ["Crew-13 Rocket and Spacecraft at Launch Pad", "Europa Clipper Sees Jupiter"]
    assert items[0]["summary"] == "Ahead of NASA’s SpaceX Crew-13 mission launch, a Falcon 9 stands at the pad"
    assert items[1]["link"] == "https://www.nasa.gov/news-release/europa/"


def _video(vid, published, views):
    return {"id": vid, "title": f"Short {vid}", "published": published.isoformat().replace("+00:00", "Z"), "views": views}


def _history(candidate_views=None, peers=6, peer_views=100):
    """Daily snapshots: `peers` Shorts, each measured about 30 hours after going live, then today's snapshot with
    a Short 20 hours old."""
    snapshots = []
    for n in range(peers):
        taken = NOW - timedelta(days=peers - n)
        snapshots.append({"date": taken.date().isoformat(), "taken_at": taken.isoformat(),
                          "videos": [_video(f"peer{n}", taken - timedelta(hours=30), peer_views + n)]})
    if candidate_views is not None:
        snapshots.append({"date": NOW.date().isoformat(), "taken_at": NOW.isoformat(),
                          "videos": [_video("hit", NOW - timedelta(hours=20), candidate_views)]})
    return snapshots


def test_breakout_needs_ratio_and_floor():
    assert growth.breakouts(_history(candidate_views=250, peer_views=100)) == []  # 2.4x
    # 3x+ of a tiny median is no breakout.
    assert growth.breakouts(_history(candidate_views=40, peer_views=10)) == []
    found = growth.breakouts(_history(candidate_views=5000, peer_views=1000))
    assert [b["video"] for b in found] == ["hit"]
    assert found[0]["median"] == 1002.5 and found[0]["ratio"] == round(5000 / 1002.5, 1)
    assert found[0]["hours"] == 20


def test_breakout_guards_and_peer_minimum():
    history = _history(candidate_views=5000, peer_views=1000)
    assert growth.breakouts(history, done={"hit"}) == []
    assert growth.breakouts(_history(candidate_views=5000, peers=3, peer_views=1000)) == []
    # 100k views within 48 hours is a breakout whatever the peers did.
    assert [b["video"] for b in growth.breakouts(_history(candidate_views=120_000, peer_views=60_000))] == ["hit"]


def test_breakout_only_while_young_in_newest_snapshot():
    history = _history(candidate_views=5000, peer_views=1000)
    # The next day the hit is 44 hours old and still counts; a day later it's past 48 hours.
    later = {"date": (NOW + timedelta(days=1)).date().isoformat(), "taken_at": (NOW + timedelta(hours=24)).isoformat(),
             "videos": [_video("hit", NOW - timedelta(hours=20), 9000)]}
    assert [b["views"] for b in growth.breakouts(history + [later])] == [9000]
    much_later = dict(later, taken_at=(NOW + timedelta(hours=40)).isoformat())
    assert growth.breakouts(history + [much_later]) == []


def test_early_views_falls_back_to_the_date_for_old_snapshots():
    snapshot = {"date": "2026-10-20", "videos": [_video("a", datetime(2026, 10, 19, 21, tzinfo=timezone.utc), 10)]}
    assert growth.early_views([snapshot])["a"]["hours"] == 12.0
