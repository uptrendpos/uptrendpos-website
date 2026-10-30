"""UpTrendPos daily page automation helper.

  python3 automation/daily.py next            -> the next queued business type(s), config.json per_run (default 1) (JSON) with their facts
  python3 automation/daily.py build A B       -> build pages A and B, run every quality gate, export to the assets repo
  python3 automation/daily.py mark A B        -> mark A and B published in queue.json (after the site confirms)

Pages are registered for the build in site/pages.json (one entry per new page, same fields as build_kit.P plus
"builder": "build_<x>.py" and "images": "hw/gen_<x>.py"). See automation/DAILY_RUNBOOK.md.
"""
import datetime, html, json, pathlib, re, shutil, subprocess, sys

SITE = pathlib.Path(__file__).resolve().parents[1]
AUTO = SITE / 'automation'
CFG = json.loads((AUTO / 'config.json').read_text())
QUEUE = AUTO / 'queue.json'
OUT = pathlib.Path(CFG.get('kit_out', '/home/claude/out/kit'))
ASSETS = pathlib.Path(CFG['assets_dir'])
RAW = f"https://raw.githubusercontent.com/{CFG['asset_repo']}/{CFG.get('branch', 'main')}/"
REG = json.loads((SITE.parent / 'kit/uptrendpos-site-kit/data/industries.json').read_text())

BANNED = [r'installation (fee|charge|cost)', r'setup fee', r'\bAGR\b', r'AGR ?Soft', r'elo ?erp', r'sada ?hisab', r'free plan', r'free forever',
          r'\bcertified\b', r'FBR[- ]approved', r'approved by FBR', r'licensed integrator', r'unlimited offline', r"pakistan'?s (first|1st|no\.? ?1)",
          r'\bno\.? ?1 POS\b', r'\bbest in pakistan\b', r'100\+ (shops|merchants|startups)', r'iOS app', r'App Store']


def text(s):
    s = re.sub(r'<svg.*?</svg>', '', s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


def cmd_next():
    q = json.loads(QUEUE.read_text())
    todo = [x for x in q if x['status'] == 'queued'][:int(CFG.get('per_run', 1))]
    print(json.dumps(todo, indent=1))


def gates(p, page_html):
    errs = []
    t = text(page_html)
    words = len(t.split())
    kw = p['kw']
    n = len(re.findall(r'(?<![\w-])' + re.escape(kw) + r'(?![\w-])', t, re.I))
    dens = 100 * n / max(words, 1)
    if words < 2200:
        errs.append(f'only {words} words (need 2200+)')
    if not 0.75 <= dens <= 1.05:
        errs.append(f'keyword density {dens:.2f}% (need 0.75-1.05)')
    if page_html.count('<summary>') < 10:
        errs.append('fewer than 10 FAQs')
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', page_html, re.S)
    if not h1 or kw.lower() not in text(h1.group(1)).lower():
        errs.append('focus keyword not in H1')
    if len(p['title']) > 60 or kw.lower() not in p['title'].lower():
        errs.append('SEO title over 60 or missing keyword')
    if not 120 <= len(p['desc']) <= 160 or kw.lower() not in p['desc'].lower():
        errs.append('meta description length/keyword')
    for b in BANNED:
        if re.search(b, t, re.I) or re.search(b, p['title'] + ' ' + p['desc'], re.I):
            errs.append(f'banned claim: {b}')
    if p['n'] not in [x['slug'] for x in REG['types']]:
        errs.append('slug not in data/industries.json')
    if 'data-stage-items=' not in page_html and 'data-stage="' not in page_html:
        errs.append('hero stage missing')
    imgs = re.findall(r'<img[^>]+src="https://uptrendpos\.com/wp-content/uploads/(uptrendpos-[a-z0-9-]+\.webp)"', page_html)
    for f in imgs:
        if not (SITE / 'hw/img' / f).exists():
            errs.append(f'image not generated: {f}')
    if len(imgs) < 4:
        errs.append('fewer than 4 page images')
    for f in set(imgs):
        if not re.fullmatch(r'uptrendpos-[a-z0-9]+(-[a-z0-9]+)*\.webp', f) or re.search(r'-\d{1,2}\.webp$', f):
            errs.append(f'bad image name {f}')
    return errs, dict(words=words, kw=n, density=round(dens, 2), faqs=page_html.count('<summary>'), images=sorted(set(imgs)))


def cmd_build(slugs):
    pages = {p['n']: p for p in json.loads((SITE / 'pages.json').read_text())}
    for s in slugs:
        p = pages[s]
        subprocess.run([sys.executable, p['builder']], cwd=SITE, check=True)
        subprocess.run([sys.executable, p['images']], cwd=SITE / 'hw', check=True)
    if OUT.exists():
        shutil.rmtree(OUT)
    subprocess.run([sys.executable, 'build_kit.py', str(OUT)], cwd=SITE, check=True, stdout=subprocess.DEVNULL)
    plan, failed = {'date': datetime.date.today().isoformat(), 'media': [], 'pages': [], 'report': {}}, {}
    (ASSETS / 'pages').mkdir(parents=True, exist_ok=True)
    (ASSETS / 'img').mkdir(parents=True, exist_ok=True)
    for s in slugs:
        f = next((OUT / '2-pages').glob(f'*-{s}.html'))
        page_html = f.read_text()
        errs, stats = gates(pages[s], page_html)
        plan['report'][s] = dict(stats, errors=errs)
        if errs:
            failed[s] = errs
            continue
        (ASSETS / 'pages' / f'{s}.html').write_text(page_html)
        for img in stats['images']:
            shutil.copy(SITE / 'hw/img' / img, ASSETS / 'img' / img)
            alt = re.search(r'src="[^"]*/' + re.escape(img) + r'"[^>]*\salt="([^"]*)"', page_html)
            plan['media'].append({'name': img, 'url': RAW + 'img/' + img, 'alt': html.unescape(alt.group(1)) if alt else ''})
        plan['pages'].append({'slug': s, 'html_url': RAW + f'pages/{s}.html', 'publish': True})
    (AUTO / 'out').mkdir(exist_ok=True)
    (AUTO / 'out/plan.json').write_text(json.dumps(plan, indent=1))
    print(json.dumps(plan, indent=1))
    if failed:
        print('GATES FAILED:', json.dumps(failed, indent=1), file=sys.stderr)
        sys.exit(2)


def cmd_mark(slugs):
    q = json.loads(QUEUE.read_text())
    for x in q:
        if x['slug'] in slugs:
            x['status'] = 'published'
            x['published'] = datetime.date.today().isoformat()
    QUEUE.write_text(json.dumps(q, indent=1))


if __name__ == '__main__':
    c = sys.argv[1] if len(sys.argv) > 1 else 'next'
    {'next': lambda: cmd_next(), 'build': lambda: cmd_build(sys.argv[2:]), 'mark': lambda: cmd_mark(sys.argv[2:])}[c]()
