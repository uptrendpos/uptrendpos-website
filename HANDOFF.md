# UpTrendPos Website: Site Kit handoff (20 Oct 2026, updated 29 Oct 2026 for 1.3)

Read this first in a new chat. It replaces the "Fixed setup" part of claude/HANDOFF_Website_Build_20Oct2026.md. The content rules, confirmed app facts and next-page queue in that file still apply.

## 1. Restore the workspace
1. Upload `UpTrendPos_Website_Workspace_v3_20Oct2026.zip`.
2. Unzip it to /home/claude. It holds `site/` and `kit/`.
3. Tools: Python 3, Playwright + Chromium, Pillow, PHP (lint and preview stubs), pdftoppm.

## 2. Fixed setup (one plugin replaces the 2 WPCode snippets)
- ONE plugin: **UpTrendPos Site Kit**, `kit/uptrendpos-site-kit/`, **version 1.1.0**. Delivered as `UpTrendPos-Site-Kit-v1.1.zip`. It holds 1-plugin, 2-pages, 3-images, seo-sheet.csv, INSTALL-GUIDE.html, README.txt and UpTrendPos-Product-Guide.pdf.
- The WPCode snippets "UpTrendPos Design System" and "UpTrendPos SEO Snippet" are retired. Abdul has already switched them off, along with the old Elementor header and footer, and activated plugin 1.0.0 on the live site. Update path: Upload Plugin > Replace current with uploaded.
- Plugin parts:
  - `inc/config.php`: brand data, settings, industries registry, live pages.
  - `inc/front.php`: fonts, CSS/JS, header + Industries mega menu, footer, live-link gate + ALT pass.
  - `inc/schema.php`: Rank Math graph merge.
  - `inc/seo.php`: OG fallback, en-PK, /llms.txt, 301s, clean-up.
  - `inc/admin.php`: SEO Health + Settings.
  - `data/industries.json`: 32 business types.
  - `assets/css/utp.css`, `assets/js/utp.js`.
- Live pages are automatic: a page counts as live when it is published and not noindex. Menu, footer, hub ItemList, llms.txt and `data-page` links all follow this.
- Download links and the EEAT reviewer live in UpTrendPos > Settings.
- Every page root carries `data-seo-title`, `data-seo-desc`, `data-seo-kw` and `data-seo-robots`. SEO Health fills Rank Math from them with one click.

## 3. Hero in 1.1 (atom / nuclear orbit)
- Cleaner hero:
  - H1 size is clamp(36px, 4.3vw, 58px), max 15ch.
  - The highlight is a green-to-yellow underline. The yellow block is gone because it overlapped the line above.
  - The lead is 16–18px.
- Stage: `<div class="utp-stage" data-stage="KEY" role="img" aria-label="...">`, built by utp.js `buildStage()`.
  - It is a 2D atom: 3 elliptical orbits (blue, green, yellow) rotated -28, 32 and 92 degrees, with 2 icon electrons each.
  - Motion uses CSS `offset-path: path(ellipse)`. Do not use 3D rotateX, because it rendered dark squares in Chrome.
  - Nucleus: "UpTrend POS" with pulse waves.
- Market-gap cards: 6 per page, each "problem -> UpTrendPos fix". They show 2 at a time in slots top-left and bottom-right, on an 18 s cycle with 3 s stagger.
- Presets live in utp.js `P` (home, grocery, pharmacy, tailor, mobile, solar, electronics, fbr, pricing, downloads, about, hub, contact). A new trade needs one new preset.
- Compact mode (stage under 460px wide) shrinks the orbit to 300px.
- Reduced motion stops the animation.
- The old Elementor footer `div.utp-foot` is hidden by CSS and JS, so the footer shows once.

## 4. Plans (confirmed 20 Oct 2026)
- Staff commission (rules + report) is now part of **Enterprise** and Custom.
- Staff attendance and salaries (payroll) are Custom only.
- This is updated in the pricing page (plan list, fit card, compare row N/Y/Y), the pricing stage preset, llms.txt and the commission lines on the industry pages (`GLOBAL_FIX` in build_kit.py).

## 5. Product guide (new)
- Sources:
  - `site/docs/content.py`: STATS, 10 GAPS, 9 STEPS, 16 MODULES, PLANS, 22-term GLOSSARY.
  - `site/docs/build_docs.py` and `site/docs/docs.css` (brand palette, Poppins, A4 print rules).
- Outputs:
  - `docs/index.html`: artifact "UpTrendPos Product Guide", https://claude.ai/artifact/XpzUYaZphwjKp3jDgz6VKZ
  - `docs/guide-print.html`: rendered to an 18-page A4 PDF with Playwright `page.pdf()`. Swap the Google Fonts link for the local Poppins `@font-face` first, because the sandbox has no Google Fonts.
- It covers only built features, written in simple English, with no "FBR approved / certified" claims.

## 6. Build commands
- `python3 site/build_kit.py`: delivery pages + seo-sheet.csv + keyword checks. Output goes to `delivery/UpTrendPos-Site-Kit-v1.1`.
- `python3 site/preview/build_site.py`, then `python3 site/build_guide.py`: preview site + INSTALL-GUIDE.
- Review artifact: "UpTrendPos Site Kit Review", https://claude.ai/artifact/1NGSJ5xxq2zaXoMQpy84Mf (version 2 = 1.1).

## 7. Install steps for 1.1 (told to Abdul)
1. Upload `uptrendpos-site-kit-1.1.0.zip` and choose Replace current.
2. Re-paste all 16 pages. The stage labels and content changed, and the pricing page changed.
3. Run SEO Health > Fill Rank Math.
4. Purge the LiteSpeed / hPanel cache.

## 8. Open questions for Abdul
- Grocery catalog size: his feature list says 600+, but the website says about 7,000. The guide currently says "ready catalog".
- Which job cards are live. Earlier notes said electronics and mobile have no job cards.
- EEAT reviewer name.
- Customer logo mapping.
- Whether GTM maps `utp_contact_click`.
- Next: new pages (Electrical & LED + Clothing) on the same plugin.

## 9. Site Kit 1.2 (20 Oct 2026, evening) — current version
- Restore from `UpTrendPos_Website_Workspace_v4_20Oct2026.zip` (replaces v3). Delivery: `UpTrendPos-Site-Kit-v1.2.zip` (plugin `uptrendpos-site-kit-1.2.0.zip` + 16 pages + seo-sheet + INSTALL-GUIDE + product guide PDF).
- Abdul's asks: remove the picture under the hero on every page; Home keeps the dark blue hero (agrsoft.com home style); every other page gets a light hero (agrsoft.com service-page style); orbit nucleus = white disc with the colour logo (not full blue); smaller cards; orbit structure like agrsoft.com but own styling.
- Theme rule: dark hero only when the page root is `utp utp-home` (or is_front_page). `utpk_current_dark_hero()` in front.php; header gets `is-dark` on Home, `is-light` (transparent, navy text) on other hero pages, `is-solid is-static` without a hero. Light hero CSS = `.utp:not(.utp-home) .utp-hero` block at the end of utp.css.
- Picture under hero: `SHOWCASE = False` in build_kit.py (no `.utp-showcase`, no `.utp-doc-fig`); plugin CSS also hides both, so old page code is fixed by the plugin alone. The focus keyword moves to the first content image ALT (step 5b in build_kit.py).
- Stage 1.2 (utp.js `buildStage`): canvas --cw 560 x --ch 540, centre --cy 270, orbit --R 196; compact (<460px) 400 x 494, --cy 200, --R 140, card under the orbit. Nucleus = `assets/img/logo-stacked.svg` (built from src/logo.svg paths) on a white disc with a turning brand-colour ring and pulse waves. 6 nodes FIXED at -90 + i*60 deg (so the card never covers one), soft float, label pill; flowing dashed data lines; dashed orbit ring turns with two light dots; outer conic ring turns. JS cycles the active node + its card every 3.6 s; pauses off screen / hidden tab; reduced motion = still.
- Presets `P` now have a 6th field = short node label (all 13 presets). New trade = one preset with 6 entries [problem, icon, colour, fix title, fix line, label].
- Cards: 214px, one at a time, left side top/bottom alternating on desktop (never bottom-right, where the WhatsApp float sits).
- Review artifact "UpTrendPos Site Kit Review" = version 3 (1.2).
- Install told to Abdul: Replace plugin with 1.2.0 → purge LiteSpeed + hPanel → (optional, when free) re-paste 16 pages → SEO Health fill.

## 10. Site Kit 1.2.1 (21 Oct 2026) — current version
- Bug (Abdul's phone): after scrolling, the mobile menu showed only a thin "Industries" strip and the screen froze until closed. Cause: `.utp-nav.is-solid` has backdrop-filter, which makes the header the containing block for the position:fixed `.utn-drawer`, so the drawer was clipped to the header height while html overflow was locked. Fix in utp.css (mobile block): `.utp-nav.is-menu{backdrop-filter:none;transform:none}` + drawer `overscroll-behavior:contain`; utp.js setMenu removes `is-hidden` on open. Rule: never put backdrop-filter/transform/filter on `.utp-nav` while the drawer is open.
- Plugin only (`uptrendpos-site-kit-1.2.1.zip`), no page re-paste. Workspace backup = `UpTrendPos_Website_Workspace_v5_21Oct2026.zip`. Review artifact = version 4.

## 11. Next chat (saved 21 Oct 2026, 09:51)
- Restore: upload `UpTrendPos_Website_Workspace_v5_21Oct2026.zip`, unzip to /home/claude (holds `site/` + `kit/`). Live plugin = 1.2.1.
- NEW FACT (Abdul, 21 Oct 2026): the solar catalog has reached **1,100+ products** (was "600+ shared" for Electronics/Solar/Appliances/CCTV).
  - Ask first: is 1,100+ solar-only, or the shared electronics + solar + CCTV catalog? And has the electronics/CCTV count changed?
  - Then update every "600+" solar mention: `build_solar.py` (page copy, FAQs, meta description "600+ products ready"), `seo-sheet` desc in build_kit.py P (solar + electronics if shared), utp.js presets `solar` (and `electronics`, `hub`, `home` card "600+ electronics"), product guide `content.py` STATS/MODULES, hub page, home page, llms.txt in config.php, data/industries.json lines. Rebuild with build_kit.py → bump plugin to 1.2.2 if JS/PHP changed → re-paste only the changed pages.
- Still open from section 8: grocery catalog size (600+ vs 7,000), live job cards, EEAT reviewer name, customer logo mapping, GTM `utp_contact_click`.
- Next new pages after that: Electrical & LED Lighting + Clothing & Garments (ask catalog size first).

## 12. Site Kit 1.3 (29 Oct 2026) - current version
- Restore: `UpTrendPos_Website_Workspace_v6_29Oct2026.zip` (replaces v5), unzip to /home/claude (holds `site/` + `kit/`). Delivery: `UpTrendPos-Site-Kit-v1.3.zip` (plugin 1.3.0 + 18 pages + 11 images + seo-sheet + README).
- Audit vs `CONTENT_STRATEGY_Website_Copy_Playbook_27Oct2026.md` + `HANDOFF_Website_Content_Customer_Features_27Oct2026.md`: industry pages already follow pain->fix, flow strip, FAQ; only factual fixes needed.
- Facts applied (Abdul, 21/29 Oct): Electronics + Solar + Appliances + CCTV shared catalog **1,100+** (app shows 1117); Mobile & Computer **670+** (was 700+, lowered); Cosmetics **5,000+**; Clothing **0** (no ready catalog). Yearly **10% off first year stays**.
- Pricing: one-time installation fee now shown (card line `.utp-fee-note`, compare row, FAQ): Premium Rs 20,000, Enterprise Rs 30,000, Custom Rs 60,000. Terms: "installation fee", amount on pricing page + first invoice. llms.txt facts carry fees + catalog counts.
- NEW pages: `build_clothing.py` -> /industries/clothing-store-pos-software/ (focus "clothing store POS software", 0.82%, 11 FAQs) and `build_cosmetics.py` -> /industries/cosmetics-store-pos-software/ (focus "cosmetics store POS software", 0.86%, 11 FAQs). Images: `hw/gen_fashion_beauty.py` (8). Stage presets `clothing`, `cosmetics` + icon `tag` in utp.js. Icons layers/sync/spark/drop/heart added to industry.py.
- LAUNCH items shown only with the grey "Coming soon" tag: season sale offers, loyalty points, stock transfer between branches, salon booking.
- build_kit.py: `upd=True` pages get "Last updated 29 October 2026"; other pages keep 20 October so they stay byte-identical to 1.2.1 (no re-paste).
- Re-paste list for Abdul: 08 clothing, 09 cosmetics (new), 07 mobile, 10 electronics, 13 solar, 15 pricing, 18 terms; 06 industries optional.
- At launch (not now): terms trial/grace text must follow S87 (trial end -> shop paused read-only, data kept 90 days; paid grace monthly 7 / yearly 15 days), plus storage and counter limits per plan, offline reports, 2FA, morning briefing (all LAUNCH in the 27 Oct content handoff).
- Next pair (growing-business priority): Shoes & Footwear + Electrical & LED Lighting, or Vehicle Showroom (bikes / EV) - ask catalog counts first.

## 13. Site Kit 1.3.1 (29 Oct 2026, afternoon) - current version
- Restore: `UpTrendPos_Website_Workspace_v7_29Oct2026.zip` (replaces v6). Delivery `UpTrendPos-Site-Kit-v1.3.1.zip` (plugin 1.3.1 + 20 pages + 11 images + seo-sheet + README).
- Live state when 1.3.1 was made: plugin 1.3.0 uploaded; only clothing + cosmetics pasted from 1.3; every other page = 1.2.1.
- DECISION (Abdul): installation charges are never on the website; sales team handles them per client. Pricing + Terms reverted to the 1.2.1 code (byte-identical to live), fee line removed from llms.txt, `.utp-fee-note` CSS removed. Content handoff + playbook updated.
- NEW `inc/auto.php`: on every page save (save_post_page + elementor/document/after_save) Rank Math title, description, focus + secondary keywords (comma list, max 5) and robots are written from the page code; `update_post_metadata` / `add_post_metadata` guard keeps code values if Rank Math later writes different ones. Featured image = first content image (`utpk_page_image`); File-Manager files are registered as attachments (`utpk_attachment_for`); a hand-picked thumbnail is kept (`_utpk_auto_thumb` marks ours). One-time backfill of all designed pages on the first admin_init after an update (`utpk_auto_done` option). Settings switches `auto_seo`, `auto_thumb` (default on). SEO Health shows "No featured image". Stub-tested: fill, overwrite guard, manual thumbnail kept, other meta untouched.
- NEW pages: `build_shoes.py` -> /industries/shoe-store-pos-software/ (focus "shoe store POS software", 0.82%) and `build_vehicle.py` -> /industries/vehicle-showroom-software/ (focus "vehicle showroom software", 0.84%; new slug breaks the -pos-software pattern on purpose so the keyword is in the URL; page must be created under Industries). Both catalog 0. Images `hw/gen_shoes_vehicle.py`. Presets `shoes`, `vehicle`. Vehicle added to data/industries.json (group hardware) and as a hub card (Hardware, auto and home = 7 types).
- Vehicle claims kept to what is built: one serial per unit = chassis; engine / battery second serial and registration + documents tracking = Coming soon; qist with guarantor Enterprise+.
- Re-paste list: 13 shoes (new), 20 vehicle (new), 07 mobile, 10 electronics, 14 solar, 06 industries.
- Next pair: ask catalog counts first. Candidates by growth: Electrical & LED, Baby & Diaper, Hardware & Sanitary.

## 14. Site Kit 1.4 (29 Oct 2026, evening) - current version
- Restore: `UpTrendPos_Website_Workspace_v8_29Oct2026.zip` (replaces v7). Delivery `UpTrendPos-Site-Kit-v1.4.zip` (plugin 1.4.0 + 22 pages + 19 images + seo-sheet + README). Replaces 1.3.1 fully.
- STANDING RULE (Abdul): Home "POS software in Pakistan for 30+ types of shops" and the Industries hub must link EVERY business type; new verticals must appear and link on their own. Implemented 3 ways: (1) `inc/pages.php` `utpk_fill_industry_lists()` completes both lists from data/industries.json on output (before the live-link gate; idempotent; hub "N types" recounted); (2) build_kit.py asserts every registry slug is in core/home.html and the hub source; (3) SEO Health card "Business type links".
- STANDING RULE (Abdul): full automation - Abdul only pastes HTML. `utpk_create_missing_pages()` makes a DRAFT for every registry type and core page with no WP page: slug, parent Industries, Elementor layout cloned from a designed page (clothing/pharmacy/grocery) with ONE empty HTML widget and fresh element ids, hide_title yes, same page template, rank_math_robots noindex, `_utpk_autocreated`. Runs on admin_init when sig(version + registry + core list) changes; button "Create missing pages now"; admin notice lists drafts waiting for code. Publish -> auto.php fills SEO/index/featured image. Stub-tested (lists on live 1.2.1 Home + hub, draft meta, no duplicates on 2nd run).
- New pages: `build_electrical.py` -> /industries/electrical-store-pos-software/ (focus "electrical store POS software", 0.86%; coil->meter, box->piece units, A4 contractor quotes, udhaar, damage; price lists for electricians = Coming soon) and `build_baby.py` -> /industries/baby-store-pos-software/ (focus "baby store POS software", 0.84%; pack/piece, diaper sizes, batch + expiry; no brand names). Catalog 0 for both. Images `hw/gen_electrical_baby.py`. Presets `electrical`, `baby`.
- Vehicle Showroom added to Home source (Hardware, auto and home group).
- Next pair: ask catalog counts first. Candidates: Hardware & Sanitary, Auto Spare Parts, Jewellery & Gold.

## 15. Daily automation setup (29 Oct 2026, in progress)
- Goal (Abdul): every day ~8:00 PKT, 2 new industry pages built, designed, published and a notification sent; no manual work; media always clean.
- Site connected through the WPVibe connector (admin sales@uptrendpos.com, WP 7.1.4, Hello Elementor, UpdraftPlus, LiteSpeed). Free plan 300 calls/day.
- Media audit 29 Oct: Media Library uploads never overwrite, they add `-1/-2/-3`, so Solar/Electronics/Mobile still showed the OLD 600+/700+ catalog images; 17 unused duplicate copies + 6 unused images (pos5, pos7, privacy/support/terms webp, favicon-white).
- Plugin 1.5.0 (`inc/api.php`, utpk/v1, admin login only): GET status; POST media (uptrendpos-*.webp only, base64 or allowlisted URL, same name replaced in place + sizes regenerated, sha1 no-op); POST page (registry/core slugs only, validates UTP code, writes first HTML widget via Elementor Document::save, publish, auto SEO + thumbnail, LiteSpeed purge); POST backup (schedules updraft_backup_all + spawn_cron); POST media-cleanup (merges newest `-N` copy into the base file name, deletes unreferenced copies and uptrendpos-*.webp unused > 48h; reference check = postmeta + content + thumbnails + options). Setting `asset_source` = public raw GitHub folder allowed for URL downloads. utp.js reads `data-stage-items` so new trades need no plugin update. Stub-tested.
- Pipeline: `site/automation/` = queue.json (21 types, growth order, catalog 0, safe specials), FACTS.md (allowed / coming-soon / never-write), daily.py (next / build with gates / mark), DAILY_RUNBOOK.md (scheduled-session steps), config.json (asset_repo OWNER placeholder). build_kit reads extra pages from site/pages.json and embeds stage_items. End-to-end tested on Baby.
- Decisions (Abdul): publish directly when gates pass; I create the GitHub repos; all remaining 21 types catalog 0; media cleanup after an UpdraftPlus backup.
- Waiting on Abdul: (1) upload plugin 1.5.0, (2) connect GitHub in claude.ai connectors, (3) turn on WPVibe "Dangerously bypass approvals" for unattended runs.
- Then: create private `uptrendpos-website` + public `uptrendpos-site-assets` repos, set asset_source + config.json, backup -> media-cleanup apply -> delete pos5/pos7/favicon-white via wp-cli (approval) -> publish fixed Mobile/Electronics/Solar pages via /utpk/v1/page, create the daily scheduled task (07:4x PKT, push + email), do one supervised test run.

## 16. Website design record: catalog counts + social-post look (30 Oct 2026) - current
- Source of truth: `social/docs/HANDOFF_Website_Catalog_Counts_and_Post_Design_30Oct2026.md` (also in the claude.ai project). It is part of the website design record: every website page (manual builds, Site Kit releases and the daily automation) follows its counts table (section 1) and design guide (sections 3.1-3.5).
- Catalog facts (Abdul, 30 Oct 2026): full UpTrendPos catalog **38,000+ products**, live, and more are on the way. Any shop can search the whole catalog by name or category and add any product. Write exactly "38,000+" until Abdul gives a new number; never round up.
- Solar / Electronics / Appliances / CCTV shared catalog = **1,100+** (unchanged; the solar page already says 1,100+). This closes the 21 Oct open question in section 10.
- Per-type counts: Pharmacy 17,000+, Grocery 7,000+, Cosmetics 5,500+, Crockery 2,000+, Solar/Electronics 1,100+, Toys 1,000+, Clothing 950+, Mobile 700+, Bags 680+, Undergarments 400+, Baby 350+, Perfume 300+, Sports 250+, Shoes 200+, Stationery 200+, Watch 150+, Gift 150+; starter lists (body line only): Furniture 70+, LED 50+, Veterinary 50+, Vape 50+. No catalog: Tailoring, Hardware, Paint, Auto Parts, Tyre, Battery, Jewellery & Gold, Artificial Jewellery, Glass, Meat, Agri, Vehicle, Electrical (non-LED).
- Design: one trade accent per page (`--acc1/--acc2` on the page root, e.g. Jewellery #B7791F->#F7B731), plus yellow only as a navy-text background; new Site Kit components = kicker pill, coloured-second-half headline, catalog phone mockup ("search, tick, add"), yellow catalog stat card, info card, floating chip, 3 icon tiles, navy contact pill; new sections = "Ready catalog" on every industry page with a count, "Full catalog" band on Home + Industries hub, count badges on hub cards.
- DONE 30 Oct 2026: Site Kit 1.5.2 (counts in hero stages, industries.json lines + menu, llms.txt incl. 38,000+) and republished Clothing 950+, Baby 350+, Shoes 200+, Cosmetics 5,500+, Mobile 700+ (with images), Grocery 7,000+, Pharmacy, Furniture 70+, Electrical LED 50+, Industries hub (count lines + full-catalog callout). Home: one full-catalog sentence in core/home.html, needs a manual paste (Home is not writable through utpk/v1/page). Still open: the new design components and sections (3.2-3.3).
