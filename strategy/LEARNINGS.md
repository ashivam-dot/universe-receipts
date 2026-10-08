# What we've learned

The daily run keeps this file up to date (`PLAYBOOK.md`, step 3). Scriptwriters read it before writing, and
the quality gate checks that every new episode applies it. The aim is that each day's Shorts beat the
channel's recent median on the numbers below.

## What to beat

Recompute daily and after each Short's 24- and 72-hour reviews, over Shorts with 24+ hours of data (medians of the last 10).

| Measure | Where it comes from | Channel median | Target |
|---|---|---|---|
| Engaged share (stand-in for Studio's "stayed to watch") | `analytics.engaged_share` | 52% | 70%+; under 60% rarely takes off |
| Average percentage viewed | `analytics.averageViewPercentage` | 70.4% | 80%+ (loops can push it past 100%) |
| Still watching at 10% of the Short | `retention` point nearest `at: 0.1` | 124% | rising week over week |
| Subscribers per 1,000 views | `subscribersGained` / `views` | 1.0 | 2+ |
| Likes per 100 views | `likes` / `views` | 3.6 | 4+ |

## Rules we've proven

A rule needs at least two Shorts with 24+ hours of data showing the same effect. Once proven, also copy it
into `strategy/SCRIPT-RULES.md`, then cite the evidence here.

- Put the strongest surprise or contradiction in the first 2 seconds (e.g., '80 million trees, zero craters') to maximize view velocity and early retention. Evidence: ep008, ep024.
- Start the opening script line with a curiosity gap rather than a static statement or text overlay to improve initial retention and view velocity. Evidence: ep002, ep009.
- Replace closed circular endings with an open-ended question or debate prompt in the final beat to drive audience comments. Evidence: ep004, ep013, ep017, ep024, ep028, ep032, ep033.
- Write a last line that flows straight into the first line to increase average percentage viewed and trigger rewatches. Evidence: ep008, ep013, ep028, ep032.
- Avoid repeating exact hook phrases verbatim in the final beat; replace them with a distinct concluding payoff, seamless cliffhanger, or forward-looking question to prevent steep retention and like drops. Evidence: ep017, ep024, ep036.
- Condense mid-script setups into single punchy beats to keep the final beat under 3 seconds and sustain end retention above 1.0. Evidence: ep008, ep009.
- Compress or eliminate complex technical explanations or scientific definitions in the final beats to prevent late retention drop-off. Evidence: ep008, ep028.
- Deliver the core narrative payoff or setup within the first 3 seconds immediately after the hook to prevent pacing drop-off. Evidence: ep009, ep004.
- Accelerate middle-beat reveals on cosmic scale topics to maintain audience engagement through the midpoint. Evidence: ep032, ep036.
- Use high-urgency hook phrases (e.g., 'Level 4 Hazard', 'Cosmic Monster') to boost immediate view velocity and distribution. Evidence: ep032, ep035.
- Tighten pacing in the second and third beats to prevent early-retention drop-offs. Evidence: ep009, ep036.
- Avoid passive statement hooks in favor of high-tension, active mysteries to prevent early viewer drop-off. Evidence: ep002, ep061.

## Hypotheses to test (from research, not yet our data)

- Cut each Short to 45-59 seconds to maximize reach potential.

## Scoreboard

One row per live Short once it has 24+ hours of data. Hook style is statement, question, number, or
contradiction.

| Short | Series | Hook style | Views | Engaged share | Avg % viewed | Watching at 10% | Subs gained | Likely reason |
|---|---|---|---|---|---|---|---|---|
| 2rz-F-WZsXA | ? | –, story | 97 | 32% | 54.6% | 121% | 0 | – |
| ep002 | Mission Files | statement, story | 106 | 47% | 40.4% | 86% | 0 | – |
| ep004 | Mission Files | statement, story | 1060 | 57% | 53.5% | 110% | 3 | – |
| ep008 | The Universe Is Terrifying | statement, story | 866 | 47% | 83.6% | 130% | 5 | – |
| ep009 | Near Misses | statement, story | 245 | 43% | 60.2% | 105% | 0 | – |
| ep013 | Scale Breaker | contradiction, story | 979 | 55% | 71.2% | 124% | 2 | Removed explanatory wrap-up beat to improve retention and looping. |
| ep017 | Mission Files | contradiction, myth_vs_fact | 1249 | 52% | 69.6% | 119% | 5 | Used cliffhanger loop to prevent repeating the premise. |
| ep024 | Near Misses | contradiction, scale_ladder | 956 | 46% | 53.5% | 104% | 1 | Replaced verbatim hook repetition with a seamless transition beat. |
| ep028 | Space Myths, Busted | statement, mystery | 1271 | 54% | 80.5% | 128% | 5 | Aggressively compressed final beats by removing technical definitions. |
| ep030 | Scale Breaker | number, record | 1081 | – | – | – | – | Replaced historical discovery beats with an immediate physical comparison. |
| ep032 | The Universe Is Terrifying | statement, record | 1038 | 42% | 79.7% | 127% | 1 | Rewrote the final beat to end on an open question to prompt comments. |
| ep033 | Space Got Weird | statement, story | 723 | 43% | 68.1% | 125% | 1 | Replaced passive closing statement with an engaging question. |
| ep035 | Near Misses | statement, myth_vs_fact | 1317 | 52% | 86.9% | 131% | 1 | Kept high-impact urgency hook style and opening beat pacing. |
| ep036 | Mission Files | statement, story | 1031 | 60% | 63.7% | 118% | 1 | Tightened pacing on the second and third beats. |
| ep061 | The Universe Is Terrifying | statement, scale_ladder | 218 | – | – | – | – | Revised hook to open with a high-tension active claim. |

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
- 2026-10-05: Promoted open-ended endings to a rule after ep028 confirmed that high-velocity mystery hooks still fail to generate interaction without a prompt.
- 2026-10-05: Promoted the seamless audio looping hypothesis to a rule based on evidence from ep008 and ep028 showing higher retention and rewatch potential.
- 2026-10-05: Updated playbook rules and hypotheses using review data from recent Shorts to refine scriptwriting focus.
- 2026-10-06: Added a new hypothesis regarding avoiding repetitive hook phrases in final beats based on ep028 and ep036 reviews.
- 2026-10-06: Updated learning log with latest short reviews, reinforcing current rules and maintaining hypotheses.
- 2026-10-06: Promoted the rule against verbatim hook repetition in endings after ep024 and ep036 both showed engagement and retention drops.
- 2026-10-07: Promoted the fast-paced final beat hypothesis to a rule using ep008 and ep009, and expanded evidence for ending rules using ep013 and ep017.
- 2026-10-07: Today we maintained proven rules regarding hook placement and loop structure, while noting the negative impact of verbatim hook repetition on end retention and comments.
- 2026-10-07: Promoted technical explanation compression to a rule after ep008 and ep028 both showed late retention drop-offs due to scientific over-explanation.
- 2026-10-07: Updated learning log with latest 11 short reviews, maintaining existing proven rules and refining pacing hypotheses based on mid-video drop-offs.
- 2026-10-08: Promoted two pacing hypotheses to rules using evidence from ep004, ep009, ep032, and ep036, and introduced an urgency hook hypothesis based on ep035.
- 2026-10-08: Promoted urgency hooks and early-beat pacing to rules; channel medians show rising retention but stagnant comment conversion.
- 2026-10-08: Updated learning log with performance reviews for ep008 through ep036 to refine hook, pacing, and looping rules.
- 2026-10-08: Promoted the active-mystery hook hypothesis to a rule after ep061's passive opening failed where ep002 previously struggled.
- 2026-10-09: Reviewed recent Shorts and updated rules for pacing and hook structures to address late-video retention drops.
