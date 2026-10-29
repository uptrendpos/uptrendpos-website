"""Industry page renderer (template v3 = Grocery v2 / Pharmacy v1 structure). Content lives in build_<trade>.py."""
import contextlib, io, pathlib, re
with contextlib.redirect_stdout(io.StringIO()):
    from build_fbr import ico, ICON, ul, head, wa, UP
P = pathlib.Path('/home/claude/site/pages')
ICON.update({
    'search': '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.5-4.5"/>',
    'clock': '<circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.5 2.5M9 2h6"/>',
    'truck': '<path d="M3 6h11v10H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    'book': '<path d="M4 4h11a3 3 0 0 1 3 3v13H7a3 3 0 0 1-3-3z"/><path d="M8 8h6M8 12h6"/>',
    'chart': '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    'bill': '<path d="M6 2h12v20l-3-2-3 2-3-2-3 2z"/><path d="M9 7h6M9 11h6M9 15h4"/>',
    'store': '<path d="M3 9l2-5h14l2 5"/><path d="M3 9h18v11H3zM9 20v-6h6v6"/>',
    'printer': '<path d="M6 9V3h12v6"/><rect x="3" y="9" width="18" height="8" rx="2"/><path d="M7 14h10v7H7z"/>',
    'pc': '<rect x="2" y="4" width="20" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>',
    'scan': '<path d="M3 7V4h3M21 7V4h-3M3 17v3h3M21 17v3h-3M7 8v8M10 8v8M13 8v8M16 8v8"/>',
    'tag': '<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8.5" r="1.5"/>',
    'scissors': '<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M8.1 8.1L20 20M8.1 15.9L20 4"/>',
    'ruler': '<path d="M3 17L17 3l4 4L7 21z"/><path d="M7 13l2 2M10 10l2 2M13 7l2 2"/>',
    'users': '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17.5" cy="9" r="2.5"/><path d="M16 14.2a5 5 0 0 1 5.5 5.8"/>',
    'shirt': '<path d="M8 3l4 3 4-3 5 4-3 4-2-1v11H8V10l-2 1-3-4z"/>',
    'cash': '<rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18M7 15h3"/>',
    'cal': '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    'chip': '<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>',
    'laptop': '<rect x="4" y="5" width="16" height="11" rx="1.5"/><path d="M2 19h20"/>',
    'headset': '<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="3" y="14" width="4" height="6" rx="1.5"/><rect x="17" y="14" width="4" height="6" rx="1.5"/>',
    'sun': '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
    'battery': '<rect x="2" y="7" width="17" height="10" rx="2"/><path d="M22 11v2M6 10v4M10 10v4"/>',
    'bolt': '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
    'tv': '<rect x="2" y="5" width="20" height="13" rx="2"/><path d="M8 21h8M12 18v3"/>',
    'cam': '<path d="M3 8h13l5-3v12l-5-3H3z"/><circle cx="9" cy="11" r="2.5"/>',
    'snow': '<path d="M12 2v20M4 6l16 12M20 6L4 18"/>',
    'doc': '<path d="M6 2h9l5 5v15H6z"/><path d="M14 2v6h6M9 13h8M9 17h6"/>',
    'star': '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
    'layers': '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
    'sync': '<path d="M19.5 8A8 8 0 0 0 5 7.5M4.5 16a8 8 0 0 0 14.5.5"/><path d="M19.5 3.5V8H15M4.5 20.5V16H9"/>',
    'spark': '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/>',
    'drop': '<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/>',
    'heart': '<path d="M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0 1 12 7.4 4.3 4.3 0 0 1 19.5 10c0 5.4-7.5 10-7.5 10z"/>',
})
TICK = ('<span class="utp-tk-ic"><svg width="14" height="14" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2.6" '
        'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 10.5l3.2 3.2L15 6.8"/></svg></span>')
WA_ICON = ('<svg width="20" height="20" viewBox="0 0 24 24" fill="#25D366" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 '
           '18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2z"/></svg>')


def plan(txt):
    return f' <em class="utp-ptag">{txt}</em>'


def soon():
    return ' <em class="utp-ptag soon">Coming soon</em>'


def section(sid, hid, inner, extra=''):
    idattr = f' id="{sid}"' if sid else ''
    return f'  <section class="utp-sec{extra}"{idattr} aria-labelledby="{hid}">\n    <div class="utp-wrap">\n{inner}    </div>\n  </section>\n\n'


def big_ico(n, c):
    return ico(n, c).replace('utp-ico sm', 'utp-ico')


def alt_pass(h):
    n = [0]

    def f(m):
        cls = m.group(1).replace(' utp-alt', '')
        n[0] += 1
        return '<section class="utp-sec' + cls + (' utp-alt' if n[0] % 2 else '') + '"'
    return re.sub(r'<section class="utp-sec([^"]*)"', f, h)


def split_section(sid, hid, eyebrow, h2, p, img, alt, h3, para, items, rev=False):
    fig = (f'        <figure class="utp-figure utp-figure-img">\n          <img src="{UP}{img}" width="1200" height="900" loading="lazy" decoding="async" alt="{alt}">\n        </figure>\n')
    txt = f'        <div class="utp-usp-copy">\n          <h3>{h3}</h3>\n          <p>{para}</p>\n          {ul(items, "utp-feat")}\n        </div>\n'
    return section(sid, hid, head(eyebrow, hid, h2, p) + '      <div class="utp-usp-row' + (' rev' if rev else '') + '">\n' + fig + txt + '      </div>\n')


def groups_section(sid, hid, eyebrow, h2, p, groups, note=''):
    return section(sid, hid, head(eyebrow, hid, h2, p) + '      <div class="utp-fgroups">\n'
                   + ''.join(f'        <article class="utp-fgroup">\n          <div class="utp-fgroup-head">{ico(i, cl)}<h3>{h}</h3></div>\n          {ul(l)}\n        </article>\n' for i, cl, h, l in groups)
                   + '      </div>\n' + (f'      <p class="utp-note">{note}</p>\n' if note else ''))


def render(c):
    k = c['key']
    hero = f'''  <section class="utp-hero" aria-labelledby="utp-h1">
    <div class="utp-wrap utp-hero-grid">
      <div class="utp-hero-copy">
        <nav class="utp-crumb" aria-label="Breadcrumb">
          <ol>
            <li><a href="https://uptrendpos.com/">Home</a></li>
            <li><a href="https://uptrendpos.com/industries/" data-page="industries">Industries</a></li>
            <li><span aria-current="page">{c['crumb']}</span></li>
          </ol>
        </nav>
        <p class="utp-kicker">{c['kicker']}</p>
        <h1 id="utp-h1">{c['h1']}</h1>
        <p class="utp-lead">{c['lead']}</p>
        <div class="utp-cta">
          <a class="utp-btn utp-btn-primary" href="https://live.uptrendpos.com/" target="_blank" rel="noopener" data-track="{k}_hero_trial">Start 14-day free trial</a>
          <a class="utp-btn utp-btn-ghost" href="{wa(c['wa_demo'])}" target="_blank" rel="noopener" data-track="{k}_hero_whatsapp">{WA_ICON} {c['demo_btn']}</a>
        </div>
        <p class="utp-smart-note">{c['smart_note']}</p>
        <ul class="utp-ticks">
''' + ''.join(f'          <li>{x}</li>\n' for x in c['ticks']) + f'''        </ul>
      </div>
      <figure class="utp-hero-img">
        <img src="{UP}{c['hero_img'][0]}" width="1200" height="900" fetchpriority="high" decoding="async" alt="{c['hero_img'][1]}">
      </figure>
    </div>
  </section>

  <div class="utp-ticker" aria-label="{c['ticker_label']}">
    <div class="utp-marquee">
      <ul class="utp-mq-track">
''' + ''.join(f'        <li>{TICK}{x}</li>\n' for x in c['ticker']) + '''      </ul>
    </div>
  </div>

  <nav class="utp-jump" aria-label="On this page">
    <div class="utp-wrap">
      <ul>
''' + ''.join(f'        <li><a href="#{a}">{b}</a></li>\n' for a, b in c['jump']) + '''      </ul>
    </div>
  </nav>

'''
    ph = c['problems']
    problems = section('utp-problems', 'utp-pain-title', head('The problems', 'utp-pain-title', ph[0], ph[1]) + '      <ul class="utp-pain c3">\n'
                       + ''.join(f'        <li>\n          <span class="utp-tag">The problem</span>\n          <h3>{h}</h3>\n          <p>{p}</p>\n          <p class="utp-fix">{f}</p>\n        </li>\n' for h, p, f in ph[2])
                       + '      </ul>\n')
    u = c['usp']
    rows = ''
    for i, (img, alt, h3, p, items) in enumerate(u['rows']):
        rows += (f'      <div class="utp-usp-row{" rev" if i % 2 else ""}">\n        <figure class="utp-figure utp-figure-img">\n'
                 f'          <img src="{UP}{img}" width="1200" height="900" loading="lazy" decoding="async" alt="{alt}">\n        </figure>\n'
                 f'        <div class="utp-usp-copy">\n          <span class="utp-num">{i+1}</span>\n          <h3>{h3}</h3>\n          <p>{p}</p>\n          {ul(items, "utp-feat")}\n        </div>\n      </div>\n\n')
    usp = (f'  <section class="utp-sec utp-usp" id="{u["id"]}" aria-labelledby="utp-usp-title">\n    <div class="utp-wrap">\n'
           + head(u['eyebrow'], 'utp-usp-title', u['h2'], u['p']) + '\n' + rows.rstrip('\n') + '\n    </div>\n  </section>\n\n')
    cp = c['caps']
    caps = section('', 'utp-cap-title', head('With UpTrendPos', 'utp-cap-title', cp[0], cp[1]) + '      <div class="utp-fgrid">\n'
                   + ''.join(f'        <article class="utp-fcard">\n          {ico(i, cl)}\n          <h3>{h}</h3>\n          {ul(l, "utp-feat sm")}\n        </article>\n' for i, cl, h, l in cp[2])
                   + '      </div>\n')
    fg = c['features']
    feats = section('utp-features', 'utp-feat-title', head('Features', 'utp-feat-title', fg[0], fg[1]) + '      <div class="utp-fgroups">\n'
                    + ''.join(f'        <article class="utp-fgroup">\n          <div class="utp-fgroup-head">{ico(i, cl)}<h3>{h}</h3></div>\n          {ul(l)}\n        </article>\n' for i, cl, h, l in fg[2])
                    + f'      </div>\n      <p class="utp-note">{fg[3]}</p>\n')
    hw = c['hardware']
    hwsec = section('utp-hardware', 'utp-hw-title', head('Hardware', 'utp-hw-title', hw[0], hw[1])
                    + f'      <div class="utp-split utp-hw-split">\n        <figure class="utp-figure utp-figure-img">\n          <img src="{UP}{hw[2][0]}" width="1200" height="900" loading="lazy" decoding="async" alt="{hw[2][1]}">\n        </figure>\n        <ul class="utp-hwlist">\n'
                    + ''.join(f'          <li>{ico(i, cl)}<div><h3>{h}</h3><p>{p}</p></div></li>\n' for i, cl, h, p in hw[3])
                    + f'        </ul>\n      </div>\n      <p class="utp-note">Already have a printer or scanner? <a class="utp-link" href="{wa(hw[4])}" target="_blank" rel="noopener" data-track="{k}_hw_check">Send us the model on WhatsApp</a> and we will check it.</p>\n')
    st = c['setups']
    cards = ''
    for i, (icn, cl, h, best, items) in enumerate(st[2]):
        rec = i == 1
        cards += (f'        <article class="utp-card{" is-rec" if rec else ""}">\n' + ('          <span class="utp-rec">Easy first step</span>\n' if rec else '')
                  + f'          {big_ico(icn, cl)}\n          <h3>{h}</h3>\n          <p class="utp-best">{best}</p>\n          {ul(items, "utp-feat")}\n        </article>\n')
    setups = section('utp-setup', 'utp-setup-title', head('Your setup', 'utp-setup-title', st[0], st[1]) + '      <div class="utp-cards">\n' + cards + '      </div>\n')
    pr = c['process']
    proc = section('utp-process', 'utp-proc-title', head('How it works', 'utp-proc-title', pr[0], pr[1])
                   + f'      <div class="utp-proc">\n        <figure class="utp-figure utp-figure-img">\n          <img src="{UP}{pr[2][0]}" width="1200" height="900" loading="lazy" decoding="async" alt="{pr[2][1]}">\n        </figure>\n        <ol class="utp-rep">\n'
                   + ''.join(f'          <li><strong>{h}</strong><span>{p}</span></li>\n' for h, p in pr[3]) + '        </ol>\n      </div>\n')
    of = c['offline']
    offline = section('', 'utp-off-title', head('Load-shedding ready', 'utp-off-title', of[0], of[1]) + '      <div class="utp-sync-row">\n'
                      + f'        <div class="utp-node"><strong>{of[2][0][0]}</strong><span>{of[2][0][1]}</span></div>\n        <span class="utp-arrow" aria-hidden="true"></span>\n'
                      + f'        <div class="utp-node cloud"><strong>{of[2][1][0]}</strong><span>{of[2][1][1]}</span></div>\n        <span class="utp-arrow" aria-hidden="true"></span>\n'
                      + f'        <div class="utp-node"><strong>{of[2][2][0]}</strong><span>{of[2][2][1]}</span></div>\n      </div>\n      <p class="utp-sync-note">{of[3]}</p>\n')
    bn = c['benefits']
    bens = section('', 'utp-ben-title', head('Benefits', 'utp-ben-title', bn[0], bn[1]) + '      <ol class="utp-rep c2">\n'
                   + ''.join(f'        <li><strong>{h}</strong><span>{p}</span></li>\n' for h, p in bn[2]) + '      </ol>\n')
    rp = c['reports']
    reps = section('utp-reports', 'utp-rep-title', head('Reports', 'utp-rep-title', rp[0], rp[1]) + '      <ol class="utp-rep c2">\n'
                   + ''.join(f'        <li><strong>{h}</strong><span>{p}</span></li>\n' for h, p in rp[2])
                   + '      </ol>\n      <p class="utp-more-h">More reports in the app</p>\n      <ul class="utp-mini-chips">\n'
                   + ''.join(f'        <li>{x}</li>\n' for x in rp[3]) + '      </ul>\n')
    du = c['duo']
    duo = section('', 'utp-safe-title', head(du[0], 'utp-safe-title', du[1], du[2]) + '      <div class="utp-duo">\n'
                  + f'        <article class="utp-fgroup">\n          <div class="utp-fgroup-head">{ico("shield", "g")}<h3>{du[3][0]}</h3></div>\n          {ul(du[3][1])}\n'
                  + (f'          <p class="utp-fgroup-foot utp-light">{du[3][2]}</p>\n' if du[3][2] else '') + '        </article>\n'
                  + f'        <article class="utp-fgroup utp-fgroup-dark">\n          <div class="utp-fgroup-head">{ico(du[4][3], "y")}<h3>{du[4][0]}</h3></div>\n          {ul(du[4][1])}\n'
                  + f'          <p class="utp-fgroup-foot">{du[4][2]}</p>\n        </article>\n      </div>\n')
    sg = c['segments']
    segs = section('', 'utp-seg-title', head('Every shop', 'utp-seg-title', sg[0], sg[1]) + '      <div class="utp-fgrid">\n'
                   + ''.join(f'        <article class="utp-fcard">\n          {ico(i, cl)}\n          <h3>{h}</h3>\n          <p>{p}</p>\n        </article>\n' for i, cl, h, p in sg[2])
                   + '      </div>\n')
    pl = c['plans']
    plans = section('utp-plans', 'utp-plan-title', head('Plans', 'utp-plan-title', pl[0], pl[1]) + '      <div class="utp-fgrid">\n'
                    + ''.join(f'        <article class="utp-fcard utp-fit{" is-rec" if t_ == "Enterprise" else ""}">\n          <p class="utp-fit-tag">{t_}</p>\n          <h3>{h}</h3>\n          <p>{p}</p>\n        </article>\n' for t_, h, p in pl[2])
                    + f'      </div>\n      <p class="utp-center"><a class="utp-btn utp-btn-brand" href="https://uptrendpos.com/pos-software-pricing/" data-track="{k}_plans">Compare UpTrendPos plans</a></p>\n')
    fq = c['faq']
    faq = section('utp-faq', 'utp-faq-title', head('FAQ', 'utp-faq-title', fq[0]) + '      <div class="utp-faq-list">\n'
                  + ''.join(f'        <details{" open" if n == 0 else ""}>\n          <summary>{q}</summary>\n          <p>{a}</p>\n        </details>\n' for n, (q, a) in enumerate(fq[1]))
                  + '      </div>\n')
    rel = section('', 'utp-rel-title', head('Related', 'utp-rel-title', 'Also selling these? See their setup') + '      <div class="utp-chips">\n'
                  + ''.join(f'        <a href="https://uptrendpos.com/industries/{s}/" data-page="{s}">{n}</a>\n' for s, n in c['related'])
                  + '        <a href="https://uptrendpos.com/industries/" data-page="industries">All 30+ business types</a>\n      </div>\n')
    fn = c['final']
    final = f'''  <section class="utp-final" aria-labelledby="utp-final-title">
    <div class="utp-wrap">
      <div class="utp-final-box">
        <h2 id="utp-final-title">{fn[0]}</h2>
        <p>{fn[1]}</p>
        <div class="utp-cta">
          <a class="utp-btn utp-btn-primary" href="https://live.uptrendpos.com/" target="_blank" rel="noopener" data-track="{k}_final_trial">Start 14-day free trial</a>
          <a class="utp-btn utp-btn-ghost" href="https://uptrendpos.com/contact-us/" data-track="{k}_final_contact">Book a free demo</a>
        </div>
        <div class="utp-contact">
          <a href="tel:+923192223292" data-track="{k}_final_call">Call 0319 2223292</a>
          <a href="mailto:sales@uptrendpos.com" data-track="{k}_final_email">sales@uptrendpos.com</a>
        </div>
      </div>
    </div>
  </section>
'''
    order = c.get('order', ['problems', 'usp', 'caps', 'feats', 'hwsec', 'setups', 'proc', 'offline', 'bens', 'reps', 'duo', 'segs', 'plans', 'faq', 'rel'])
    parts = dict(problems=problems, usp=usp, caps=caps, feats=feats, hwsec=hwsec, setups=setups, proc=proc, offline=offline, bens=bens, reps=reps, duo=duo,
                 segs=segs, plans=plans, faq=faq, rel=rel)
    parts.update(c.get('custom', {}))
    html = alt_pass(f'<div class="utp utp-gro {c["root"]}" id="{c["root_id"]}">\n\n' + hero + ''.join(parts[x] for x in order) + final + '</div>\n')
    assert '<!--' not in html and '<style' not in html and '<script' not in html
    (P / c['file']).write_text(html)
    txt = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', re.sub(r'<svg.*?</svg>', '', html, flags=re.S)))
    w = len(txt.split()); kw = len(re.findall(re.escape(c['focus']), txt, re.I))
    print(c['file'], 'words', w, 'kw', kw, '%.2f%%' % (100 * kw / w), 'faqs', html.count('<summary>'))
    for s2 in c.get('secondary', []):
        print('  secondary', s2, len(re.findall(re.escape(s2), txt, re.I)))
    return html
