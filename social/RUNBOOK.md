# UpTrendPos daily social post (starts about 14:34 PKT, ready by about 15:00)

You are the scheduled UpTrendPos social-post session. Abdul is NOT watching. Do not ask questions. You design ONE post (image + captions) for ONE business type. You publish nothing to any social network or website. Abdul uploads it himself.

## Hard limits
- Exactly 1 post per run: the entry from `python3 social/post.py next`.
- Content only from `social/SOCIAL_FACTS.md`, `site/automation/FACTS.md`, the calendar entry and that business's website page (`page`). Never invent features, catalog counts, customers or prices.
- The only repo writes allowed are under `social/` (`out/<date>/`, `log.json`). Do not touch `site/`, `kit/` or any other file.
- Never touch uptrendpos.com, WordPress or any social account.

## 1. Workspace
1. Call `add_repo` with uptrendpos/uptrendpos-website (access push). Clone it with `git clone --depth 1 https://github.com/uptrendpos/uptrendpos-website /home/claude/uptrendpos-website` and a 10-minute timeout.
2. `cd /home/claude/uptrendpos-website && python3 social/post.py setup`. This is an npm install of Tabler icons and Poppins. Playwright and Chromium are pre-installed; never run `playwright install`.
3. Read `social/SOCIAL_FACTS.md`, `site/automation/FACTS.md` and the three files in `social/examples/`.
4. `python3 social/post.py next`. The output is today's entry (key, name, catalog, angle, idea, page) plus the last 7 keys.

## 2. Gather facts
1. If `page` is set, extract its visible text and use it as the fact source:
   ```
   python3 -c "import re,sys,html;t=open(sys.argv[1]).read();t=re.sub(r'<(script|style)[^>]*>.*?</\1>','',t,flags=re.S);print(html.unescape(re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',t)))[:12000])" <page>
   ```
2. Also use the `specials` for `site_slug` in `site/automation/queue.json`, if present, and its `line` in `kit/uptrendpos-site-kit/data/industries.json`.
3. Pick ONE strong angle:
   - a real shop-owner pain in Pakistan (udhaar register, expiry loss, Eid rush, load-shedding, searching for items while the customer waits), with the fix;
   - or, on catalog/full-catalog days, the catalog itself.
4. It must not repeat the headline idea of the last 7 posts (`git log -- social/out` or the `recent` keys).

## 3. Design
1. Write `social/out/<YYYY-MM-DD>/spec.json` (PKT date, `"date"` = that date, `"slug"` = Title-Case-Key such as `Pharmacy-Catalog`).
   - Follow the examples and the layout guide in SOCIAL_FACTS.md.
   - Catalog businesses show their count in a `stat` or in the headline.
2. `python3 social/post.py render social/out/<date>/spec.json`.
   - Exit 2 means the gates failed (banned wording, headline too long, blocks overlapping or outside the hero, phone rows cut, text too wide).
   - Fix the spec and render again, up to 5 rounds.
3. Open the `-1640x2048.jpg` with the Read tool and check it like a designer:
   - nothing cut or overlapping;
   - no big empty holes in the hero;
   - headline readable in one line;
   - numbers that add up;
   - generic product names only;
   - spelling is "UpTrendPos".
   Fix and re-render if anything is off.
4. If it still fails after 5 rounds, render the closest working spec from `social/examples/` with today's date and business badge changed. Say so in the report.

## 4. Post content
Write `social/out/<date>/caption.md` exactly in the shape given in SOCIAL_FACTS.md "Post content": ONE caption and ONE hashtag line, used as-is on Facebook, Instagram and LinkedIn. Nothing else goes in the file (no headings, no alt text, no notes).

## 5. Save and deliver
1. `python3 social/post.py mark <key> <date> "<headline text>"`.
2. `git add social/out/<date>/spec.json social/out/<date>/*.jpg social/out/<date>/caption.md social/log.json`.
   - PNGs are gitignored.
   - `git fetch origin main && git rebase origin/main`, then commit "Social post <date>: <key>" ending with the attribution lines from the session, then push. If the push fails twice, continue: delivery matters more.
3. Deliver in this order (Abdul copies straight from the chat, so the text must be visible, not only in a file):
   1. SendUserMessage with the full caption text inside ONE plain code block (```text ... ```) so it copies in one tap, under the line "Post text (Facebook, Instagram, LinkedIn - same for all 3):". Nothing else in that message.
   2. SendUserFile (status "proactive") with ONE file only: the `-1640x2048.png`. Do not send the 4K master or any other file.
   3. If SendUserMessage is not available in the session, put the same code block at the top of the final message instead.

## 6. Final message (this becomes Abdul's notification: short, Roman Urdu + English)
Example: "Aaj ka social post ready: Clothing & Garments - 'Every Size. Every Colour.' 1 image + post text + hashtags (FB, Insta, LinkedIn teeno ke liye same). Kal: Grocery (7,000+)."

On failure, say which step stopped and what was or was not delivered.
