"""Writes the review + install guide: preview_site/index.html (artifact hub with preview links)
and <delivery>/INSTALL-GUIDE.html (standalone copy for the zip)."""
import html, pathlib, sys
sys.path.insert(0, '/home/claude/site')
from build_kit import P, OUT  # noqa: E402

E = lambda s: html.escape(s, quote=True)
WP_NAME = {'about-us': 'About Us', 'contact-us': 'Contact Us', 'downloads': 'Downloads', 'fbr-pos-integration': 'FBR POS Integration', 'home': 'Home', 'industries': 'Industries',
           'mobile-shop-pos-software': 'mobile shop POS software', 'electronics-store-pos-software': 'POS Software for Electronics, Home Appliances & CCTV Shop',
           'grocery-store-pos-software': 'POS Software for Grocery Store', 'pharmacy-pos-software': 'POS Software for Pharmacy & Medical Store', 'solar-shop-pos-software': 'POS Software for Solar Shop',
           'tailor-shop-pos-software': 'tailor shop POS software', 'pricing': 'POS Software Pricing Plans', 'privacy-policy': 'Privacy And Policy', 'support': 'Support', 'terms-and-conditions': 'Terms & Conditions'}
NOTE = {'contact-us': 'Keep <code>[fluentform id="1"]</code> inside the code. If a separate Fluent Forms widget is still under the HTML widget, delete it.',
        'home': 'Only page with the dark blue hero.'}


def copy_btn(val):
    return f'<button class="cp" type="button" data-copy="{E(val)}">Copy</button>'


def page_rows(preview):
    out = []
    for i, p in enumerate(P, 1):
        fn = f'{i:02d}-{p["n"]}.html'
        kw = p['kw'] + (', ' + p['sec'] if p['sec'] else '')
        prev = f'<a class="pv" href="p/{fn}" target="_blank" rel="noopener">Open preview</a>' if preview else ''
        note = f'<p class="note">{NOTE[p["n"]]}</p>' if p['n'] in NOTE else ''
        out.append(f'''<article class="pg" id="pg-{p["n"]}">
  <header><span class="num">{i:02d}</span><div class="pgt"><h3>{E(WP_NAME[p["n"]])}</h3><p class="url">uptrendpos.com{E(p["url"])} · paste <code>2-pages/{fn}</code></p></div>{prev}</header>
  {note}
  <dl>
    <div><dt>SEO title <span class="len">{len(p["title"])}</span></dt><dd><span>{E(p["title"])}</span>{copy_btn(p["title"])}</dd></div>
    <div><dt>Description <span class="len">{len(p["desc"])}</span></dt><dd><span>{E(p["desc"])}</span>{copy_btn(p["desc"])}</dd></div>
    <div><dt>Focus + secondary keywords</dt><dd><span>{E(kw)}</span>{copy_btn(kw)}</dd></div>
  </dl>
</article>''')
    return '\n'.join(out)


def body(preview):
    steps = f'''
<section class="blk" id="install">
  <h2>Update in 4 steps</h2>
  <ol class="steps">
    <li><h3>Replace the plugin</h3><p>Plugins &rarr; Add New &rarr; Upload Plugin &rarr; <code>1-plugin/uptrendpos-site-kit-1.2.1.zip</code> &rarr; Install &rarr; <b>Replace current with uploaded</b>. Settings stay as they are. This alone gives every page the new look: light hero on all pages except Home, the new orbit with the white UpTrendPos logo, small cards, and no picture under the hero.</p></li>
    <li><h3>Clear cache and check</h3><p>LiteSpeed Cache &rarr; Purge All, then hPanel &rarr; Clear cache. Open Home (dark blue) and one inner page (light) on a computer and on a phone.</p></li>
    <li><h3>Paste the 16 pages (when you have time)</h3><p>The new page code no longer carries the picture under the hero, and the focus keyword moved to the first picture's ALT. For each page below: open it with Elementor, click the HTML widget, select all, paste the new file, click <b>Update</b>. Keep "Hide Title" on.</p></li>
    <li><h3>Refresh Rank Math</h3><p><b>UpTrendPos &rarr; SEO Health</b> &rarr; tick all &rarr; <b>Fill Rank Math from page code</b>. Titles, descriptions and keywords have not changed, so this is only a refresh.</p></li>
  </ol>
</section>'''
    return f'''
<header class="top">
  <p class="eyebrow">uptrendpos.com · 20 October 2026</p>
  <h1>UpTrendPos Site Kit 1.2.1</h1>
  <p class="lead">Home keeps the dark blue hero. Every other page now has a light hero, like a service page. The orbit animation is new: a white UpTrendPos logo in the centre, six tools around it with flowing data lines, and one small card at a time that shows a shop problem and the fix. The picture under the hero is gone from every page. {"Open any page below to review it before you change the live site." if preview else ""}</p>
  <ul class="facts"><li><b>1</b> plugin update</li><li><b>16</b> pages (optional re-paste)</li><li><b>0</b> new pictures</li><li><b>0</b> SEO changes</li></ul>
</header>
<nav class="toc"><a href="#install">Update</a><a href="#pages">16 pages + SEO</a><a href="#auto">What runs on its own</a><a href="#future">Next new page</a><a href="#check">Please confirm</a></nav>
{steps}
<section class="blk" id="pages">
  <h2>The 16 pages, in WordPress list order</h2>
  <p class="sub">Clothing, Shoes, Cosmetics and Baby are skipped because their pages are not built yet. They stay hidden from the menu until they are published and set to index.</p>
  {page_rows(preview)}
</section>
<section class="blk" id="auto">
  <h2>What the plugin does on its own</h2>
  <ul class="ticks">
    <li><b>Menu, footer and links follow live pages.</b> A page counts as live when it is published and set to index. No list to edit any more.</li>
    <li><b>Schema on every page:</b> Organization with address, map and support hours; the app with its 3 plans; FAQ from the page; breadcrumbs; the Industries hub list; page picture; who reviewed the page and when.</li>
    <li><b>ALT text</b> for any picture that has none, and Fluent Forms inside the page code.</li>
    <li><b>Open Graph picture</b> from the page when no featured image is set.</li>
    <li><b>/llms.txt</b> for AI search, built from the live pages.</li>
    <li><b>301 redirects</b> for old links such as /tailor-shop-software/, /about-us/ and /downloads/ (only when they would show a 404).</li>
    <li><b>Faster pages:</b> Poppins is served from the site itself, no Google Fonts call; CSS and JS load once and are cached.</li>
    <li><b>Settings</b> (UpTrendPos &rarr; Settings): APK and Windows links, page reviewer, on/off switches for every part.</li>
  </ul>
</section>
<section class="blk" id="future">
  <h2>Next new page</h2>
  <ol class="mini"><li>Paste the page HTML into one Elementor HTML widget and publish.</li><li>UpTrendPos &rarr; SEO Health &rarr; tick it &rarr; Fill Rank Math from page code.</li><li>Purge the cache. It appears in the menu, footer, hub schema and llms.txt by itself.</li></ol>
</section>
<section class="blk" id="check">
  <h2>Please confirm</h2>
  <ul class="ticks warn">
    <li><b>Page reviewer (EEAT):</b> pages now say "checked by the UpTrendPos team". For stronger trust, add a real person in Settings, for example your name and title. Tell me if you want it.</li>
    <li><b>Customer logos:</b> 8 of 9 logos still have the generic ALT "UpTrendPos customer logo". Send which file is which shop and I will name them.</li>
    <li><b>Tracking:</b> every WhatsApp, call and email click now sends <code>utp_contact_click</code> to Google Tag Manager, also on buttons. Map it as the GA4 lead event.</li>
    <li><b>FBR items still open:</b> Simulated-mode QR marked "not an FBR invoice", offline FBR bills reporting on reconnect, and the PRAL route.</li>
  </ul>
</section>'''


CSS = '''
:root{--bg:#f6f8fc;--card:#ffffff;--ink:#10224A;--text:#3c4a63;--muted:#6b7890;--line:#e2e8f2;--accent:#024691;--ok:#1E8A43;--sun:#FAE814;--warn:#9a5b00;--code:#eef2f8;
 --f-d:'Poppins',ui-sans-serif,system-ui,sans-serif;--f-b:'Poppins',ui-sans-serif,system-ui,-apple-system,sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0b1428;--card:#111d38;--ink:#eef3fb;--text:#c3cde0;--muted:#8e9bb5;--line:#22314f;--accent:#8db8ff;--ok:#4fd28a;--sun:#FAE814;--warn:#f2c14e;--code:#1a2846;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#0b1428;--card:#111d38;--ink:#eef3fb;--text:#c3cde0;--muted:#8e9bb5;--line:#22314f;--accent:#8db8ff;--ok:#4fd28a;--sun:#FAE814;--warn:#f2c14e;--code:#1a2846;color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--text);font:400 15px/1.65 var(--f-b);margin:0}
.wrap{max-width:980px;margin:0 auto;padding-block:40px 80px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
h1,h2,h3{font-family:var(--f-d);color:var(--ink);letter-spacing:-.01em;text-wrap:balance;margin:0}
h1{font-size:clamp(30px,5vw,44px);line-height:1.1;font-weight:800}
h2{font-size:24px;font-weight:700;margin-bottom:14px}
h3{font-size:16.5px;font-weight:700}
code{font:500 12.5px/1.4 ui-monospace,SFMono-Regular,Menlo,monospace;background:var(--code);padding:2px 6px;border-radius:6px;color:var(--ink);overflow-wrap:anywhere}
.top{display:grid;gap:12px;padding-bottom:22px;border-bottom:1px solid var(--line)}
.eyebrow{margin:0;font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}
.lead{margin:0;font-size:16.5px;max-width:70ch}
.facts{list-style:none;margin:6px 0 0;padding:0;display:flex;flex-wrap:wrap;gap:10px}
.facts li{padding:8px 14px;border-radius:999px;background:var(--card);border:1px solid var(--line);font-size:13.5px}
.facts b{color:var(--ink);font-variant-numeric:tabular-nums}
.toc{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;display:flex;gap:6px;overflow-x:auto;padding:12px 0;background:var(--bg);border-bottom:1px solid var(--line)}
.toc a{white-space:nowrap;padding:7px 13px;border-radius:999px;color:var(--ink);text-decoration:none;font-size:13.5px;font-weight:600;border:1px solid var(--line);background:var(--card)}
.toc a:hover,.toc a:focus-visible{border-color:var(--accent);color:var(--accent);outline:none}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--bg)}
.blk{padding-top:36px}
.blk>.sub{margin:-6px 0 16px;color:var(--muted)}
.steps{list-style:none;counter-reset:s;margin:0;padding:0;display:grid;gap:12px}
.steps li{position:relative;padding:16px 18px 16px 62px;background:var(--card);border:1px solid var(--line);border-radius:16px;min-width:0}
.steps li::before{counter-increment:s;content:counter(s);position:absolute;left:18px;top:16px;width:30px;height:30px;border-radius:9px;display:grid;place-items:center;background:var(--ink);color:var(--bg);font:700 14px var(--f-d)}
.steps p{margin:6px 0 0}
.pg{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px 18px;margin-bottom:12px;min-width:0}
.pg header{display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.num{font:800 15px var(--f-d);color:var(--accent);font-variant-numeric:tabular-nums;width:30px}
.pgt{flex:1;min-width:200px}
.url{margin:2px 0 0;font-size:13px;color:var(--muted);overflow-wrap:anywhere}
.pv{padding:8px 14px;border-radius:999px;background:var(--sun);color:#10224A;font-weight:700;font-size:13.5px;text-decoration:none}
.pv:hover,.pv:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.note{margin:10px 0 0;padding:8px 12px;border-radius:10px;background:var(--code);font-size:13.5px}
dl{margin:12px 0 0;display:grid;gap:8px}
dl>div{display:grid;grid-template-columns:190px minmax(0,1fr);gap:10px;align-items:start;padding-top:8px;border-top:1px dashed var(--line)}
dt{font-size:12.5px;font-weight:600;color:var(--muted)}
.len{display:inline-block;margin-left:6px;padding:0 7px;border-radius:999px;background:var(--code);color:var(--ink);font-variant-numeric:tabular-nums}
dd{margin:0;display:flex;gap:10px;align-items:flex-start;justify-content:space-between;min-width:0}
dd span{color:var(--ink);overflow-wrap:anywhere}
.cp{flex:none;border:1px solid var(--line);background:var(--bg);color:var(--ink);border-radius:8px;padding:4px 10px;font:600 12px var(--f-b);cursor:pointer}
.cp:hover,.cp:focus-visible{border-color:var(--accent);outline:none}
.cp.ok{border-color:var(--ok);color:var(--ok)}
.ticks{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.ticks li{position:relative;padding-left:28px}
.ticks li::before{content:"";position:absolute;left:4px;top:7px;width:12px;height:7px;border:solid var(--ok);border-width:0 0 2.5px 2.5px;transform:rotate(-45deg)}
.ticks.warn li::before{border-color:var(--warn)}
.ticks b{color:var(--ink)}
.mini{margin:0;padding-left:20px;display:grid;gap:6px}
@media (max-width:640px){dl>div{grid-template-columns:1fr;gap:4px}.steps li{padding-left:56px}}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
'''
JS = '''
document.querySelectorAll('.cp').forEach(function(b){b.addEventListener('click',function(){var v=b.getAttribute('data-copy');var done=function(){b.textContent='Copied';b.classList.add('ok');setTimeout(function(){b.textContent='Copy';b.classList.remove('ok')},1400)};
try{navigator.clipboard.writeText(v).then(done,function(){sel(b)})}catch(e){sel(b)}})});
function sel(b){var s=b.previousElementSibling;var r=document.createRange();r.selectNodeContents(s);var w=window.getSelection();w.removeAllRanges();w.addRange(r)}
'''
FONT = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap">'

art = (f'<title>UpTrendPos Site Kit Review</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n{FONT}\n<style>{CSS}</style>\n'
       f'<div class="wrap">{body(True)}</div>\n<script>{JS}</script>\n')
pathlib.Path('/home/claude/preview_site/index.html').write_text(art)
std = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>UpTrendPos Site Kit 1.0 - Install Guide</title>{FONT}<style>{CSS}</style></head>'
       f'<body><div class="wrap">{body(False)}</div><script>{JS}</script></body></html>')
(OUT / 'INSTALL-GUIDE.html').write_text(std)
print('guide ok')
