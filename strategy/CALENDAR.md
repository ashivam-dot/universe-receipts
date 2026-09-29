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

## Anniversaries (publish on the date, 8 p.m. Eastern)

| Date | Story | Series |
|---|---|---|
| Oct 1 | NASA (1958): the agency opened a year after Sputnik, built out of a 43-year-old agency called NACA — making (ep002) | Mission Files |
| Oct 4 | Sputnik 1 (1957): a satellite the size of a beach ball whose beeps anyone with a shortwave radio could hear — making (ep003) | Mission Files |
| Oct 7 | Luna 3 (1959): humanity's first look at the far side of the Moon | Mission Files |
| Oct 10 | Outer Space Treaty (1967): the law of space bans nuclear weapons in orbit and forbids any nation from claiming the Moon | Space Got Weird |
| Oct 15 | Oh-My-God particle (1991): one subatomic particle hit Earth's atmosphere with the energy of a baseball thrown at about 60 mph | The Universe Is Terrifying |
| Oct 19 | 1I/ʻOumuamua (2017): the first known visitor from another star system sped up as it left, with no visible tail | Space Got Weird |
| Oct 21 | Orionids: the shooting stars peaking tonight are crumbs shed by Halley's Comet | Space Myths, Busted |
| Oct 22 | Venera 9 (1975): the first photo ever taken on the surface of another planet came from Venus | Mission Files |
| Oct 29 | STS-95 (1998): John Glenn went back to space at 77, 36 years after his first orbit | Mission Files |
| Oct 31 | 2015 TB145 (2015): a skull-shaped asteroid flew past Earth on Halloween | Near Misses |
| Nov 2 | Expedition 1 (2000): since this crew moved in, the space station has had people aboard every single day | Mission Files |
| Nov 3 | Laika (1957): the first animal to orbit Earth; the truth about how she died only came out in 2002 | Mission Files |
| Nov 9 | Carl Sagan (1934): the astronomer famous for billions and billions never actually said it on Cosmos | Space Myths, Busted |
| Nov 14 | Apollo 12 (1969): lightning struck the rocket twice in its first minute, and the mission flew on | Near Misses |
| Nov 16 | Arecibo message (1974): humanity beamed a picture message at a star cluster 25,000 light-years away | Space Got Weird |
| Nov 17 | Leonids (1833): a meteor storm so intense it launched the science of meteors | Space Got Weird |
| Nov 20 | International Space Station (1998): its first piece launched this day; it grew into the most expensive object ever built | Mission Files |
| Nov 26 | InSight (2018): its heat probe spent two years trying to dig into Mars and never got deep enough | Mission Files |
| Nov 30 | Sylacauga (meteorite) (1954): the only well-documented person hit by a meteorite was napping on her couch | Space Got Weird |

## Backlog

### The Universe Is Terrifying

- Boötes Void (1981): a hole in space holding just 60 galaxies where about 2,000 would be expected
- Sagittarius A* (1974): the black hole at the center of our galaxy weighs about four million Suns, and we photographed it in 2022
- Magnetar (1979): a dead star whose magnetic field would be lethal from 1,000 kilometers away
- HD 189733 b (2005): a deep-blue planet where it may rain glass sideways in 5,400 mph winds
- Great Attractor: an unseen mass pulling our galaxy and thousands of others toward it, hidden behind the Milky Way's glare
- Kessler syndrome (1978): one collision in orbit could start a chain reaction of debris that closes some orbits for generations
- WR 104: a pinwheel-shaped star system that could end in a gamma-ray burst, once feared to be pointed at Earth
- Rogue planet (2011): billions of planets may drift through the Milky Way in total darkness, with no star at all
- Spaghettification: a small black hole would stretch you like a noodle, but falling into a giant one you might cross the edge in one piece
- Andromeda–Milky Way collision (2025): a new study found the famous galactic crash is closer to a coin flip than a certainty

### Scale Breaker

- TON 618: a black hole estimated at around 40 billion Suns, first catalogued as a faint blue star
- Stephenson 2 DFK 1 (1990): a star so big that, put where the Sun is, it would swallow Saturn's orbit
- UY Scuti (1860): crowned the biggest known star, then it shrank when astronomers remeasured its distance
- Laniakea Supercluster (2014): our galaxy turned out to be one of about 100,000 in a supercluster only mapped in 2014
- Hercules–Corona Borealis Great Wall (2013): a structure about 10 billion light-years long, possibly too big for our models of the universe
- Observable universe: 93 billion light-years across, though the universe is only 13.8 billion years old
- Pale Blue Dot (1990): Voyager 1's photo of Earth from 6 billion kilometers, where our planet is smaller than one pixel
- Voyager 1 (1977): in late 2026 it becomes the first human-made object a full light-day from Earth
- Olympus Mons (1971): a Martian volcano two and a half times the height of Everest and about 600 kilometers wide
- Neutron star (1967): a teaspoon of it would weigh about 900 times as much as the Great Pyramid of Giza
- Proxima Centauri (1915): the nearest star to the Sun, yet Voyager 1 would need over 70,000 years to get there

### Mission Files

- Soyuz 11 (1971): the only people ever to die in space, killed when a valve opened as their capsule separated
- Venera 13 (1982): a lander built to last 32 minutes on Venus kept working for 127
- Mars Climate Orbiter (1999): lost at Mars because one team's software used pound-force and another's used newtons
- OSIRIS-REx (2020): it grabbed so much of asteroid Bennu that rocks jammed its lid open and pieces drifted off into space
- Double Asteroid Redirection Test (2022): we crashed a spacecraft into an asteroid on purpose and shortened its orbit by about half an hour
- Cassini–Huygens (2017): the mission ended by diving into Saturn on purpose, to protect moons that might hold life
- New Horizons (2015): the probe that flew past Pluto carries some of the ashes of the man who discovered it
- Hubble Space Telescope (1990): launched with a mirror polished precisely to the wrong shape, so its first pictures came back blurry
- James Webb Space Telescope (2021): 344 single points of failure all had to work, nearly a million miles from any repair crew
- Voyager 2 (1977): still the only spacecraft ever to visit Uranus and Neptune

### Space Got Weird

- PSR B1257+12 (1992): the first planets ever confirmed outside our solar system orbit a dead star
- Przybylski's Star (1961): a star whose light seems to show short-lived elements astronomers still can't fully explain
- Hoag's Object (1950): a near-perfect ring of stars around a yellow core, and nobody is sure how it formed
- Wow! signal (1977): a 72-second radio signal so strong the astronomer circled it and wrote Wow! in the margin
- Tabby's Star (2015): a star that dimmed by up to 22 percent sparked talk of alien megastructures; dust was the answer
- Gamma-ray burst (1967): the brightest explosions in the universe were found by satellites watching for secret nuclear tests
- Betelgeuse (2019): the Great Dimming made the famous red star fade so much people wondered if it was about to explode
- Enceladus (2005): a tiny moon of Saturn sprays jets of water into space from a hidden ocean under its ice
- Voyager Golden Record (1977): a gold-plated record sent to aliens, with a drawing of how to play it on its cover
- Moon tree (1971): seeds that orbited the Moon on Apollo 14 grew into trees across the US, and many were forgotten
- Skylab (1979): when it fell on Western Australia, a local shire fined NASA $400 for littering

### Near Misses

- Apollo 13 (1970): after the lunar module carried the crippled ship home, its builder Grumman jokingly sent the command module's maker an invoice for "towing"
- Carrington Event (1859): the biggest solar storm on record; some telegraph lines kept working with their batteries unplugged
- 99942 Apophis (2004): once given a 2.7 percent chance of hitting Earth, it will pass closer than some satellites in 2029
- 2024 YR4 (2024): for a few weeks the most threatening asteroid ever measured, with a 3.1 percent chance of hitting Earth in 2032
- Chelyabinsk meteor (2013): nobody saw it coming, on the same day astronomers were watching a different asteroid fly past
- July 2012 solar storm (2012): a Carrington-class blast crossed Earth's orbit about nine days after Earth had passed that spot
- Gemini 8 (1966): Neil Armstrong's first spaceflight nearly killed him when a stuck thruster sent the capsule into a violent spin
- Mir (1997): a fire and then a crash with a cargo ship nearly doomed the space station within four months
- 1983 Soviet nuclear false alarm incident (1983): a satellite mistook sunlight on clouds for incoming missiles, and one officer decided it was a false alarm
- Tunguska event (1908): an explosion in the sky flattened forest across 2,150 square kilometers and left no crater
- Gliese 710: a star is on course to pass through the Sun's cloud of comets in about 1.3 million years

### Space Myths, Busted

- Great Wall of China: you can't see it from the Moon with the naked eye, and astronauts struggle to spot it even from orbit
- Far side of the Moon: there's no dark side of the Moon; the far side gets as much sunlight as the side we see
- Season: Earth is closest to the Sun in early January, so distance isn't what makes summer
- Venus: it's hotter than Mercury, though it's nearly twice as far from the Sun
- Uncontrolled decompression: a body exposed to the vacuum of space doesn't explode; that's a persistent movie myth
- Sun: the Sun is white; our atmosphere is what makes it look yellow
- Meteoroid: shooting stars aren't stars at all; most are specks of space dust burning up
- Pluto (2006): it didn't shrink; a vote by just 424 astronomers changed the rules
- Polaris: the North Star isn't the brightest star in the sky, and it isn't even close
- Black hole: if the Sun became a black hole of the same mass, Earth would keep orbiting just as before
- Weightlessness: astronauts don't float because gravity is gone; they're falling around Earth nonstop
