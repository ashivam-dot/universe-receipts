# Universe Receipts: script and episode rules

Channel: **Universe Receipts** (@UniverseReceipts), true, mind-bending space and astronomy Shorts in American
English for a US audience. Every claim comes with receipts: at least two reputable sites behind it.
Promise: one true, jaw-dropping space story or fact in under a minute, told well and sourced.

Before writing, read `strategy/LEARNINGS.md`: what's working on this channel, what isn't, and the numbers
each new Short should beat. Apply every proven rule in it.

## Deliverables per episode

Folder: `content/episodes/<id>/` (ids are `ep001`, `ep002`, ...).

1. `short.yaml`: the spec the renderer reads (schema below).
2. `research.md`: a claims table. Each factual claim in the narration gets one row: claim, at least two
   independent reputable sources (URLs), and confidence. Add notes on disputed details and how the script
   handles them. End with a line `Better than the last: ...` naming the learning or improvement this
   episode applies and where (for example, "hook states the twist in 9 words, per the rule on first-2-second
   surprises").

## Script rules

- **Length:** 70–90 spoken words (about 30 seconds), 5–8 beats, one or two short sentences per beat
  (`writer.MIN_WORDS`/`MAX_WORDS`; since 2026-10-29, after Days of Odd's 24–34 s Shorts held through the 24 Oct cut).
- **Hook (beat 1):** a curiosity-gap statement of 12 words or fewer that is literally true and concrete: it
  opens a question the rest of the Short answers ("An oxygen tank exploded 200,000 miles from Earth."; "There is
  a star that seems to be made partly of rare metals."). No "Did you know", no greeting, no channel name, no
  question the Short can't answer. Open inside the story.
- **Shape:** hook, then context, 2–3 escalating beats, a twist or payoff, and a last line that loops back to
  the first. The twist is the fact a curious viewer is least likely to already know. For a famous subject
  (Apollo 13, Voyager, Pluto), build the Short around its least-known true detail rather than retelling the
  familiar story in order: reviewers score a well-told but well-known story 3 on payoff.
- **Loop:** the last line is a complete sentence on its own that echoes the hook's image or question, so
  replaying the hook feels like the next line ("It was built to last 32 minutes." / "A Soviet lander kept
  talking from the surface of Venus for 127 minutes."). Never end on a dangling "because", "when", "until",
  or "that": the reviewer scores it 2 or 3 as jarring.
- **Clarity:** one idea per beat. After the hook, tell events in the order they happened; for a fact Short,
  build from the familiar to the mind-bending. Introduce each person the first time with who they are
  ("Apollo 13 commander Jim Lovell"), and name at most 3 people in a Short. Explain any object type in a few
  plain words the first time ("a magnetar, a dead star with a monstrous magnetic field"). Don't open a beat
  with "he", "she", "they", or "it" unless the previous beat named that person or thing. Each line should name
  something a picture can show (an object, spacecraft, mission, person, or place) or a date, number, or quote a
  title card can show.
- **On-screen hook:** `hook_text` is 2–6 words shown over beat 1. It adds to the spoken hook (a number, a
  distance, the stakes) without repeating it or giving away the payoff: "3 ASTRONAUTS, 1 DYING SHIP".
- **Truth:** every claim must be supported by at least two independent reputable sources (NASA, ESA, ESO,
  JPL, observatories and universities, peer-reviewed journals, established science publications such as
  Scientific American, Sky & Telescope, or Nature's news pages, encyclopedias, established newspapers). Disputed
  details and open questions are either left out or attributed ("according to one study", "astronomers think").
  Never invent quotes, numbers, names, or dates. Prefer understatement to exaggeration.
- **Numbers:** state every number precisely as the sources give it, with its unit, and keep "about", "at
  least", or "up to" when the source has it. Don't round up, stack superlatives, or convert units yourself;
  use a conversion or everyday comparison only when it is in the claims. Keep the distinction between
  estimates, measurements, and probabilities (an impact chance is a probability, not a prediction).
- **No sensationalism:** no false or unfalsifiable framing: "NASA is hiding...", "scientists are baffled",
  "this could end all life tomorrow", aliens as the explanation, or doom the sources don't state. A hypothesis
  is called a hypothesis. A myth in "Space Myths, Busted" is named as a myth and then busted with sourced facts.
- **Tone:** awed, precise, a little wry; the wonder comes from the facts, not from hype. "The Universe Is
  Terrifying" earns its dread with real numbers, never fear-mongering. Crew losses (Soyuz 11, Challenger,
  Columbia, Apollo 1) are told with respect: no graphic injury or death detail, no mocking anyone. No
  present-day politics, no medical, legal, or financial advice.
- **Language:** American English. Years as digits (the narrator reads "1977" as "nineteen seventy-seven").
  Big numbers as digits with commas ("200,000") or words for the scale ("330 million light-years"); never
  scientific notation. Spell out units and names the narrator might misread ("kilometers", not "km";
  "astronomical units", not "AU"; "the James Webb Space Telescope" or "Webb", not "JWST"). Check catalog
  designations ("SGR 1806-20") with `ytc phonemes`.
- **Originality:** write the story from the sources in your own words. Don't paraphrase another creator's
  script or video.

## Metadata rules

- **Title:** 60 characters or fewer, accurate, curiosity-driven. At most one word in capitals, no emojis,
  no false promises, no "NASA is hiding" or "scientists are terrified" style bait.
- **Description:** 1–2 plain sentences. The pipeline appends sources and image credits from `sources`
  and the asset manifest.
- **Hashtags:** exactly 3: `#space`, then 2 specific ones (`#apollo13`, `#nasa`, `#blackhole`).
- **Tags:** 4–8 plain keywords.
- **Series:** one of `The Universe Is Terrifying`, `Scale Breaker`, `Mission Files`, `Space Got Weird`,
  `Near Misses`, `Space Myths, Busted`. Spell it exactly: each live Short is added to the playlist with that name.
- **synthetic_media:** `false` unless a beat uses a realistic AI image of a real person, object, or event.

## Visual rules

The studio picks pictures itself (`pick.py`). For each beat the writer gives:

- `visual`: the ideal picture as NASA or ESO would caption the image (subject, kind of picture, instrument or
  mission, year), 15 words or fewer: "Hubble image of the Crab Nebula, 2005", "photograph of the damaged
  Apollo 13 service module, 1970".
- `subjects`: 0–3 exact English Wikipedia article titles for what that picture shows, most specific first
  ("Apollo 13", "Crab Nebula"). They lead to the subject's own picture on Wikidata, its Commons category, and
  files tagged as depicting it.
- `year`: when the beat takes place (0 if it has no time, as for most facts about an object).
- `queries`: 2–3 Commons keyword searches naming the exact subject.
- `card`: a title card for when no picture fits: `dateline` (a date and place or mission), `fact` (a number or
  a short fact), or `quote` (words quoted in the claims, exactly), using only the beat's text and claims;
  `none` otherwise. At most 2 cards are used per Short, never for the hook.

Kinds of pictures, best first: real telescope images of the object (Hubble, Webb, Chandra, ESO's VLT,
NOIRLab's telescopes), real spacecraft and mission photos (including crew and launch photos, and pictures
taken by the spacecraft), mission patches, and clear diagrams. An artist's concept from NASA, ESO, ESA/Hubble,
ESA/Webb, or NOIRLab is fine for something never photographed (an exoplanet's surface, a black hole up close,
a magnetar), and the narration never calls it a photo; a real image of the subject always beats an
illustration. Never sci-fi or movie stills, fan art, or AI renderings of real objects.

Candidates are ranked by how well they match `visual` (SigLIP, on the CPU), the model picks from the best six per
beat and marks the subject, a quick second look flags clear problems, and a beat with no fitting picture gets
its card, or an earlier picture reframed. A tall picture fills the screen; a wide, square, or small one is
shown whole as a framed print over a blurred copy of itself; a beat of about 3 seconds or more cuts to a
close-up of the part the line names.

Pictures are public domain, CC0, or CC BY (credited in the description); never CC BY-SA, NC, or ND. That
means: NASA, JPL, Goddard, NOAA/NESDIS, and USGS astrogeology imagery (public domain); ESO, ESA/Hubble
(esahubble.org), ESA/Webb (esawebb.org), and NOIRLab (CC BY 4.0, credited); and Wikimedia Commons files under
those licenses. Never imagery from the main esa.int site (CC BY-SA IGO, ShareAlike) or anything NonCommercial.
Flickr Commons scans marked "no known copyright restrictions" are used only when dated before 1931.

In a spec written by hand, each beat's visual comes from public-domain or openly licensed archives via the
pipeline, at least 1,200 px on the long side:
  - `commons`: Wikimedia Commons, auto-filtered to public domain, CC0, or CC BY.
  - `nasa`: NASA images (images.nasa.gov), public domain.
  - `met`: The Met, CC0 (rarely useful here: old astronomical prints and instruments).
  - `aic`: Art Institute of Chicago, CC0 (rarely useful here).
  - `url`: a picture already chosen, with `url` (the file to fetch) and `credit` (source, title, credit,
    license, url of its page); 600 px is enough, as it's then shown as a card.
  - `card`: a designed title card, `card: {kind: dateline, big: "April 1970", small: "Apollo 13"}`.
  - `color`: a plain gradient, as a last resort.
- `query` must name the exact subject so the search hits the right image (for example
  `Crab Nebula Hubble mosaic`, not `space cloud`). The actual object or mission beats a generic starfield.
- Each source takes its best-ranked result, so the same query always gives the same image. To get a
  different one, change the query. On Commons, `intitle:"words from the file name"` pins a single file.
- `met` and `aic` only take an artwork whose title, artist, date, or subject tags contain most of the query's
  subject words, so give them short subject queries. Their images are also on Commons.
- Always give `fallbacks` in a sensible order, ending with `color`.
- Vary `motion` across beats: `zoom_in`, `zoom_out`, `pan_left`, `pan_right`, `pan_up`, `pan_down`.
- The vertical crop keeps the middle of a tall image. To keep another part, set `focus_x` (0 is the
  left edge, 1 the right) or `focus_y` (0 is the top, 1 the bottom). `box: [left, top, right, bottom]` (0 to 1)
  marks the part a close-up cuts to. Changing only `motion`, the focus, or the box keeps the image already
  downloaded.
- Avoid images showing corpses, wounds, executions, or nudity, and pictures with large watermarks or
  burned-in text.
- Don't use the same image for two beats, except that the loop line may return to the hook's image with
  `visual: {reuse: 1, motion: zoom_out}`.

## Sound rules

- `sfx: whoosh` on up to 3 scene changes, `pop` on up to 2 punchlines, `riser` once before the twist,
  otherwise `none`. No music.

## Spec schema (short.yaml)

```yaml
id: ep001
title: "Apollo 13's crew rode home in a lunar lifeboat"
series: "Mission Files"
description: |
  In April 1970 an oxygen tank exploded on Apollo 13, and three astronauts had to use their lunar module to get home.
sources:
  - https://www.nasa.gov/...
  - https://www.britannica.com/...
hashtags: ["#space", "#apollo13", "#nasa"]
tags: [apollo 13, nasa, lunar module, 1970]
voice: {voice: af_heart, speed: 1.05}
hook_text: "3 ASTRONAUTS, 1 DYING SHIP"
beats:
  - text: An oxygen tank exploded 200,000 miles from Earth.
    emphasis: [exploded]
    sfx: whoosh
    visual: {source: nasa, query: Apollo 13 damaged service module, fallbacks: [commons, color], motion: zoom_in}
  - text: It was April 1970, and Apollo 13 was on its way to the Moon.
    emphasis: [April 1970]
    visual: {source: card, card: {kind: dateline, big: April 1970, small: "Apollo 13"}}
```

`emphasis` words must appear in that beat's text; use 1–2 per beat, single words or short phrases.

## Render and check

From `/Users/ashivam/Desktop/YouTube/YouTube-100-Day-Autopilot/youtube-studio/pipeline`:

```bash
uv run --no-sync ytc make ../content/episodes/<id>/short.yaml
uv run --no-sync ytc check ../content/episodes/<id>/<id>.mp4
```

Keep `--no-sync`: the environment is already installed, and without it every `uv run` re-checks a
GitHub-hosted dependency and waits on other agents' runs, which can stall a command for minutes.

`ytc make` renders on Modal's cloud when `MODAL_TOKEN_ID` is set in `pipeline/.env` and falls back to this
Mac if the cloud fails; add `--where local` or `--where cloud` to force one. Only the Short and the files
under `work/` that `ytc check` and `ytc publish` read are kept; intermediate clips are deleted.

The check prints duration, loudness, and each beat's asset and source, plus `warnings` for anything outside
the limits or any beat that fell back to a gradient; fix every warning. Its `speech.differences` lists where
a speech recognizer heard something other than the script. Check each with
`uv run --no-sync ytc phonemes "<the sentence>"`, which prints the narrator's pronunciation. If a word is
wrong, write it as `[word](/phonemes/)` using that alphabet (`[Oumuamua](/ʔoʊmuːəmuːə/)`), re-render, and note
it in `research.md`. Other spellings of a correctly spoken name and skipped short words are normal. It also writes one frame per beat to
`content/episodes/<id>/work/frames/`. Look at every frame. If an image is wrong, off-topic, low quality,
or has distracting burned-in text, change that beat's `query` or `source` and re-render; a changed visual
is fetched again automatically. Aim for 40–50 seconds.
