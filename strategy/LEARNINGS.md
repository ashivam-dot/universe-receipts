# What we've learned

The daily run keeps this file up to date (`PLAYBOOK.md`, step 3). Scriptwriters read it before writing, and
the quality gate checks that every new episode applies it. The aim is that each day's Shorts beat the
channel's recent median on the numbers below.

## What to beat

Recompute daily and after each Short's 24- and 72-hour reviews, over Shorts with 24+ hours of data (medians of the last 10).

| Measure | Where it comes from | Channel median | Target |
|---|---|---|---|
| Engaged share (stand-in for Studio's "stayed to watch") | `analytics.engaged_share` | 43% | 70%+; under 60% rarely takes off |
| Average percentage viewed | `analytics.averageViewPercentage` | 56.9% | 80%+ (loops can push it past 100%) |
| Still watching at 10% of the Short | `retention` point nearest `at: 0.1` | 105% | rising week over week |
| Subscribers per 1,000 views | `subscribersGained` / `views` | 0.0 | 2+ |
| Likes per 100 views | `likes` / `views` | 3.6 | 4+ |

## Rules we've proven

A rule needs at least two Shorts with 24+ hours of data showing the same effect. Once proven, also copy it
into `strategy/SCRIPT-RULES.md`, then cite the evidence here.

- Put the strongest surprise or contradiction in the first 2 seconds (e.g., '80 million trees, zero craters') to maximize view velocity and early retention. Evidence: ep008, ep024.
- Start the opening script line with a curiosity gap rather than a static statement or text overlay to improve initial retention and view velocity. Evidence: ep002, ep009.
- Replace closed circular endings with an open-ended question or debate prompt in the final beat to drive audience comments. Evidence: ep013, ep024.

## Hypotheses to test (from research, not yet our data)

- Cut each Short to 45-59 seconds to maximize reach potential.
- Write a last line that flows straight into the first line to increase average percentage viewed.
- Deliver the core narrative payoff or setup within the first 3 seconds immediately after the hook to prevent pacing drop-off.

## Scoreboard

One row per live Short once it has 24+ hours of data. Hook style is statement, question, number, or
contradiction.

| Short | Series | Hook style | Views | Engaged share | Avg % viewed | Watching at 10% | Subs gained | Likely reason |
|---|---|---|---|---|---|---|---|---|
| ep002 | Mission Files | statement, story | 103 | 44% | 42.7% | 88% | 0 | Static statement hook and slow pacing caused low retention and engagement below channel medians. |
| ep008 | The Universe Is Terrifying | statement, story | 868 | 47% | 89.9% | 136% | 5 | Intriguing physical black hole hook drove high initial retention and 89.9% view percentage, well above channel medians. |
| ep009 | Near Misses | statement, story | 232 | 42% | 62.0% | 105% | 0 | Strong solar storm topic generated solid early traction, but delayed narrative payoff slowed post-hook pacing. |
| ep013 | Scale Breaker | contradiction, story | 734 | – | – | – | – | Paradox hook drove high view velocity and likes, but a closed factual loop resulted in zero comments. |
| ep024 | Near Misses | contradiction, scale_ladder | 892 | 42% | 51.8% | 105% | 1 | High-concept contradiction hook achieved strong reach, but passive historical resolution dragged down final engagement. |

## Log

- Day 0: the studio is set up. Nothing to learn from yet.
- 2026-09-30: No new Shorts with 48+ hours of data today, so no metrics to evaluate or rules to promote.
- 2026-10-01: No changes made today as no Shorts have accumulated 24+ hours of data yet.
- 2026-10-02: Initial analysis of ep008 shows strong hook performance from physical-object angles but a total lack of engagement at the finish.
- 2026-10-02: Added ep008 performance data, highlighting a critical need to replace passive summary endings with active debate prompts to drive comments.
- 2026-10-03: Added ep002 and ep008 to the learning log, introducing a curiosity-gap hook hypothesis and supporting the debate-prompt ending hypothesis.
- 2026-10-03: Logged 24h+ reviews for ep002 and ep008; retained all core script hypotheses as evidence remains under the two-Short rule threshold.
- 2026-10-04: Logged performance reviews for ep002, ep008, and ep009; keeping all existing hypotheses as no single effect has appeared in two shorts yet.
- 2026-10-04: Promoted curiosity gaps and surprise hooks to rules after high-concept hooks in ep008 and ep024 outperformed static historical statements in ep002 and ep009.
- 2026-10-04: Added a post-hook pacing hypothesis from ep009's diagnosis while tracking looping and debate endings toward rule promotion.
- 2026-10-05: Promoted comment-prompt ending hypothesis to a rule after ep013 and ep024 showed zero comments from closed factual endings.
