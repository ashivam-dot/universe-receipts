# 100-day plan

Day 0 is 2026-10-01; Day 100 is 2027-01-09. Production runs around the clock and keeps up to two weeks of
finished Shorts ready; publishing follows the cadence below. At 3 a day that's about 300 Shorts by Day 100,
and up to about 420 if the code's step-ups to 4 a day (Day 30) and 5 a day (Day 50) both trigger.

| Phase | Days | Dates | Focus | Exit milestone |
|---|---|---|---|---|
| 0. Build | -2–0 | Sep 29–Oct 1 | Niche adapted, brand, accounts (channel, Buffer, Cloudinary, Modal, Google app), first Shorts through the quality gate | First Shorts scheduled |
| 1. Launch | 1–21 | Oct 2–Oct 22 | 3 a day across all 6 series; anniversaries (Sputnik, Oh-My-God particle, Orionids); learn which hooks and topics work | 60+ Shorts live, first KPI baseline |
| 2. Double down | 22–50 | Oct 23–Nov 20 | 70% of output into the top 2–3 series; weekly experiments; sequels to any breakout within 48 hours; 4 a day from Day 30 if engaged share holds; cross-posting once the owner opens those accounts | 1,000 subscribers; 1M+ views in a 28-day window |
| 3. YPP push | 51–75 | Nov 21–Dec 15 | 5 a day if quality and engaged share hold; apply for YPP the day Studio shows eligibility | YPP application in by mid-December, or a clear path chosen at Day 60 |
| 4. Scale | 76–100 | Dec 16–Jan 9 | Monetization setup if approved, otherwise keep applying before the Feb 1 rule change; best formats at full volume; Day 100 review | Day 100 report and the next 100 days' plan |

## Targets

These are the targets we steer by. They aren't promises. Subscribers follow from views at the 0.15–0.36%
Shorts conversion in `research/shorts-strategy.md`; the base case assumes about 0.2%.

| By | Base case | Stretch (on track for 100k) |
|---|---|---|
| Day 21 (Oct 22) | 63 Shorts, 70k total views, 200 subscribers | 1M views, 2,200 subscribers |
| Day 30 (Oct 31) | 90 Shorts, 180k views, 450 subscribers; 7-day median 1,000+ views a Short | 3M views, 6,500 subscribers |
| Day 50 (Nov 20) | about 170 Shorts, 1.3M views, 2,500 subscribers | 11M views, 24,000 subscribers |
| Day 75 (Dec 15) | about 295 Shorts, 5M views in 90 days, 9,500 subscribers | 30M views, 65,000 subscribers, YPP applied |
| Day 100 (Jan 9) | about 420 Shorts, 10M total views, 15,000–25,000 subscribers | 45M+ views, 100,000 subscribers |

What the base case means for money: 10M views in 90 days is reached around Day 100, after mid-December, so
in the base case YPP before the Feb 1, 2027 change needs either a breakout or an application in late
December or January (review takes about a month, and YouTube hasn't said which bar applies to pending
applications). The **floor** is below the base: fewer than 50k total views by Day 30, which triggers the
Day 30 format change.

### Weekly targets

Cumulative at the end of each week (Shorts counts assume the step-ups trigger).

| Week | Ends | Shorts | Base views | Base subs | Stretch views | Stretch subs |
|---|---|---|---|---|---|---|
| 1 | Oct 8 | 21 | 10k | 30 | 50k | 100 |
| 2 | Oct 15 | 42 | 30k | 100 | 500k | 1,100 |
| 3 | Oct 22 | 63 | 70k | 200 | 1M | 2,200 |
| 4 | Oct 29 | 84 | 150k | 400 | 2.5M | 5,500 |
| 5 | Nov 5 | 110 | 300k | 700 | 4M | 9,000 |
| 6 | Nov 12 | 138 | 600k | 1,200 | 6M | 13,000 |
| 7 | Nov 19 | 166 | 1.2M | 2,200 | 10M | 22,000 |
| 8 | Nov 26 | 200 | 2M | 3,500 | 14M | 31,000 |
| 9 | Dec 3 | 235 | 3M | 5,500 | 18M | 40,000 |
| 10 | Dec 10 | 270 | 4.2M | 7,500 | 23M | 51,000 |
| 11 | Dec 17 | 305 | 5.5M | 10,000 | 28M | 62,000 |
| 12 | Dec 24 | 340 | 7M | 13,000 | 34M | 75,000 |
| 13 | Dec 31 | 375 | 8.5M | 16,500 | 40M | 88,000 |
| 14 | Jan 7 | 410 | 10M | 20,000 | 45M | 100,000 |

The Sunday weekly review in `reports/` compares the week with both columns and says which one the channel is tracking.

## Decision points

- **Day 3:** Read the first Shorts' `research.json` and `review.json`. If claims are thin or pictures weak,
  fix the prompts, `strategy/SCRIPT-RULES.md`, or the trusted sites, not the thresholds.
- **Day 7:** Retire hook styles whose engaged share (engaged views / views, the API's stand-in for Studio's
  "stayed to watch") is below 50%.
- **Day 14:** Pick a voice from the blind test plus the retention data.
- **Day 21:** Rank series by views per Short and subscribers per 1,000 views. Keep the top 3–4 at 70% of
  output; the rest continue at a trickle so they can be re-tested.
- **Day 30:** If the 7-day median views per Short is still under 1,000, change the format (on-screen hook
  text, first frame, faster pacing, a different voice) before adding volume, and hold the step-up by moving
  the first value of `PACE_STEPS` in `pipeline/src/ytc/auto.py` later. Otherwise the code goes to 4 a day by
  itself while the last 10 Shorts keep at least 90% of the engaged share of the ones before, and every Short
  must still score 4+ at the quality gate.
- **Day 45, stretch check:** If no Short has passed 100k views and total views are under 2M, the 100k goal
  is off for this 100 days. The weekly report says so plainly, and the channel steers by the base case and YPP.
- **Day 50:** 5 a day on the same test (also automatic).
- **Cadence ceiling:** 5 a day. More than that starts to look mass-produced, which the Partner Program's
  inauthentic-content rule rejects, and YouTube gives no boost for volume.
- **Day 60, YPP path:** Check engaged Shorts views in the last 90 days.
  - 4M or more: on pace for 10M by mid-December; keep going and apply the day Studio shows eligibility.
  - 1M to 4M: apply for the fan-funding tier as soon as it's reached (500 subscribers and 3M views in 90
    days; whether it locks in the old ads thresholds is unverified), and still apply for the ads tier the
    day it's reached, up to Jan 31.
  - Under 1M: the ads tier before Feb 1 is unlikely. Target the 20M bar, and review the format, the
    owner's own voice, and long-form bridges (`research/niche-selection.md` found long-form converts
    viewers to subscribers several times better).
- **Day 60–75:** Apply for YPP as soon as Studio shows eligibility, aiming for mid-December (Day 75).
- **Any breakout** (a Short at 5x the channel's median or 100k+ views): within 48 hours, add 2–4 sequels on
  the same subject or angle to the top of the calendar, pin a comment, and set the Short's Related video to
  the next episode.
- **Every Sunday:** weekly review in `reports/`, next week's experiments, and a check for better open-source tools.
- **Day 100:** Review against both cases, and decide the next 100 days (including whether to add long-form).

## Owner touchpoints

- **Before launch:** create the accounts and sign in (START-HERE and `OWNER-CHECKLIST.md`). The agent never
  types passwords or codes.
- **Early:** phone verification and advanced features on the channel, needed for the Related video link,
  pinned comments, and the YPP application.
- **Optional:** TikTok, Instagram, and Facebook accounts for native cross-posting; recording narration in
  the owner's own voice if YouTube ever questions the channel.
- **When eligible:** the YPP application, AdSense, and the tax form (about 20 minutes).
- Nothing else is required. Daily reports land in `reports/`.
