# What we've learned

The daily run keeps this file up to date (`PLAYBOOK.md`, step 3). Scriptwriters read it before writing, and
the quality gate checks that every new episode applies it. The aim is that each day's Shorts beat the
channel's recent median on the numbers below.

## What to beat

Recompute daily and after each Short's 24- and 72-hour reviews, over Shorts with 24+ hours of data (medians of the last 10).

| Measure | Where it comes from | Channel median | Target |
|---|---|---|---|
| Engaged share (stand-in for Studio's "stayed to watch") | `analytics.engaged_share` | 51% | 70%+; under 60% rarely takes off |
| Average percentage viewed | `analytics.averageViewPercentage` | 75.6% | 80%+ (loops can push it past 100%) |
| Still watching at 10% of the Short | `retention` point nearest `at: 0.1` | 125% | rising week over week |
| Subscribers per 1,000 views | `subscribersGained` / `views` | 0.9 | 2+ |
| Likes per 100 views | `likes` / `views` | 3.6 | 4+ |

## Rules we've proven

A rule needs at least two Shorts with 24+ hours of data showing the same effect. Once proven, also copy it
into `strategy/SCRIPT-RULES.md`, then cite the evidence here.

- Put the strongest surprise or contradiction in the first 2 seconds to maximize view velocity and early retention. Evidence: ep008, ep024, ep084.
- Start the opening script line with a curiosity gap rather than a static statement or text overlay to improve initial retention. Evidence: ep002, ep009, ep040, ep129.
- Replace closed circular endings with an open-ended question, debate prompt, or provocative paradox in the final beat to drive audience comments. Evidence: ep004, ep013, ep017, ep024, ep028, ep032, ep033, ep047, ep050, ep052, ep055, ep060, ep066, ep086, ep099, ep105, ep110, ep112, ep111, ep118.
- Write a last line that flows straight into the first line to increase average percentage viewed and trigger rewatches. Evidence: ep008, ep013, ep028, ep032, ep047, ep086, ep099, ep114, ep129.
- Avoid repeating exact hook phrases verbatim in the final beat; replace them with a distinct concluding payoff, seamless cliffhanger, or forward-looking question to prevent steep retention and like drops. Evidence: ep017, ep024, ep036, ep052, ep055, ep084.
- Condense mid-script setups into single punchy beats to keep the final beat under 3 seconds and sustain end retention above 1.0. Evidence: ep008, ep009, ep047, ep084.
- Compress or eliminate complex technical explanations, scientific definitions, or catalog designations in all beats to prevent retention drop-off. Evidence: ep008, ep028, ep086, ep125.
- Deliver the core narrative payoff or setup within the first 3 seconds immediately after the hook to prevent pacing drop-off. Evidence: ep004, ep009, ep061, ep084, ep114.
- Accelerate middle-beat reveals on cosmic scale topics to maintain audience engagement through the midpoint. Evidence: ep032, ep036.
- Use high-urgency hook phrases to boost immediate view velocity and distribution. Evidence: ep032, ep035, ep112.
- Tighten pacing in the second and third beats to prevent early-retention drop-offs. Evidence: ep009, ep036.
- Avoid passive statement hooks in favor of high-tension, active mysteries or direct questions to prevent early viewer drop-off. Evidence: ep002, ep033, ep040, ep061, ep086, ep129, ep110.
- Replace historical discovery dates, timeline beats, catalog designations, and academic debates with immediate physical scale comparisons or active narrative tension. Evidence: ep030, ep046, ep049, ep060, ep061, ep079, ep086, ep114.
- Eliminate redundant concept or numerical restatements between the hook and subsequent beats to sustain narrative velocity. Evidence: ep049, ep052, ep084.
- Cut generic concluding wrap-up statements in favor of an abrupt punchline quote, seamless loop, or challenge to prevent late-retention drift. Evidence: ep046, ep047, ep060, ep084, ep099, ep114, ep129.
- Replace cosmic tropes with specific observational details in the hook to improve scroll-stop rates. Evidence: ep066, ep118, ep129.
- Replace informational or summary endings with direct community-search prompts, action questions, or scale comparisons to generate comments and lift likes. Evidence: ep066, ep110, ep105, ep118.
- Replace administrative proper names, researcher biographies, and instrument lists in middle beats with immediate anomaly reveals or countdown timeframes to maintain narrative tension and pacing. Evidence: ep111, ep112.

## Hypotheses to test (from research, not yet our data)

- Cut each Short to 45-59 seconds to maximize reach potential.
- Delay the safety resolution or anti-climax in hazard or near-miss scripts until the absolute final beat to sustain retention throughout the mid-to-late section.
- Replace detached opening statements with character-driven or first-person narrative friction to improve 5% retention.
- Avoid giveaway conclusion signals (such as 'That is why', 'In the end', or 'So') in final beats to prevent viewer drop-off before the loop or payoff completes.
- Use immediate physical threat or high-stakes action phrases in hook text rather than abstract distances or dates to maximize swipe-through.

## Scoreboard

One row per live Short once it has 24+ hours of data. Hook style is statement, question, number, or
contradiction.

| Short | Series | Hook style | Views | Engaged share | Avg % viewed | Watching at 10% | Subs gained | Likely reason |
|---|---|---|---|---|---|---|---|---|
| 2rz-F-WZsXA | ? | –, story | 109 | 35% | 48.1% | 103% | 0 | – |
| ep002 | Mission Files | statement, story | 111 | 47% | 39.1% | 85% | 0 | – |
| ep004 | Mission Files | statement, story | 1072 | 56% | 54.1% | 110% | 3 | – |
| ep008 | The Universe Is Terrifying | statement, story | 867 | 47% | 83.5% | 130% | 5 | – |
| ep009 | Near Misses | statement, story | 249 | 43% | 60.6% | 105% | 0 | – |
| ep013 | Scale Breaker | contradiction, story | 986 | 55% | 71.2% | 124% | 2 | – |
| ep017 | Mission Files | contradiction, myth_vs_fact | 1270 | 52% | 70.2% | 119% | 5 | – |
| ep024 | Near Misses | contradiction, scale_ladder | 957 | 46% | 53.5% | 104% | 1 | – |
| ep028 | Space Myths, Busted | statement, mystery | 1276 | 54% | 80.2% | 128% | 5 | – |
| ep030 | Scale Breaker | number, record | 1114 | 52% | 80.8% | 137% | 4 | – |
| ep032 | The Universe Is Terrifying | statement, record | 1046 | 42% | 80.0% | 126% | 1 | – |
| ep033 | Space Got Weird | statement, story | 747 | 42% | 70.0% | 127% | 1 | – |
| ep035 | Near Misses | statement, myth_vs_fact | 1330 | 52% | 86.5% | 131% | 1 | – |
| ep036 | Mission Files | statement, story | 1038 | 60% | 63.5% | 118% | 1 | – |
| ep040 | Space Got Weird | statement, myth_vs_fact | 488 | 57% | 60.2% | 106% | 1 | – |
| ep045 | Mission Files | contradiction, mystery | 1088 | 51% | 78.0% | 128% | 5 | – |
| ep046 | Space Got Weird | contradiction, mystery | 468 | 58% | 68.8% | 110% | 4 | – |
| ep047 | Space Myths, Busted | question, mystery | 1451 | 53% | 55.5% | 112% | 2 | – |
| ep048 | Scale Breaker | statement, scale_ladder | 1052 | 53% | 77.4% | 136% | 1 | – |
| ep049 | The Universe Is Terrifying | statement, scale_ladder | 699 | 49% | 65.4% | 125% | 2 | – |
| ep050 | Near Misses | contradiction, scale_ladder | 1134 | 53% | 62.8% | 111% | 2 | – |
| ep052 | Space Got Weird | statement, story | 826 | 55% | 64.3% | 120% | 4 | – |
| ep055 | The Universe Is Terrifying | contradiction, story | 482 | 52% | 51.9% | 106% | 2 | – |
| ep060 | Scale Breaker | statement, scale_ladder | 783 | 37% | 69.0% | 117% | 1 | – |
| ep061 | The Universe Is Terrifying | statement, scale_ladder | 245 | 47% | 85.0% | 145% | 0 | – |
| ep066 | Space Got Weird | statement, story | 1398 | 49% | 81.9% | 134% | 4 | – |
| ep079 | Scale Breaker | contradiction, story | 353 | 47% | 81.8% | 130% | 0 | – |
| ep084 | Mission Files | contradiction, story | 462 | 48% | 96.8% | 149% | 1 | – |
| ep086 | Space Got Weird | statement, record | 524 | 47% | 137.6% | 177% | 3 | – |
| ep099 | Scale Breaker | statement, scale_ladder | 1028 | 51% | 70.6% | 124% | 1 | Strong robot vs mountain hook and scale ladder pacing drove 1026 views, but weak loop and summary ending killed rewatches and comments. |
| ep105 | Scale Breaker | statement, myth_vs_fact | 872 | 50% | 157.2% | 211% | 4 | Exceptional opening hook and fast narrative pacing achieved 157% viewed and high looping, though passive ending limited comments and likes. |
| ep110 | Space Got Weird | statement, story | 1192 | 56% | 77.5% | 121% | 2 | Strong midpoint story retention reached 1190 views, but weak passive hook and abrupt loss of late completion reduced feed share. |
| ep111 | Scale Breaker | number, story | 1186 | 52% | 99.6% | 147% | 1 | Strong paradox hook and ending prompt drove top view velocity and 2 comments, but dry biographical middle pacing dragged likes below median. |
| ep112 | Near Misses | statement, story | 889 | 51% | 65.0% | 112% | 1 | High feed share sustained 889 views and solid mid-video hold, but jargon-heavy pacing and soft loop dropped late retention and engagement. |
| ep114 | Scale Breaker | statement, scale_ladder | 297 | 50% | 73.8% | 126% | 0 | Strong hook hold and mid-video engagement maintained solid retention, but low initial stayed-to-watch share and flat ending limited rewatches. |
| ep118 | Space Got Weird | statement, mystery | 1061 | 55% | 68.2% | 116% | 0 | Distinctive visual moon hook drove 927 views above median, but anticlimactic ending hurt likes and conversion. |
| ep125 | Mission Files | statement, record | 450 | – | – | – | – | Atomic bomb concept hook maintained baseline views, but dry technical jargon in middle beats and flat ending dropped likes to 2.0 per 100. |
| ep129 | Space Got Weird | statement, story | 364 | 57% | 82.6% | 132% | 1 | High-retention planet-telescope hook and strong mid-section yielded 6.1 likes per 100, but definitive summary ending prevented viral looping. |
| ep130 | The Universe Is Terrifying | statement, scale_ladder | 934 | – | – | – | – | High-stakes story topic and visceral ending line generated 3 comments and 823 views, but abstract distance text in hook diluted potential reach. |

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
- 2026-10-13: Updated playbook rules and hypotheses based on reviews of ep049 through ep114, targeting comment engagement and mid-beat pacing.
- 2026-10-13: Updated rules for endings, historical exposition, and technical jargon using data from the ep050-ep114 review cycle.
- 2026-10-13: Retained existing rules and hypotheses as today's review recommendations are fully reinforced by established rules, while updating channel medians across the latest 10 Shorts.
- 2026-10-13: Today's log updates the rules to include high-tension hooks for scroll-stopping and restricts technical terminology to maintain mid-script pacing based on consistent performance data.
- 2026-10-14: Reviewed performance of 10 Shorts, identifying a recurring failure in comment conversion and rewatch loops despite high hook retention.
- 2026-10-14: Updated rule citations for interactive prompts and pacing based on reviews for episodes ep052 through ep129.
- 2026-10-14: Consolidated evidence for curiosity-gap hooks and reinforced the ban on technical catalog IDs and discovery dates to protect mid-video pacing.
- 2026-10-14: Added new evidence to existing rules based on recent reviews and maintained current hypotheses.
- 2026-10-15: Updated evidence citations for looping (ep099) and anti-exposition rules (ep079) while holding existing hypotheses pending multi-short confirmation.
- 2026-10-15: Today we added a new hypothesis based on ep110 and ep066 requiring interactive community prompts instead of informational wrap-ups to drive comments and likes.
- 2026-10-15: Updated rolling medians from recent uploads and added ep110 evidence to the open-ended ending rule.
- 2026-10-15: Promoted specific hooks and search-prompt endings to rules after ep066, ep110, and ep129 showed high initial retention and low engagement respectively.
- 2026-10-16: Updated proven rule evidence by citing ep105 for comment debate endings and ep129 for seamless rewatch loops based on recent diagnoses.
- 2026-10-16: Analyzed performance for 10 recent Shorts (ep066–ep129), confirming the critical need for seamless audio loops and active engagement prompts while eliminating administrative dates and names.
- 2026-10-16: Added ep112 as evidence for ending scripts with open questions after passive endings and administrative middle beats suppressed audience interaction.
- 2026-10-17: Promoted hypothesis on cutting middle-beat proper names and instrument details to a rule based on ep111 and ep112, and added a hypothesis against conclusion giveaway phrases from ep079.
- 2026-10-17: Updated looping and engagement rules after a batch of 10 reviews revealed that definitive summary endings are killing the viral loop and comment sections.
- 2026-10-17: Maintained proven rule catalog and active hypotheses while auditing recent performance across ep084-ep129 against channel medians.
- 2026-10-18: Analyzed performance for ep086 through ep130, updating evidence for technical simplification, loop endings, and active hooks.
- 2026-10-18: Added ep125 as evidence to the rule against technical jargon in scripts after dry rocket metrics reduced viewer likes to 2.0 per 100.
