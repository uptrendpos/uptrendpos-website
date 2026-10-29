# UpTrendPos daily run: 2 industry pages a day (runs ~07:40 PKT, pages live by ~08:15)

You are the scheduled UpTrendPos website session. Abdul is NOT watching. Do not ask questions. Work only on uptrendpos.com through the WPVibe connector and only through the endpoints listed here. When anything below says STOP, stop all writes, finish with a short failure report (it becomes the notification) and do not publish anything.

## Hard limits (never break)
- Site writes allowed: `POST /utpk/v1/backup`, `POST /utpk/v1/media`, `POST /utpk/v1/page`, `POST /utpk/v1/media-cleanup`. Nothing else: no wp-cli writes, no plugin/theme/user/option/settings changes, no deletes, no SQL writes, no code snippets.
- Publish only pages whose `daily.py build` gates passed. Never publish a page with an error.
- Content only from automation/FACTS.md + the queue entry. Never invent features, numbers, customers or prices.
- Max 2 pages per run. If fewer than 2 remain, do what remains. If none remain, report "Queue finished" and stop.

## 1. Workspace
1. `add_repo` uptrendpos/uptrendpos-website (access push) and uptrendpos/uptrendpos-site-assets (access push); clone each (`git clone --depth 1`, 10-minute timeout, one at a time) into /home/claude/uptrendpos-website and /home/claude/uptrendpos-site-assets.
2. `ln -s /home/claude/uptrendpos-website/site /home/claude/site && ln -s /home/claude/uptrendpos-website/kit /home/claude/kit && ln -s /home/claude/uptrendpos-site-assets /home/claude/assets` (the builders use these paths).
3. Read: site/automation/FACTS.md, this runbook, HANDOFF.md in the website repo (sections 12-15), and two finished builders (site/build_electrical.py, site/build_baby.py) as the pattern.
4. `python3 site/automation/daily.py next` -> today's 2 types.

## 2. Pre-flight and backup (WPVibe, site https://uptrendpos.com)
1. `rest_api` GET `/utpk/v1/status`. Plugin `version` must be 1.5.0 or newer, and both slugs must exist in `types`. If not: STOP.
2. `rest_api_write` POST `/utpk/v1/backup` with body `{}`. Note `last_backup_before`.
3. Continue to step 3 while the backup runs. Before step 5, GET `/utpk/v1/status` until `last_backup` > `last_backup_before`. Check about once a minute, using the build work as the wait. If it has not finished after 25 minutes: STOP (report "backup did not finish").

## 3. Write the 2 pages
For each slug:
1. `site/build_<short>.py`: copy the structure of build_electrical.py / build_baby.py and write fresh, trade-specific copy for this business (problems, flows, FAQs in the shop owner's own words). Use only FACTS.md + the queue `specials`. File name of the output: `pages/website_<short>_v1.html`, root class `utp-<2 letters>`.
2. `site/hw/gen_<short>.py`: 4 images using the shared helpers (see FACTS.md "Images"), names `uptrendpos-<trade>-<topic>.webp`.
3. Append to `site/pages.json` one entry: `n` (slug), `src` ("pages/website_<short>_v1.html"), `url` ("/industries/<slug>/"), `stage` ("<short>"), `stage_items` (6 items), `cap` "", `label` "", `upd` true, `title`, `desc`, `kw` (queue focus), `sec` (3 Pakistani-phrased secondary keywords), `builder` ("build_<short>.py"), `images` ("gen_<short>.py").

## 4. Build and check
1. `python3 site/automation/daily.py build <slug1> <slug2>`. Exit code 2 = gate errors: fix the copy/images and rebuild (max 3 rounds). A page that still fails is dropped for today (it stays queued).
2. Look at a contact sheet of the 8 images (Pillow, 2 x 4 grid) and fix anything overlapping or cut off.
3. Commit and push repo (message "Daily pages <date>: <slugs>") and the assets repo (message "Assets <date>").

## 5. Publish (WPVibe)
1. Backup must be finished (step 2.3).
2. For every item in `site/automation/out/plan.json` -> `media`: `rest_api_write` POST `/utpk/v1/media` body `{"name":..., "url":..., "alt":...}`. Any error: STOP before any page is published.
3. For every item in `pages`: POST `/utpk/v1/page` body `{"slug":..., "html_url":..., "publish":true}`. The response must show status `publish`, robots `["index"]`, a keywords list starting with the focus keyword and a thumbnail id > 0.
4. GET `/utpk/v1/status`: both slugs `live: true`.
5. POST `/utpk/v1/media-cleanup` body `{"apply":true}`.
6. `python3 site/automation/daily.py mark <published slugs>`, append a line to LOG.md in the website repo (date, slugs, words, density, URLs), commit and push.

## 6. Final message (this is Abdul's notification, keep it short, Roman Urdu + English)
"Aaj ke 2 pages live: <Name 1> <url>, <Name 2> <url>. Backup OK. Media clean (<n> removed). Queue: <k> pages baqi."
On failure: what stopped, at which step, and that nothing was published (or which page was).
