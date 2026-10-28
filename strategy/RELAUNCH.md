# Relaunch: format v2 (owner's go-ahead 2026-10-28)

## Why

From 24 Oct ~16:30 UTC the Shorts feed stopped showing the channel: Shorts-feed views 3,064 (23 Oct) -> 825 -> 455
(25 Oct) while search held, and new Shorts get 9-286 views where they got ~1,000. Retention held (~60%). No change
of ours preceded it, Studio shows no notice, and Shorts uploaded straight to YouTube do no better than Buffer's
(ep225 30 views, ep078 52), so it is a channel-level distribution cut, not one bad upload or the publisher.

Atlas in Numbers was cut at the same hour; Orbitwire was not. What the two cut channels share and Orbitwire
doesn't: a stock Kokoro voice (af_heart here, am_fenrir there), the same word-pop karaoke captions (heavy
all-caps sans, yellow and cyan highlights), evergreen fact narration, and 3-4 uploads a day from one template.
Atlas's custom 3D visuals didn't protect it, so the pictures alone are not the trigger. YouTube's 2026 Shorts
originality update demotes exactly this mass-produced pattern.

## What changes (studio.FORMAT = "v2")

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

## The test

10 v2 Shorts at one a day, through Buffer once its pause ends (29 Oct 19:00 UTC, `auto.BUFFER_PAUSED_UNTIL`). Compare each
one's 24-hour views and Shorts-feed share with the post-drop baseline (47-286 views at 24 h, Shorts feed under
half of views). A clear win is a median over 500 at 24 h or the feed share back over 80%; then raise the pace
one step at a time as `auto.slots_per_day` allows. No clear change after 10 means the cut isn't about the format:
then the next lever is the visuals (scenes made for each script) and the owner decides on the channel's future.
Never promise views; never buy engagement.
