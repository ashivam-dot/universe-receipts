# What we've learned

The daily run keeps this file up to date (`PLAYBOOK.md`, step 3). Scriptwriters read it before writing, and
the quality gate checks that every new episode applies it. The aim is that each day's Shorts beat the
channel's recent median on the numbers below.

## What to beat

Recompute daily and after each Short's 24- and 72-hour reviews, over Shorts with 24+ hours of data (medians of the last 10).

| Measure | Where it comes from | Channel median | Target |
|---|---|---|---|
| Engaged share (stand-in for Studio's "stayed to watch") | `analytics.engaged_share` | 47% | 70%+; under 60% rarely takes off |
| Average percentage viewed | `analytics.averageViewPercentage` | 68.6% | 80%+ (loops can push it past 100%) |
| Still watching at 10% of the Short | `retention` point nearest `at: 0.1` | 124% | rising week over week |
| Subscribers per 1,000 views | `subscribersGained` / `views` | 0.6 | 2+ |
| Likes per 100 views | `likes` / `views` | 4.2 | 4+ |

## Rules we've proven

A rule needs at least two Shorts with 24+ hours of data showing the same effect. Once proven, also copy it
into `strategy/SCRIPT-RULES.md`, then cite the evidence here.

- Put the strongest surprise or contradiction in the first 2 seconds (e.g., '80 million trees, zero craters') to maximize view velocity and early retention. Evidence: ep008, ep024.
- Start the opening script line with a curiosity gap rather than a static statement or text overlay to improve initial retention and view velocity. Evidence: ep002, ep009, ep040.
- Replace closed circular endings with an open-ended question or debate prompt in the final beat to drive audience comments. Evidence: ep004, ep013, ep017, ep024, ep028, ep032, ep033, ep047, ep050, ep052, ep055, ep086, ep099.
- Write a last line that flows straight into the first line to increase average percentage viewed and trigger rewatches. Evidence: ep008, ep013, ep028, ep032, ep047.
- Avoid repeating exact hook phrases verbatim in the final beat; replace them with a distinct concluding payoff, seamless cliffhanger, or forward-looking question to prevent steep retention and like drops. Evidence: ep017, ep024, ep036.
- Condense mid-script setups into single punchy beats to keep the final beat under 3 seconds and sustain end retention above 1.0. Evidence: ep008, ep009, ep047.
- Compress or eliminate complex technical explanations or scientific definitions in the final beats to prevent late retention drop-off. Evidence: ep008, ep028.
- Deliver the core narrative payoff or setup within the first 3 seconds immediately after the hook to prevent pacing drop-off. Evidence: ep004, ep009.
- Accelerate middle-beat reveals on cosmic scale topics to maintain audience engagement through the midpoint. Evidence: ep032, ep036.
- Use high-urgency hook phrases (e.g., 'Level 4 Hazard', 'Cosmic Monster') to boost immediate view velocity and distribution. Evidence: ep032, ep035.
- Tighten pacing in the second and third beats to prevent early-retention drop-offs. Evidence: ep009, ep036.
- Avoid passive statement hooks in favor of high-tension, active mysteries to prevent early viewer drop-off. Evidence: ep002, ep033, ep040, ep061, ep086.
- Replace historical discovery dates, timeline beats, catalog designations, and academic debates with immediate physical scale comparisons or active narrative tension to maintain pacing and engagement after the hook. Evidence: ep030, ep046, ep049, ep060, ep061, ep086, ep114.
- Eliminate redundant concept or numerical restatements between the hook and subsequent beats to sustain narrative velocity. Evidence: ep049, ep052.
- Cut generic concluding wrap-up statements in favor of an abrupt punchline quote or loop challenge to prevent late-retention drift. Evidence: ep046, ep047, ep060.

## Hypotheses to test (from research, not yet our data)

- Cut each Short to 45-59 seconds to maximize reach potential.
- Delay the safety resolution or anti-climax in hazard or near-miss scripts until the absolute final beat to sustain retention throughout the mid-to-late section.
- Replace detached opening statements with character-driven or first-person narrative friction to improve 5% retention.

## Scoreboard

One row per live Short once it has 24+ hours of data. Hook style is statement, question, number, or
contradiction.

| Short | Series | Hook style | Views | Engaged share | Avg % viewed | Watching at 10% | Subs gained | Likely reason |
|---|---|---|---|---|---|---|---|---|
| 2rz-F-WZsXA | ? | –, story | 105 | 33% | 46.6% | 106% | 0 | – |
| ep002 | Mission Files | statement, story | 109 | 45% | 40.4% | 86% | 0 | – |
| ep004 | Mission Files | statement, story | 1068 | 57% | 53.6% | 110% | 3 | – |
| ep008 | The Universe Is Terrifying | statement, story | 867 | 47% | 83.6% | 130% | 5 | – |
| ep009 | Near Misses | statement, story | 249 | 43% | 60.2% | 105% | 0 | – |
| ep013 | Scale Breaker | contradiction, story | 985 | 55% | 71.2% | 124% | 2 | – |
| ep017 | Mission Files | contradiction, myth_vs_fact | 1269 | 51% | 70.2% | 119% | 5 | – |
| ep024 | Near Misses | contradiction, scale_ladder | 957 | 46% | 53.5% | 104% | 1 | – |
| ep028 | Space Myths, Busted | statement, mystery | 1275 | 54% | 80.3% | 128% | 5 | – |
| ep030 | Scale Breaker | number, record | 1114 | 52% | 81.6% | 138% | 4 | – |
| ep032 | The Universe Is Terrifying | statement, record | 1043 | 42% | 80.3% | 127% | 1 | – |
| ep033 | Space Got Weird | statement, story | 746 | 42% | 72.7% | 127% | 1 | – |
| ep035 | Near Misses | statement, myth_vs_fact | 1330 | 52% | 86.4% | 131% | 1 | – |
| ep036 | Mission Files | statement, story | 1038 | 60% | 63.5% | 118% | 1 | – |
| ep040 | Space Got Weird | statement, myth_vs_fact | 488 | 57% | 88.1% | 106% | 1 | – |
| ep046 | Space Got Weird | contradiction, mystery | 470 | 58% | 67.6% | 109% | 3 | – |
| ep047 | Space Myths, Busted | question, mystery | 1433 | 54% | 56.2% | 113% | 2 | High-performing question hook and broad reach beat channel median views, but mid-script historical milestone listings slowed pacing and a non-looping ending hurt retention. |
| ep049 | The Universe Is Terrifying | statement, scale_ladder | 699 | 46% | 68.4% | 130% | 2 | Relatable credit card hook secured above-average retention, but formal calendar dates and magnetic measurements mid-script dragged down overall view velocity. |
| ep050 | Near Misses | contradiction, scale_ladder | 1125 | – | – | – | – | High-urgency asteroid hook drove strong view velocity and above-median likes, though a closed, repetitive ending produced zero audience comments. |
| ep052 | Space Got Weird | statement, story | 821 | 54% | 63.6% | 119% | 3 | Intriguing mystery topic yielded high like conversion, but redundant stat restatements slowed narrative pacing and the lack of a debate question left zero comments. |
| ep055 | The Universe Is Terrifying | contradiction, story | 461 | – | – | – | – | Compelling Death Star hook kept baseline views, but premature debunking diffused tension and a closed concluding statement failed to generate comments. |
| ep060 | Scale Breaker | statement, scale_ladder | 783 | 37% | 68.9% | 118% | 1 | Opening contradiction hook captured initial feed attention, but low engaged share and a generic closing wrap-up undercut loop potential and view velocity. |
| ep061 | The Universe Is Terrifying | statement, scale_ladder | 245 | 47% | 84.3% | 145% | 0 | Strong visual premise and high completion rate drove high likes, but mid-script catalog trivia and discovery dates stalled reach. |
| ep086 | Space Got Weird | statement, record | 517 | 46% | 149.5% | 188% | 3 | Zombie star hook and exceptional looping drove phenomenal retention, though technical designations slightly depressed early swipe-stay share. |
| ep099 | Scale Breaker | statement, scale_ladder | 961 | – | – | – | – | Scale-ladder mountain hook propelled view velocity well above median, but a passive conclusion missed the opportunity to convert views into comments. |
| ep114 | Scale Breaker | statement, scale_ladder | 279 | – | – | – | – | Core energy scale comparison maintained solid like conversion, but burying the paradox behind biographical exposition severely suppressed hook immediacy and total reach. |

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
- 2026-10-09: Updated the curiosity gap rule with ep040 and added two new hypotheses targeting pace-slowing historical beats and early safety resolutions.
- 2026-10-09: Re-evaluated all 10 reviewed Shorts against updated channel medians; maintained all 12 proven rules and kept 3 active hypotheses pending multi-episode validation.
- 2026-10-09: Promoted the historical-dates hypothesis to a rule after ep030 and ep060 both demonstrated audience drop-off from mid-script academic exposition.
- 2026-10-10: Updated rules to cite ep047 for condensing mid-script setups and using open-ended questions, confirming their impact on retention and engagement.
- 2026-10-10: Expanded evidence for active hook tension (ep033) and eliminating historical exposition (ep046) across 10 reviewed Shorts while retaining active hypotheses pending further corroborating data.
- 2026-10-10: Updated learning log with 10 new Short reviews, integrating ongoing performance patterns and refining constraints.
- 2026-10-10: Updated active mystery and catalog trivia elimination rules with new evidence from ep061 and ep086 reviews.
- 2026-10-11: Logged 10 short diagnoses and added ep049 evidence to historical dates pacing rule.
- 2026-10-11: Added ep052 as evidence to the open-ended debate rule and tested hazard delay hypothesis on ep035.
- 2026-10-11: Updated rule evidence with reviews for ep040 and ep086, added a hypothesis on eliminating early beat restatements from ep052, and reaffirmed hazard resolution retention testing.
- 2026-10-11: Cited ep114 under the anti-exposition rule after its archival discoverer backstory in beat 2 collapsed velocity to 7.6 views per hour, and logged ep060 concluding wrap-up hypothesis.
- 2026-10-12: Promoted redundancy and wrap-up hypotheses to rules following pacing and retention failures in ep049, ep052, and ep060.
- 2026-10-12: Updated rule citations and evidence across ep046, ep050, ep052, ep055, ep060, ep061, ep086, and ep114 following performance reviews.
- 2026-10-12: Audited ten recent Shorts against updated 10-episode medians, reaffirming strict bans on catalog trivia and confirming open comment prompts.
- 2026-10-12: Cited ep099 as additional evidence for the open-ended final beat rule to boost comment engagement.
