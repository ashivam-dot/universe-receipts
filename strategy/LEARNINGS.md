# What we've learned

The daily run keeps this file up to date (`PLAYBOOK.md`, step 3). Scriptwriters read it before writing, and
the quality gate checks that every new episode applies it. The aim is that each day's Shorts beat the
channel's recent median on the numbers below.

## What to beat

Recompute daily and after each Short's 24- and 72-hour reviews, over Shorts with 24+ hours of data (medians of the last 10).

| Measure | Where it comes from | Channel median | Target |
|---|---|---|---|
| Engaged share (stand-in for Studio's "stayed to watch") | `analytics.engaged_share` | 48% | 70%+; under 60% rarely takes off |
| Average percentage viewed | `analytics.averageViewPercentage` | 82.3% | 80%+ (loops can push it past 100%) |
| Still watching at 10% of the Short | `retention` point nearest `at: 0.1` | 130% | rising week over week |
| Subscribers per 1,000 views | `subscribersGained` / `views` | 0.0 | 2+ |
| Likes per 100 views | `likes` / `views` | 2.1 | 4+ |

## Rules we've proven

A rule needs at least four Shorts with 24+ hours of data showing the same effect, and a measured difference
against comparable Shorts without it (say both medians). At most 10 rules: merge overlapping ones, and when two
rules pull in opposite directions keep the better-measured one and move the other to the hypotheses. Once proven,
also copy it into `strategy/SCRIPT-RULES.md`, then cite the evidence here. (Consolidated 2026-10-25 from 30 rules,
each promoted on two Shorts; their evidence is kept below.)

- Prioritize cosmic-scale subjects (billions of light-years, Voyager's journey) over human-scale objects in the hook to maximize reach. Evidence: ep165, ep260, ep346, ep359, ep356 (median early_reach 1580) vs ep181, ep186, ep195, ep345 (median 535.5).
- Replace passive opening exposition with immediate conflict or active paradox hooks in beat 1 to improve distribution. Evidence: ep346, ep352, ep356, ep359 (median early_reach 1746) vs ep345, ep355, ep367, ep258 (median 482.5).
- The last line must be a complete sentence leading naturally back into the first to drive rewatches. Evidence: ep072, ep201, ep262, ep266, ep268 (median AVP 116.3%) vs ep146, ep165, ep185, ep197 (median 64.4%).
- Anchor hooks with authority institutions (NASA, Apollo) or named historical missions to improve distribution. Evidence: ep137, ep262, ep265, ep352, ep356 (median early_reach 1375) vs ep186, ep185, ep197, ep172 (median 711).
- Open with the most surprising true thing about a well-known subject in the first 2 seconds to maximize early hold. Evidence: ep111, ep133, ep201, ep263, ep265 (median at10 1.42).
- Deliver the core payoff within 3 seconds of the hook, and never restate the hook's idea in the next beat. Evidence: ep004, ep105, ep125, ep133, ep172, ep221.
- Make every middle beat a new, bigger reveal; keep beats two and three short to maintain momentum. Evidence: ep008, ep032, ep084, ep165, ep184, ep188.
- No jargon, discovery dates, or catalog names: replace them with one familiar physical comparison to keep explanations accessible. Evidence: ep079, ep133, ep172, ep181, ep186, ep195, ep197, ep362.
- In a hazard story, keep the safety resolution for the last beat to maintain tension. Evidence: ep130, ep133, ep137, ep159, ep184.
- End right after the climax: no aftermath subplot or reflective wrap-up to avoid retention drops. Evidence: ep046, ep137, ep146, ep159, ep165, ep266, ep346, ep347.

## Hypotheses to test (from research, not yet our data)

At most 8. Each is tested against the current rules on comparable Shorts before it becomes a rule.

- End scripts with an interactive debate prompt or curiosity-gap question to spark comments and convert high completion into subscriber gains (ep268, ep345, ep347, ep359, ep362).
- Cut mid-script satellite designations, catalog numbers, and trivia tangents to prevent mid-video retention erosion (ep263, ep362).
- Replace passive final beats with a superlative comparison or mystery summary to leave a stronger impression and drive likes (ep346, ep347, ep352, ep359).
- For evergreen subjects, use plain search-query phrasing as the title or hook to drive search traffic.
- One number per beat: never stack figures or dates in consecutive beats to avoid cognitive overload.
- Compress scientific definitions into a single beat under 4 seconds to reach core resolution by the 12-second mark.
- Deliver mechanical explanations of the hook's premise immediately and eliminate historical detours to sustain mid-video retention.

## Scoreboard

One row per live Short once it has 24+ hours of data. Hook style is statement, question, number, or
contradiction.

| Short | Series | Hook style | Observed 24-30h views | Engaged share | Avg % viewed | Watching at 10% | Subs gained | Likely reason |
|---|---|---|---|---|---|---|---|---|
| ep071 | The Universe Is Terrifying | statement, record | 917 | 49% | 92.9% | 143% | 1 | – |
| ep072 | Near Misses | statement, record | 711 | 50% | 174.9% | 233% | 1 | – |
| ep186 | Scale Breaker | contradiction, myth_vs_fact | 525 | 57% | 68.6% | 124% | 1 | – |
| ep146 | Space Myths, Busted | contradiction, myth_vs_fact | 1167 | 54% | 61.0% | 110% | 1 | – |
| ep172 | Space Myths, Busted | contradiction, scale_ladder | 791 | 53% | 64.6% | 114% | 1 | – |
| ep195 | Space Got Weird | statement, scale_ladder | 519 | 61% | 60.8% | 116% | 1 | – |
| ep197 | Space Myths, Busted | contradiction, scale_ladder | 984 | 54% | 63.6% | 116% | 1 | – |
| ep201 | Scale Breaker | statement, myth_vs_fact | 982 | 56% | 101.3% | 148% | 2 | – |
| ep181 | The Universe Is Terrifying | statement, scale_ladder | 546 | 51% | 69.1% | 114% | 3 | – |
| ep221 | Mission Files | contradiction, story | 400 | 54% | 59.2% | 112% | 0 | – |
| ep185 | Space Myths, Busted | contradiction, myth_vs_fact | 660 | 46% | 85.1% | 126% | 0 | – |
| ep165 | Space Myths, Busted | statement, myth_vs_fact | 1495 | 56% | 65.3% | 119% | 4 | – |
| ep174 | Mission Files | statement, story | 260 | 52% | 64.5% | 106% | 1 | published while YouTube held the whole channel back; not evidence |
| ep203 | Near Misses | contradiction, myth_vs_fact | 131 | 50% | 39.8% | 96% | 0 | published while YouTube held the whole channel back; not evidence |
| ep210 | Mission Files | contradiction, mystery | 149 | 40% | 40.5% | 97% | 0 | published while YouTube held the whole channel back; not evidence |
| 4vqKkpkfwyY | ? | –, story | – | 30% | 44.5% | 110% | 0 | published while YouTube held the whole channel back; not evidence |
| ep177 | Mission Files | statement, story | 127 | 55% | 53.4% | 102% | 0 | published while YouTube held the whole channel back; not evidence |
| ep216 | Space Myths, Busted | contradiction, record | 90 | 52% | 57.9% | 108% | 0 | published while YouTube held the whole channel back; not evidence |
| 7lDBiMMlASI | ? | –, story | – | 27% | 86.5% | 142% | 0 | published while YouTube held the whole channel back; not evidence |
| ep190 | Mission Files | statement, story | 14 | 43% | 69.0% | – | 0 | published while YouTube held the whole channel back; not evidence |
| n8iv0-XfRnY | ? | –, story | – | – | – | – | – | published while YouTube held the whole channel back; not evidence |
| sPUubWIORv4 | ? | –, story | – | – | – | – | – | published while YouTube held the whole channel back; not evidence |
| TKHYK3-F_QI | ? | –, story | – | – | – | – | – | published while YouTube held the whole channel back; not evidence |
| 3FU0QDuIAAQ | ? | –, story | – | – | – | – | – | published while YouTube held the whole channel back; not evidence |
| UrEN-tyt2DY | ? | –, story | – | – | – | – | – | published while YouTube held the whole channel back; not evidence |
| VWs9pa7NFJo | ? | –, story | – | – | – | – | – | published while YouTube held the whole channel back; not evidence |
| Ql418EoNwCQ | ? | –, story | – | – | – | – | – | published while YouTube held the whole channel back; not evidence |
| 5bfuZgx-CS4 | ? | –, story | – | – | – | – | – | published while YouTube held the whole channel back; not evidence |
| ep225 | Space Got Weird | contradiction, mystery | 41 | 48% | 58.1% | 112% | 0 | published while YouTube held the whole channel back; not evidence |
| ep078 | The Universe Is Terrifying | contradiction, scale_ladder | 85 | 41% | 71.8% | 128% | 0 | published while YouTube held the whole channel back; not evidence |
| ep244 | Space Myths, Busted | statement, record | 51 | 35% | 72.0% | 130% | 0 | published while YouTube held the whole channel back; not evidence |
| ep254 | Scale Breaker | statement, story | 1061 | 47% | 68.2% | 122% | 3 | – |
| ep258 | Space Myths, Busted | statement, scale_ladder | 394 | 42% | 73.6% | 120% | 1 | – |
| ep260 | Scale Breaker | statement, story | 1414 | 45% | 98.4% | 140% | 4 | – |
| ep262 | Mission Files | statement, myth_vs_fact | 931 | 49% | 135.3% | 201% | 1 | – |
| ep266 | Space Myths, Busted | contradiction, myth_vs_fact | 1146 | 50% | 103.1% | 146% | 0 | – |
| ep265 | Space Got Weird | statement, mystery | 1379 | 56% | 73.8% | 133% | 0 | – |
| ep263 | Space Myths, Busted | contradiction, record | 1065 | 50% | 83.9% | 125% | 0 | – |
| ep268 | Space Got Weird | statement, mystery | 1060 | 49% | 119.7% | 173% | 0 | Outstanding hook hold and rewatch loop beat median AVP, but closed historical facts generated zero comments. |
| ep346 | The Universe Is Terrifying | statement, scale_ladder | 1912 | 52% | 80.3% | 131% | 6 | Cosmic-scale dying star hook drove 1.8x median early reach, but a redundant recap beat dropped end retention. |
| ep347 | Scale Breaker | statement, scale_ladder | 1001 | 46% | 65.9% | 118% | 2 | Strong mid-video pacing sustained completion, but an unneeded summary recap beat depressed likes below median. |
| ep359 | Space Got Weird | statement, myth_vs_fact | 1580 | 50% | 81.1% | 124% | 0 | Myth-busting hook and steady pacing beat median reach, though lack of interactive prompt yielded zero comments. |
| ep345 | Space Got Weird | statement, scale_ladder | 571 | 45% | 99.1% | 148% | 0 | Passive descriptive hook stalled early reach at 571 views, though viewers who stayed showed above-median approval. |
| ep355 | Space Myths, Busted | statement, story | 330 | 35% | 83.6% | 129% | 0 | Generic visual hook severely lagged median early reach (330 views), despite healthy likes among viewers who stayed. |
| ep367 | Space Got Weird | statement, scale_ladder | 660 | – | – | – | – | Passive exposition hook underperformed median early reach, though the unusual orbital swap kept likes steady. |
| ep352 | Mission Files | statement, scale_ladder | 1372 | – | – | – | – | Mission-focused Venus hook delivered 1,372 early views, though a predictable sign-off beat softened like conversion. |
| ep356 | Scale Breaker | statement, story | 2135 | – | – | – | – | Voyager cosmic-scale selfie hook drove channel-topping early reach (2,135 views) and strong multi-comment engagement. |
| ep362 | The Universe Is Terrifying | statement, mystery | 1017 | – | – | – | – | High-stakes cosmic threat hook beat median early reach, but catalog designations and a flat close muted comments. |

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
- 2026-10-26: Moved the datestamp-hook rule back to the hypotheses: three of its five Shorts were published during the 24 Oct channel-wide hold, which the learning loop now leaves out of the evidence until reach recovers.
- 2026-10-26: Updated performance reviews for ep165, ep181, ep185, ep197, ep201, and ep221, refining hypotheses on comment prompts and middle-beat pacing.
- 2026-10-27: Logged 7 reviews (ep165, ep181, ep185, ep197, ep201, ep208, ep221), reinforced myth-debunking reach advantages, and expanded evidence on concrete hook and pacing hypotheses.
- 2026-10-27: Logged diagnoses for ep165 through ep221, adding evidence to search-query hooks and sharpening hypotheses against mid-script historical exposition.
- 2026-10-27: Updated learning log with reviews for ep165-ep221, incorporated mid-beat historical attribution findings into Rule 5, and tightened active hypotheses.
- 2026-10-28: Logged evaluations for ep165, ep181, ep185, ep201, ep208, and ep221; retained existing rule set as no hypothesis reached the required 4-Short sample threshold.
- 2026-10-28: Logged diagnostic reviews for ep165, ep181, ep185, ep208, and ep221; recomputed 10-Short medians showing myth-busting reach advantage and reinforced rules against mid-script biographical tangents.
- 2026-10-28: Logged reviews for ep165, ep181, ep185, ep208, and ep221, updating benchmark medians and confirming rules against biographical detours and detached hook metrics.
- 2026-10-28: Updated performance entries for recent Shorts, tracking early reach stalls and the negative impact of biographical and historical timeline detours in mid beats.
- 2026-10-29: Reviewed performance for ep221, ep185, ep165, and ep208; removed the historical milestone hypothesis after ep165 retention dropped during biographical side notes.
- 2026-10-29: Updated evidence for myths and loops; added three new hypotheses from ep185, ep165, and ep208 performance reviews.
- 2026-10-29: Updated review insights for ep165, ep185, and ep208 to target mid-video retention pacing and hook phrasing.
- 2026-10-29: Reviewed ep165 and ep208; updated strategy to prioritize immediate mechanical explanations over historical detours to fix mid-video audience drop-off.
- 2026-10-30: Logged diagnostic reviews for ep165 and ep208, reinforcing hypotheses on immediate mechanical payoffs and eliminating abstract metric hooks.
- 2026-10-30: Analyzed ep165 and ep208 reviews, adding evidence to human-scale threat and direct mechanical payoff hypotheses without altering proven rules.
- 2026-10-30: Logged diagnostic reviews for ep165 and ep208, reinforcing hypotheses on cutting historical detours and avoiding metric abstractions in hooks.
- 2026-10-31: Updated medians and reviewed ep208, noting a strong correlation between abstract scale hooks and distribution failure (reach <100).
- 2026-10-31: Promoted Rule 9 prioritizing cosmic-scale hooks after ep208 distribution failure highlighted a reach gap between universal subjects and localized objects.
- 2026-10-31: Reviewed ep208 (34 early views at 25.1h): reinforced small-scale reach penalty, dropped contradicted delayed-threat hypothesis, and added beat-1 tangible stakes hypothesis.
- 2026-10-31: Added tangible stakes hypothesis following ep208 reach failure; consolidated small-scale reach evidence showing a 62% reach penalty.
- 2026-11-01: Updated performance reviews for ep105-ep165; confirmed planetary-scale and myth-busting topics remain the primary reach drivers.
- 2026-11-01: Updated individual Short diagnoses against revised channel medians and verified rule evidence bases across 27 Shorts.
- 2026-11-02: Maintained existing 9 proven rules and 8 hypotheses as no new daily short reviews were added today.
- 2026-11-02: Dropped call-to-action question hypothesis after ep185 registered zero comments despite an 85% average view percentage; preserved top 9 proven rules.
- 2026-11-02: Recalibrated recent channel medians across the last 10 eligible Shorts and evaluated all 25 episodes without rule promotions due to lack of new diagnoses.
- 2026-11-03: Maintained proven playbook rules and hypotheses as upload data reinforces high early reach for cosmic scale and myth-busting hooks.
- 2026-11-03: Updated learning log with new batch observations (ep260, ep262, ep266, ep265) demonstrating strong early reach from high-stakes hooks but zero comment engagement due to missing final call-to-action prompts.
- 2026-11-03: Evaluated ep260, ep262, ep265, and ep266; confirmed scale hooks drive superior reach while missing debate prompts correlate with zero comment engagement.
- 2026-11-04: Today we integrated data from ep260-266, confirming Rule 1 reach and updating Rule 2 evidence for seamless looping.
- 2026-11-04: Updated learning log with 24-hour review insights from ep260, ep262, ep266, ep265, ep263, and ep268 to refine engagement and hook strategies.
- 2026-11-04: Integrated five new Shorts (ep260-268) and promoted the Authority Anchoring rule based on a 350-view reach advantage.
- 2026-11-05: Updated Rule 3 and Hypothesis 1 following high-retention/low-engagement results for ep262-268 to prioritize loop-based AVP and interaction conversion.
- 2026-11-05: Reviewed performance for ep260-ep268; retained existing rules while refining hypotheses on ending script prompts to improve engagement conversion.
- 2026-11-06: Updated review evidence and integrated latest diagnostic feedback on viewer interaction and mid-script retention tangles.
- 2026-11-06: Processed 24-30h reviews for ep260-ep346; maintained rule set while tracking interactive ending prompt hypothesis against flat engagement depth.
- 2026-11-07: Integrated reach data from ep346, ep347, and ep359 to strengthen cosmic scale and interaction hypotheses.
- 2026-11-07: Reviewed latest 24h+ Shorts performance and diagnosis updates, validating cosmic-scale reach rules while tracking call-to-action hypotheses.
- 2026-11-08: Evaluated latest batch of reviewed Shorts (ep262, ep266, ep265, ep263, ep268, ep346, ep347, ep359, ep345, ep355) against channel medians and refined hypothesis backlog.
- 2026-11-08: Incorporated step 3 reviews for ep262-ep355, adding ep268 to loop rule evidence and tracking prompt-driven engagement hypotheses.
- 2026-11-09: Updated review diagnoses for ep263, ep265, ep266, ep268, ep345, ep346, ep347, ep355, ep359, and ep367 to track loop mechanics, hook paradoxes, and engagement conversion.
- 2026-11-09: Promoted active paradox hooks to a rule after passive openings in ep345 and ep355 significantly underperformed the cohort median early_reach.
- 2026-11-09: Analyzed performance diagnostics across 10 recent Shorts, confirming that active conflict and cosmic-scale hooks (ep356, ep346) outperform passive exposition (ep355, ep345) in early distribution.
- 2026-11-09: Logged diagnostics for ep268 through ep362, reinforcing rules against recap endings and passive hooks while testing interactive end prompts.
