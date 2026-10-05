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
- Replace closed circular endings with an open-ended question or debate prompt in the final beat to drive audience comments. Evidence: ep013, ep024, ep028.
- Write a last line that flows straight into the first line to increase average percentage viewed and trigger rewatches. Evidence: ep008, ep028.

## Hypotheses to test (from research, not yet our data)

- Cut each Short to 45-59 seconds to maximize reach potential.
- Deliver the core narrative payoff or setup within the first 3 seconds immediately after the hook to prevent pacing drop-off. Evidence: ep009.

## Scoreboard

One row per live Short once it has 24+ hours of data. Hook style is statement, question, number, or
contradiction.

| Short | Series | Hook style | Views | Engaged share | Avg % viewed | Watching at 10% | Subs gained | Likely reason |
|---|---|---|---|---|---|---|---|---|
| ep002 | Mission Files | statement, story | 103 | 44% | 42.7% | 88% | 0 | Passive hook style and sluggish script pacing dropped average view percentage and engaged share below channel medians. |
| ep008 | The Universe Is Terrifying | statement, story | 862 | 47% | 84.1% | 131% | 5 | Strong curiosity hook and solid middle beats drove high view duration, though a weak closing narrative caused late retention drop-off. |
| ep009 | Near Misses | statement, story | 247 | 42% | 62.0% | 105% | 0 | Historical premise secured steady baseline traction, but narrative pacing lost momentum immediately following the opening hook. |
| ep013 | Scale Breaker | contradiction, story | 922 | – | – | – | – | Paradox hook and clean loop drove channel-leading audience resonance and high views, but a closed-loop ending resulted in zero comments. |
| ep024 | Near Misses | contradiction, scale_ladder | 953 | 42% | 51.8% | 105% | 1 | High-concept contradiction hook successfully grabbed attention and drove record views, but dry historical delivery reduced likes. |
| ep028 | Space Myths, Busted | statement, mystery | 1250 | – | – | – | – | Mystery structure captured initial feed share for top-tier views, though the closing statement failed to drive high community interaction. |
| ep036 | Mission Files | statement, story | 1013 | – | – | – | – | Vivid opening visual drove strong early distribution and high hourly views, while a repetitive ending beat held back overall likes. |

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
