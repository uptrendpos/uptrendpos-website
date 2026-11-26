# Daily Urdu page run (05:00 PKT, ONE page a day)

Goal: turn the next English page of uptrendpos.com into a 100% Urdu twin with the SAME design, then publish it at
`/ur/<same path>/`, with complete on-page, technical and local SEO, and run the daily site health check.
Abdul's decision (26 Nov 2026): 1 page a day, Jameel Noori Nastaleeq, Urdu pages link to Urdu pages, English to English.

Paths in this run: website repo `/home/claude/site` (= uptrendpos-website/site), plugin `/home/claude/kit`,
asset repo `/home/claude/assets`. Tool: `T=/home/claude/site/urdu-pages/ur_tool.py`. Work dir: `/home/claude/ur`.

## 0. Rules that never change
- Only these site writes: POST /utpk/v1/backup, /page (with "lang":"ur"), /font. GET reads: /status, /source, /check.
  No plugin, theme, option, SQL, file, user, self-update, delete or /replace calls.
- Exactly ONE new Urdu page per run: the slug from `python3 $T next`. Never rewrite an English page.
- Content = the English page, translated. Do not add, drop or change facts, numbers, prices, plans, features or claims.
  Never: installation/setup charges, competitor names, AGR, "FBR approved/certified" (منظور شدہ), customer counts,
  product brand names, iOS app, free plan.
- Urdu quality: clear, simple, natural Urdu a Pakistani shop owner reads easily (see GLOSSARY.md). No machine-style
  literal word order. Headings short. Same meaning as English, sentence by sentence.
- Backup first (POST /utpk/v1/backup {"now":true} -> done:true) before /page or /font.
- If any gate fails after 3 fix rounds: publish nothing, the slug stays queued, report why.

## 1. Pick and read
1. `python3 $T next` -> slug. Empty -> report "Urdu queue finished" and only do step 6.
2. GET `/utpk/v1/status` (check version >= 1.7.1, `urdu` list, the English page is live). For a business type the Urdu hub
   (/ur/industries/) must be live (it is, since 26 Nov).
3. GET `/utpk/v1/source?slug=<slug>&pad=1` with max_chars 300000. The padding makes the connector save the reply to a
   file (the result names the file). Then `python3 $T source <that file> /home/claude/ur/<slug>.en.html` (md5 checked).
   Never retype page code by hand.

## 2. Translate
1. `python3 $T extract <slug>.en.html <slug>.units.json` -> every text block and attribute as a unit with placeholders
   ([[a1]]...[[/a1]] link, [[s2]] icon or span, [[br]]). Fill `ur` for EVERY unit and attr:
   - keep every placeholder exactly once (you may move it to where it reads right in Urdu);
   - keep numbers, Rs amounts, domains, emails and phone numbers exactly; keep the Latin terms listed in GLOSSARY.md;
   - data-seo-title / data-seo-desc / data-seo-kw: follow "SEO in Urdu" in GLOSSARY.md (main Urdu keyword first);
   - alt and aria-label in Urdu (describe the picture or element in plain Urdu);
   - write the translations with a Python script that loads the units JSON and sets `ur` from a dict, then saves
     `<slug>.ur.json`.
2. Hero animation: `python3 $T stage <slug>.en.html` prints its 6 items. Translate fields 0, 3, 4, 5 of each (short:
   field 5 is a 1-3 word label), keep 1 (icon) and 2 (colour). Save as `<slug>.stage.json` (list of 6 lists).
3. `python3 $T apply <slug>.en.html <slug>.ur.json <slug>.ur.html --stage <slug>.stage.json`
   (adds class utp-urdu, lang="ur", dir="rtl", id "-ur", Urdu stage, Roman-Urdu WhatsApp text, today's reviewed date,
   <bdi> around numbers, removes iframe/form that the site refuses).

## 3. Gates (all must pass)
1. `python3 $T check <slug>.en.html <slug>.ur.html` -> "ok": true. It checks: page-code rules, Urdu root, SEO title 25-70
   and description 100-165 chars in Urdu, one H1, same h2/h3/section/details/a/img/li/table counts, same links, same ids,
   every English number present, no English words left outside <bdi> (except the glossary list), mostly-Urdu text,
   forbidden phrases, Urdu stage items. Fix and re-run until ok (max 3 rounds).
2. Read the Urdu text once more as a shop owner: every sentence clear and correct? Fix anything awkward.
3. Visual check: `node /home/claude/site/urdu-pages/preview.js <slug>.ur.html /home/claude/ur/<slug>` -> must report
   no errors, scrollWidth = viewport (1440 and 390), empty `overflow`, empty `smallUrdu`. Open both screenshots
   (<slug>-desktop.png, <slug>-mobile.png) and look: right-to-left layout, Urdu readable, nothing overlapping.
   If a layout problem needs CSS, do NOT change the plugin: publish only if it is minor and report it for Abdul.

## 4. Font + publish
1. Save the page code to `/home/claude/assets/pages/ur/<slug>.html`.
2. `ASSETS=/home/claude/assets bash /home/claude/site/urdu-pages/build_font.sh` -> rebuilds the Jameel Noori subset
   from ALL Urdu pages and must print "0 mismatches".
3. Commit + push the asset repo (pages/ur/<slug>.html + fonts/...woff2). `git fetch origin main` and rebase first.
   Wait until `https://raw.githubusercontent.com/uptrendpos/uptrendpos-site-assets/main/pages/ur/<slug>.html` serves the new
   file (raw GitHub can lag ~1-5 min; fetch it with curl and compare md5 before using it).
4. Backup (step 0).
5. POST `/utpk/v1/page` {"slug":"<slug>","lang":"ur","title":"<short Urdu page name>","html_url":"<raw url>","publish":true}
   -> url must be https://uptrendpos.com/ur/<english path>/ (business types: /ur/industries/<slug>/).
6. POST `/utpk/v1/font` {} -> installed:true (new version).

## 5. Verify live (GET /utpk/v1/check?path=<path>)
For the new Urdu page: status 200, lang ur-PK, dir rtl, Urdu title/description, canonical = its own URL, og_locale ur_PK,
hreflang en-PK + ur-PK + x-default pairing the English and Urdu URLs, exactly one Urdu H1, NAP (name, phone, city) true,
security headers present, `links_to_en` = only pages that have no Urdu twin yet (plus the English switch link).
Also check the English twin: its hreflang now lists the Urdu URL.
Then `python3 $T mark <slug> <url>`, append a line to `/home/claude/uptrendpos-website/LOG.md`, commit + push the website repo.

## 6. Daily site health check (every run, also when the queue is finished)
GET /utpk/v1/check for: `/`, `/ur/`, `/pos-software-pricing/`, `/contact-us/`, the new Urdu page, and 2 other pages
(rotate through the queue list). Report anything wrong: status not 200, missing/duplicate H1, title or description
missing or too long, canonical not self, robots not index, missing hreflang on a pair, NAP false, a security header missing,
images without alt (except the decorative logo), non-WebP images, ms > 1500 (slow), html_kb > 250.
GET /utpk/v1/status: last_backup recent, downloads apk/exe found, urdu_font version set.
Do NOT fix site settings yourself; list issues for Abdul with the page and the fix.

## 7. Report (final message = Abdul's notification; Roman Urdu + English, short)
"Aaj ka Urdu page live: <Urdu title> <url>. Backup OK. Font updated. Health: <OK / issues>. Urdu queue: <n> pages baqi."
On failure: what stopped, at which step, and whether anything was published.
