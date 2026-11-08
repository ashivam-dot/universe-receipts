# ep381 research: The Hand-Woven Computer That Saved Apollo 11 (Space Myths, Busted)

Researched 2026-11-08 by the cloud studio (gemini-3.7-flash) from the sources below, read in full by the studio. Only claims backed by two or more independent sites were allowed into the script.

Story: When Apollo 11 hurtled toward the Moon in 1969, navigation did not rely on massive supercomputers aboard the spacecraft. Instead, astronauts Neil Armstrong and Buzz Aldrin depended on the Apollo Guidance Computer, a machine housed in a single cubic foot box weighing about 70 pounds. Designed by MIT and built by Raytheon, it was one of the first computers to use silicon integrated circuits. Its permanent software, overseen by pioneering computer scientist Margaret Hamilton, was literally woven by hand into magnetic core rope memory holding just 36 kilowords of code. Alongside 2 kilowords of RAM, this lean system calculated critical trajectories in real time. During the Apollo 11 lunar descent, the computer became overloaded by radar data, triggering 1202 program alarms. Because its software was engineered with priority scheduling, it dropped non-essential tasks to keep guiding the lander safely to the surface, earning it the nickname the fourth astronaut.

## Sources

| Key | Source | URL |
|---|---|---|
| S1 | Apollo Guidance Computer (wikipedia.org) | https://en.wikipedia.org/wiki/Apollo_Guidance_Computer |
| S2 | Ch2-5 (nasa.gov) | https://web.archive.org/web/20231229162736/https://history.nasa.gov/computers/Ch2-5.html |
| S3 | The Apollo Guidance Computer (caltech.edu) | https://web.archive.org/web/20070612155102/http://authors.library.caltech.edu/5456/01/hrst.mit.edu/hrs/apollo/public/ |
| S4 | Apollo Guidance Computer and the First Silicon Chips (si.edu) | https://airandspace.si.edu/stories/editorial/apollo-guidance-computer-and-first-silicon-chips |
| S5 | BBC World Service - 13 Minutes: Trouble with Hubble, 13 Minutes to the Moon, 5. The fourth astronaut (bbc.co.uk) | https://www.bbc.co.uk/programmes/w3csz4dn |
| S6 | Scene at MIT: Margaret Hamilton’s Apollo code (mit.edu) | https://news.mit.edu/2016/scene-at-mit-margaret-hamilton-apollo-code-0817 |
| S7 | Going Retro With AGC: Smart Computer That Powered Apollo Missions in the 60s (itsfoss.com) | https://itsfoss.com/apollo-guidance-computer/ |

## Claims table

| # | Beats | Claim | Sources | Confidence |
|---|---|---|---|---|
| 1 | 1, 10 | The Apollo Guidance Computer was installed on board both the Apollo Command Module and the Apollo Lunar Module. | S1, S2, S4, S7 | high |
| 2 | - | The Apollo Guidance Computer was designed by the MIT Instrumentation Laboratory. | S1, S2, S3, S4, S6, S7 | high |
| 3 | - | Flight hardware for the AGC was manufactured by Raytheon. | S1, S2, S3, S4 | high |
| 4 | - | The AGC was one of the first computers to use silicon integrated circuit chips. | S1, S3, S4, S7 | high |
| 5 | - | Astronauts communicated with the computer using a numeric display and keyboard interface called the DSKY. | S1, S2, S7 | high |
| 6 | - | The Block II version of the computer contained 2,048 words (2K) of erasable magnetic-core RAM memory. | S1, S2, S7 | high |
| 7 | 4 | The Block II computer read-only memory consisted of 36,864 words (36K) of core rope memory. | S1, S2, S7 | high |
| 8 | 3, 7 | The AGC software development team at MIT was directed by computer scientist Margaret Hamilton. | S1, S5, S6, S7 | high |
| 9 | - | Primary navigation for Apollo missions was conducted by mainframe computers in Houston, with the onboard AGC serving as a secondary system. | S1, S4 | high |
| 10 | 5, 6, 8 | During Apollo 11's lunar descent, the AGC triggered 1201 and 1202 program alarms. | S1, S7 | high |
| 11 | 9 | The AGC earned the nickname 'the fourth astronaut' for its vital role alongside the crew. | S1, S5, S7 | high |
| 12 | - | The Apollo Guidance Computer hardware took up approximately 1 cubic foot of space. | S1, S7 | high |
| 13 | - | The AGC hardware weighed approximately 70 pounds. | S2, S7 | high |
| 14 | 2, 4 | The AGC read-only memory was physically constructed by weaving copper wires through magnetic cores into core rope. | S1, S2 | high |
| 15 | - | The Lunar Module carried an independent backup guidance system called the Abort Guidance System (AGS). | S1, S4 | high |
| 16 | 3 | Margaret Hamilton is credited with popularizing the concept of software engineering through her work on the Apollo project. | S6, S7 | high |

## Disputed or left out

- The exact clock speed calculation varies across sources (S2 states a 1 MHz clock speed, while S1 explains a 2.048 MHz crystal clock divided to 1.024 MHz internal clock); a script should state 'around 1 MHz'.
- The exact root cause of the Apollo 11 radar cycle steals (hardware phase mismatch vs user command overhead); a script should attribute the overload generally to spurious rendezvous radar signals and the 1668 display command without getting bogged down in phase lock technicalities.

## Images

- Beat 1: CHM Artifacts Apollo Guidance Computer (4063525954).jpg (CC BY 2.0, judged exact), https://commons.wikimedia.org/wiki/File:CHM_Artifacts_Apollo_Guidance_Computer_(4063525954).jpg
- Beat 2: 16Kb Rope Core Memory Board from Wagner WAC-40.jpg (CC0, judged exact), https://commons.wikimedia.org/wiki/File:16Kb_Rope_Core_Memory_Board_from_Wagner_WAC-40.jpg
- Beat 3: Margaret Hamilton 1989.jpg (Public domain, judged exact), https://commons.wikimedia.org/wiki/File:Margaret_Hamilton_1989.jpg
- Beat 4: Agc rope.jpg (Public domain, judged exact), https://commons.wikimedia.org/wiki/File:Agc_rope.jpg
- Beat 5: Apollo DSKY from CM Simulator (6378253427).jpg (CC BY 2.0, judged exact), https://commons.wikimedia.org/wiki/File:Apollo_DSKY_from_CM_Simulator_(6378253427).jpg
- Beat 6: Early LEM Lunar Excursion Module (LRC-1964-B701 P-11511).tiff (Public domain, judged exact), https://commons.wikimedia.org/wiki/File:Early_LEM_Lunar_Excursion_Module_(LRC-1964-B701_P-11511).tiff
- Beat 7: a designed quote card, "Margaret Hamilton" / "MIT software lead"
- Beat 8: LUNAR LANDING - ART CONCEPT (S69-33765).jpg (Public domain, judged exact), https://commons.wikimedia.org/wiki/File:LUNAR_LANDING_-_ART_CONCEPT_(S69-33765).jpg
- Beat 9: AS11-40-5962 - Apollo 11 - Apollo 11 Mission image - Lunar Module at Tranquility Base - NARA - 16685323.jpg (Public domain, judged exact), https://commons.wikimedia.org/wiki/File:AS11-40-5962_-_Apollo_11_-_Apollo_11_Mission_image_-_Lunar_Module_at_Tranquility_Base_-_NARA_-_16685323.jpg
- Beat 10: beat 1's picture again, for the loop.

## Render log

- Render 1: 32.37 s, 94 words, -13.9 LUFS, -2.4 dBFS true peak, warnings: none; speech differences: 's' heard as 'is' after 'data but hamilton'; 's' heard as 'is' after 'from crashing that'. Scores hook 4, clarity 4, payoff 4, visuals 4, loop 4. Passed.

## Quality gate (cloud studio, 2026-11-08)

| Hook | Clarity | Payoff | Visuals | Loop |
|---|---|---|---|---|
| 4 | 4 | 4 | 4 | 4 |

- Hook: Strong curiosity hook pairing physical weaving with space travel.
- Clarity: Logical narrative progression from the physical build to the software save.
- Payoff: Solid historical reveal explaining how priority scheduling prevented disaster.
- Visuals: Accurate archival hardware, portraits, and mission graphics throughout.
- Loop: Last line loops cleanly back into the opening premise.

Better than the last: Integrates archival hardware close-ups with a compelling human narrative more effectively than recent episodes.
