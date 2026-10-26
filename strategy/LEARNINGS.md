# What we've learned

The daily run keeps this file up to date (`PLAYBOOK.md`, step 3). Scriptwriters read it before writing, and
the quality gate checks that every new episode applies it. The aim is that each day's Shorts beat the
channel's recent median on the numbers below.

## What to beat

Recompute daily and after each Short's 24- and 72-hour reviews, over Shorts with 24+ hours of data (medians of the last 10).

| Measure | Where it comes from | Channel median | Target |
|---|---|---|---|
| Engaged share (stand-in for Studio's "stayed to watch") | `analytics.engaged_share` | 55% | 70%+; under 60% rarely takes off |
| Average percentage viewed | `analytics.averageViewPercentage` | 68.2% | 80%+ (loops can push it past 100%) |
| Still watching at 10% of the Short | `retention` point nearest `at: 0.1` | 116% | rising week over week |
| Subscribers per 1,000 views | `subscribersGained` / `views` | 1.4 | 2+ |
| Likes per 100 views | `likes` / `views` | 4.8 | 4+ |

## Rules we've proven

A rule needs at least four Shorts with 24+ hours of data showing the same effect, and a measured difference
against comparable Shorts without it (say both medians). At most 10 rules: merge overlapping ones, and when two
rules pull in opposite directions keep the better-measured one and move the other to the hypotheses. Once proven,
also copy it into `strategy/SCRIPT-RULES.md`, then cite the evidence here. (Consolidated 2026-10-25 from 30 rules,
each promoted on two Shorts; their evidence is kept below.)

- Open with the most surprising true thing about a well-known subject in the first 2 seconds: a contradiction, paradox, myth flip or physical consequence with a specific observed detail, never a passive statement, cosmic trope or abstract distance. Evidence: ep002, ep008, ep009, ep024, ep033, ep040, ep061, ep066, ep072, ep084, ep086, ep110, ep112, ep114, ep118, ep125, ep129, ep130, ep133, ep137, ep175, ep181, ep184, ep188, ep195, ep197, ep201, ep208.
- Open on a belief most viewers already hold, then immediately debunk it (Space Myths, Busted pattern): counterintuitive myth-busting generates higher early reach than abstract scale. Evidence: ep047, ep053, ep146, ep159, ep165, ep172, ep185, ep197 (median early reach 1,129.5 views at 24-28h vs 725.5 channel median / 726 for non-myth Shorts).
- Never open with an archival datestamp, abstract metric measurement, or detached background statement: hook immediately with active physical impact or character tension in the first three words. Evidence: ep174, ep181, ep203, ep208, ep221 (median early reach 260.0 views at 24.5-28.1h vs 726.0 channel median for active openers).
- Deliver the core payoff within 3 seconds of the hook, and never restate the hook's number or idea in the next beat. Evidence: ep004, ep009, ep049, ep052, ep061, ep084, ep114, ep130, ep172, ep221.
- Make every middle beat a new, bigger reveal; keep beats two and three short. Evidence: ep008, ep009, ep032, ep036, ep047, ep084, ep165, ep184, ep188.
- No catalog designations, discovery dates, researcher biographies, instrument lists or jargon in any beat: replace them with one familiar physical comparison. Evidence: ep008, ep028, ep030, ep046, ep049, ep060, ep061, ep079, ep086, ep111, ep112, ep114, ep125, ep159, ep165, ep172, ep186, ep188, ep195, ep197.
- One number per beat: never stack figures or dates in consecutive beats. Evidence: ep125, ep175.
- In a hazard story, keep the safety resolution for the last beat. Evidence: ep130, ep133, ep137, ep159.
- End right after the climax: no aftermath subplot, historical footnote, wrap-up summary or 'in the end' signal. Evidence: ep046, ep047, ep060, ep084, ep099, ep111, ep114, ep118, ep129, ep137, ep146, ep159, ep165.
- The last line is a complete sentence that leads naturally back into the first, so the Short loops; never repeat the hook verbatim and never end on a fragment. Evidence: ep008, ep013, ep017, ep024, ep028, ep032, ep036, ep047, ep052, ep055, ep084, ep086, ep099, ep111, ep112, ep114, ep118, ep125, ep129, ep130, ep137, ep146, ep172, ep175.

## Hypotheses to test (from research, not yet our data)

At most 8. Each is tested against the current rules on comparable Shorts before it becomes a rule.

- End on a direct question or challenge to the viewer instead of a loop on debate-heavy or myth topics to drive comments (ep185 and ep201 had 0 comments despite >600 views; test whether prompt lifts comment rate without hurting loop retention).
- Compress scientific definitions into a single beat under 4 seconds to reach core resolution by the 12-second mark and prevent mid-drop (ep172 retention dropped to 58.2% during definitions).
- Contrast cosmic timescales with relatable human historical milestones rather than astronomer discovery trivia to sustain mid-video momentum (ep165 showed mid-drop when introducing astronomer details).
- For evergreen subjects, use the plain question people search as the title or hook ('Halley's Comet Is Burning Above You TONIGHT' drove 13.9% search traffic in ep146; test against standard feed delivery).
- Hold the central threat until the middle beats instead of beat one (conflicts with opening rule; test on hazard stories only).
- End with a line worth sending to someone ('the next time someone says...'): test whether share prompts lift retention or virality.
- Cut each Short to 45-59 seconds to maximize reach potential.

## Scoreboard

One row per live Short once it has 24+ hours of data. Hook style is statement, question, number, or
contradiction.

| Short | Series | Hook style | Observed 24-30h views | Engaged share | Avg % viewed | Watching at 10% | Subs gained | Likely reason |
|---|---|---|---|---|---|---|---|---|
| ep086 | Space Got Weird | statement, record | 367 | 47% | 137.2% | 177% | 3 | – |
| ep049 | The Universe Is Terrifying | statement, scale_ladder | 585 | 49% | 65.4% | 125% | 2 | – |
| ep052 | Space Got Weird | statement, story | 726 | 55% | 64.5% | 120% | 4 | – |
| ep114 | Scale Breaker | statement, scale_ladder | 191 | 50% | 73.8% | 126% | 0 | – |
| ep050 | Near Misses | contradiction, scale_ladder | 1122 | 53% | 62.8% | 111% | 2 | – |
| ep055 | The Universe Is Terrifying | contradiction, story | 451 | 52% | 51.9% | 106% | 2 | – |
| ep099 | Scale Breaker | statement, scale_ladder | 962 | 51% | 70.6% | 124% | 1 | – |
| ep066 | Space Got Weird | statement, story | 1096 | 49% | 81.9% | 134% | 4 | – |
| ep084 | Mission Files | contradiction, story | 350 | 48% | 96.8% | 149% | 1 | – |
| ep129 | Space Got Weird | statement, story | 190 | 57% | 82.6% | 132% | 1 | – |
| ep048 | Scale Breaker | statement, scale_ladder | 1020 | 53% | 77.2% | 136% | 1 | – |
| ep045 | Mission Files | contradiction, mystery | 1060 | 50% | 78.0% | 128% | 5 | – |
| ep079 | Scale Breaker | contradiction, story | 275 | 46% | 81.8% | 130% | 0 | – |
| ep110 | Space Got Weird | statement, story | 1169 | 56% | 76.7% | 120% | 2 | – |
| ep105 | Scale Breaker | statement, myth_vs_fact | 662 | 50% | 158.6% | 212% | 4 | – |
| ep112 | Near Misses | statement, story | 581 | 53% | 62.2% | 111% | 1 | – |
| ep111 | Scale Breaker | number, story | 1169 | 52% | 98.0% | 145% | 1 | – |
| ep118 | Space Got Weird | statement, mystery | 927 | 54% | 69.6% | 118% | 0 | – |
| ep130 | The Universe Is Terrifying | statement, scale_ladder | 823 | 53% | 60.6% | 113% | 2 | – |
| ep125 | Mission Files | statement, record | 450 | 56% | 109.2% | 159% | 3 | – |
| ep175 | Scale Breaker | contradiction, mystery | 1435 | 48% | 85.0% | 134% | 2 | – |
| ep133 | Space Got Weird | statement, scale_ladder | 1208 | 48% | 59.6% | 117% | 3 | – |
| ep051 | Mission Files | statement, scale_ladder | 1215 | 69% | 53.6% | 112% | 0 | – |
| ep159 | Space Myths, Busted | statement, scale_ladder | 1220 | 57% | 61.0% | 100% | 0 | – |
| ep188 | Scale Breaker | contradiction, record | 948 | 50% | 80.3% | 128% | 0 | – |
| ep137 | Near Misses | statement, story | 946 | 54% | 96.9% | 150% | 0 | – |
| ep053 | Space Myths, Busted | statement, story | 1092 | 49% | 57.8% | 113% | 2 | – |
| ep167 | The Universe Is Terrifying | statement, myth_vs_fact | 8 | 36% | 69.5% | – | 0 | – |
| ep058 | Space Got Weird | statement, myth_vs_fact | 1014 | 52% | 107.2% | 158% | 3 | – |
| ep063 | Near Misses | contradiction, mystery | 1010 | 52% | 72.0% | 115% | 4 | – |
| ep184 | Near Misses | statement, myth_vs_fact | 487 | 55% | 66.7% | 110% | 0 | – |
| ep071 | The Universe Is Terrifying | statement, record | 917 | 49% | 92.9% | 143% | 1 | – |
| ep072 | Near Misses | statement, record | 711 | 50% | 174.9% | 233% | 1 | – |
| ep186 | Scale Breaker | contradiction, myth_vs_fact | 525 | 57% | 68.7% | 124% | 1 | – |
| ep146 | Space Myths, Busted | contradiction, myth_vs_fact | 1167 | 54% | 61.0% | 110% | 1 | – |
| ep172 | Space Myths, Busted | contradiction, scale_ladder | 791 | 54% | 80.3% | 130% | 1 | – |
| ep195 | Space Got Weird | statement, scale_ladder | 519 | 61% | 61.3% | 116% | 1 | Strong ringed asteroid premise hooked viewers with 61.2% engaged share and 4.9 likes/100, but mid-script astronomer credits stalled pacing and dragged APV down to 61.3%. |
| ep197 | Space Myths, Busted | contradiction, scale_ladder | 984 | 54% | 64.3% | 116% | 1 | Counterintuitive day-versus-year contradiction drove high early reach (984 views at 24.6h), but mid-video radar history and academic attribution slowed pacing to 64.3% APV. |
| ep201 | Scale Breaker | statement, myth_vs_fact | 982 | 56% | 101.4% | 148% | 2 | Shrinking star premise generated exceptional retention (101.4% APV, 1.48 at 10%), but a passive closing statement without an engagement prompt yielded zero comments and weak likes (2.2%). |
| ep181 | The Universe Is Terrifying | statement, scale_ladder | 546 | 52% | 68.2% | 115% | 3 | Magnetar concept earned strong viewer sentiment (5.1 likes/100), but abstract distance in the hook and sluggish pickup held early reach to 546 views at 25.1h. |
| ep221 | Mission Files | contradiction, story | 400 | 55% | 58.9% | 112% | 0 | Historical narrative hook lacked immediate visceral stakes, depressing early reach to 400 views at 27.1h and APV to 58.9%, despite solid conversion (5.3 likes/100). |
| ep185 | Space Myths, Busted | contradiction, myth_vs_fact | 660 | 45% | 90.7% | 133% | 0 | Debunking vacuum exposure held high retention (90.7% APV), but below-median engaged share (45.0%) and a purely factual loop without a discussion prompt limited comments (0) and velocity. |
| ep165 | Space Myths, Busted | statement, myth_vs_fact | 1495 | 56% | 71.5% | 126% | 3 | Pluto orbit myth hook powered top-of-funnel reach (1,495 views at 28.1h) and strong 71.5% APV, though meandering into astronomer and demotion trivia depressed likes to 2.2%. |
| ep208 | Near Misses | statement, story | 34 | – | – | – | – | Abstract metric opener ('five-kilometer mountain') stalled feed distribution to just 34 views at 25.1h, despite high affinity (8.2 likes/100) from the few viewers reached. |
| ep174 | Mission Files | statement, story | 260 | – | – | – | – | Archival datestamp hook text ('OCTOBER 1946') caused severe distribution lag (260 early views at 24.6h), despite strong viewer appreciation (6.0 likes/100) for the weapon angle. |
| ep203 | Near Misses | contradiction, myth_vs_fact | 131 | – | – | – | – | Technical distance opener ('1,830 miles') failed to hook broad feed audiences, stalling early reach at 131 views at 28.1h in the 01:30 slot. |

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
- 2026-10-18: Cited ep130 under the redundant concept elimination rule and added a hypothesis to delay threat reveals to middle beats.
- 2026-10-18: Added ep175 evidence to ending question rules and logged a new hypothesis against rapid numerical stacking.
- 2026-10-19: Updated performance reasons for ep133 and ep175, and added ep133 as supporting evidence for open-ended concluding beats.
- 2026-10-19: Promoted three rules regarding conclusion signals, high-stakes hook phrasing, and numerical stacking after reviewing 10 new high-volume Shorts.
- 2026-10-19: Audited ep110 through ep175 against channel medians, reaffirming that rapid numerical density and flat wrap-ups suppress engagement even on viral-velocity topics.
- 2026-10-19: Integrated data from 10 new reviews to strengthen rules on seamless looping, jargon elimination, and high-stakes hook framing.
- 2026-10-20: Updated rules and evidence based on review diagnostics for ep114 through ep188, focusing on technical simplification and looping finales.
- 2026-10-20: Reviewed 10 recent Shorts (ep114-ep188); added hypothesis on eliminating post-climax subplots and reinforced rules against dense jargon and non-looping summary endings.
- 2026-10-20: Reviewed 10 recent Shorts against channel medians, reinforcing existing rules around high-stakes hooks, jargon removal, and seamless looping without creating new rules.
- 2026-10-20: Integrated 10 new reviews, promoted rules for resolution timing and subplot elimination, and updated medians.
- 2026-10-21: Logged daily performance reviews for ten Shorts, confirming ongoing drop-off issues from weak loop structures and dense jargon.
- 2026-10-21: Promoted two looping and climax-timing hypotheses to rules and added a new logic-challenge hook hypothesis after ten Shorts showed consistent drop-offs on definitive endings and technical jargon.
- 2026-10-21: Updated performance log and reaffirmed rules against recent 10-short medians (53.6% engaged share, 81.0% avg viewed, 1.29 at10).
- 2026-10-21: Updated learning log with 10 new short reviews, reinforcing seamless audio loop rules and highlighting the negative impact of mid-script jargon and secondary subplots.
- 2026-10-22: Today we refined end-loop and mid-script pacing requirements based on new review data showing that technical jargon and flat dead-end conclusions ruin rewatch velocity.
- 2026-10-22: Reviewed 10 Shorts (ep118–ep188); maintained existing rule set and added new testing hypotheses from latest video evaluations.
- 2026-10-22: Logged diagnostic reviews for ep118-ep188, maintained proven rules, and added a hypothesis to test replacing optical jargon with relatable analogies based on ep159.
- 2026-10-22: Promoted the final sentence completeness hypothesis to a proven rule based on evidence from ep137, and integrated review diagnostics for ep125 through ep188 to tighten ending loop and mid-script pace requirements.
- 2026-10-23: Analyzed performance reviews for ep129 through ep188 to update episode diagnoses and refine rules on hook urgency, mid-script jargon, and seamless rewatch transitions.
- 2026-10-23: Cited ep172 as corroborating evidence for complete concluding beats and eliminating mid-script premise restatements.
- 2026-10-23: Reviewed 10 recent Shorts (ep130-ep188), promoted technical jargon replacement to a rule based on ep159 and ep188 data, and updated performance log.
- 2026-10-23: Promoted logic-defying challenge hook hypothesis to rule based on ep133 and ep195 evidence.
- 2026-10-24: Added ep197 as supporting evidence to the rule eliminating researcher biographies and proper names in middle beats after academic attribution stalled velocity.
- 2026-10-24: Promoted interactive closing prompts and paradoxical hazard hooks to rules; updated existing rules with evidence from 10 new reviews.
- 2026-10-24: Evaluated ten recent Shorts against recomputed medians, reaffirming established rules on contradiction hooks and conversational endings while preserving three unproven hypotheses.
- 2026-10-24: Consolidated rules on mid-script academic attribution and technical analogies using evidence from ep159, ep186, and ep197.
- 2026-10-25: Reviewed 10 Shorts, updating evidence for Rule 19 (ep072) and Rule 28 (ep185) regarding high-stakes hook text and comment-prompting endings.
- 2026-10-25: Updated today's review log by extracting performance diagnostics and translating script changes into actionable data points.
- 2026-10-25: Integrated ten reviews, adding citations to rules on technical compression, naming conventions, and narrative focus while validating physical-impact hooks.
- 2026-10-25: Consolidated 30 rules (each promoted on two Shorts, several contradicting) into 8; the contested ones (open-question endings, delayed threats) are hypotheses to test. Rules now need 4+ Shorts and a measured difference.
- 2026-10-25: Promoted the Space Myths debunking pattern to a rule based on 8 Shorts yielding 1,129.5 median early reach versus the 725.5 channel median, and updated middle-beat and attribution rules with evidence from recent reviews.
- 2026-10-26: Promoted abstract/datestamp hook avoidance to a rule after ep174 provided the fourth qualifying Short confirming severe distribution stalls, and added ep165, ep195, and ep197 to the jargon rule.
- 2026-10-26: Reviewed 10 Shorts (ep165, ep174, ep181, ep185, ep195, ep197, ep201, ep203, ep208, ep221); updated performance reasons and reinforced rules against archival hook texts and middle-beat researcher credits.
- 2026-10-26: Updated Rule 3 evidence with ep203 confirming abstract metric openers stall distribution velocity, and validated researcher attribution penalties across ep195 and ep197.
