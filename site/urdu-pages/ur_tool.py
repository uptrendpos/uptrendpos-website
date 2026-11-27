#!/usr/bin/env python3
"""UpTrendPos Urdu page tool (daily Urdu twin automation).

Commands
  next                                  print the next queued slug (status "queued") as JSON
  extract EN.html UNITS.json            write every translatable unit of the English page code
  stage EN.html                         print the 6 hero-stage items (English) this page uses
  apply EN.html UR_UNITS.json OUT.html [--stage STAGE_UR.json] [--date YYYY-MM-DD]
                                        build the Urdu page code from the English one
  check EN.html UR.html                 quality gates (structure, links, numbers, English left, SEO, rules)
  source RESULT.json OUT.html           save page code from a GET /utpk/v1/source?slug=..&pad=1 reply file (md5 checked)
  mark SLUG URL                         mark a queue entry published (today)

Units: each block of text (a <p>, <li>, <h2>, a button text ...) is ONE unit, with its inline tags
replaced by placeholders such as [[a1]]...[[/a1]], [[s1]] (an icon), [[br]]. Translate the text and keep
every placeholder exactly once, in the place that reads right in Urdu. Attributes (alt, aria-label,
title, placeholder, data-seo-*) are units too.
"""
import json, re, sys, os, html as H, datetime
from bs4 import BeautifulSoup, NavigableString, Tag, Comment

HERE = os.path.dirname(os.path.realpath(__file__))
QUEUE = os.path.join(HERE, 'queue.json')

INLINE = {'a', 'span', 'strong', 'em', 'b', 'i', 'small', 'bdi', 'time', 'br', 'code', 'sup', 'sub', 'mark', 'abbr', 'u', 's', 'img', 'svg', 'kbd', 'q', 'cite', 'del', 'ins'}
ATTRS = ('alt', 'aria-label', 'title', 'placeholder', 'data-seo-title', 'data-seo-desc', 'data-seo-kw')
SHORTCODE = re.compile(r'^\s*\[[a-z_]+[^\]]*\]\s*$')
MONTHS_UR = ['جنوری', 'فروری', 'مارچ', 'اپریل', 'مئی', 'جون', 'جولائی', 'اگست', 'ستمبر', 'اکتوبر', 'نومبر', 'دسمبر']
URDU = re.compile(r'[؀-ۿ]')
RUN = re.compile(r'(?<![A-Za-z0-9.@])(?:Rs\s)?[A-Za-z0-9][A-Za-z0-9.,+%:/@-]*(?:\s[A-Za-z0-9][A-Za-z0-9.,+%:/@-]*)*')
ALLOW = {'UpTrendPos', 'POS', 'FBR', 'QR', 'IMEI', 'CCTV', 'LED', 'USB', 'Type-C', 'NTN', 'STRN', 'API', 'PDF', 'CSV',
         'Excel', 'Rs', 'EV', 'EVs', 'ID', 'PIN', 'SMS', 'OTP', 'HTTPS', 'PECA', 'Tier-1', 'Tier', 'GPS', 'UPS', 'AC', 'DC', 'LCD',
         'Enterprise', 'Premium', 'Custom', 'Enterprise+', 'A4', 'mm', 'kg', 'KG', 'ft', 'IMEIs', 'HD', 'WiFi', 'Wi-Fi', 'SKU', 'GST', 'Mac', 'iPhone', 'iPad'}
FORBID = ['FBR approved', 'FBR-approved', 'certified', 'AGR', 'installation charge', 'setup charge', 'setup fee', 'installation fee',
          'free plan', 'iOS app', 'ElOERP', 'EloERP', 'customers trust us', 'منظور شدہ', 'سرٹیفائیڈ', 'انسٹالیشن چارج', 'سیٹ اپ چارج',
          'سیٹ اپ فیس', 'مفت پلان', 'آئی او ایس ایپ']
WA_UR = 'Assalam%20o%20Alaikum%2C%20mujhe%20UpTrendPos%20ke%20baray%20mein%20maloomat%20chahiye'


def soup_of(path):
    return BeautifulSoup(open(path, encoding='utf-8').read(), 'html.parser')


def root_of(soup):
    for el in soup.children:
        if isinstance(el, Tag):
            return el
    raise SystemExit('no root element')


def has_text(el):
    return any(isinstance(t, NavigableString) and not isinstance(t, Comment) and t.strip() and not SHORTCODE.match(t)
               for t in el.descendants if not (isinstance(t, NavigableString) and t.parent and t.parent.name in ('svg', 'script', 'style')))


def inline_only(el):
    for d in el.descendants:
        if isinstance(d, Tag) and d.name not in INLINE and not (d.find_parent('svg')):
            return False
    return True


def units_of(soup):
    """Deterministic list of (tag, kind) units in document order."""
    root = root_of(soup)
    out = []
    taken = set()
    for el in root.descendants:
        if not isinstance(el, Tag) or el.name in ('svg', 'script', 'style') or el.find_parent('svg'):
            continue
        if any(id(p) in taken for p in el.parents):
            continue
        if el.name in INLINE and el.parent is not None and el.parent is not root and inline_only(el.parent) and has_text(el.parent):
            continue  # its parent is the unit
        if has_text(el) and inline_only(el):
            out.append(el)
            taken.add(id(el))
    return out


def encode_unit(el):
    """Inner HTML with inline tags as placeholders. Returns (text, tags) where tags maps ph -> (open, close)."""
    tags = {}
    n = {'c': 0}

    def walk(node):
        s = ''
        for ch in node.children:
            if isinstance(ch, Comment):
                continue
            if isinstance(ch, NavigableString):
                s += str(ch)
            elif ch.name == 'br':
                s += '[[br]]'
            elif ch.name in ('svg', 'img'):
                n['c'] += 1
                k = 's%d' % n['c']
                tags[k] = (str(ch), '')
                s += '[[%s]]' % k
            else:
                n['c'] += 1
                k = '%s%d' % (ch.name[0], n['c'])
                attrs = ''.join(' %s="%s"' % (a, H.escape(' '.join(v) if isinstance(v, list) else v, quote=True)) for a, v in ch.attrs.items())
                tags[k] = ('<%s%s>' % (ch.name, attrs), '</%s>' % ch.name)
                s += '[[%s]]%s[[/%s]]' % (k, walk(ch), k)
        return s
    txt = re.sub(r'\s+', ' ', walk(el)).strip()
    return txt, tags


def decode_unit(txt, tags):
    out = txt.replace('[[br]]', '<br>')
    for k, (o, c) in tags.items():
        if c == '':
            out = out.replace('[[%s]]' % k, o)
        else:
            out = out.replace('[[%s]]' % k, o).replace('[[/%s]]' % k, c)
    return out


def attr_units(soup):
    root = root_of(soup)
    res = []
    for el in [root] + [d for d in root.descendants if isinstance(d, Tag)]:
        for a in ATTRS:
            v = el.get(a)
            if isinstance(v, str) and re.search(r'[A-Za-z]{3}', v):
                res.append((el, a))
    return res


def cmd_extract(en, out):
    soup = soup_of(en)
    data = {'units': [], 'attrs': []}
    for i, el in enumerate(units_of(soup)):
        txt, tags = encode_unit(el)
        if not re.search(r'[A-Za-z]{2}', H.unescape(re.sub(r'\[\[[^\]]+\]\]', '', txt))):
            continue  # numbers / symbols only: kept as is
        data['units'].append({'id': 'u%d' % i, 'tag': el.name, 'en': H.unescape(txt), 'ur': ''})
    for j, (el, a) in enumerate(attr_units(soup)):
        data['attrs'].append({'id': 'a%d' % j, 'attr': a, 'en': el.get(a), 'ur': ''})
    json.dump(data, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('units', len(data['units']), 'attrs', len(data['attrs']), '->', out)


def stage_items(path):
    soup = soup_of(path)
    st = soup.find(attrs={'data-stage': True})
    if not st:
        return None, None
    key = st['data-stage']
    if st.get('data-stage-items'):
        return key, json.loads(st['data-stage-items'])
    js = open(os.path.join(HERE, '..', '..', 'kit', 'uptrendpos-site-kit', 'assets', 'js', 'utp.js'), encoding='utf-8').read()
    m = re.search(r'\n\s+' + re.escape(key) + r': \[(.*?)\]\],?\n', js, re.S)
    if not m:
        return key, None
    arr = '[' + m.group(1) + ']]'
    arr = re.sub(r"'((?:[^'\\]|\\.)*)'", lambda x: json.dumps(x.group(1).replace("\\'", "'")), arr)
    return key, json.loads(arr)


def cmd_stage(en):
    key, items = stage_items(en)
    print(json.dumps({'stage': key, 'items': items}, ensure_ascii=False, indent=1))
    print('Translate fields 0, 3, 4 and 5 of each item; keep 1 (icon) and 2 (colour). Save as a JSON list of 6 lists.', file=sys.stderr)


def bidi(soup):
    """Wrap Latin/number runs that hold a digit or symbol in <bdi> inside Urdu text."""
    for t in list(soup.find_all(string=True)):
        if isinstance(t, Comment) or not t.strip() or not URDU.search(t) or t.find_parent(['bdi', 'svg', 'script', 'style']):
            continue
        parts, last, s = [], 0, str(t)
        for m in RUN.finditer(s):
            if re.search(r'[0-9+%-]', m.group(0)):
                parts.append(s[last:m.start()])
                parts.append(('B', m.group(0)))
                last = m.end()
        if not parts:
            continue
        parts.append(s[last:])
        new = []
        for p in parts:
            if isinstance(p, tuple):
                b = soup.new_tag('bdi')
                b.string = p[1]
                new.append(b)
            elif p:
                new.append(NavigableString(p))
        t.replace_with(*new)


def ur_date(d):
    return '%d %s %d' % (d.day, MONTHS_UR[d.month - 1], d.year)


def cmd_apply(en, urj, out, stage=None, date=None):
    soup = soup_of(en)
    data = json.load(open(urj, encoding='utf-8'))
    tr = {u['id']: u for u in data['units']}
    units = units_of(soup)
    miss = []
    for i, el in enumerate(units):
        u = tr.get('u%d' % i)
        if not u:
            continue
        txt, tags = encode_unit(el)
        if H.unescape(txt) != u['en']:
            raise SystemExit('unit u%d changed since extract (page code was edited?)' % i)
        ur = (u.get('ur') or '').strip()
        if not ur:
            miss.append(u['id'])
            continue
        want = sorted(re.findall(r'\[\[/?[a-z]+\d*\]\]', txt))
        got = sorted(re.findall(r'\[\[/?[a-z]+\d*\]\]', ur))
        if want != got:
            raise SystemExit('placeholders differ in %s: want %s got %s' % (u['id'], want, got))
        frag = BeautifulSoup(decode_unit(H.escape(ur, quote=False).replace('&lt;br&gt;', '<br>'), tags), 'html.parser')
        el.clear()
        for ch in list(frag.contents):
            el.append(ch)
    atr = {a['id']: a for a in data['attrs']}
    for j, (el, a) in enumerate(attr_units(soup)):
        x = atr.get('a%d' % j)
        if x and (x.get('ur') or '').strip():
            el[a] = x['ur'].strip()
        elif x:
            miss.append(x['id'])
    if miss:
        raise SystemExit('untranslated: ' + ', '.join(miss[:30]))
    for fr in soup.find_all(['iframe', 'script', 'style', 'form']):
        fr.decompose()  # the site refuses these in page code (contact map: the Get directions button stays)
    root = root_of(soup)
    cls = root.get('class', [])
    if 'utp-urdu' not in cls:
        root['class'] = cls + ['utp-urdu']
    if root.get('id') and not root['id'].endswith('-ur'):
        root['id'] = root['id'] + '-ur'
    root['lang'] = 'ur'
    root['dir'] = 'rtl'
    if stage:
        st = soup.find(attrs={'data-stage': True})
        items = json.load(open(stage, encoding='utf-8'))
        assert isinstance(items, list) and len(items) >= 4 and all(len(r) == 6 for r in items), 'stage items: 6 fields each'
        lri = lambda s: RUN.sub(lambda m: '⁦' + m.group(0) + '⁩' if re.search(r'[0-9+%-]', m.group(0)) else m.group(0), s)
        items = [[x if k in (1, 2) else lri(x) for k, x in enumerate(r)] for r in items]
        st['data-stage'] = re.sub(r'-ur$', '', st['data-stage']) + '-ur'
        st['data-stage-items'] = json.dumps(items, ensure_ascii=False)
    for a in soup.find_all('a', href=True):
        if 'wa.me/' in a['href'] and 'text=' in a['href']:
            a['href'] = re.sub(r'text=[^&"]*', 'text=' + WA_UR, a['href'])
    d = datetime.date.fromisoformat(date) if date else datetime.date.today()
    for t in soup.select('.utp-reviewed time, time[datetime]'):
        if t.find_parent(class_='utp-reviewed'):
            t['datetime'] = d.isoformat()
            t.string = ur_date(d)
    bidi(soup)
    html = str(soup)
    html = html.replace('<br/>', '<br>')
    open(out, 'w', encoding='utf-8').write(html)
    print('written', out, len(html))


def visible_text(soup, skip_bdi=False):
    root = root_of(soup)
    parts = []
    for t in root.find_all(string=True):
        if isinstance(t, Comment) or t.find_parent(['svg', 'script', 'style']):
            continue
        if skip_bdi and t.find_parent('bdi'):
            continue
        if SHORTCODE.match(t):
            continue
        parts.append(str(t))
    return ' '.join(parts)


def cmd_check(en, ur):
    e, u = soup_of(en), soup_of(ur)
    raw = open(ur, encoding='utf-8').read()
    errs, warns = [], []
    if len(raw) > 409600:
        errs.append('page code over 400 KB')
    if not re.match(r'^\s*<div class="utp[ "]', raw):
        errs.append('must start with <div class="utp')
    if re.search(r'<script|<style|<!--|<iframe|<form|<object|<embed|javascript:|\son[a-z]+\s*=', raw, re.I):
        errs.append('forbidden markup (script/style/comment/iframe/form/on*=) - the site refuses it')
    # 27 Nov 2026 (Abdul): every page image must be WebP; fix the English twin via /media first
    nonwebp = sorted(set(re.findall(r'<img[^>]+src="([^"]+\.(?:png|jpe?g|gif|bmp))"', raw, re.I)))
    if nonwebp:
        errs.append('non-WebP images (upload WebP with /media and swap src): ' + ', '.join(nonwebp))
    r = root_of(u)
    if 'utp-urdu' not in r.get('class', []) or r.get('lang') != 'ur' or r.get('dir') != 'rtl':
        errs.append('root needs class utp-urdu, lang="ur", dir="rtl"')
    t, dsc, kw = r.get('data-seo-title', ''), r.get('data-seo-desc', ''), r.get('data-seo-kw', '')
    if not URDU.search(t) or not (25 <= len(t) <= 70):
        errs.append('data-seo-title: Urdu, 25-70 characters (now %d)' % len(t))
    if not URDU.search(dsc) or not (100 <= len(dsc) <= 165):
        errs.append('data-seo-desc: Urdu, 100-165 characters (now %d)' % len(dsc))
    if not URDU.search(kw):
        errs.append('data-seo-kw: Urdu keywords needed')
    h1 = u.find_all('h1')
    if len(h1) != 1:
        errs.append('exactly one h1 (now %d)' % len(h1))
    for tag in ('h2', 'h3', 'section', 'details', 'a', 'img', 'li', 'table'):
        a, b = len(e.find_all(tag)), len(u.find_all(tag))
        if a != b:
            errs.append('<%s> count differs: English %d, Urdu %d' % (tag, a, b))
    norm = lambda h: re.sub(r'text=[^&]*', 'text=', h)
    he = sorted(norm(a['href']) for a in e.find_all('a', href=True))
    hu = sorted(norm(a['href']) for a in u.find_all('a', href=True))
    if he != hu:
        errs.append('links differ from the English page: %s' % sorted(set(he) ^ set(hu))[:6])
    ie = sorted(x['id'] for x in e.find_all(id=True) if x is not root_of(e))
    iu = sorted(x['id'] for x in u.find_all(id=True) if x is not r)
    if ie != iu:
        errs.append('element ids differ')
    if re.search(r'\[\[/?[a-z]+\d*\]\]', raw):
        errs.append('placeholder left in the page')
    # numbers: every number on the English page must be on the Urdu page
    num = lambda s: set(re.findall(r'\d[\d,]*(?:\.\d+)?', s))
    for t in e.select('.utp-reviewed time'):
        t.decompose()
    ne, nu = num(visible_text(e)), num(visible_text(u))
    lost = sorted(ne - nu)
    if lost:
        errs.append('numbers missing on the Urdu page: %s' % lost[:15])
    # English words left outside <bdi>
    vt = visible_text(u, skip_bdi=True)
    vt = re.sub(r'\b[\w.-]+@[\w.-]+\.\w+\b|\b[\w-]+(?:\.[\w-]+)+\.\w{2,}\b|https?://\S+', ' ', vt)
    words = [w for w in re.findall(r'[A-Za-z][A-Za-z+\-]*', vt) if w not in ALLOW and len(w) > 1]
    if words:
        (errs if len(words) > 6 else warns).append('English words left: %s' % sorted(set(words))[:25])
    ur_chars = len(URDU.findall(vt))
    lat = len(re.findall(r'[A-Za-z]', vt))
    if ur_chars < 0.85 * (ur_chars + lat):
        errs.append('page is not mostly Urdu (%d Urdu letters, %d Latin)' % (ur_chars, lat))
    for f in FORBID:
        if f.lower() in raw.lower():
            errs.append('forbidden phrase: %s' % f)
    for img in u.find_all('img'):
        if not URDU.search(img.get('alt', '')):
            warns.append('image alt not Urdu: %s' % img.get('src', '')[-50:])
    st = u.find(attrs={'data-stage': True})
    if st is not None and not (st.get('data-stage-items') and URDU.search(st['data-stage-items'])):
        errs.append('hero stage needs Urdu data-stage-items (use: stage EN.html, then apply --stage)')
    print(json.dumps({'ok': not errs, 'errors': errs, 'warnings': warns, 'urdu_letters': ur_chars, 'latin_letters': lat, 'bytes': len(raw)}, ensure_ascii=False, indent=1))
    sys.exit(0 if not errs else 1)


def cmd_source(res, out):
    """Write the page code from a saved GET /source?pad=1 reply (connector result file) and check its md5."""
    import hashlib
    t = open(res, encoding='utf-8').read()
    try:
        j = json.loads(t)
        if isinstance(j, list):
            j = json.loads(''.join(x.get('text', '') for x in j))
    except Exception:
        j = json.loads(t[t.index('{'):])
    d = j.get('data', j)
    html = d['html']
    if hashlib.md5(html.encode('utf-8')).hexdigest() != d['md5']:
        raise SystemExit('md5 mismatch - read the reply again')
    open(out, 'w', encoding='utf-8').write(html)
    print('saved', out, d['bytes'], 'bytes, md5 ok', d['md5'])


def cmd_next():
    q = json.load(open(QUEUE, encoding='utf-8'))
    for it in q:
        if it['status'] == 'queued':
            print(json.dumps(it, ensure_ascii=False))
            return
    print('{}')


def cmd_mark(slug, url):
    q = json.load(open(QUEUE, encoding='utf-8'))
    for it in q:
        if it['slug'] == slug:
            it['status'] = 'published'
            it['published'] = datetime.date.today().isoformat()
            it['url'] = url
    json.dump(q, open(QUEUE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('marked', slug)


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a:
        print(__doc__)
    elif a[0] == 'next':
        cmd_next()
    elif a[0] == 'extract':
        cmd_extract(a[1], a[2])
    elif a[0] == 'stage':
        cmd_stage(a[1])
    elif a[0] == 'apply':
        opt = {'stage': None, 'date': None}
        rest = a[4:]
        while rest:
            k = rest.pop(0)
            opt[k.lstrip('-')] = rest.pop(0)
        cmd_apply(a[1], a[2], a[3], **opt)
    elif a[0] == 'check':
        cmd_check(a[1], a[2])
    elif a[0] == 'source':
        cmd_source(a[1], a[2])
    elif a[0] == 'mark':
        cmd_mark(a[1], a[2])
    else:
        print(__doc__)
