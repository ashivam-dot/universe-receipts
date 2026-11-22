# ep494 research: The Million-Times-Faster Star Hunt (Mission Files)

Researched 2026-11-22 by the cloud studio (gemini-3-flash-preview, gemini-3.5-flash-lite, gemini-3.6-flash, gemini-3.8-flash) from the sources below, read in full by the studio. Only claims backed by two or more independent sites were allowed into the script.

Story: Since launching in 2008, NASA's Fermi Gamma-ray Space Telescope has swept the entire sky every three hours, sharing its raw data freely with the world. But buried in that data are hidden pulsars—rapidly spinning neutron stars whose signals are muffled by cosmic noise. To find them, traditional methods required volunteers around the globe to donate computing power for months, burning through hundreds of computer-years to find a single target. Even after chewing through the equivalent of 600 years of processing time on one candidate, conventional algorithms found nothing. Then, astrophysicists borrowed an algorithm from post-quantum cryptographers designing codes to resist quantum computers. By turning the search into a high-dimensional lattice geometry problem, they found pulsar PSR J1622-7204—spinning 261 times a second—in just 10 hours on an ordinary computer processor. By applying codebreaking mathematics to open space data, scientists accelerated deep-space discovery by one million times.

## Sources

| Key | Source | URL |
|---|---|---|
| S1 | Fermi Gamma-ray Space Telescope (wikipedia.org) | https://en.wikipedia.org/wiki/Fermi_Gamma-ray_Space_Telescope |
| S2 | NASA Science Data Powers New Method to Discover Hard-to-Find Pulsars - NASA Science (nasa.gov) | https://science.nasa.gov/open-science/fermi-data-pulsar-discovery/ |
| S3 | Fermi Telescope Makes First Big Discovery: Gamma Ray Pulsar (universetoday.com) | https://www.universetoday.com/19879/fermi-telescope-makes-first-big-discovery-gamma-ray-pulsar/ |
| S4 | The Fermi Large Area Telescope (stanford.edu) | http://www-glast.stanford.edu/ |
| S5 | Fermi Observations of High-Energy Gamma-Ray Emission from GRB 080916C (osti.gov) | https://www.osti.gov/biblio/1357451 |
| S6 | NASA’s Fermi data reveals hidden pulsar using a million times faster search method (yahoo.com) | https://tech.yahoo.com/science/articles/nasa-fermi-data-reveals-hidden-175000974.html |
| S7 | Lattice Algorithm Speeds Fermi Pulsar Discovery — CASRAI (casrai.org) | https://casrai.org/news/fermi-gamma-ray-telescope-cryptography-algorithm-accelerates-pulsar-discovery-2026 |

## Claims table

| # | Beats | Claim | Sources | Confidence |
|---|---|---|---|---|
| 1 | - | The Fermi Gamma-ray Space Telescope launched into orbit on June 11, 2008. | S1, S4 | high |
| 2 | - | Originally named the Gamma-ray Large Area Space Telescope (GLAST), the observatory was renamed in honor of physicist Enrico Fermi. | S1, S4 | high |
| 3 | - | Fermi's primary instrument is the Large Area Telescope (LAT), which detects gamma rays ranging from roughly 20 MeV to over 300 GeV. | S1, S4 | high |
| 4 | 3 | Fermi's observational mode scans and maps the entire sky every three hours. | S1, S2, S3, S4, S6 | high |
| 5 | - | NASA releases Fermi telescope data freely to the public along with data analysis software. | S1, S2, S4, S6, S7 | high |
| 6 | 1, 8 | Pulsars are rapidly rotating neutron stars that sweep lighthouse-like beams of radiation toward Earth. | S2, S3, S6, S7 | high |
| 7 | 3, 4 | Detecting gamma-ray pulsars is computationally brutal because Fermi captures only sparse photons mixed with background radiation, requiring researchers to test multidimensional grids of position, spin rate, and slowdown rate. | S2, S6, S7 | high |
| 8 | 4 | Traditional blind searches relied on distributed computing via the Einstein@Home volunteer network and regularly consumed hundreds of computer-years per pulsar. | S2, S6, S7 | high |
| 9 | 1, 5, 9 | Physicists adapted mathematical algorithms from cryptography to search NASA Fermi data roughly one million times faster than prior methods. | S2, S6, S7 | high |
| 10 | 6 | The new method reformulates pulsar hunting as a geometric shortest-vector problem in a high-dimensional lattice. | S2, S6, S7 | high |
| 11 | 5 | The lattice algorithms were originally developed by cryptographers testing encryption schemes built to resist future quantum computers. | S2, S6, S7 | high |
| 12 | - | Dotan Gazith and Barak Zackay of the Weizmann Institute of Science applied the lattice cryptography technique to the astronomical problem. | S2, S6, S7 | high |
| 13 | - | The research project was led by Daniel Pook-Kolb of the Max Planck Institute for Gravitational Physics (Albert Einstein Institute). | S2, S6, S7 | high |
| 14 | 8 | The algorithm discovered PSR J1622-7204, an isolated pulsar spinning 261 times per second. | S2, S6, S7 | high |
| 15 | - | The research findings were published in the scientific journal Physical Review Letters. | S2, S6, S7 | high |
| 16 | 7 | The team identified the pulsar using approximately 10 hours of computation time on a standard computer processor. | S2, S6, S7 | high |
| 17 | 2 | The previous best search method failed to detect PSR J1622-7204 despite consuming processing power equivalent to 600 years on a standard processor. | S2, S6, S7 | high |
| 18 | - | Individual trial runs of the algorithm took approximately five minutes on a single computer core. | S2, S6 | high |
| 19 | - | The researchers used NASA's open-source Fermitools software to prepare the archival dataset for analysis. | S2, S6 | high |

## Disputed or left out

- S7 specifies the exact publication date as November 19, 2026, and outlines rollout milestones in 2026 and 2027, whereas S2 refers to publication on 'Thursday'. Scripts should focus on the verified publication in Physical Review Letters rather than stating forward-looking calendar dates.

## Images

- Beat 1: Noirlab2218a Neutron Star Merger in the Early Universe.jpg (CC BY 4.0, judged close), https://commons.wikimedia.org/wiki/File:Noirlab2218a_Neutron_Star_Merger_in_the_Early_Universe.jpg
- Beat 2: Einstein@home working.jpg (CC BY 2.0, judged exact), https://commons.wikimedia.org/wiki/File:Einstein@home_working.jpg
- Beat 3: Fermi Gamma-ray Space Telescope spacecraft model.png (Public domain, judged exact), https://commons.wikimedia.org/wiki/File:Fermi_Gamma-ray_Space_Telescope_spacecraft_model.png
- Beat 4: Fermi's 12-year View of the Gamma-ray Sky (SVS14090 - Fermi 144-month Fermi all-sky hammer 4000x2000).png (Public domain, judged exact), https://commons.wikimedia.org/wiki/File:Fermi%27s_12-year_View_of_the_Gamma-ray_Sky_(SVS14090_-_Fermi_144-month_Fermi_all-sky_hammer_4000x2000).png
- Beat 5: a designed fact card, "Post-quantum" / "Lattice cryptography math"
- Beat 6: beat 4's picture again, no better picture was found.
- Beat 7: ULSI_AMC_DX_DLC_40MHz_2015-03-14-11.56.50_-_ZS-DMap_-_Stack-DSC09781-DSC09831 (CC0, judged exact), http://www.flickr.com/photos/130561288@N04/16205191643
- Beat 8: Pulsar model.jpg (Public domain, judged exact), https://commons.wikimedia.org/wiki/File:Pulsar_model.jpg
- Beat 9: beat 1's picture again, for the loop.

## Render log

- Render 1: 31.65 s, 87 words, -14.0 LUFS, -2.3 dBFS true peak, warnings: none; speech differences: none. Scores hook 5, clarity 5, payoff 5, visuals 5, loop 5. Passed.

## Quality gate (cloud studio, 2026-11-22)

| Hook | Clarity | Payoff | Visuals | Loop |
|---|---|---|---|---|
| 5 | 5 | 5 | 5 | 5 |

- Hook: The million-times-faster claim is a powerful specific hook that immediately creates a curiosity gap.
- Clarity: The narrative arc from computational failure to mathematical solution is exceptionally clear.
- Payoff: The concrete results of 10 hours versus 600 years provide a satisfying resolution to the opening claim.
- Visuals: The use of actual Fermi data maps and satellite models makes the abstract mathematical concepts feel grounded.
- Loop: Ending on the word 'fast' creates a perfect grammatical and conceptual bridge back to the 'million times faster' start.

Better than the last: This Short handles a much more complex mathematical concept than ep484 while maintaining better clarity and a stronger hook.
