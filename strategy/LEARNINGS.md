# What we've learned

The daily run keeps this file up to date (`PLAYBOOK.md`, step 3). Scriptwriters read it before writing, and
the quality gate checks that every new episode applies it. The aim is that each day's Shorts beat the
channel's recent median on the numbers below.

## What to beat

Recompute daily and after each Short's 24- and 72-hour reviews, over Shorts with 24+ hours of data (medians of the last 10).

| Measure | Where it comes from | Channel median | Target |
|---|---|---|---|
| Engaged share (stand-in for Studio's "stayed to watch") | `analytics.engaged_share` | 46% | 70%+; under 60% rarely takes off |
| Average percentage viewed | `analytics.averageViewPercentage` | 98.3% | 80%+ (loops can push it past 100%) |
| Still watching at 10% of the Short | `retention` point nearest `at: 0.1` | 144% | rising week over week |
| Subscribers per 1,000 views | `subscribersGained` / `views` | 1.2 | 2+ |
| Likes per 100 views | `likes` / `views` | 2.9 | 4+ |

## Rules we've proven

A rule needs at least two Shorts with 24+ hours of data showing the same effect. Once proven, also copy it
into `strategy/SCRIPT-RULES.md`, then cite the evidence here.

- None yet.

## Hypotheses to test (from research, not yet our data)

- Put the strongest surprise in the first 2 seconds, then give context.
- Cut each Short to 45-59 seconds to maximize reach potential.
- Write a last line that flows straight into the first line to increase average percentage viewed.
- Replace informational summaries with direct debate prompts or open-ended reaction hooks in the final beat to drive audience interaction.
- Start the opening script line with a curiosity gap rather than a static statement or text overlay to improve initial retention and view velocity.

## Scoreboard

One row per live Short once it has 24+ hours of data. Hook style is statement, question, number, or
contradiction.

| Short | Series | Hook style | Views | Engaged share | Avg % viewed | Watching at 10% | Subs gained | Likely reason |
|---|---|---|---|---|---|---|---|---|
| ep002 | Mission Files | statement, story | 94 | – | – | – | – | Static statement hook on a historical topic fell far below median views, proving the need for curiosity gaps. |
| ep008 | The Universe Is Terrifying | statement, story | 862 | 46% | 98.3% | 144% | 2 | Strong physical-drive hook and terrifying black hole topic beat median likes, but a passive informational ending failed to generate comments. |

## Log

- Day 0: the studio is set up. Nothing to learn from yet.
- 2026-09-30: No new Shorts with 48+ hours of data today, so no metrics to evaluate or rules to promote.
- 2026-10-01: No changes made today as no Shorts have accumulated 24+ hours of data yet.
- 2026-10-02: Initial analysis of ep008 shows strong hook performance from physical-object angles but a total lack of engagement at the finish.
- 2026-10-02: Added ep008 performance data, highlighting a critical need to replace passive summary endings with active debate prompts to drive comments.
- 2026-10-03: Added ep002 and ep008 to the learning log, introducing a curiosity-gap hook hypothesis and supporting the debate-prompt ending hypothesis.
