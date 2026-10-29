# Relaunch: format v3, Days of Odd's format 2 (2026-10-29)

v3 replaces v2 before any v2 Short was posted. The owner asked to apply Days of Odd's changes to this channel, and
Tarun's kit (`Desktop/YouTube/tarun-channels-2026-10-29/kit/`, CHANNEL.md decision of 2026-10-07) records the format
that brought Days of Odd back from the same kind of drop on the same pipeline. v2 was our own guess; v3 is that
proven package, ported piece by piece because the two pipelines have diverged.

## What changes (studio.FORMAT = "v3")

- **Topics:** famous subjects first. A backlog topic with at least 15,000 English Wikipedia readers in 30 days
  (`auto.MIN_READERS`) goes before any without, and new topics are only added above it, 8 a day while fewer than
  14 open topics are that famous (`auto.FAMOUS_TARGET`, `RESTOCK`). On 29 Oct the open backlog's median was 1,928
  readers, with 1 of 20 measured over the bar: the clearest difference from Days of Odd.
- **Script:** 65-95 words (22-32 s) in 7-12 beats of 14 words or fewer, a hook of 10 words or fewer that states
  the surprise plainly and never opens on a year or date, beat 2 making it stranger (never background), told the
  way you'd tell a friend, at most 2 years named (`writer`; `check.DURATION` 20-40 s).
- **Voice:** Days of Odd's narrator, Gemini `Zubenelgenubi` (en-US), played 1.05 times as fast with pauses inside
  the take cut to 0.25 s (`studio.VOICE`, `tts._tempo`, `tts._tighten`). Its direction goes as a style note, not
  spoken text, and a take that says things not in the script is refused (`tts._unscripted`). A mispronounced
  word is respelled for the voice only (`Voice.say`).
- **Look:** `look: bold`: a picture at least 1,000 px tall fills the screen around its subject instead of a
  framed print, with a brighter grade (`plates.fill`, `plates.vivid`, `render.BOLD_GRADE`); the on-screen hook
  is 150 px. Captions are the kit's word-by-word style, as on Days of Odd.
- **Music:** a bed composed for each Short in its series' mood (`bed.py`, `studio.MOODS`), fading out at the end.
- **Volume:** 2 a day at the channel's two evening slots (19:00 and 21:30 ET), keeping 14 ready
  (`auto.DAILY_CAP`, `INVENTORY_TARGET`), as Days of Odd does.
- **Older Shorts:** v2 Shorts (ep245-ep253) are shelved like the old format: never scheduled, kept on disk.

## The test

The first 10 v3 Shorts, compared with the post-drop baseline (47-286 views at 24 h, Shorts feed under half of
views). A clear win is a median over 500 at 24 h or the feed share back over 80%. No clear change after 10 means
the next lever is the visuals (scenes made for each script) and the owner decides on the channel's future. Never
promise views; never buy engagement.

## Before: format v2 (owner's go-ahead 2026-10-28; replaced by v3 before posting)

### Why

From 24 Oct ~16:30 UTC the Shorts feed stopped showing the channel: Shorts-feed views 3,064 (23 Oct) -> 825 -> 455
(25 Oct) while search held, and new Shorts get 9-286 views where they got ~1,000. Retention held (~60%). No change
of ours preceded it, Studio shows no notice, and Shorts uploaded straight to YouTube do no better than Buffer's
(ep225 30 views, ep078 52), so it is a channel-level distribution cut, not one bad upload or the publisher.

Atlas in Numbers was cut at the same hour; Orbitwire was not. What the two cut channels share and Orbitwire
doesn't: a stock Kokoro voice (af_heart here, am_fenrir there), the same word-pop karaoke captions (heavy
all-caps sans, yellow and cyan highlights), evergreen fact narration, and 3-4 uploads a day from one template.
Atlas's custom 3D visuals didn't protect it, so the pictures alone are not the trigger. YouTube's 2026 Shorts
originality update demotes exactly this mass-produced pattern.

**Correction, 29 Oct (public stats of all the studio's channels, `Desktop/YouTube/tarun-channels-2026-10-29/`):**
Days of Odd, made by the same studio kit with the same Kokoro voice and captions, was *not* cut: median ~1,100
views a Short before 24 Oct and ~1,050 after, at 24-34 s and 2 a day. So the voice and captions are not the
trigger. What the cut channels share is volume: Universe 3.3 a day and Atlas 2.4 before the cut; Days of Odd 1.9
and Orbitwire 1 were not cut. Length alone doesn't separate them (Atlas ~38 s was cut, Orbitwire ~55 s wasn't),
but Days of Odd's ~30 s is the best-performing shape on this kit, so v2 now aims for it (`writer.MIN_WORDS`/
`MAX_WORDS` 70-90, `check.DURATION` 22-38 s). The first 7 v2 Shorts (ep245-ep253) were made at ~54 s; later ones
are ~30 s, which gives a length comparison inside the test.

### What changes (studio.FORMAT = "v2")

- **Voice:** the channel's own host voice, Gemini TTS `Sadaltager` with a conversational host direction
  (`studio.VOICE`), checked by Whisper (`tts._gemini`). No Kokoro fallback: a Short with no take waits.
- **Captions:** subtitles, a phrase at a time in DM Serif Display, sentence case, low in the frame, the
  emphasis words warm-tinted (`studio.CAPTIONS`, `CaptionStyle.karaoke = False`). No word-by-word pop.
- **Script:** a host thinking out loud with one viewer: "you", at most two "I"s, and at least one beat that says
  why it matters or what it means, from the claims only (`writer.PROMPT`).
- **Volume:** one Short a day (`auto.DAILY_CAP`), aiming for 10 made (`auto.INVENTORY_TARGET`), with no
  last-resort Gemma reviews (`auto.LAST_RESORT_BELOW = 0`).
- **Older Shorts:** finished Shorts without `format: v2` are shelved (`auto.episodes`): never scheduled, never
  counted as ready. The owner started the test early: the 8 old-format Shorts scheduled on YouTube for 29 Oct -
  5 Nov are private with no release date (not deleted; `hold.json` "withdrawn" keeps the video id).
- **Compute:** this repository is public, so GitHub's runner is free; when Modal's credit can't make the Shorts
  wanted, the run says so (`status.json` `starved`) and the backup workflow makes them (`.github/backup_gate.py`).

### The test

10 v2 Shorts at one a day, through Buffer once its pause ends (29 Oct 19:00 UTC, `auto.BUFFER_PAUSED_UNTIL`). Compare each
one's 24-hour views and Shorts-feed share with the post-drop baseline (47-286 views at 24 h, Shorts feed under
half of views). A clear win is a median over 500 at 24 h or the feed share back over 80%; then raise the pace
one step at a time as `auto.slots_per_day` allows. No clear change after 10 means the cut isn't about the format:
then the next lever is the visuals (scenes made for each script) and the owner decides on the channel's future.
Never promise views; never buy engagement.
