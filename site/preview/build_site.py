"""Builds a click-through preview of the 16 pages with the REAL plugin header, footer, CSS and JS.
Output: /home/claude/preview_site (index.html + p/*.html + assets/)."""
import json, pathlib, re, shutil, subprocess, sys

sys.path.insert(0, '/home/claude/site')
from build_kit import P, OUT  # noqa: E402

KIT = pathlib.Path('/home/claude/kit/uptrendpos-site-kit')
IMG = pathlib.Path('/home/claude/site/hw/img')
SITE = pathlib.Path('/home/claude/preview_site')
LIVE = ['', 'about-uptrendpos', 'contact-us', 'download-pos-software', 'fbr-pos-integration', 'industries', 'mobile-shop-pos-software', 'electronics-store-pos-software',
        'grocery-store-pos-software', 'pharmacy-pos-software', 'solar-shop-pos-software', 'tailor-shop-pos-software', 'clothing-store-pos-software', 'cosmetics-store-pos-software', 'shoe-store-pos-software', 'vehicle-showroom-software', 'electrical-store-pos-software', 'baby-store-pos-software', 'pos-software-pricing', 'privacy-policy', 'support', 'terms-and-conditions']

if SITE.exists():
    shutil.rmtree(SITE)
(SITE / 'p').mkdir(parents=True)
A = SITE / 'assets'
(A / 'img').mkdir(parents=True)
shutil.copy(KIT / 'assets/css/utp.css', A / 'utp.css')
shutil.copy(KIT / 'assets/js/utp.js', A / 'utp.js')
shutil.copytree(KIT / 'assets/fonts', A / 'fonts')
for f in (KIT / 'assets/img').iterdir():
    shutil.copy(f, A / 'img' / f.name)
for f in IMG.glob('*.webp'):
    shutil.copy(f, A / 'img' / f.name)

url2file = {}
for i, p in enumerate(P, 1):
    url2file['https://uptrendpos.com' + p['url']] = f'{i:02d}-{p["n"]}.html'

PH = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='1200' height='900'%3E%3Crect width='100%25' height='100%25' fill='%23e9f0fb'/%3E"
      "%3Ctext x='50%25' y='50%25' font-family='sans-serif' font-size='36' fill='%2364748b' text-anchor='middle'%3EImage already on the live site%3C/text%3E%3C/svg%3E")
LOGO_PH = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='72'%3E%3Crect width='100%25' height='100%25' rx='8' fill='%23f1f5fb'/%3E"
           "%3Ctext x='50%25' y='56%25' font-family='sans-serif' font-size='14' fill='%2394a3b8' text-anchor='middle'%3ECustomer logo%3C/text%3E%3C/svg%3E")


def localize(h, depth='../'):
    def img(m):
        name = m.group(1)
        if (A / 'img' / name).exists():
            return f'src="{depth}assets/img/{name}"'
        return f'src="{LOGO_PH if re.match(r"(pos\d+|hamza)", name) else PH}"'
    h = re.sub(r'src="https://uptrendpos\.com/wp-content/uploads/([^"]+)"', img, h)
    h = re.sub(r'(src|href)="' + re.escape(str(KIT) + '/') + r'assets/img/', lambda m: f'{m.group(1)}="{depth}assets/img/', h)
    def link(m):
        u = m.group(1)
        base = u.split('#')[0]
        frag = u[len(base):]
        if base in url2file:
            return f'href="{url2file[base]}{frag}"'
        return m.group(0)
    return re.sub(r'href="(https://uptrendpos\.com/[^"]*)"', link, h)


fonts = ''.join(f"@font-face{{font-family:'Poppins';font-style:normal;font-weight:{w};font-display:swap;src:url(../assets/fonts/poppins-latin-{w}-normal.woff2) format('woff2')}}" for w in (400, 500, 600, 700, 800))
for i, p in enumerate(P, 1):
    fn = f'{i:02d}-{p["n"]}.html'
    src = OUT / '2-pages' / fn
    slug = p['url'].strip('/').split('/')[-1]
    r = subprocess.run(['php', str(pathlib.Path(__file__).with_name('render_parts.php')), str(KIT), slug, str(src), str(KIT), ','.join(LIVE)], capture_output=True, text=True)
    if r.returncode:
        print(r.stderr); sys.exit(1)
    d = json.loads(r.stdout)
    body = d['gated'].replace('[fluentform id="1"]', '<p>The Fluent Forms demo form shows here on the live site.</p>')
    doc = f'''<!doctype html>
<html lang="en-PK"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p["title"]}</title><meta name="description" content="{p["desc"]}">
<style>{fonts}body{{margin:0;background:#fff}}</style>
<link rel="stylesheet" href="../assets/utp.css"></head>
<body class="utp-site utp-has-nav{' utp-has-hero' if 'utp-hero' in body else ''}">
{d["sprite"]}
{d["header"]}
<main>
{body}
</main>
{d["footer"]}
<script>window.UTPK={json.dumps(d["cfg"])};</script>
<script src="../assets/utp.js" defer></script>
</body></html>'''
    (SITE / 'p' / fn).write_text(localize(doc))
    print('preview', fn)
