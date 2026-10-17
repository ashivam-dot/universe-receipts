# Content calendar

The studio takes topics from here: timely topics added in the last 3 days first (made even when the
inventory is full, and posted in the next free slot with one extra slot a day), then anniversaries dated
within the next 7 days, then the backlog,
rotating through the series and taking each one's most-read topic (by English Wikipedia pageviews) first.
It marks a topic `— making (epNNN)` when its Short starts and `— done (epNNN)` when the Short is
scheduled. A Short that fails the quality gate is `— parked` (it comes back once after 14 days), and one
that fails again, or whose research is too thin, is `— dropped`. The daily routine adds new topics on its
own (`auto.add_topics`), plus up to 2 timely topics a day from NASA's news and the space articles trending
on English Wikipedia (`auto.add_timely`), and 2 follow-ups to any Short that breaks out
(`auto.breakout_topics`). A timely topic older than 3 days waits in line with the backlog.

Each topic is one line naming the story, its year if it has one, and its twist, with an English Wikipedia
article behind it. Every topic still has to pass the two-source rule.

The seed topics (2026-09-29) each start with the exact title of their English Wikipedia article, checked
against Wikipedia's API. Stories are told as science, never as conspiracy: an unexplained signal is
unexplained, not alien.

## Timely (news, trending, and breakout follow-ups: made and posted first)

| Added | Story | Series | Why |
|---|---|---|---|
| 2026-10-01 | Space Shuttle Challenger disaster (1986): it didn't actually explode, it was torn apart by aerodynamic forces — dropped (ep158) | Space Myths, Busted | Trending on Wikipedia with over 32,000 views in the last day. |
| 2026-10-01 | NGC 772 (1785): a spiral galaxy with a single, lopsided arm twice as long as the others — dropped (ep160) | Space Got Weird | Featured as NASA's Astronomy Picture of the Day on September 30. |
| 2026-10-02 | Theia (planet) (1975): a Mars-sized world that vaporized the infant Earth to form the Moon — done (ep167) | The Universe Is Terrifying | NASA's Webb telescope recently released new findings on planet-shattering collisions, mirroring the historic clash of Earth and Theia. |
| 2026-10-03 | DAVINCI (2021): a titanium sphere built to survive a 900-degree plunge through the toxic atmosphere of Venus — done (ep036) | Mission Files | NASA recently highlighted extreme thermal testing on the probe's engineering model for its mission to Venus. |
| 2026-10-05 | Andromeda Galaxy (1923): a single star proved the Milky Way wasn't the entire universe — done (ep060) | Scale Breaker | October 5th is the anniversary of Edwin Hubble identifying the star that proved galaxies exist beyond our own. |
| 2026-10-05 | Sombrero Galaxy (1781): a massive ring of stars that hides a violent history of galactic cannibalism — done (ep061) | The Universe Is Terrifying | Featured on NASA's APOD today with new evidence of tidal streams from its past mergers. |
| 2026-10-06 | White dwarf (2024): archival Hubble data suggests these dead stellar remnants can spawn a second generation of planets from the ruins of their destroyed solar systems — parked (ep074) | Space Got Weird | A new analysis of archival Hubble data points to the possibility of dead white dwarfs hosting second-generation planetary systems. |
| 2026-10-06 | Anorthosite (1969): the rare, bright rock that covers the lunar highlands and baffled scientists is found in massive, moon-like deposits in Madagascar — parked (ep075) | Space Got Weird | NASA recently highlighted Madagascar's anorthosite deposits, which perfectly mimic the geological composition of the Moon's surface. |
| 2026-10-07 | SN 1181 (1181): a zombie star that survived its own supernova and now screams through space at 16,000 kilometers per second — done (ep086) | Space Got Weird | A spectacular new image of its remnant, Pa 30, was featured as NASA's Astronomy Picture of the Day on October 7, 2026. |
| 2026-10-08 | Aeolis Mons (2012): a Martian mountain taller than Mount Rainier that a robotic rover has been slowly climbing for over a decade — done (ep099) | Scale Breaker | NASA's Curiosity rover recently reached a major elevation milestone on the mountain, capturing new panoramas of its wind-carved cliffs. |
| 2026-10-08 | Artemis II (2026): the first crewed lunar mission in over half a century, which will send humans farther into deep space than any flight since Apollo — parked (ep100) | Mission Files | NASA recently released newly annotated lunar navigation training photos prepared by the Artemis II crew. |
| 2026-10-09 | Stickney (crater) (1973): an impact scar so colossal it nearly blasted the Martian moon Phobos into rubble — parked (ep113) | The Universe Is Terrifying | Featured as NASA's Astronomy Picture of the Day this week and in the spotlight ahead of NASA's briefing on the Martian Moons eXploration mission. |
| 2026-10-09 | Fast radio burst (2007): millisecond flashes of deep-space energy that release as much power as the Sun radiates across entire days — done (ep114) | Scale Breaker | NASA announced that the James Webb Space Telescope just measured the distance to the farthest fast radio burst ever detected. |
| 2026-10-10 | Gravitational lens: MACS J0454.1-0300 (2026): a galaxy cluster warping light like a cosmic house of mirrors — dropped (ep124) | The Universe Is Terrifying | NASA just released a stunning new James Webb Space Telescope image of this cluster. |
| 2026-10-11 | IceCube Neutrino Observatory (2010): a telescope made of a cubic kilometer of Antarctic ice that looks straight down through Earth — done (ep129) | Space Got Weird | Featured on NASA's Astronomy Picture of the Day on October 11. |
| 2026-10-12 | Ganymede (moon) (1996): bigger than Mercury and the only moon in the solar system that generates its own magnetic field — dropped (ep135) | Scale Breaker | Highlighted in NASA's Astronomy Picture of the Day featuring Jupiter and its Galilean moons. |
| 2026-10-12 | Io (moon) (1979): tidal forces squeeze this world so violently that hundreds of volcanoes shoot sulfur plumes hundreds of miles into space — parked (ep136) | The Universe Is Terrifying | Featured in NASA's Astronomy Picture of the Day showcasing Jupiter and its moons. |
| 2026-10-13 | Spider crater (1977): a bizarre impact scar in the Australian outback whose spider-like legs were carved by shockwaves from a cosmic collision — parked (ep141) | Space Got Weird | Featured in NASA Earth Observatory reporting highlighting Earth's eerily spider-shaped impact structure |
| 2026-10-16 | Deimos (moon) (1877): its surface gravity is so weak that a human sprinting could launch straight off into interplanetary space — parked (ep169) | Space Got Weird | NASA highlighted its collaboration on JAXA's upcoming MMX mission targeting Mars' moons. |
| 2026-10-17 | Phobos (moon) (1877): Mars is slowly dragging its largest moon to its doom, where tidal forces will eventually tear it into a planetary ring — parked (ep179) | The Universe Is Terrifying | NASA announced its partnership and science instruments for JAXA's upcoming MMX mission to explore Mars' moons. |

## Anniversaries (publish on the date, 8 p.m. Eastern)

| Date | Story | Series |
|---|---|---|
| Oct 29 | 951 Gaspra (1991): became the first asteroid ever visited by a spacecraft when Galileo flew past it on this day | Mission Files |
| Nov 3 | Mariner 10 (1973): the first mission to use a "gravity assist," stealing momentum from Venus to reach Mercury | Mission Files |
| Nov 8 | 2005 YU55 (2011): on this day, a giant 1,200-foot asteroid swept past Earth inside the orbit of the Moon, close enough to be tracked with commercial radar | Near Misses |
| Nov 9 | Apollo 4 (1967): the first launch of the Saturn V rocket was so loud its shockwaves shook buildings and shattered windows miles away | Scale Breaker |
| Nov 11 | SN 1572 (1572): on this day, Tycho Brahe spotted a 'new star' so bright it cast shadows, shattering the ancient belief that the heavens were unchanging | Space Myths, Busted |
| Nov 12 | Philae (spacecraft) (2014): the first probe to land on a comet bounced twice after its harpoons failed, landing in a dark shadow | Mission Files |
| Nov 13 | Mariner 9 (1971): on this day, Mariner 9 became the first spacecraft to orbit another planet, arriving at Mars during a planet-wide dust storm | Mission Files |
| Nov 13 | 2020 VT4 (2020): an asteroid skimmed just 230 miles above Earth's surface on this day, flying closer than the International Space Station | Near Misses |
| Nov 13 | WT1190F (2015): an unknown piece of deep-space debris on a collision course with Earth burned up over the Indian Ocean and was identified as lost Apollo-era hardware | Space Got Weird |
| Nov 14 | 90377 Sedna (2003): discovered on this day, this freezing dwarf planet has an orbit so distant it takes over 11,000 years to circle the Sun once | Scale Breaker |
| Nov 15 | Buran (spacecraft) (1988): the Soviet Union's only shuttle flew to orbit and landed entirely on autopilot | Mission Files |
| Nov 28 | Mariner 4 (1964): the first probe to send back close-up photos of Mars, revealing a dead, cratered moon-like world that shattered dreams of Martian civilizations | Mission Files |
| Nov 28 | PSR B1919+21 (1967): the first discovered pulsar flashed with such unnatural precision that astronomers initially cataloged the signal as Little Green Men 1 | Space Got Weird |
| Dec 2 | Solar and Heliospheric Observatory (1995): designed to monitor the Sun, this spacecraft accidentally became history's greatest comet finder with over 5,000 discoveries | Space Got Weird |
| Dec 07 | Apollo 17 (1972): the final crewed flight to the Moon, whose astronauts snapped the iconic whole-Earth Blue Marble photograph | Mission Files |
| Oct 1 | NASA (1958): at the peak of its Apollo program, an estimated 5% of the entire American workforce contributed to it in some capacity — done (ep002) | Mission Files |
| Oct 4 | Sputnik 1 (1957): the "Sputnik" most people saw crossing the night sky was really its 85-foot rocket stage; the satellite was barely visible — parked (ep003) | Mission Files |
| Oct 7 | Luna 3 (1959): its first photos of the Moon's far side were shot on American film the Soviets salvaged from downed US spy balloons — done (ep004) | Mission Files |
| Oct 10 | Outer Space Treaty (1967): the law of space bans nuclear weapons in orbit and forbids any nation from claiming the Moon — done (ep033) | Space Got Weird |
| Oct 15 | Oh-My-God particle (1991): one subatomic particle hit Earth's atmosphere with the energy of a baseball thrown at about 63 mph — parked (ep091) | The Universe Is Terrifying |
| Oct 19 | 1I/ʻOumuamua (2017): the first known visitor from another star system sped up as it left, with no visible tail — parked (ep134) | Space Got Weird |
| Oct 21 | Orionids: the shooting stars peaking tonight are crumbs shed by Halley's Comet — done (ep146) | Space Myths, Busted |
| Oct 22 | Venera 9 (1975): the first photo ever taken on the surface of another planet came from Venus — parked (ep155) | Mission Files |
| Oct 24 | V-2 rocket (1946): a captured rocket took the first-ever photo of Earth from space, showing the planet's curve from 65 miles up — done (ep174) | Mission Files |
| Oct 29 | STS-95 (1998): John Glenn went back to space at 77, 36 years after his first orbit | Mission Files |
| Oct 31 | 2015 TB145 (2015): a skull-shaped asteroid flew past Earth on Halloween | Near Misses |
| Nov 2 | Expedition 1 (2000): since this crew moved in, the space station has had people aboard every single day | Mission Files |
| Nov 3 | Laika (1957): the first animal to orbit Earth; the truth about how she died only came out in 2002 | Mission Files |
| Nov 9 | Carl Sagan (1934): the astronomer famous for billions and billions never actually said it on Cosmos | Space Myths, Busted |
| Nov 14 | Apollo 12 (1969): lightning struck the rocket twice in its first minute, and the mission flew on | Near Misses |
| Nov 16 | Arecibo message (1974): humanity beamed a picture message at a star cluster 25,000 light-years away | Space Got Weird |
| Nov 17 | Leonids (1833): a meteor storm so intense it launched the science of meteors | Space Got Weird |
| Nov 20 | International Space Station (1998): its first piece launched this day; NASA is paying SpaceX up to $843 million for a craft to steer it into the ocean | Mission Files |
| Nov 26 | InSight (2018): its heat probe spent two years trying to dig into Mars and never got deep enough | Mission Files |
| Nov 30 | Sylacauga (meteorite) (1954): after a meteorite hit a woman napping on her couch, her landlord claimed it, and her family paid $500 for the rock | Space Got Weird |

## Backlog

### The Universe Is Terrifying

- Boötes Void (1981): a hole in space holding just 60 galaxies where about 2,000 would be expected — dropped (ep039)
- Sagittarius A* (1974): the black hole at the center of our galaxy weighs about four million Suns, and we photographed it in 2022 — done (ep008)
- Magnetar (1979): a dead star whose magnetic field would be lethal from 1,000 kilometers away — done (ep049)
- HD 189733 b (2005): a deep-blue planet where it may rain glass sideways in 5,400 mph winds — parked (ep122)
- Great Attractor: an unseen mass pulling our galaxy and thousands of others toward it, hidden behind the Milky Way's glare — done (ep032)
- Kessler syndrome (1978): one collision in orbit could start a chain reaction of debris that closes some orbits for generations — dropped (ep157)
- WR 104: a pinwheel-shaped star system that could end in a gamma-ray burst, once feared to be pointed at Earth — done (ep055)
- Rogue planet (2011): billions of planets may drift through the Milky Way in total darkness, with no star at all — parked (ep043)
- Spaghettification: a small black hole would stretch you like a noodle, but falling into a giant one you might cross the edge in one piece — dropped (ep068)
- Andromeda–Milky Way collision (2025): a new study found the famous galactic crash is closer to a coin flip than a certainty — done (ep071)
- R Coronae Borealis (1783): a star that acts like a reverse variable star, regularly fading to near invisibility as it chokes on its own soot — parked (ep085)
- 3C 273 (1963): the first identified quasar, it is 4 trillion times brighter than the Sun but 2.4 billion light-years away — done (ep023)
- Hypervelocity star (2005): stars being flung out of the Milky Way at millions of miles per hour, doomed to wander intergalactic space alone — done (ep097)
- Hanny's Voorwerp (2007): a galaxy-sized green structure that is actually a light "echo" from a quasar that died 100,000 years ago — done (ep109)
- Abell 2261 (2012): a galaxy whose central supermassive black hole—one of the largest ever found—has mysteriously vanished — done (ep117)
- OGLE-2011-BLG-0462 (2022): the first confirmed rogue stellar-mass black hole detected wandering completely alone and invisible through our galaxy — parked (ep103)
- False vacuum decay: a hypothetical cosmic catastrophe where a bubble of true vacuum could expand at the speed of light, rewriting the laws of physics and erasing our universe instantly — done (ep078)
- V404 Cygni (1989): a black hole system that suddenly wakes up every few decades to shoot relativistic plasma jets — parked (ep126)
- Swift J1644+57 (2011): a dormant supermassive black hole ripped a star apart and fired a relativistic jet of X-rays directly at Earth — done (ep130)
- ASASSN-15lh (2015): a cosmic explosion that shone twenty times brighter than our entire galaxy combined, blasting out more energy than the Sun will in its lifetime — parked (ep139)
- Barnard 68 (1919): a molecular cloud of freezing cosmic dust so dense it creates an ink-black void that looks like a hole in the universe — parked (ep145)
- Tidal disruption event (1975): when a star wanders too close to a supermassive black hole, gravitational forces shred it into a blinding stream of stellar debris — dropped (ep144)
- Comet West (1976): a dazzling sungrazer that split into four pieces and was bright enough to be seen in broad daylight — parked (ep152)
- Black widow pulsar (1988): a hyper-spinning dead star blasts its companion star with a relativistic particle beam, slowly vaporizing it down to nothing — parked (ep163)
- GRB 221009A (2022): the brightest cosmic explosion ever recorded blinded space telescopes and physically warped Earth's upper atmosphere from two billion light-years away — parked (ep171)
- SGR 1806-20 (2004): a starquake on a magnetar 50,000 light-years away blasted out more energy in a tenth of a second than the Sun emits in 150,000 years — making (ep181)

### Scale Breaker

- TON 618: a black hole estimated at roughly 40.7 billion Suns, first catalogued in 1957 as a faint blue star — dropped (ep150)
- Stephenson 2 DFK 1 (1990): a star so big that, put where the Sun is, it would swallow Saturn's orbit — dropped (ep067)
- UY Scuti (1860): crowned the biggest known star, then it shrank when astronomers remeasured its distance — parked (ep070)
- Laniakea Supercluster (2014): our galaxy turned out to be one of about 100,000 in a supercluster only mapped in 2014 — done (ep048)
- Hercules–Corona Borealis Great Wall (2013): a structure about 10 billion light-years long, possibly too big for our models of the universe — parked (ep054)
- Observable universe: 93 billion light-years across, though the universe is only 13.8 billion years old — done (ep175)
- Pale Blue Dot (1990): Earth fills just 0.12 of one pixel, and the beam of light it sits in is sunlight glinting off the camera itself — parked (ep042)
- Voyager 1 (1977): to work around a failed memory chip in 2024, engineers deleted its old Jupiter code, because its total memory is only 68 kilobytes — dropped (ep148)
- Olympus Mons (1971): standing near its summit you wouldn't know you were on a mountain; its slope runs past a horizon just 3 kilometers away — done (ep013)
- Neutron star (1967): a teaspoon of it would weigh about 900 times as much as the Great Pyramid of Giza — done (ep030)
- Proxima Centauri (1915): the nearest star to the Sun, yet Voyager 1 would need 73,775 years to get there — dropped (ep166)
- IC 1101 (1790): a galaxy six million light-years wide that could fit 50 Milky Ways inside it — done (ep079)
- Eridanus Supervoid (2004): a region of space spanning a billion light-years that contains almost no matter and no galaxies — parked (ep089)
- Great White Spot (1876): a periodic storm on Saturn so massive it wraps around the entire planet until it hits its own tail — done (ep105)
- Lunar distance: every other planet in the solar system can fit in the gap between the Earth and the Moon with room to spare — dropped (ep076)
- Boomerang Nebula (1980): the coldest place in the natural universe, colder than the background glow of the Big Bang — done (ep095)
- El Gordo (galaxy cluster) (2012): a colossal collision of two galaxy clusters that weighs about three quadrillion times more than our Sun — done (ep120)
- Giant Arc (2021): a crescent of galaxies 3.3 billion light-years long that is so massive it challenges our basic understanding of cosmology — done (ep111)
- Barnard's Star (1916): the fastest-moving star in our night sky, crossing a moon-width every 180 years — parked (ep128)
- Tarantula Nebula (1751): a star nursery so intensely luminous that if it were at Orion's distance, it would cast visible shadows at night — parked (ep131)
- Alcyoneus (galaxy) (2022): a colossal radio galaxy spanning 16 million light-years, making it more than 150 times wider than the Milky Way — parked (ep138)
- Valles Marineris (1971): a Martian canyon system that would stretch across the entire continental United States, plunging four times deeper than the Grand Canyon — parked (ep142)
- Solar wind (1958): a relentless stream of charged particles tearing through the solar system at a million miles per hour — parked (ep153)
- Parker Solar Probe (2018): the fastest human-made craft in history plunges through the Sun's blistering outer atmosphere at over 400,000 miles per hour — done (ep161)
- R136a1 (2010): the most massive known star is over 200 times heavier than the Sun and shines millions of times brighter, burning so violently it will destroy itself completely — making (ep182)

### Mission Files

- Soyuz 11 (1971): the only people ever to die in space, killed when a valve opened as their capsule separated — dropped (ep178)
- Venera 13 (1982): a lander built to last 32 minutes on Venus kept working for 127 — parked (ep069)
- Mars Climate Orbiter (1999): lost at Mars because one team's software used pound-force and another's used newtons — parked (ep057)
- OSIRIS-REx (2020): it grabbed so much of asteroid Bennu that rocks jammed its lid open and pieces drifted off into space — parked (ep062)
- Double Asteroid Redirection Test (2022): we crashed a spacecraft into an asteroid on purpose and shortened its orbit by about half an hour — parked (ep077)
- Cassini–Huygens (2017): the mission ended by diving into Saturn on purpose, to protect moons that might hold life — done (ep045)
- New Horizons (2015): the probe that flew past Pluto carries some of the ashes of the man who discovered it — done (ep177)
- Hubble Space Telescope (1990): a backup mirror polished the traditional way by Kodak never flew; it's on display at the National Air and Space Museum — dropped (ep016)
- James Webb Space Telescope (2021): 344 potential single-point failures all had to work, 930,000 miles from any repair crew — dropped (ep015)
- Voyager 2 (1977): despite its name it launched first, two weeks before its twin Voyager 1, and is still the only probe to visit Uranus and Neptune — done (ep017)
- Churyumov–Gerasimenko (2014): the comet smelled like rotten eggs, horse urine, and bitter almonds when we finally landed on it — done (ep084)
- Skylab 4 (1973): astronauts staged the first strike in space by cutting off communication with mission control after a brutal workload — parked (ep096)
- Venera 7 (1970): the first probe to transmit data from the surface of another planet, though it landed on its side and barely signaled — parked (ep090)
- Mariner 1 (1962): a missing hyphen in a line of guidance code caused NASA's first planetary probe to veer off course and be destroyed — done (ep106)
- Genesis (spacecraft) (2004): a sample return probe crashed into the desert because its parachute switches were installed upside down — done (ep051)
- Pioneer 10 (1972): the first spacecraft to navigate through the asteroid belt and reach Jupiter, carrying a golden plaque designed for alien life — parked (ep121)
- Magellan (spacecraft) (1989): mapped 98 percent of Venus's surface with radar before intentionally diving into its crushing atmosphere — done (ep116)
- Project Orion (nuclear propulsion) (1958): a Cold War plan to launch a massive spaceship using a rapid-fire series of atomic bomb explosions — done (ep125)
- Giotto (spacecraft) (1986): a probe survived a battering of 150,000 mph comet dust to capture the first close-up images of Halley's nucleus — parked (ep132)
- Deep Impact (spacecraft) (2005): NASA intentionally fired an 820-pound copper projectile into a speeding comet at 23,000 mph just to study the blast crater — parked (ep143)
- Lucy (spacecraft) (2021): a mission designed to tour a record number of asteroids, featuring a twelve-year journey past the Trojan swarms — parked (ep151)

### Space Got Weird

- PSR B1257+12 (1992): the first planets ever confirmed outside our solar system orbit a dead star — dropped (ep083)
- Przybylski's Star (1961): a star whose light seems to show short-lived elements astronomers still can't fully explain — parked (ep092)
- Hoag's Object (1950): look through the gap in this rare ring galaxy and you can see another, more distant ring galaxy — done (ep058)
- Wow! signal (1977): it lasted the full 72 seconds the telescope could watch one spot, exactly as a signal from deep space should — dropped (ep164)
- Tabby's Star (2015): a star that dimmed by up to 22 percent sparked talk of alien megastructures; dust was the answer — done (ep052)
- Gamma-ray burst (1967): the brightest explosions in the universe were found by satellites watching for secret nuclear tests — done (ep046)
- Betelgeuse: a runaway star flung from its birthplace near Orion's Belt, plowing through space at 30 km/s with a bow shock over four light-years wide — dropped (ep147)
- Enceladus (2005): the most reflective body in the Solar System, and its water jets supply most of the material in one of Saturn's rings — done (ep176)
- Voyager Golden Record (1977): its cover carries ultra-pure uranium-238, a clock that could tell whoever finds it how old the record is — done (ep156)
- Moon tree (1971): most NASA staff didn't know these trees existed until 1996, when a third-grade teacher and her students found one — done (ep110)
- Skylab (1979): a shire in Western Australia fined NASA A$400 for littering; a radio show's listeners finally paid it in 2009 — done (ep040)
- SNC 420 (2020): a meteorite that sat in a museum drawer for decades before scientists realized it was from Mars — parked (ep123)
- 55 Cancri e (2004): a planet twice the size of Earth where the pressure and heat likely turned its interior into solid diamond — done (ep066)
- 16 Psyche (1852): a giant metal asteroid that might be the exposed core of a destroyed protoplanet — dropped (ep064)
- Gliese 436 b (2004): a planet where gravity is so intense it forces water into solid ice despite temperatures reaching 800 degrees Fahrenheit — parked (ep098)
- Tennis racket theorem (1985): a physical law in zero gravity that causes any spinning asymmetrical object to spontaneously flip back and forth without outside force — dropped (ep082)
- Miranda (moon) (1986): a moon of Uranus that looks like it was shattered into pieces and hastily glued back together — done (ep118)
- WASP-12b (2008): a pitch-black planet that is actively being eaten alive by its parent star — parked (ep104)
- Stephan's Quintet (1877): a visual galaxy group where one interloper is actually much closer, plowing through the others at supersonic speeds — done (ep127)
- Saturn's hexagon (1981): a bizarre six-sided jet stream spinning at Saturn's north pole that is wide enough to swallow two whole Earths — done (ep133)
- Iapetus (moon) (1671): a bizarre world shaped like a walnut, with a 12-mile-high equatorial ridge and one hemisphere ten times darker than the other — parked (ep140)
- WASP-76b (2020): an ultra-hot world where extreme temperatures vaporize iron on the dayside, driving winds that make it rain liquid iron droplets at night — making (ep183)

### Near Misses

- Apollo 13 (1970): after the lunar module carried the crippled ship home, its builder Grumman jokingly sent the command module's maker an invoice for "towing" — dropped (ep007)
- Carrington Event (1859): the biggest solar storm on record; some telegraph lines kept working with their batteries unplugged — done (ep009)
- 99942 Apophis (2004): once given a 2.7 percent chance of hitting Earth, it will pass closer than some satellites in 2029 — done (ep035)
- 2024 YR4 (2024): for a few weeks the most threatening asteroid ever measured, with a 3.1 percent chance of hitting Earth in 2032 — parked (ep094)
- Chelyabinsk meteor (2013): nobody saw it coming, on the same day astronomers were watching a different asteroid fly past — done (ep050)
- July 2012 solar storm (2012): a Carrington-class blast crossed Earth's orbit about nine days after Earth had passed that spot — done (ep072)
- Gemini 8 (1966): Neil Armstrong's first spaceflight nearly killed him when a stuck thruster sent the capsule into a violent spin — parked (ep056)
- Mir (1997): a fire and then a crash with a cargo ship nearly doomed the space station within four months — parked (ep108)
- 1983 Soviet nuclear false alarm incident (1983): a satellite mistook sunlight on clouds for incoming missiles, and one officer decided it was a false alarm — parked (ep044)
- Tunguska event (1908): an explosion in the sky flattened forest across 2,150 square kilometers and left no crater — done (ep024)
- Gliese 710: a star is on course to pass through the Sun's cloud of comets in about 1.29 million years — done (ep063)
- 4581 Asclepius (1989): a 300-meter asteroid missed Earth by just six hours, and we didn't see it until it had already passed — parked (ep088)
- 2019 OK (2019): a city-killer sized asteroid that came from the Sun's direction and was detected just hours before its closest approach — done (ep112)
- 4179 Toutatis (2004): a 5-kilometer asteroid that passed within four lunar distances of Earth, close enough to see its strange "ginger-root" shape — parked (ep080)
- 1972 Great Daylight Fireball (1972): a meteoroid bounced off Earth's atmosphere like a skipping stone and escaped back into space — parked (ep102)
- 2023 NT1 (2023): a 200-foot asteroid approached from the direction of the Sun and flew past Earth undetected until two days later — done (ep119)
- Voskhod 2 (1965): the first spacewalker was trapped outside his ship when his suit ballooned stiff, forcing him to bleed off vital oxygen to squeeze back inside — done (ep137)
- STS-27 (1988): space shuttle Atlantis lost over 700 thermal tiles on ascent, surviving fiery reentry only because a missing tile sat over a thick steel antenna plate — done (ep162)
- STS-93 (1999): an electrical short and a stray pin nearly forced the space shuttle into a catastrophic emergency ditching in the Atlantic Ocean — parked (ep170)
- Apollo 11 (1969): computer overloads and a boulder-strewn landing zone forced astronauts to fly manually, touching down on the Moon with under 30 seconds of fuel left — dropped (ep180)

### Space Myths, Busted

- Great Wall of China: you can't see it from the Moon with the naked eye, and astronauts struggle to spot it even from orbit — done (ep159)
- Far side of the Moon: there's no dark side of the Moon; the far side gets as much sunlight as the side we see — done (ep047)
- Season: Earth is closest to the Sun in early January, so distance isn't what makes summer — dropped (ep037)
- Venus: it's hotter than Mercury, though it's nearly twice as far from the Sun — dropped (ep021)
- Uncontrolled decompression: a body exposed to the vacuum of space doesn't explode; that's a persistent movie myth — parked (ep041)
- Sun: sunlight's energy spent 10,000 to 170,000 years escaping the core; neutrinos from the same reactions reach the surface in 2.3 seconds — parked (ep081)
- Meteoroid: shooting stars aren't stars at all; an estimated 25 million meteoroids and bits of debris hit Earth's atmosphere each day — done (ep053)
- Pluto (2006): it hasn't finished a single orbit since its discovery in 1930, and won't until 2178 — done (ep165)
- Polaris: the North Star isn't the brightest star in the sky, and it isn't even close — done (ep028)
- Black hole: if the Sun became a black hole of the same mass, Earth would keep orbiting just as before — dropped (ep149)
- Weightlessness: astronauts don't float because gravity is gone; they're falling around Earth nonstop — parked (ep065)
- Sun (1970): it's actually pure white; Earth's atmosphere scatters blue light to make it look yellow to our eyes — parked (ep107)
- Comet tail (1531): comet tails do not trail behind them as they travel, but always point directly away from the Sun — parked (ep073)
- Micro-g environment (1961): astronauts are not beyond Earth's gravity, which is still about 90 percent as strong on the space station as on the ground — done (ep059)
- Tidal locking (1959): the Moon actually rotates on its axis, but at the exact same speed it orbits Earth, hiding its far side forever — parked (ep093)
- Asteroid belt (1801): despite movie scenes of ships dodging giant rocks, the average distance between asteroids in the belt is about 600,000 miles — done (ep087)
- Halley's Comet (1910): rumors that its toxic tail would wipe out life on Earth led people to buy 'comet pills' and gas masks — parked (ep101)
- Lunar soil (1969): early scientists feared lunar landers would sink into deep dust, but the surface proved to be compact rock and abrasive glass shards — parked (ep115)
- Pioneer anomaly (1980): deep-space probes that mysteriously drifted off course, baffling scientists for decades until thermal radiation provided the answer — parked (ep154)
- Vulcan (hypothetical planet) (1859): astronomers spent half a century hunting a phantom world inside Mercury's orbit before Einstein proved space itself was warping — done (ep168)
- Space Pen (1965): the famous legend claims NASA spent millions while Soviets used pencils, but pencil graphite was a dangerous fire hazard and the pen was funded privately — parked (ep173)
- Van Allen radiation belt (1958): critics claimed Apollo astronauts would be fried passing through them, but their high-speed trajectory meant they received less radiation than a standard CT scan — done (ep172)
