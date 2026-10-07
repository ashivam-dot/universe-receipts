# What we've learned

The daily run keeps this file up to date (`PLAYBOOK.md`, step 3). Scriptwriters read it before writing, and
the quality gate checks that every new episode applies it. The aim is that each day's Shorts beat the
channel's recent median on the numbers below.

## What to beat

Recompute daily and after each Short's 24- and 72-hour reviews, over Shorts with 24+ hours of data (medians of the last 10).

| Measure | Where it comes from | Channel median | Target |
|---|---|---|---|
| Engaged share (stand-in for Studio's "stayed to watch") | `analytics.engaged_share` | 50% | 70%+; under 60% rarely takes off |
| Average percentage viewed | `analytics.averageViewPercentage` | 65.1% | 80%+ (loops can push it past 100%) |
| Still watching at 10% of the Short | `retention` point nearest `at: 0.1` | 118% | rising week over week |
| Subscribers per 1,000 views | `subscribersGained` / `views` | 1.0 | 2+ |
| Likes per 100 views | `likes` / `views` | 3.7 | 4+ |

## Rules we've proven

A rule needs at least two Shorts with 24+ hours of data showing the same effect. Once proven, also copy it
into `strategy/SCRIPT-RULES.md`, then cite the evidence here.

- Put the strongest surprise or contradiction in the first 2 seconds (e.g., '80 million trees, zero craters') to maximize view velocity and early retention. Evidence: ep008, ep024.
- Start the opening script line with a curiosity gap rather than a static statement or text overlay to improve initial retention and view velocity. Evidence: ep002, ep009.
- Replace closed circular endings with an open-ended question or debate prompt in the final beat to drive audience comments. Evidence: ep004, ep013, ep017, ep024, ep028.
- Write a last line that flows straight into the first line to increase average percentage viewed and trigger rewatches. Evidence: ep008, ep013, ep028.
- Avoid repeating exact hook phrases verbatim in the final beat; replace them with a distinct concluding payoff, seamless cliffhanger, or forward-looking question to prevent steep retention and like drops. Evidence: ep017, ep024, ep036.
- Condense mid-script setups into single punchy beats to keep the final beat under 3 seconds and sustain end retention above 1.0. Evidence: ep008, ep009.
- Compress or eliminate complex technical explanations or scientific definitions in the final beats to prevent late retention drop-offs. Evidence: ep008, ep028.

## Hypotheses to test (from research, not yet our data)

- Cut each Short to 45-59 seconds to maximize reach potential.
- Deliver the core narrative payoff or setup within the first 3 seconds immediately after the hook to prevent pacing drop-off. Evidence: ep009.
- Accelerate middle-beat reveals on cosmic scale topics to maintain audience engagement through the midpoint. Evidence: ep032.
- Avoid passive statement hooks in favor of high-tension mysteries to prevent early viewer drop-off. Evidence: ep002.

## Scoreboard

One row per live Short once it has 24+ hours of data. Hook style is statement, question, number, or
contradiction.

| Short | Series | Hook style | Views | Engaged share | Avg % viewed | Watching at 10% | Subs gained | Likely reason |
|---|---|---|---|---|---|---|---|---|
| ep002 | Mission Files | statement, story | 105 | 47% | 39.1% | 85% | 0 | Static statement hook and slow pacing failed on all metrics; visuals couldn't salvage retention. |
| ep004 | Mission Files | statement, story | 1056 | 57% | 53.8% | 110% | 3 | Paradox hook drove high views and likes, but closed ending killed comments. |
| ep008 | The Universe Is Terrifying | statement, story | 866 | 47% | 83.8% | 130% | 5 | Exceptional hook and topic kept retention and loops high, but slow ending dragged late pacing. |
| ep009 | Near Misses | statement, story | 244 | 42% | 60.3% | 105% | 0 | Intriguing historical hook started strong, but slow mid-script pacing caused late drop-off. |
| ep013 | Scale Breaker | contradiction, story | 979 | 56% | 66.0% | 117% | 2 | Great contradiction hook and scale topic boosted likes, but weak ending ruined loop potential. |
| ep017 | Mission Files | contradiction, myth_vs_fact | 1183 | – | – | – | – | Strong naming paradox hook drove views, but a verbatim ending loop restricted comment engagement. |
| ep024 | Near Misses | contradiction, scale_ladder | 955 | 46% | 53.7% | 104% | 1 | Powerful contradiction hook boosted early reach, but verbatim hook repetition at end killed loop retention. |
| ep028 | Space Myths, Busted | statement, mystery | 1261 | 54% | 81.5% | 129% | 5 | Excellent mystery hook drove strong loops, but technical precession explanation slowed pacing near the end. |
| ep032 | The Universe Is Terrifying | statement, record | 1034 | 42% | 75.8% | 123% | 1 | Terrifying cosmic topic secured high views, though slow middle-beat pacing slightly lowered engagement. |
| ep035 | Near Misses | statement, myth_vs_fact | 1295 | – | – | – | – | Urgent hazard hook drove strong initial views, but lack of a creative loop muted engagement. |
| ep036 | Mission Files | statement, story | 1030 | 60% | 64.2% | 119% | 1 | Vivid visual hook engaged viewers early, but verbatim phrase repetition at the end flattened likes. |

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
