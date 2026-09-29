# Universe Receipts: source of truth

- **Channel:** Universe Receipts (@UniverseReceipts), <https://www.youtube.com/@UniverseReceipts>, a Brand Account
  managed by akshshivam5@gmail.com. Channel ID `UCal2hAu7VaZimTwaAgeBEyg`. Buffer channel ID
  `6abbffabea19ca0bde264803`.
- **Niche:** true, mind-bending space and astronomy stories and facts, every claim backed by two reputable
  sites ("receipts") listed in the description. English, for a US audience (then the UK, Canada, Australia).
- **Series:** The Universe Is Terrifying, Scale Breaker, Mission Files, Space Got Weird, Near Misses, Space
  Myths, Busted. First hashtag `#space`.
- **Owner account:** akshshivam5@gmail.com (a personal Google account); the owner lives in India, so the
  channel country is India. Chrome profile: Profile 3.
- **Accounts (all on akshshivam5@gmail.com, created 2026-09-29):** Google Cloud project `universe-receipts`
  (YouTube Data and Analytics APIs, OAuth app "Universe Receipts tools" in production, unverified, Desktop
  client); AI Studio key "universe-receipts studio" in that project; Buffer (free, email sign-up); Cloudinary
  (free, cloud `gtr1bxym`); Modal (workspace `akshshivam5`, Starter, no card: $1/month); GitHub `ashivam-dot`.
  Private repository <https://github.com/ashivam-dot/universe-receipts>. App home page and privacy policy on
  GitHub Pages: <https://ashivam-dot.github.io/universe-receipts-site/>. Modal app: `universe-receipts`.
- **Dates:** Day 0 is 2026-10-01; Day 100 is 2027-01-09.
- **Target:** YouTube Partner Program monetization on Shorts before the 2027-02-01 threshold change, and as
  much growth toward the owner's 100,000-subscriber goal as original, accurate Shorts can earn. The honest
  base and stretch cases are in `strategy/PLAN-100.md`.
- **Format:** YouTube Shorts only, 40–58 seconds, 3 a day at US Eastern slots (4 from Day 30 and 5 from Day 50
  while engaged share holds), monetized through the Shorts path of the YouTube Partner Program.
- **Built from:** the studio of Days of Odd, a strange-but-true history channel. `reference/days-of-odd/`
  has that channel's documents; its decision log explains why the pipeline works the way it does.

Start here: `PLAYBOOK.md` (the daily routine), `strategy/STRATEGY.md`, `strategy/PLAN-100.md`,
`strategy/CALENDAR.md`, `strategy/SCRIPT-RULES.md`, `OWNER-CHECKLIST.md`.

## Standing instructions from the owner

- The agent manages the channel end to end: niche, audience, format, settings, branding, scripts, voice,
  editing, captions, titles, hashtags, scheduling, promotion, and analytics. It writes a daily report in
  `reports/`.
- Use the best available open-source repo, library, framework, or tool for each job. Re-check GitHub
  (stars, recent pushes, archived status, commercial-use license) before adopting or replacing a tool, and
  record the check in `research/`.
- Production never stops and never needs the Mac: it runs in the cloud on free tiers (see "How it runs").
  The Mac only monitors.
- Open anything on the channel's Google account in the owner's own Chrome profile, never with bare `open`.
- The owner signs in to every service himself. The agent never stores or types passwords, SMS codes, or
  card details, and keys go into `pipeline/.env` with `kit/setkey.py`, never through the chat.

## Hard rules

- No bought subscribers or views, bots, sub-for-sub, engagement pods, spam comments, fake accounts,
  reuploads of other creators' content, or misleading titles. These violate YouTube policy and end monetization.
- No automated use of YouTube's website for anything recurring: uploads, comments, likes, subscriptions,
  views, or scraping. YouTube's terms forbid automated access. Publishing goes through Buffer's official API
  integration; analytics through the official APIs. One-time account setup (creating the channel, branding, settings) is done by the owner, in his own
  browser.
- The YouTube API sign-in can edit the channel, but the pipeline only reads analytics, adds Shorts to
  playlists, and (when built) moderates held comments. Never edit, delete, or upload videos through it.
- Every Short has an original, sourced script with a claims table, so it passes YouTube's inauthentic-content review.
  Disclose realistic synthetic media when YouTube requires it.
- Use only assets whose licenses allow commercial use: public domain, CC0, or CC BY with credit.

## How it runs

| Job | Tool | Cost |
|---|---|---|
| Running the channel | The cloud studio on Modal: `studio_run` in the Modal app `universe-receipts` runs `ytc auto` four times a day (11:05, 17:05, 23:05, 05:05 IST) on a fresh clone of the private repository <https://github.com/ashivam-dot/universe-receipts>, and pushes what changed with a deploy key that reaches only that repository. Each run deploys that clone's code as the app first (so `slot_watch` runs the latest code), syncs Buffer, files live Shorts into playlists, collects finished Shorts, does the daily routine in the first run after 14:00 IST (stats, learnings, new topics, report), schedules Shorts into Buffer, and starts new ones when fewer than 42 are ready. Its state lives in the repository (`status/`, `content/`, `strategy/`); its keys in the Modal secret `universe-receipts-studio` (`pipeline/modal_secret.py`). GitHub's `studio` workflow is the backup: its schedule is 2 hours behind, and it works only when Modal's last run failed or is over 8 hours old. The Mac isn't needed | free: about $1 a month of Modal's credit ($1 on the Starter plan, $30 with a card on file; keep the spend limit at $0) |
| Research, scripts, image picks, reviews | Gemini's free tier first (AI Studio project `universe-receipts`), about 15 seconds a prompt: every step starts on the six Flash models (20 requests a day each), except the picture checks, which start on the Flash-Lite models (500 a day each). Once Flash is spent, scripts go to Flash-Lite, and the other steps to Flash-Lite and then to other providers' free models through their OpenAI-compatible APIs (`llm.PROVIDERS`; one whose key isn't set is skipped): OVHcloud AI Endpoints without an account (Qwen3.5-397B and two Qwen 27B models; 2 requests a minute per model, shared by everyone on the same address, so best effort), Mistral's free plan (Ministral 14B, 30 requests a minute, key in the `YTC_MISTRAL_API_KEY` secret; it researches, picks, and checks, but broke the script rules in testing, so it writes nothing), and OpenRouter's free Dots3-Note Preview (50 requests a day for the account, key in the `YTC_OPENROUTER_API_KEY` secret; it writes and researches after Qwen3.5-397B and ahead of Gemma, but doesn't judge). Gemma 4 31B, in the same Gemini project, takes prompts under its 16,000-token-a-minute cap. So no Short is held for Gemini's reset. The review, which decides what gets published, uses a Flash model while 9 or more are ready: a Short finished after Flash is spent waits for the reset (12:35 IST, 13:35 in winter) and is reviewed first after it. With fewer than 9 ready, Qwen3.5-397B or Cursor judges (a backup model passes only a Short it finds nothing to fix in), and with fewer than 3, Gemma. When nothing else can answer (or Gemini refuses a prompt), Cursor's agent models do, through the Cursor SDK (`cursor_llm.py`, key in the `YTC_CURSOR_API_KEY` secret), in 2 to 5 minutes a prompt. Each Cursor prompt goes to a fresh agent with no tools, so it can only answer in text. Cursor takes the best model the key allows: Opus, Sonnet, GPT, Gemini, then Grok, newest first. Apart from prompts Gemini refuses, Cursor answers only while fewer than 9 are ready. `YTC_LLM_FIRST=cursor` puts Cursor first | Gemini, OVHcloud, Mistral, OpenRouter: free; Cursor: counts against the key's Cursor plan (optional) |
| Making each Short | A Modal worker (`studio_episode`, a quarter CPU, since it mostly waits on the language models) makes one Short end to end: research, script, images, render, review, fixes, and hosting. The run that starts it exits at once, and the next run collects the result. Runs start as many as the credit covers after a $2 reserve for the runs themselves. Only GitHub's backup makes Shorts on its runner, once Modal's credit is used up: three at a time (they mostly wait on the language model, so the waits overlap and renders take turns), within a share of the Actions minutes paced over the month | free: about $0.12 per Short; $30 of credit (with a card on file) covers about 230 a month, and without a card GitHub's runner makes them |
| Voice | Kokoro-82M, `af_heart` (Apache-2.0) | free |
| Visuals | Found from each beat's named subjects first (`sources.py`: the Wikipedia article's pictures, Wikidata's image, Commons category and "depicts" statements, then searches), with Openverse, Wellcome Collection, The Met, and the Art Institute of Chicago for weak beats; public domain, CC0, and CC BY only. SigLIP (`google/siglip-base-patch16-224`, Apache-2.0) ranks them against each beat on Modal (`rank_pictures`), a Gemini model picks from the top six and marks the detail to show, and a second model checks the picks. A beat no picture fits gets a designed title card (a date, a number, or a quote the script cites; `plates.py`). No AI-generated pictures | free |
| Render | `pipeline/` (FFmpeg, libass captions, two-pass loudness) on Modal (8 CPUs) for Modal workers, on the runner for Shorts made there. Each shot is a plate: a tall picture fills the screen, others sit as a framed print over a blurred copy, long beats cut to a close-up, with an eased camera, a warm grade and grain, and the hook as on-screen text in the first seconds. Fonts: Anton, Montserrat, DM Serif Display (all OFL) | free |
| Watching | `monitor/monitor.py` (read-only): the studio's status and run history, Buffer, Cloudinary, Modal credit, YouTube's public feed. GitHub's `watchdog` workflow runs it every 3 hours and pushes each new alert to the owner's phone through ntfy (topic in the `YTC_NTFY_TOPIC` secret and `pipeline/.env`), plus a summary each morning; a run on Modal that fails or can't save pushes at once. On the Mac it runs every 15 minutes (launchd) with notifications and `monitor/out/dashboard.html`, reading Buffer at most every 2 hours (Buffer's API allows 250 requests a day) | free |
| Speech check | faster-whisper `small.en` (MIT) in the same Modal job; `ytc check` lists words it heard differently from the script | free, inside the render's cost |
| Publishing | Buffer free plan API, official YouTube partner; queue of up to 10. Buffer fetches each video from Cloudinary when the post goes out and never retries a post it fails, so `slot_watch` on Modal looks 5, 20, and 40 minutes after each slot hour (ET) and sends a post that just failed again under the same id, 5 minutes out, after checking its video downloads. A failure over an hour old goes back to waiting at the next studio run | free: about 15 of Buffer's 250 requests a day |
| Video hosting for Buffer | Cloudinary free plan | free |
| Analytics and playlists | YouTube Data and Analytics APIs through the owner's own Google Cloud app (project `universe-receipts`): `ytc stats` writes `analytics/<date>.json` with per-Short retention; `ytc playlists` adds each live Short to its series playlist | free |
| App home page and privacy policy | <https://universereceipts.pages.dev/> on Cloudflare Pages (project `universereceipts`, source in `site/`), required by Google for the app | free |
| GPU models (voice tests, later) | Modal, same account and credit | free within credit |

## Decisions log

| Date | Decision | Why |
|---|---|---|
| 2026-09-29 | Built the studio from the Days of Odd kit | Its pipeline already runs a channel unattended on free tiers; that channel's decisions and their reasons are in `reference/days-of-odd/CHANNEL.md` |
| 2026-09-29 | Niche: true, mind-bending space and astronomy stories and facts, English, US audience | Ranked first of six niches in `research/niche-selection.md`: the top long-form RPM category (useful if long-form is added; Shorts pay by the viewer's country, about $0.33 per 1,000 US views), free real imagery (NASA, JPL, and USGS public domain; ESO, ESA/Hubble, ESA/Webb, and NOIRLab CC BY), low policy risk, evergreen topics with news spikes, and a verified newcomer, Cosmic Lens, near 100k subscribers in under a year. Not Days of Odd's niche (strange-but-true history), so the kit's two channels don't compete |
| 2026-09-29 | Name: Universe Receipts (@UniverseReceipts) | "Receipts" means proof: every claim is backed by two sources listed in the description, which is also the channel's defense against the inauthentic-content review and space misinformation. The handle was free and no channel used the name when checked |
| 2026-09-29 | Six series: The Universe Is Terrifying, Scale Breaker, Mission Files, Space Got Weird, Near Misses, Space Myths, Busted | Named series look curated rather than templated and give viewers a reason to follow. They cover the space hooks that travel (danger with real numbers, scale comparisons, mission stories, strange discoveries, close calls, myth-busting); promises in `strategy/STRATEGY.md` |
| 2026-09-29 | Day 0 is 2026-10-01 (Day 100 is 2027-01-09); first hashtag `#space`; the calendar seeded with 64 backlog topics and 19 anniversaries (Oct 1 to Nov 30), each starting with an English Wikipedia title checked against Wikipedia's API | Launching Oct 1 leaves about 75 days to reach YPP's 10M-view bar before the mid-December application target, ahead of the 20M bar from 2027-02-01. Every topic has an article because research and demand ranking go through Wikipedia |
| 2026-09-29 | Timely topics: the daily routine adds up to 2 a day to a new Timely table at the top of `strategy/CALENDAR.md`, picked by the language model from the space articles among English Wikipedia's 300 most-read of the last 2 days (Wikimedia's keyless "top" pageviews API, filtered by each article's short description) and NASA's news feed (<https://www.nasa.gov/news-release/feed/>, checked: 200, RSS, hourly). Each still needs a series, an existing English Wikipedia article (its title starts the line), and no overlap with known topics. For 3 days a timely topic is made first, even with the inventory full, and posted in the next free slot with one slot a day over the pace (never over 5); after that it waits with the backlog (`growth.py`, `auto.add_timely`) | Topic demand is the second growth lever in `strategy/STRATEGY.md`: well-known subjects stop more thumbs, and the niche has "news spikes" (`research/niche-selection.md`). A Short made 2 weeks after the news misses it, since the inventory runs 2 weeks ahead. On 2026-09-29 the feeds surfaced "Starship flight 14" (92,167 Wikipedia views in a day) and 10 NASA items in 48 hours. The existing checks (article, series, near-duplicates) keep news topics to the channel's sourced standard |
| 2026-09-29 | Breakout follow-ups: when a Short has 3x its peers' median views at the same age within 48 hours of going live (and at least 1,000 views), or 100,000 views, the daily routine asks the language model for follow-ups in its series and neighbourhood and queues the first 2 that pass the topic checks in the Timely table. Each breakout is noted in the day's report and kept in `status/state.json` so a Short triggers once. `ytc stats` snapshots now record when they were taken, so a Short's age at each count is exact | `strategy/PLAN-100.md` and lever 3 of `strategy/STRATEGY.md`: queue sequels to any breakout within 48 hours. Growth here comes in bursts (Cosmic Lens's 2.5M-view Pluto video, `research/niche-selection.md`), and the best of ten new-channel Shorts reaches about 6x the median (`research/shorts-strategy.md`, section 3), so 3x within 48 hours flags the top Shorts early enough to feed them. Comparing views at the same age is fairer than lifetime totals. The 1,000-view floor stops 3x of a handful of Day-2 views from counting |
| 2026-09-29 | Optional cross-posting: with `BUFFER_TIKTOK_CHANNEL_ID` or `BUFFER_INSTAGRAM_CHANNEL_ID` set, each Short scheduled on YouTube is also scheduled natively on that Buffer channel: same Cloudinary file (no watermark), same time, a caption with the title, description, sources by site, the synthetic-voice note, and up to 5 hashtags without `#shorts`; Instagram as a Reel shared to the feed, both with the AI-disclosure flag YouTube gets. It fills each channel's own queue of 10, checks Buffer for a twin before posting, and records failures instead of failing the run. Off by default | Lever 6 of `strategy/STRATEGY.md`; TikTok and Instagram push down watermarked reposts and recommend originals (`research/shorts-strategy.md`, section 5). Buffer's free plan has 3 channels, and its GraphQL schema (checked 2026-09-29 at developers.buffer.com) takes `metadata.instagram {type: reel, shouldShareToFeed, isAiGenerated}` and `metadata.tiktok {isAiGenerated}`. It costs about 1 request per channel per run plus 1 per post, well within the 250 a day. TikTok isn't available in India, so the owner may only be able to add Instagram |
| 2026-09-29 | The agent created every account in the owner's signed-in Chrome profile (Profile 3): the Universe Receipts Brand Account and handle, the Google Cloud project and OAuth app, the Gemini key, Modal, Cloudinary, and Buffer (email sign-up; its password was generated inside the page and never seen or stored, so the owner resets it by email if he ever needs to sign in), and connected Buffer and the studio to the new channel | The owner asked not to be involved in setup. Keys went straight from the page into `pipeline/.env` through `kit/setkey.py` without being displayed. A first Gemini key was deleted and replaced because the new `AQ.` key format slipped past a redaction filter into a local log |
| 2026-09-29 | The OAuth app's home page and privacy policy are on GitHub Pages (<https://ashivam-dot.github.io/universe-receipts-site/>, public repo `ashivam-dot/universe-receipts-site`) instead of Cloudflare Pages | Google requires them to publish the app to production. `github.io` subdomains are on the public suffix list, so they count as their own authorized domain, and GitHub was already signed in |
| 2026-09-29 | Channel description, keywords, country India, language English, banner, and not-made-for-kids set through the YouTube Data API; the picture uploaded in Studio | One-time channel setup; the API can't set the picture. Studio's comment filters and upload defaults were left at YouTube's defaults (Buffer sets each Short's metadata) |
| 2026-09-29 | Phone verification deferred | It needs the SMS code on the owner's phone. Shorts don't need it; the Partner Program application does. Tracked in `OWNER-CHECKLIST.md` |
| 2026-09-29 | `llm._configured` counts Gemini models only when `YTC_GEMINI_API_KEY` is set, so without the key the ladder falls through to the keyless backups instead of failing | The first local test had no key and stopped at the first Gemini call |
| 2026-09-29 | First cloud run (GitHub `studio`, run 1): deployed the Modal app with its schedule and started ep001 (Apollo 13), ep002 (NASA's founding, Oct 1 anniversary), ep003 (Sputnik 1, Oct 4) on Modal; the watchdog ran clean | Modal's Starter plan without a card gives $1 a month, so most Shorts will be made on GitHub's runner until a card is added with a $0 spend limit |
| 2026-09-30 | Modal: the owner added a card (Starter plan, $30 of credit a month); the agent set the spend limit to $0, the total usage limit to $30 (the owner's cap), and `YTC_MODAL_CREDIT=30` in `pipeline/.env`, the Modal secret, and the GitHub variable | Modal's default usage limit was $42.50, which would have allowed $12.50 of charges. At $0, work stops when the credit runs out and nothing is charged. $30 covers about 230 Shorts a month, so every Short is made on Modal |

## Layout

- `strategy/`: strategy, 100-day plan, calendar, script rules
- `brand/`: avatar, banner, watermark (`brand/out/`), channel copy, image credits
- `content/episodes/<id>/`: spec, research, render, publish record, one folder per Short
- `content/rejected/<id>/`: episodes that failed the quality gate twice, kept for learning
- `pipeline/`: the `ytc` production and publishing code (`ytc auto` is the cloud studio's run)
- `pipeline/src/ytc/cloud.py`: the Modal app (`studio_run`, `studio_episode`, `render_episode`, `slot_watch`); `pipeline/modal_secret.py` makes its deploy key, ntfy topic, and secret
- `.github/workflows/`: `studio.yml` (the backup for Modal's runs, gated by `.github/backup_gate.py`), `watchdog.yml` (alerts to the owner's phone), and `selftest.yml` (renders an existing Short on a runner)
- `status/`: the last run's `status.json`, every run in `history.jsonl`, and `state.json` (daily routine, quota hold)
- `monitor/`: the read-only monitor (the watchdog's, and the Mac's with its launchd job)
- `analytics/`: daily snapshots from the YouTube Analytics API
- `reports/`: daily reports `day-NNN.md`, weekly reviews, `BLOCKERS.md`
- `kit/`: the setup guide's helpers and notes (`configure.py`, `setkey.py`, `push_secrets.py`, `verify.py`)
- `reference/days-of-odd/`: the documents of the channel this studio was built for
- `research/`: research notes and tool sweeps
- `site/`: the analytics app's public home page and privacy policy; redeploy with
  `npx wrangler pages deploy site --project-name=universereceipts --branch=main`
- `secrets/` and `pipeline/.env`: credentials (git-ignored)
