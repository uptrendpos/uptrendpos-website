"""Site Kit 1.0 page pass: takes the current page code, puts the animated stage in every hero,
moves the hero picture into a showcase under the hero, adds SEO data attributes and the
EEAT 'reviewed' strip, and writes the delivery folder + SEO sheet in WordPress page order."""
import csv, html, json, pathlib, re, sys

SITE = pathlib.Path('/home/claude/site')
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/delivery/UpTrendPos-Site-Kit-v1.4')
PAGES = OUT / '2-pages'
UP = 'https://uptrendpos.com/wp-content/uploads/'
TODAY_ISO, TODAY = '2026-10-20', '20 October 2026'
NEW_ISO, NEW = '2026-10-29', '29 October 2026'  # pages changed in 1.3
SHOWCASE = False  # 1.2 (Abdul, 20 Oct 2026): no picture under the hero on any page

WA = ('<svg width="20" height="20" viewBox="0 0 24 24" fill="#25D366" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.4.1-.6.3-.2.2-.8.8-.8 2s.8 2.3.9 2.5c.1.2 1.6 2.5 4 3.5 1.5.6 2 .7 2.8.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/></svg>')
TOK = {
    '{{WA}}': WA,
    '{{WAC}}': WA.replace('fill="#25D366"', 'fill="currentColor"'),
    '{{TK}}': '<span class="utp-tk-ic"><svg width="16" height="16" viewBox="0 0 20 20" aria-hidden="true"><path d="M6 10.2l2.6 2.6L14 7.4" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></span>',
    '{{Y}}': '<span class="utp-yes" role="img" aria-label="Included"></span>',
    '{{N}}': '<span class="utp-no" role="img" aria-label="Not included"></span>',
    '{{PHONE_IC}}': '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
    '{{MAIL_IC}}': '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 6l-10 7L2 6"/></svg>',
}
TOK['{{PHONE_IC24}}'] = TOK['{{PHONE_IC}}'].replace('width="18" height="18"', 'width="24" height="24"').replace('stroke-width="2"', 'stroke-width="1.8"')
LOGOS = [('pos10.png', 'UpTrendPos customer logo'), ('pos8.png', 'UpTrendPos customer logo'), ('pos1.jpeg', 'UpTrendPos customer logo'), ('pos2.jpeg', 'UpTrendPos customer logo'),
         ('pos9.png', 'UpTrendPos customer logo'), ('pos3.jpeg', 'UpTrendPos customer logo'), ('pos4.jpeg', 'UpTrendPos customer logo'), ('pos6.jpeg', 'UpTrendPos customer logo'),
         ('hamza-pharmacy1.png', 'Hamza Pharmacy logo, an UpTrendPos customer')]
TOK['{{LOGOS}}'] = ('<div class="utp-marquee utp-logos">\n      <ul class="utp-mq-track">\n'
                    + ''.join(f'          <li class="utp-logo"><img src="{UP}{f}" width="180" height="72" loading="lazy" decoding="async" alt="{a}"></li>\n' for f, a in LOGOS)
                    + '      </ul>\n    </div>')

SHIELD = ('<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
          '<path d="M12 3l7.5 3v5.5c0 4.5-3.2 8.2-7.5 9.5-4.3-1.3-7.5-5-7.5-9.5V6z"/><path d="M8.8 12l2.2 2.2 4.2-4.4"/></svg>')

# WordPress "All Pages" order (Abdul's screenshots). Pages not built yet are skipped.
# key, file name, source, url, stage preset, stage label, showcase caption, seo
P = [
 dict(n='about-us', src='core/about.html', url='/about-uptrendpos/', stage='about', cap='Made in Sahiwal for Pakistani counters',
      label='Animated demo: UpTrendPos makes a bill on a phone, prints it on a small Type-C printer and shows team facts: built in Sahiwal, support on WhatsApp, free updates',
      title='About UpTrendPos: POS Software Company in Pakistan', desc='Meet UpTrendPos, the POS and accounting software team in Sahiwal. Built for Pakistani shops: offline billing, udhaar, stock and FBR invoices.',
      kw='UpTrendPos', sec='about UpTrendPos, POS software company in Pakistan, UpTrend POS'),
 dict(n='contact-us', src='core/contact.html', url='/contact-us/', stage='contact', cap='Free demo on WhatsApp, made for your shop type',
      label='Animated demo: a shop owner books a free POS software demo with the UpTrendPos team on WhatsApp',
      title='Free POS Software Demo on WhatsApp | Contact UpTrendPos', desc='Book a free POS software demo on WhatsApp or call 0319 2223292. See UpTrendPos for your shop type and get help with setup, prices and FBR.',
      kw='free POS software demo', sec='contact UpTrendPos, POS software demo, UpTrendPos phone number'),
 dict(n='downloads', src='core/downloads.html', url='/download-pos-software/', stage='downloads', cap='One account on your PC, phone and the web',
      label='Animated demo: UpTrendPos keeps billing offline, saves bills on the device and syncs them to the Windows, Android and web apps',
      title='Download POS Software for PC, Android & Web | UpTrendPos', desc='Download POS software for your Windows PC or Android phone, or open the web app. One account on every device, offline billing, 14-day free trial.',
      kw='download POS software', sec='POS software for PC, POS app for Android, UpTrendPos app download'),
 dict(n='fbr-pos-integration', src='pages/website_fbr_pos_integration_v1.html', url='/fbr-pos-integration/', stage='fbr', cap='FBR invoice number and QR code on the bill',
      label='Animated demo: an FBR invoice in UpTrendPos gets its FBR invoice number, QR code and the Re 1 POS fee, then prints',
      title='FBR POS Integration for Retailers in Pakistan | UpTrendPos', desc='FBR POS integration for Tier-1 retailers: FBR invoice number and QR code on every bill, Re 1 POS fee, sandbox testing and billing during load-shedding.',
      kw='FBR POS integration', sec='FBR POS system, FBR integrated POS software, Tier-1 retailer POS'),
 dict(n='home', upd=True, src='core/home.html', url='/', stage='home', cap='',
      label='Animated demo: a quick bill is made on the UpTrendPos phone app, printed on a small Type-C thermal printer and sent on WhatsApp, with low stock and expiry alerts',
      title='POS Software in Pakistan: Easy & FBR Ready | UpTrendPos', desc='UpTrendPos is easy POS software in Pakistan for every shop: fast billing, stock, udhaar khata and FBR invoices. Works offline on PC, phone and web.',
      kw='POS software in Pakistan', sec='POS system in Pakistan, billing software, udhaar khata app'),
 dict(n='industries', upd=True, src='pages/website_industries_hub_v1.html', url='/industries/', stage='hub', cap='One app, ready setups for 30+ business types',
      label='Animated demo: picking a business type in UpTrendPos opens a ready setup, such as 17,000+ medicines for pharmacies and IMEI tracking for mobile shops',
      title='Industry-Specific POS Software for 30+ Shops | UpTrendPos', desc='Industry-specific POS software for 30+ shop types in Pakistan. Pick your business type and get ready units, fields and reports. Works offline.',
      kw='industry-specific POS software', sec='POS software by business type, retail POS software Pakistan'),
 dict(n='mobile-shop-pos-software', upd=True, src='pages/website_mobile_shop_v1.html', url='/industries/mobile-shop-pos-software/', stage='mobile', cap='Mobile shop counter with IMEI, warranty and qist',
      label='Animated demo: a mobile phone sale in UpTrendPos saves the IMEI, finds the warranty and sets up a qist plan',
      title='Mobile Shop POS Software in Pakistan | UpTrendPos', desc='Mobile shop POS software for phone and computer shops in Pakistan: 670+ products ready, IMEI from purchase to sale, warranty lookup and qist.',
      kw='mobile shop POS software', sec='mobile shop software, computer shop software, IMEI tracking'),
 dict(n='baby-store-pos-software', src='pages/website_baby_v1.html', url='/industries/baby-store-pos-software/', stage='baby', cap='', upd=True, label='',
      title='Baby Store POS Software in Pakistan | UpTrendPos', desc='Baby store POS software for diaper and baby care shops in Pakistan: sell by pack or piece, stock for every diaper size, batch and expiry alerts.',
      kw='baby store POS software', sec='diaper shop software, baby shop POS, baby care shop software'),
 dict(n='clothing-store-pos-software', src='pages/website_clothing_v1.html', url='/industries/clothing-store-pos-software/', stage='clothing', cap='', upd=True,
      label='',
      title='Clothing Store POS Software in Pakistan | UpTrendPos', desc='Clothing store POS software for garment shops in Pakistan: stock for every size and colour, variant generator, barcode tags and easy exchanges.',
      kw='clothing store POS software', sec='garments shop software, garment shop POS, boutique POS software'),
 dict(n='cosmetics-store-pos-software', src='pages/website_cosmetics_v1.html', url='/industries/cosmetics-store-pos-software/', stage='cosmetics', cap='', upd=True,
      label='',
      title='Cosmetics Store POS Software in Pakistan | UpTrendPos', desc='Cosmetics store POS software for beauty shops in Pakistan: 5,000+ products loaded, stock for every shade, batch and expiry alerts, barcode billing.',
      kw='cosmetics store POS software', sec='cosmetics shop software, beauty store POS, makeup shop software'),
 dict(n='electronics-store-pos-software', upd=True, src='pages/website_electronics_v1.html', url='/industries/electronics-store-pos-software/', stage='electronics', cap='Electronics counter with serials and warranty lookup',
      label='Animated demo: an electronics sale in UpTrendPos saves serial numbers, finds a warranty, sends a CCTV quote and sets up qist',
      title='Electronics Store POS Software in Pakistan | UpTrendPos', desc='Electronics store POS software for electronics, home appliance and CCTV shops: 1,100+ products ready, serial numbers, warranty lookup and qist.',
      kw='electronics store POS software', sec='home appliance shop software, CCTV shop software, electronics shop software'),
 dict(n='electrical-store-pos-software', src='pages/website_electrical_v1.html', url='/industries/electrical-store-pos-software/', stage='electrical', cap='', upd=True, label='',
      title='Electrical Store POS Software in Pakistan | UpTrendPos', desc='Electrical store POS software for electric and LED shops in Pakistan: wire by the meter, boxes by the piece, A4 quotes and udhaar for electricians.',
      kw='electrical store POS software', sec='electrical shop software, LED light shop software, electric store billing software'),
 dict(n='grocery-store-pos-software', src='pages/website_grocery_v2.html', url='/industries/grocery-store-pos-software/', stage='grocery', cap='Kiryana counter: bill, print, WhatsApp, udhaar',
      label='Animated demo: a kiryana bill is made on a phone, printed on a Type-C thermal printer and sent on WhatsApp, with udhaar and low stock alerts',
      title='Grocery Store POS Software in Pakistan | UpTrendPos', desc='Grocery store POS software for kiryana shops in Pakistan. Bill on your phone, print with a Type-C printer, send bills on WhatsApp and track udhaar.',
      kw='grocery store POS software', sec='kiryana store software, udhaar khata, kiryana POS'),
 dict(n='pharmacy-pos-software', src='pages/website_pharmacy_v1.html', url='/industries/pharmacy-pos-software/', stage='pharmacy', cap='Medical store counter with batch and expiry',
      label='Animated demo: a medical store bill in UpTrendPos with salt search, an Rx item, and batch expiry and low stock alerts',
      title='Pharmacy POS Software in Pakistan | UpTrendPos', desc='Pharmacy POS software for medical stores in Pakistan: 17,000+ medicines loaded, salt search, batch and expiry alerts, Rx checks and FBR invoices.',
      kw='pharmacy POS software', sec='medical store software, pharmacy software in Pakistan, medicine expiry tracking'),
 dict(n='shoe-store-pos-software', src='pages/website_shoes_v1.html', url='/industries/shoe-store-pos-software/', stage='shoes', cap='', upd=True, label='',
      title='Shoe Store POS Software in Pakistan | UpTrendPos', desc='Shoe store POS software for footwear shops in Pakistan: pairs for every size and colour, variant generator, box labels and size swaps on one bill.',
      kw='shoe store POS software', sec='footwear shop software, shoe shop billing software, shoe shop POS'),
 dict(n='solar-shop-pos-software', upd=True, src='pages/website_solar_v1.html', url='/industries/solar-shop-pos-software/', stage='solar', cap='Solar shop counter with serials and qist',
      label='Animated demo: a solar system quotation in UpTrendPos is sent on WhatsApp, turned into a sale with serial numbers, warranty lookup and qist',
      title='Solar Shop POS Software in Pakistan | UpTrendPos', desc='Solar shop POS software for solar businesses in Pakistan: 1,100+ products ready, serial of every panel and inverter, warranty lookup, quotes and qist.',
      kw='solar shop POS software', sec='solar shop software, solar business software, inverter serial tracking'),
 dict(n='tailor-shop-pos-software', src='pages/website_tailor_v1.html', url='/industries/tailor-shop-pos-software/', stage='tailor', cap='Tailor shop: sizes, orders and delivery dates',
      label='Animated demo: a stitching order in UpTrendPos saves the customer sizes, takes an advance, sends a workshop slip and marks the order ready',
      title='Tailor Shop POS Software in Pakistan | UpTrendPos', desc='Tailor shop POS software for tailors and boutiques: sizes saved per customer, stitching orders, delivery dates, advance and balance, WhatsApp slips.',
      kw='tailor shop POS software', sec='tailor shop software, tailoring software, boutique software'),
 dict(n='pricing', src='core/pricing.html', url='/pos-software-pricing/', stage='pricing', cap='Runs on the devices you already have',
      label='Animated demo: UpTrendPos plans with a 14-day free trial, unlimited bills and moving up a plan without losing data',
      title='POS Software Pricing in Pakistan: 3 Easy Plans | UpTrendPos', desc='POS software pricing in Pakistan: Premium Rs 2,000, Enterprise Rs 3,000 and Custom Rs 6,000 a month. Unlimited bills and a 14-day free trial.',
      kw='POS software pricing', sec='POS software price in Pakistan, POS system cost, UpTrendPos plans'),
 dict(n='privacy-policy', src='pages/website_privacy_v1.html', url='/privacy-policy/', stage='', cap='',
      doc_img=('uptrendpos-privacy-policy.webp', 'UpTrendPos privacy policy: your shop data stays separate, protected with a PIN and can be exported or deleted'),
      title='Privacy Policy: How UpTrendPos Protects Your Data', desc='Read the UpTrendPos privacy policy: what shop data we collect, why we need it, who we share it with, how we protect it and how to export or delete it.',
      kw='privacy policy', sec='UpTrendPos privacy policy, POS data privacy Pakistan'),
 dict(n='support', src='pages/website_support_v1.html', url='/support/', stage='', cap='',
      doc_img=('uptrendpos-support-help-center.webp', 'UpTrendPos support on WhatsApp: the support team helps a shop owner fix a printer setting in Urdu or English'),
      title='UpTrendPos Support: Help on WhatsApp, Phone & Email', desc='Get UpTrendPos support on WhatsApp, phone or email in Urdu or English. Monday to Saturday, 10 am to 7 pm. Quick fixes, reply times and setup help.',
      kw='UpTrendPos support', sec='UpTrendPos help center, POS software support Pakistan'),
 dict(n='terms-and-conditions', src='pages/website_terms_v1.html', url='/terms-and-conditions/', stage='', cap='',
      doc_img=('uptrendpos-terms-and-conditions.webp', 'UpTrendPos terms and conditions in simple words: free trial, plans and payments, offline use, FBR and your data'),
      title='Terms and Conditions for UpTrendPos POS Software', desc='UpTrendPos terms and conditions for the web, Android and Windows apps: free trial, plans, payments, refunds, offline use, FBR and your data.',
      kw='terms and conditions', sec='UpTrendPos terms and conditions, POS software terms'),
 dict(n='vehicle-showroom-software', src='pages/website_vehicle_showroom_v1.html', url='/industries/vehicle-showroom-software/', stage='vehicle', cap='', upd=True, label='',
      title='Vehicle Showroom Software for Bikes, Cars & EVs | UpTrendPos', desc='Vehicle showroom software for bike, EV and car dealers in Pakistan: chassis number on every unit, warranty lookup, qist with guarantor and A4 quotes.',
      kw='vehicle showroom software', sec='motorcycle showroom software, car showroom software, bike showroom software, electric bike showroom software'),
]


# Pages added by the daily automation (site/pages.json, written by daily.py)
_extra = SITE / 'pages.json'
if _extra.exists():
    for _p in json.loads(_extra.read_text()):
        if not any(q['n'] == _p['n'] for q in P):
            P.append(_p)


# Small content fixes made in this pass (keyword use on the legal and support pages)
FIX = {
 'privacy-policy': [('Changes to this policy', 'Changes to this privacy policy'), ('In this policy,', 'In this privacy policy,'), ('as explained in this policy', 'as explained in this privacy policy'),
                    ('we will update this policy', 'we will update this privacy policy'), ('When we change this policy', 'When we change this privacy policy'),
                    ('20. Contact us', '20. Questions about this privacy policy'), ('<span class="utp-doc-n">20</span>Contact us', '<span class="utp-doc-n">20</span>Questions about this privacy policy'),
                    ('For any question about your privacy or your data, contact us:', 'For any question about this privacy policy or your data, contact us:')],
 'terms-and-conditions': [('About these terms', 'About these terms and conditions'), ('you accept these terms and our', 'you accept these terms and conditions and our'),
                          ('Changes to these terms', 'Changes to these terms and conditions'), ('We may update these terms from time', 'We may update these terms and conditions from time'),
                          ('For any question about these terms, contact us', 'For any question about these terms and conditions, contact us'),
                          ('breaches of these terms,', 'breaches of these terms and conditions,'), ('Nothing in these terms removes', 'Nothing in these terms and conditions removes'),
                          ('you accept these terms for that business', 'you accept these terms and conditions for that business')],
 'support': [('Get help with UpTrendPos on WhatsApp, phone or email. Our support team helps', 'UpTrendPos support helps you on WhatsApp, phone or email. Our team helps'),
             ('Four ways to reach the support team', 'Four ways to reach UpTrendPos support'), ('>Support hours and reply times<', '>UpTrendPos support hours and reply times<'),
             ('What our support includes', 'What UpTrendPos support includes'), ('>Support questions<', '>UpTrendPos support questions<'),
             ('Is support free?', 'Is UpTrendPos support free?'), ('Our support hours are Monday', 'UpTrendPos support hours are Monday')],
}

# Plan change (Abdul, 20 Oct 2026): staff commission is now in Enterprise too (attendance + salary stay Custom)
GLOBAL_FIX = [
 ('including staff attendance, salary and commission.', 'including staff attendance and salary.'),
 ('Adds qist plans, FBR invoices, barcode labels, profit reports and audit trail.', 'Adds qist plans, FBR invoices, barcode labels, staff commission, profit reports and audit trail.'),
 ('Adds FBR invoices, barcode labels, profit reports and audit trail.', 'Adds FBR invoices, barcode labels, staff commission, profit reports and audit trail.'),
 ('Adds barcode labels, FBR invoices, profit reports and audit trail.', 'Adds barcode labels, FBR invoices, staff commission, profit reports and audit trail.'),
 ('Adds FBR invoices, profit reports and audit trail.', 'Adds FBR invoices, staff commission, profit reports and audit trail.'),
 ('<li>Attendance, salary and staff commission <em class="utp-ptag">Custom</em></li>', '<li>Staff commission on sales <em class="utp-ptag">Enterprise+</em></li><li>Attendance and salary <em class="utp-ptag">Custom</em></li>'),
]


def expand(s):
    for k, v in TOK.items():
        s = s.replace(k, v)
    return s


def attr(v):
    return html.escape(v, quote=True)


def stage_titles():
    js = pathlib.Path('/home/claude/kit/uptrendpos-site-kit/assets/js/utp.js').read_text()
    body = js[js.index('var P = {'):js.index('function buildStage')]
    out, cur = {}, None
    for line in body.splitlines():
        m = re.match(r"\s+(\w+): \[", line)
        if m:
            cur = m.group(1)
        for g in re.findall(r"\['((?:[^'\\]|\\.)*)', '(\w+)', '(\w)', '((?:[^'\\]|\\.)*)', '((?:[^'\\]|\\.)*)'(?:, '(?:[^'\\]|\\.)*')?\]", line):
            out.setdefault(cur, []).append(g[3])
    return out


STAGE_TITLES = stage_titles()


def stage_div(p):
    items = p.get('stage_items')  # 1.5: new business types carry their 6 hero items in the page code
    titles = [i[3] for i in items] if items else STAGE_TITLES[p['stage']]
    label = 'Animated diagram: UpTrendPos at the centre with its tools circling it. It shows common shop problems and the fix: ' + ', '.join(titles) + '.'
    extra = f' data-stage-items="{attr(json.dumps(items, separators=(",", ":")))}"' if items else ''
    return f'<div class="utp-stage" data-stage="{p["stage"]}"{extra} role="img" aria-label="{attr(label)}"></div>'


def transform(p):
    s = expand((SITE / p['src']).read_text())
    assert '{{' not in s, p['n']
    for a, b in GLOBAL_FIX:
        s = s.replace(a, b)
    for a, b in FIX.get(p['n'], []):
        assert a in s, (p['n'], a)
        s = s.replace(a, b)
    # 1) SEO attributes on the root
    kw_all = p['kw'] + (', ' + p['sec'] if p['sec'] else '')
    seo = f' data-seo-title="{attr(p["title"])}" data-seo-desc="{attr(p["desc"])}" data-seo-kw="{attr(kw_all)}" data-seo-robots="index"'
    s = re.sub(r'^(<div class="utp[^"]*" id="[^"]+")', lambda m: m.group(1) + seo, s, count=1)
    assert 'data-seo-title' in s, p['n']
    # 2) hero visual -> animated stage; hero picture -> showcase under the hero
    showcase = ''
    m = re.search(r'\n(\s*)<figure class="utp-hero-img">\s*(<img[^>]+>)\s*</figure>', s)
    if m and p['stage']:
        img = m.group(2)
        img = re.sub(r'\sfetchpriority="high"', '', img)
        if 'loading=' not in img:
            img = img.replace('<img ', '<img loading="lazy" ', 1)
        cap = f'<figcaption>{p["cap"]}</figcaption>' if p['cap'] else ''
        showcase = f'\n    <div class="utp-wrap">\n      <figure class="utp-showcase">\n        {img}\n        {cap}\n      </figure>\n    </div>\n'
        s = s[:m.start()] + '\n' + m.group(1) + stage_div(p) + s[m.end():]
    else:
        m2 = re.search(r'<div class="utp-art"[^>]*>.*?</div>(?=\s*</div>\s*\n)', s, re.S)
        if p['stage']:
            assert m2, p['n']
            s = s[:m2.start()] + stage_div(p) + s[m2.end():]
    if showcase and SHOWCASE:
        hero_end = s.index('</section>', s.index('class="utp-hero'))
        s = s[:hero_end] + showcase.lstrip('\n').rstrip(' ') + '  ' + s[hero_end:]
    # 3) legal / support pages: one picture at the top of the document
    if p.get('doc_img') and SHOWCASE:
        f, alt = p['doc_img']
        fig = (f'<figure class="utp-doc-fig"><img src="{UP}{f}" width="1200" height="900" loading="lazy" decoding="async" alt="{attr(alt)}"></figure>\n')
        if 'class="utp-doc-body">' in s:
            s = s.replace('class="utp-doc-body">', 'class="utp-doc-body">\n        ' + fig, 1)
        else:  # support page: after the hero
            hero_end = s.index('</section>', s.index('class="utp-hero')) + len('</section>')
            s = s[:hero_end] + '\n\n  <div class="utp-wrap utp-doc-fig-wrap">\n    ' + fig + '  </div>' + s[hero_end:]
    # 4) EEAT strip: who wrote and checked the page, and when
    legal = p['n'] in ('privacy-policy', 'terms-and-conditions')
    who = ('Written in plain words and reviewed by the <strong>UpTrendPos team</strong> in Sahiwal, Pakistan.' if legal else
           'Written and checked against the live app by the <strong>UpTrendPos team</strong> in Sahiwal, Pakistan.')
    chips = (['Plain words', 'Pakistani law', 'Questions answered on WhatsApp'] if legal else
             ['Only features that are live', 'Local team in Sahiwal', 'Support in Urdu and English'])
    iso, day = (NEW_ISO, NEW) if p.get('upd') else (TODAY_ISO, TODAY)
    strip = ('  <section class="utp-rv-sec" aria-label="About this page">\n    <div class="utp-wrap">\n      <div class="utp-reviewed">\n'
             f'        <span class="rv-ic">{SHIELD}</span>\n'
             f'        <p class="rv-tx">{who} Last updated <time datetime="{iso}">{day}</time>. Something not clear? <a href="https://uptrendpos.com/contact-us/" data-track="reviewed_contact">Ask us</a>.</p>\n'
             '        <ul>' + ''.join(f'<li>{c}</li>' for c in chips) + '</ul>\n      </div>\n    </div>\n  </section>\n\n')
    if '<section class="utp-final"' in s:
        s = s.replace('  <section class="utp-final"', strip + '  <section class="utp-final"', 1)
    else:
        i = s.rstrip().rfind('</div>')
        s = s[:i] + strip.rstrip('\n') + '\n' + s[i:]
    # 5) legal pages: dates follow today's review
    s = s.replace('Last updated: <strong>13 October 2026</strong>', f'Last updated: <strong>{day}</strong>')
    # 5b) 1.2: the hero picture is gone, so the focus keyword moves to the first content picture's ALT
    if p['stage'] and not re.search(r'alt="[^"]*' + re.escape(p['kw']) + '[^"]*"', s, re.I):
        def kw_alt(m):
            a = m.group(2)
            return m.group(1) + p['kw'][0].upper() + p['kw'][1:] + ': ' + (a[0].lower() + a[1:] if re.match(r'(A|An|The) ', a) else a) + '"'
        s = re.sub(r'(<img(?![^>]*/(?:pos\d+|hamza)[^>]*)[^>]*\salt=")([^"]+)"', kw_alt, s, count=1)
    # 6) clean-up checks
    s = s.replace(' style="padding-top:0"', ' data-pt0').replace('class="utp-sec" data-pt0', 'class="utp-sec utp-pt0"')
    assert '<style' not in s and '<script' not in s and '<!--' not in s, p['n']
    return s


def text(s):
    s = re.sub(r'<svg.*?</svg>', '', s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


def check(p, s):
    t = text(s)
    w = len(t.split())
    kw = p['kw']
    n = len(re.findall(r'(?<![\w-])' + re.escape(kw) + r'(?![\w-])', t, flags=re.I))
    dens = 100 * n / max(w, 1)
    h1 = text(re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S).group(1))
    lead = re.search(r'class="utp-lead">(.*?)</p>', s, re.S)
    h2s = [text(h) for h in re.findall(r'<h2[^>]*>(.*?)</h2>', s, re.S)]
    alts = re.findall(r'alt="([^"]*)"', s)
    faqs = len(re.findall(r'<details', s))
    return dict(words=w, kw=n, dens=round(dens, 2), h1=kw.lower() in h1.lower(), lead=bool(lead) and kw.lower() in text(lead.group(1)).lower(),
                h2=sum(kw.lower() in h.lower() for h in h2s), alt=sum(kw.lower() in a.lower() for a in alts), imgs=len(alts), faqs=faqs,
                tlen=len(p['title']), dlen=len(p['desc']), t_kw=p['title'].lower().startswith(kw.lower()) or kw.lower() in p['title'].lower())


def main():
    PAGES.mkdir(parents=True, exist_ok=True)
    # Standing rule (Abdul, 29 Oct 2026): Home and the Industries hub must link every business type in the registry
    import json
    reg = json.loads(pathlib.Path('/home/claude/kit/uptrendpos-site-kit/data/industries.json').read_text())
    for src in ('core/home.html', 'pages/website_industries_hub_v1.html'):
        code = (SITE / src).read_text()
        miss = [t['slug'] for t in reg['types'] if f'data-page="{t["slug"]}"' not in code]
        assert not miss, (src, 'missing business types', miss)
    rows = []
    for i, p in enumerate(P, 1):
        s = transform(p)
        fn = f'{i:02d}-{p["n"]}.html'
        (PAGES / fn).write_text(s)
        c = check(p, s)
        rows.append((i, p, fn, c))
        print(f'{fn:42s} words {c["words"]:5d} kw {c["kw"]:3d} dens {c["dens"]:.2f}% H1 {c["h1"]} lead {c["lead"]} H2 {c["h2"]} alt {c["alt"]}/{c["imgs"]} faq {c["faqs"]} title {c["tlen"]} desc {c["dlen"]} kw-in-title {c["t_kw"]}')
    with open(OUT / 'seo-sheet.csv', 'w', newline='', encoding='utf-8') as f:
        wr = csv.writer(f)
        wr.writerow(['#', 'WordPress page', 'URL', 'Page HTML file', 'SEO title', 'Title length', 'Meta description', 'Description length', 'Focus keyword', 'Secondary keywords', 'Rank Math robots', 'Words', 'Keyword density'])
        names = {'about-us': 'About Us', 'contact-us': 'Contact Us', 'downloads': 'Downloads', 'fbr-pos-integration': 'FBR POS Integration', 'home': 'Home', 'industries': 'Industries',
                 'mobile-shop-pos-software': 'mobile shop POS software', 'electronics-store-pos-software': 'POS Software for Electronics, Home Appliances & CCTV Shop',
                 'grocery-store-pos-software': 'POS Software for Grocery Store', 'pharmacy-pos-software': 'POS Software for Pharmacy & Medical Store', 'solar-shop-pos-software': 'POS Software for Solar Shop',
                 'tailor-shop-pos-software': 'tailor shop POS software', 'baby-store-pos-software': 'POS Software for Baby Store & Diaper Shop', 'electrical-store-pos-software': 'Electrical & LED Lighting', 'shoe-store-pos-software': 'POS Software for Shoe Store', 'vehicle-showroom-software': 'Vehicle Showroom Software', 'clothing-store-pos-software': 'POS Software for Clothing & Garment Store', 'cosmetics-store-pos-software': 'POS Software for Cosmetics & Beauty Store', 'pricing': 'POS Software Pricing Plans', 'privacy-policy': 'Privacy And Policy', 'support': 'Support', 'terms-and-conditions': 'Terms & Conditions'}
        for i, p, fn, c in rows:
            wr.writerow([i, names.get(p['n']) or next((x['name'] for x in json.loads((SITE.parent / 'kit/uptrendpos-site-kit/data/industries.json').read_text())['types'] if x['slug'] == p['n']), p['n']), 'https://uptrendpos.com' + p['url'], '2-pages/' + fn, p['title'], c['tlen'], p['desc'], c['dlen'], p['kw'], p['sec'], 'index', c['words'], f'{c["dens"]}%'])
    return rows


if __name__ == '__main__':
    main()
