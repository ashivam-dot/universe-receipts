# What we've learned

The daily run keeps this file up to date (`PLAYBOOK.md`, step 3). Scriptwriters read it before writing, and
the quality gate checks that every new episode applies it. The aim is that each day's Shorts beat the
channel's recent median on the numbers below.

## What to beat

Recompute daily and after each Short's 24- and 72-hour reviews, over Shorts with 24+ hours of data (medians of the last 10).

| Measure | Where it comes from | Channel median | Target |
|---|---|---|---|
| Engaged share (stand-in for Studio's "stayed to watch") | `analytics.engaged_share` | 47% | 70%+; under 60% rarely takes off |
| Average percentage viewed | `analytics.averageViewPercentage` | 63.7% | 80%+ (loops can push it past 100%) |
| Still watching at 10% of the Short | `retention` point nearest `at: 0.1` | 112% | rising week over week |
| Subscribers per 1,000 views | `subscribersGained` / `views` | 0.0 | 2+ |
| Likes per 100 views | `likes` / `views` | 3.6 | 4+ |

## Rules we've proven

A rule needs at least two Shorts with 24+ hours of data showing the same effect. Once proven, also copy it
into `strategy/SCRIPT-RULES.md`, then cite the evidence here.

- Put the strongest surprise or contradiction in the first 2 seconds (e.g., '80 million trees, zero craters') to maximize view velocity and early retention. Evidence: ep008, ep024.
- Start the opening script line with a curiosity gap rather than a static statement or text overlay to improve initial retention and view velocity. Evidence: ep002, ep009.
- Replace closed circular endings with an open-ended question or debate prompt in the final beat to drive audience comments. Evidence: ep004, ep013, ep024, ep028.
- Write a last line that flows straight into the first line to increase average percentage viewed and trigger rewatches. Evidence: ep008, ep028.
- Avoid repeating exact hook phrases verbatim in the final beat; replace them with a distinct concluding payoff, seamless cliffhanger, or forward-looking question to prevent steep retention and like drops. Evidence: ep024, ep036.

## Hypotheses to test (from research, not yet our data)

- Cut each Short to 45-59 seconds to maximize reach potential.
- Deliver the core narrative payoff or setup within the first 3 seconds immediately after the hook to prevent pacing drop-off. Evidence: ep009.
- Condense mid-script setups into single punchy beats to keep the final beat under 3 seconds and sustain end retention above 1.0. Evidence: ep008, ep009.
- Accelerate middle-beat reveals on cosmic scale topics to maintain audience engagement through the midpoint. Evidence: ep032.

## Scoreboard

One row per live Short once it has 24+ hours of data. Hook style is statement, question, number, or
contradiction.

| Short | Series | Hook style | Views | Engaged share | Avg % viewed | Watching at 10% | Subs gained | Likely reason |
|---|---|---|---|---|---|---|---|---|
| ep002 | Mission Files | statement, story | 103 | 47% | 39.1% | 85% | 0 | Passive, low-tension hook and slow early pacing sank engaged share (46.6%) and avg viewed (39.14%) well below medians. |
| ep004 | Mission Files | statement, story | 1050 | – | – | – | – | Strong paradoxical espionage hook drove high views and above-median likes (4.29%), but a closed summary loop yielded zero comments. |
| ep008 | The Universe Is Terrifying | statement, story | 866 | 47% | 84.0% | 130% | 5 | Concrete mailing-drives hook and tight loop drove stellar avg viewed (84.01%) and at-10 retention (1.305), beating medians. |
| ep009 | Near Misses | statement, story | 249 | 42% | 59.9% | 104% | 0 | Intriguing battery-free hook gained strong likes (4.42%), but bloated mid-script setup dragged engaged share and avg viewed below medians. |
| ep013 | Scale Breaker | contradiction, story | 979 | 56% | 67.5% | 119% | 2 | Paradoxical mountain hook drove channel-leading engaged share (55.9%) and like rate (4.90%), though factual closure produced zero comments. |
| ep024 | Near Misses | contradiction, scale_ladder | 956 | 46% | 53.7% | 104% | 1 | Contradiction hook drove solid views, but repeating the opening line verbatim in the finale collapsed avg viewed (53.73%) and likes. |
| ep028 | Space Myths, Busted | statement, mystery | 1255 | 54% | 82.1% | 130% | 1 | Punchy myth-busting hook achieved highest views and high avg viewed (82.07%), beating medians across engagement and retention. |
| ep032 | The Universe Is Terrifying | statement, record | 1032 | – | – | – | – | Dramatic cosmic monster hook drove strong velocity and view volume, maintaining steady baseline engagement near median likes. |
| ep036 | Mission Files | statement, story | 1016 | – | – | – | – | Sensory beach-ball hook powered high view velocity, but verbatim repetition of the hook line at the end depressed likes (2.56%). |

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
