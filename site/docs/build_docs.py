"""Builds the UpTrendPos Product Guide: docs/index.html (artifact page) + docs/guide-print.html (for the PDF)."""
import base64, html, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from content import STATS, GAPS, STEPS, MODULES, PLANS, GLOSSARY  # noqa: E402

D = pathlib.Path(__file__).parent
IMG = pathlib.Path('/home/claude/kit/uptrendpos-site-kit/assets/img')
E = lambda s: html.escape(s, quote=True)
LOGO_W = 'data:image/webp;base64,' + base64.b64encode((IMG / 'logo-white.webp').read_bytes()).decode()
LOGO_C = 'data:image/webp;base64,' + base64.b64encode((IMG / 'logo-color.webp').read_bytes()).decode()

ICONS = {
    'pill': '<rect x="3" y="8.5" width="18" height="7" rx="3.5" transform="rotate(-45 12 12)"/><path d="M9.5 9.5l5 5"/>',
    'printer': '<path d="M6 9V3h12v6"/><rect x="3" y="9" width="18" height="8" rx="2"/><path d="M7 14h10v7H7z"/>',
    'wa': '<path d="M12 3.2a8.8 8.8 0 0 0-7.6 13.3L3.2 20.8l4.4-1.2A8.8 8.8 0 1 0 12 3.2z"/><path d="M9 8.6c.3 2.7 2.4 5.6 5.9 6.6l1.2-1.4-1.9-1-1 .8c-1.1-.5-2.1-1.5-2.6-2.6l.8-1-1-1.9z"/>',
    'offline': '<path d="M2 8.5a15 15 0 0 1 20 0M5.5 12a10 10 0 0 1 13 0M9 15.5a5 5 0 0 1 6 0"/><path d="M3 3l18 18"/>',
    'cal': '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    'shield': '<path d="M12 3l7.5 3v5.5c0 4.5-3.2 8.2-7.5 9.5-4.3-1.3-7.5-5-7.5-9.5V6z"/><path d="M8.8 12l2.2 2.2 4.2-4.4"/>',
    'users': '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17.5" cy="9" r="2.5"/><path d="M16 14.2a5 5 0 0 1 5.5 5.8"/>',
    'chart': '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    'qr': '<path d="M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h3v3h-3zM20 14v6h-3"/>',
    'scan': '<path d="M3 7V4h3M21 7V4h-3M3 17v3h3M21 17v3h-3M7 8v8M10 8v8M13 8v8M16 8v8"/>',
    'cart': '<path d="M3 4h2.2l2.3 11.2a1.5 1.5 0 0 0 1.5 1.2h8.6a1.5 1.5 0 0 0 1.5-1.1L21 8H6.2"/><circle cx="9.5" cy="20" r="1.3"/><circle cx="17" cy="20" r="1.3"/>',
    'bill': '<path d="M6 2h12v20l-3-2-3 2-3-2-3 2z"/><path d="M9 7h6M9 11h6M9 15h4"/>',
    'box': '<path d="M21 8l-9-5-9 5 9 5 9-5z"/><path d="M3 8v8l9 5 9-5V8M12 13v8"/>',
    'truck': '<path d="M3 6h11v10H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    'book': '<path d="M4 4h11a3 3 0 0 1 3 3v13H7a3 3 0 0 1-3-3z"/><path d="M8 8h6M8 12h6"/>',
    'wallet': '<rect x="3" y="6" width="18" height="14" rx="2.5"/><path d="M3 10h18M16 15h2"/><path d="M6 6l9-3 1.5 3"/>',
    'receipt': '<path d="M5 3h14v18l-2.3-1.5L14.3 21 12 19.5 9.7 21l-2.4-1.5L5 21z"/><path d="M9 8h6M9 12h6"/>',
    'trend': '<path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/>',
    'doc': '<path d="M6 2h9l5 5v15H6z"/><path d="M14 2v6h6M9 13h8M9 17h6"/>',
    'layers': '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
    'bell': '<path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z"/><path d="M10 20a2 2 0 0 0 4 0"/>',
    'gear': '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/>',
    'help': '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 0 1 4.8 1c0 1.7-2.3 2-2.3 3.5M12 17h.01"/>',
    'check': '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    'rocket': '<path d="M5 15c-1.5 1.5-2 4-2 6 2 0 4.5-.5 6-2"/><path d="M9 15l-3-3c1-4 4-8 12-9-1 8-5 11-9 12z"/><circle cx="14.5" cy="9.5" r="1.5"/>',
    'star': '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
    'spark': '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/>',
    'phone': '<path d="M5 4h3.5l1.7 4.3-2.2 1.4a11 11 0 0 0 6.3 6.3l1.4-2.2L20 15.5V19a1 1 0 0 1-1 1A16 16 0 0 1 4 5a1 1 0 0 1 1-1z"/>',
    'mail': '<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3.5 6.5l8.5 6.5 8.5-6.5"/>',
    'pin': '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.5 3.8 5.6 3.8 9s-1.3 6.5-3.8 9c-2.5-2.5-3.8-5.6-3.8-9S9.5 5.5 12 3z"/>',
    'book2': '<path d="M4 5a2 2 0 0 1 2-2h14v16H6a2 2 0 0 0-2 2z"/><path d="M4 19V5M8 7h8"/>',
}


def ic(k, s=20):
    return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[k]}</svg>'


NAV = [('why', 'What makes it different', 'spark'), ('start', 'Getting started', 'rocket')] + [(m[0], m[3], m[1]) for m in MODULES] + [('plans', 'Plans at a glance', 'star'), ('words', 'Words used in the app', 'book2'), ('contact', 'Contact us', 'phone')]
GROUPS = [('Start', ['why', 'start']), ('Selling', ['sale', 'sales', 'customers', 'quotes']), ('Stock and buying', ['inventory', 'procurement', 'vertical']),
          ('People', ['hrm', 'notify']), ('Money', ['accounts', 'cash', 'expenses', 'income', 'compliance']), ('Setup', ['settings', 'support', 'plans', 'words', 'contact'])]


def nav_html():
    title = {n[0]: (n[1], n[2]) for n in NAV}
    out = ['<nav class="side" aria-label="Guide sections"><a class="side-logo" href="#top"><img src="' + LOGO_C + '" width="600" height="120" alt="UpTrendPos"></a>']
    for g, ids in GROUPS:
        out.append(f'<p class="side-h">{g}</p><ul>')
        for i in ids:
            t, k = title[i]
            out.append(f'<li><a href="#{i}">{ic(k, 16)}<span>{E(t)}</span></a></li>')
        out.append('</ul>')
    out.append('</nav>')
    return ''.join(out)


def cover():
    stats = ''.join(f'<li><b>{E(a)}</b><span>{E(b)}</span></li>' for a, b in STATS)
    return f'''<header class="cover" id="top">
  <div class="cover-in">
    <img class="cover-logo" src="{LOGO_W}" width="600" height="120" alt="UpTrendPos">
    <p class="kicker">Product guide · October 2026</p>
    <h1>Everything your shop can do with <span>UpTrendPos</span></h1>
    <p class="lead">POS, stock, udhaar, installments, staff and full accounts for Pakistani shops. Works on Windows, Android and the web, even when the internet is off. This guide explains every part of the app in simple words.</p>
    <ul class="chips"><li>{ic('globe', 15)}Windows · Android · Web</li><li>{ic('offline', 15)}Works offline</li><li>{ic('qr', 15)}FBR ready</li><li>{ic('wa', 15)}WhatsApp invoices</li></ul>
    <ul class="stats">{stats}</ul>
  </div>
  <div class="orbit" aria-hidden="true"><i class="o1"></i><i class="o2"></i><i class="o3"></i><span class="core">POS</span></div>
</header>'''


def why():
    cards = ''.join(f'''<article class="gap c-{c}"><p class="gap-q">{E(q)}</p><div class="gap-a"><span class="ib">{ic(k)}</span><div><h3>{E(t)}</h3><p>{E(d)}</p></div></div></article>''' for k, c, q, t, d in GAPS)
    return f'''<section class="sec" id="why"><p class="eyebrow">Why shops switch</p><h2>What makes UpTrendPos different</h2>
<p class="intro">These are the everyday problems of Pakistani shops that most billing apps leave open. Each card shows the problem and how UpTrendPos solves it.</p>
<div class="gaps">{cards}</div></section>'''


def start():
    steps = ''.join(f'<li><span class="n">{i}</span><div><h3>{E(t)}</h3><p>{E(d)}</p></div></li>' for i, (t, d) in enumerate(STEPS, 1))
    return f'''<section class="sec" id="start"><p class="eyebrow">Day one</p><h2>Getting started in 9 steps</h2>
<p class="intro">The app shows this checklist when you first log in. Most shops finish it and make their first sale on the same day. If your business type has a ready catalog, steps 5 to 7 are mostly done for you.</p>
<ol class="steps">{steps}</ol></section>'''


def module(m):
    mid, k, c, title, intro, groups, why_ = m
    cols = ''
    for gt, items in groups:
        lis = ''.join(f'<li>{E(x)}</li>' for x in items)
        cols += f'<div class="grp"><h3>{E(gt)}</h3><ul class="ticks">{lis}</ul></div>'
    many = ' wide' if sum(len(i) for _, i in groups) > 18 else ''
    return f'''<section class="sec mod c-{c}" id="{mid}">
  <div class="mod-head"><span class="mod-ic">{ic(k, 26)}</span><div><h2>{E(title)}</h2><p class="intro">{E(intro)}</p></div></div>
  <div class="grps{many}">{cols}</div>
  <p class="why">{ic('star', 16)}<span><b>Why it matters:</b> {E(why_)}</span></p>
</section>'''


def plans():
    cards = ''
    for n, f, items in PLANS:
        rec = ' rec' if n == 'Enterprise' else ''
        lis = ''.join(f'<li>{E(x)}</li>' for x in items)
        cards += f'<article class="plan{rec}">{"<span class=badge>Most shops pick this</span>" if rec else ""}<h3>{n}</h3><p class="for">{E(f)}</p><ul class="ticks">{lis}</ul></article>'
    return f'''<section class="sec" id="plans"><p class="eyebrow">Plans</p><h2>Plans at a glance</h2>
<p class="intro">Every plan has unlimited invoices, works offline and runs on Windows, Android and the web. Tools for your business type come with every plan. Prices are on the pricing page of uptrendpos.com, and every new shop gets a 14-day free trial.</p>
<div class="plans">{cards}</div></section>'''


def words():
    rows = ''.join(f'<div><dt>{E(a)}</dt><dd>{E(b)}</dd></div>' for a, b in GLOSSARY)
    return f'<section class="sec" id="words"><p class="eyebrow">Glossary</p><h2>Words used in the app</h2><dl class="gloss">{rows}</dl></section>'


def contact():
    return f'''<section class="contact" id="contact"><div>
<p class="eyebrow light">Talk to us</p><h2>Questions, a demo or setup help?</h2>
<p>The same team that builds UpTrendPos helps you, in Urdu or English, Monday to Saturday, 10 am to 7 pm.</p>
<ul class="cl"><li>{ic('phone', 18)}<span>Call or WhatsApp <b>0319 2223292</b></span></li><li>{ic('mail', 18)}<span><b>sales@uptrendpos.com</b></span></li>
<li>{ic('globe', 18)}<span><b>uptrendpos.com</b> · web app <b>live.uptrendpos.com</b></span></li><li>{ic('pin', 18)}<span>House No 193/A, Umer Block, Shadab Town, Sahiwal 57000, Pakistan</span></li></ul>
</div><img src="{LOGO_W}" width="600" height="120" alt="UpTrendPos"></section>'''


CSS = (D / 'docs.css').read_text()


def page(for_print=False):
    main = cover() + '<div class="layout">' + ('' if for_print else nav_html()) + '<main class="main">' + why() + start() + ''.join(module(m) for m in MODULES) + plans() + words() + contact() + '<p class="foot">© 2026 UpTrendPos · Made in Sahiwal, Pakistan · Features shown here follow the app as of October 2026. Some tools depend on your plan and business type.</p></main></div>'
    head = ('<title>UpTrendPos Product Guide</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap">\n')
    if for_print:
        return f'<!doctype html><html lang="en"><head><meta charset="utf-8">{head}<style>{CSS}</style></head><body class="print">{main}</body></html>'
    return f'{head}<style>{CSS}</style>\n{main}\n'


(D / 'index.html').write_text(page())
(D / 'guide-print.html').write_text(page(True))
print('docs ok', len(page()) // 1024, 'KB')
