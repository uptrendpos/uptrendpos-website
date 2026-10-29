"""Builds pages/website_fbr_pos_integration_v1.html (Elementor HTML widget: no style/script/comments)."""
import pathlib, re, urllib.parse
P = pathlib.Path('/home/claude/site/pages')
WA = 'https://wa.me/923192223292?text='
UP = 'https://uptrendpos.com/wp-content/uploads/'
WA_SVG = '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.4.1-.6.3-.2.2-.8.8-.8 2s.8 2.3.9 2.5c.1.2 1.6 2.5 4 3.5 1.5.6 2 .7 2.8.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/></svg>'
ICON = {
    'qr': '<path d="M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h3v3h-3zM20 14v6h-3"/>',
    'coin': '<circle cx="12" cy="12" r="9"/><path d="M12 7v10M9.5 9.5c0-1.2 1.1-2 2.5-2s2.5.8 2.5 2-1.1 1.8-2.5 2.2-2.5 1-2.5 2.3 1.1 2 2.5 2 2.5-.8 2.5-2"/>',
    'counter': '<rect x="2" y="4" width="20" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>',
    'mode': '<path d="M4 6h10M4 12h16M4 18h7"/><circle cx="17" cy="6" r="2"/><circle cx="14" cy="18" r="2"/>',
    'wifi': '<path d="M5 12.5a10 10 0 0 1 14 0M8.5 16a5 5 0 0 1 7 0"/><circle cx="12" cy="19.5" r="1"/><path d="M3 3l18 18"/>',
    'box': '<path d="M21 8l-9-5-9 5 9 5 9-5z"/><path d="M3 8v8l9 5 9-5V8M12 13v8"/>',
    'tax': '<path d="M6 2h12v20l-3-2-3 2-3-2-3 2z"/><path d="M9 8l6 6M9.5 14a.5.5 0 1 0 0-1 .5.5 0 0 0 0 1zM14.5 9a.5.5 0 1 0 0-1 .5.5 0 0 0 0 1z"/>',
    'branch': '<circle cx="6" cy="5" r="2"/><circle cx="6" cy="19" r="2"/><circle cx="18" cy="12" r="2"/><path d="M6 7v10M8 12h8"/>',
    'shield': '<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    'user': '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
    'team': '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3.5 6"/>',
    'phone': '<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>',
}


def ico(n, c):
    return (f'<div class="utp-ico sm {c}"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[n]}</svg></div>')


def ul(items, cls='utp-checks'):
    return f'<ul class="{cls}">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


def head(eyebrow, hid, h2, p='', left=False):
    return (f'      <div class="utp-head{" left" if left else ""}">\n        <span class="utp-eyebrow">{eyebrow}</span>\n        <h2 id="{hid}">{h2}</h2>\n'
            + (f'        <p>{p}</p>\n' if p else '') + '      </div>\n')


def wa(msg):
    return WA + urllib.parse.quote(msg)


def sec(cls, sid, hid, inner):
    idattr = f' id="{sid}"' if sid else ''
    return f'  <section class="utp-sec{cls}"{idattr} aria-labelledby="{hid}">\n    <div class="utp-wrap">\n{inner}    </div>\n  </section>\n\n'


hero = f'''  <section class="utp-hero" aria-labelledby="utp-h1">
    <div class="utp-wrap utp-hero-grid">
      <div class="utp-hero-copy">
        <nav class="utp-crumb" aria-label="Breadcrumb">
          <ol>
            <li><a href="https://uptrendpos.com/">Home</a></li>
            <li><span aria-current="page">FBR POS Integration</span></li>
          </ol>
        </nav>
        <p class="utp-kicker">For Tier-1 retailers</p>
        <h1 id="utp-h1">FBR POS integration for retailers in <span class="utp-hl">Pakistan.</span></h1>
        <p class="utp-lead">UpTrendPos gives you ready FBR POS integration. Add the details FBR gives you, turn FBR on, and every bill prints an FBR invoice number, a QR code and the Re 1 POS fee. Billing, stock and udhaar keep working as normal, even when the internet goes off.</p>
        <div class="utp-cta">
          <a class="utp-btn utp-btn-primary" href="{wa('Hi, I need FBR POS integration for my shop')}" target="_blank" rel="noopener" data-track="fbr_hero_whatsapp">{WA_SVG} Get FBR setup help</a>
          <a class="utp-btn utp-btn-ghost" href="#utp-tier1" data-track="fbr_hero_check">Am I a Tier-1 retailer?</a>
        </div>
        <p class="utp-smart-note">Free setup call in Urdu or English · We test your first FBR bill with you</p>
        <ul class="utp-ticks">
          <li>FBR invoice number and QR</li>
          <li>Re 1 fee added on its own</li>
          <li>Practice, Sandbox and Live modes</li>
        </ul>
      </div>
      <figure class="utp-hero-img">
        <img src="{UP}uptrendpos-fbr-pos-invoice-qr.webp" width="1200" height="900" fetchpriority="high" decoding="async" alt="FBR POS integration receipt explained: NTN and STRN, POS ID, your invoice number, Re 1 FBR POS fee, FBR invoice number and QR code">
      </figure>
    </div>
  </section>

'''

stats = [('Rs 500,000', 'Penalty for the first default', 'It grows to Rs 1 million, Rs 2 million and Rs 3 million for later defaults.'),
         ('60%', 'Less input tax', 'A Tier-1 retailer who is not integrated loses 60% of adjustable input tax for that period.'),
         ('Sealed', 'Shop and utilities', 'FBR can seal the shop and ask to cut gas and electricity connections.'),
         ('24 hours', 'For offline bills', 'Bills made during an outage must reach FBR within 24 hours after the system is back.')]
risk = (f'''  <section class="utp-sec utp-risk-sec" aria-labelledby="utp-risk-title">
    <div class="utp-wrap">
      <div class="utp-risk">
        <div class="utp-risk-head">
          <span class="utp-eyebrow">Why it matters</span>
          <h2 id="utp-risk-title">What happens without FBR POS integration</h2>
          <p>If you are a Tier-1 retailer, FBR POS integration is required by the Sales Tax Act, 1990. These are the costs of waiting.</p>
        </div>
        <ul class="utp-stats">
''' + ''.join(f'          <li><strong>{a}</strong><span>{b}</span><small>{c}</small></li>\n' for a, b, c in stats) + '''        </ul>
        <p class="utp-risk-src">Source: Sales Tax Act 1990 sections 3(9A), 8B(6), 14AB and 33, and the Sales Tax Rules, 2006 (Chapter XIV). Rules change, so always check the latest on the <a href="https://www.fbr.gov.pk/" target="_blank" rel="noopener">FBR website</a>. This is general guidance, not tax advice.</p>
      </div>
    </div>
  </section>

''')

tier = [('Part of a chain', 'A unit of a national or international chain of stores, including franchises'),
        ('Shop in an air-conditioned mall or plaza', 'Any retail outlet in an air-conditioned mall, plaza or centre (kiosks are not counted)'),
        ('Big electricity bill', 'Total electricity bills of more than Rs 1.2 million in the last 12 months'),
        ('Wholesaler and retailer', 'You import or buy in bulk and also sell to the public'),
        ('Card machine at your counter', 'You accept debit or credit cards, or digital payments, through a bank or SBP-approved provider'),
        ('High withholding tax on bills', 'Your 236G or 236H withholding tax is more than the limit FBR has notified'),
        ('Notified by FBR', 'FBR has named your class of business, or sent you a Tier-1 notice')]
checker = ('  <section class="utp-sec" id="utp-tier1" aria-labelledby="utp-tier1-title">\n    <div class="utp-wrap utp-split utp-check-split">\n      <div>\n'
           + head('Free check', 'utp-tier1-title', 'Are you a Tier-1 retailer? Check in 30 seconds',
                  'Tick every line that is true for your shop. One tick is enough to make you Tier-1.', left=True)
           + '        <p class="utp-body">Not sure about one line? Tick what you know and send it to us. We will tell you what applies to your shop.</p>\n'
           + '        <ul class="utp-feat">\n          <li>Under section 2(43A) of the Sales Tax Act, 1990</li>\n          <li>Each counter that takes payment must be integrated</li>\n          <li>Wrongly listed as Tier-1? Talk to your tax advisor before you integrate</li>\n        </ul>\n      </div>\n'
           + '      <div class="utp-checker" data-utp-checker>\n        <p class="utp-checker-h">My shop is...</p>\n        <ul class="utp-check-list">\n'
           + ''.join(f'          <li><label><input type="checkbox" value="{a}"><span class="utp-cbox" aria-hidden="true"></span><span class="utp-ctext"><strong>{a}</strong><small>{b}</small></span></label></li>\n' for a, b in tier)
           + '        </ul>\n        <div class="utp-check-result" aria-live="polite">\n'
           + '          <p class="utp-check-msg" data-none="Tick the lines that are true for your shop. If none apply, you are likely not Tier-1, but you can still use FBR invoices if you are sales tax registered." data-yes="You are likely a Tier-1 retailer. FBR POS integration is required for your shop. Send this result to us and we will set it up with you.">Tick the lines that are true for your shop. If none apply, you are likely not Tier-1, but you can still use FBR invoices if you are sales tax registered.</p>\n'
           + f'          <a class="utp-btn utp-btn-primary" href="{wa("Hi, I checked the Tier-1 list on your website and need FBR POS integration")}" target="_blank" rel="noopener" data-utp-check-wa data-track="fbr_checker_whatsapp">{WA_SVG} Send my result on WhatsApp</a>\n'
           + '        </div>\n      </div>\n    </div>\n  </section>\n\n')

feats = [('qr', 'g', 'FBR number and QR on every bill', 'Each bill goes to FBR and comes back with its FBR invoice number. The QR code prints on the receipt.'),
         ('coin', 'y', 'Re 1 POS fee added on its own', 'The FBR POS service fee is added to each FBR bill and shown on the receipt, so you never add it by hand.'),
         ('counter', 'b', 'Every counter set up', 'Each counter keeps its own POS registration and terminal ID, as FBR rules ask.'),
         ('mode', 't', 'Practice, Sandbox and Live', 'Learn the bill in Practice mode, test with FBR Sandbox, then switch to Production when your details arrive.'),
         ('wifi', 'n', 'Ready for load-shedding', 'Billing keeps running when the internet goes. Bills are kept safe and reported when the connection is back.'),
         ('box', 'g', 'Stock, udhaar and accounts too', 'FBR is not a separate app. The same bill updates stock, customer khata, sales reports and accounts.'),
         ('tax', 'y', 'GST line without FBR', 'Registered for sales tax but not Tier-1? Turn on Local GST to show a GST line on bills without FBR.'),
         ('branch', 'b', 'More than one branch', 'Each branch and counter is set up with its own FBR details. The owner sees every branch in one account.'),
         ('shield', 't', 'Safe FBR details', 'Your FBR token and keys stay inside your shop account. Only staff you allow can open FBR settings.')]
featsec = sec(' utp-alt', '', 'utp-what-title',
              head('UpTrendPos + FBR', 'utp-what-title', 'What our FBR POS integration does for your shop',
                   'UpTrendPos has it built in. There is no extra software to buy and nothing to install. You only add the details FBR gives you and turn it on.')
              + '      <div class="utp-fgrid">\n'
              + ''.join(f'        <article class="utp-fcard">\n          {ico(i, c)}\n          <h3>{h}</h3>\n          <p>{p}</p>\n        </article>\n' for i, c, h, p in feats)
              + '      </div>\n      <p class="utp-note">FBR invoices come with the Enterprise and Custom plans. <a class="utp-link" href="https://uptrendpos.com/pos-software-pricing/" data-track="fbr_feat_pricing">Compare UpTrendPos plans</a></p>\n')

steps = [('Check if you are Tier-1', 'Use the checker above. Any one test is enough.'),
         ('Register in IRIS', 'Get your NTN and STRN on FBR\'s IRIS portal. Declare your outlet and register every counter that takes payment.'),
         ('Get your FBR POS details', 'FBR gives each counter a POS registration number and terminal ID, and you get your API token. FBR rules say integration runs through a licensed integrator, and PRAL offers this service free of cost.'),
         ('Add them to UpTrendPos', 'Open Settings, FBR Fiscalization. Enter your POS registration number, NTN, STRN, terminal ID and token. Test a few bills in Sandbox.'),
         ('Go live', 'Switch the mode to Production and turn FBR on. From now on, every bill carries the FBR invoice number, QR code and Re 1 fee.')]
stepsec = sec('', 'utp-steps', 'utp-steps-title',
              head('How to get FBR POS integration', 'utp-steps-title', 'FBR POS integration in 5 simple steps',
                   'Most of the work is your FBR registration. The UpTrendPos side takes a few minutes, and our team does it with you on WhatsApp.')
              + '      <div class="utp-proc">\n        <figure class="utp-figure utp-figure-img">\n'
              + f'          <img src="{UP}uptrendpos-fbr-pos-integration-steps.webp" width="1200" height="900" loading="lazy" decoding="async" alt="FBR POS integration steps: check Tier-1, register in IRIS, get FBR POS details, add them to UpTrendPos, every bill is live">\n'
              + '        </figure>\n        <ol class="utp-rep">\n'
              + ''.join(f'          <li><strong>{h}</strong><span>{p}</span></li>\n' for h, p in steps)
              + '        </ol>\n      </div>\n'
              + '      <p class="utp-note">Need help with IRIS? <a class="utp-link" href="' + wa('Hi, I need help with IRIS registration for FBR POS') + '" target="_blank" rel="noopener" data-track="fbr_iris_help">Ask us on WhatsApp</a>. We guide you, or work with your tax advisor.</p>\n')

receipt_items = ['Shop name, NTN and STRN', 'POS ID of the counter', 'Your own invoice number, date and time', 'Each item with quantity and price',
                 'Value without tax, sales tax rate and amount', 'The Re 1 FBR POS fee', 'The FBR invoice number, in the format FBR gives (for example 123456-141026103512-0001)',
                 'A QR code made from the FBR invoice number, so buyers can verify the bill', 'Buyer details when the rules ask for them']
anatomy = sec(' utp-alt', '', 'utp-anat-title',
              '      <div class="utp-split">\n        <figure class="utp-figure utp-figure-img">\n'
              + f'          <img src="{UP}uptrendpos-fbr-pos-invoice-qr.webp" width="1200" height="900" loading="lazy" decoding="async" alt="Sample FBR invoice from UpTrendPos with QR code and FBR invoice number">\n'
              + '        </figure>\n        <div>\n'
              + head('The FBR bill', 'utp-anat-title', 'What prints on an FBR invoice from UpTrendPos', '', left=True)
              + '          <p class="utp-body">FBR asks for a set format on every bill from an integrated counter. UpTrendPos prints all of it on thermal receipts and A4 invoices:</p>\n          '
              + ul(receipt_items) + '\n        </div>\n      </div>\n')

modes = [('Practice', 'Learn the FBR bill layout and train your staff before your FBR details arrive', 'No. Practice bills are not FBR invoices. Do not hand them out as FBR bills.'),
         ('Sandbox', 'Test your real FBR details on FBR\'s test system', 'Only to FBR\'s test system, not to your real records'),
         ('Production', 'Your live FBR POS integration for every bill', 'Yes. Every bill is reported to FBR and gets its FBR number and QR')]
modesec = sec('', '', 'utp-modes-title',
              head('Three modes', 'utp-modes-title', 'Practice, Sandbox and Production modes',
                   'You choose the mode in FBR settings. Start safe, test properly, then go live with confidence.')
              + '      <div class="utp-cmp-box utp-vs-box">\n        <table class="utp-cmp utp-vs">\n          <caption class="utp-sr">FBR modes in UpTrendPos</caption>\n'
              + '          <thead><tr><th scope="col">Mode</th><th scope="col">Use it for</th><th scope="col" class="is-rec">Reported to FBR?</th></tr></thead>\n          <tbody>\n'
              + ''.join(f'            <tr><th scope="row">{a}</th><td>{b}</td><td class="is-rec">{c}</td></tr>\n' for a, b, c in modes)
              + '          </tbody>\n        </table>\n      </div>\n')

ready = ['NTN and STRN (sales tax registration)', 'POS registration number for each counter', 'POS terminal ID (TID) for each counter',
         'API token, and the API address if FBR gives one', 'Outlet address as registered in IRIS', 'Internet on every counter for live reporting']
who = sec(' utp-alt', '', 'utp-ready-title',
          head('Before you start', 'utp-ready-title', 'What you need for FBR POS integration', 'Keep these ready and the setup takes one short call.')
          + '      <div class="utp-duo">\n'
          + f'        <article class="utp-fgroup">\n          <div class="utp-fgroup-head">{ico("user", "b")}<h3>You keep ready</h3></div>\n          {ul(ready)}\n        </article>\n'
          + f'        <article class="utp-fgroup utp-fgroup-dark">\n          <div class="utp-fgroup-head">{ico("team", "y")}<h3>Our team does with you</h3></div>\n          '
          + ul(['Enters your FBR details in UpTrendPos', 'Tests your first bills in Sandbox', 'Switches you to Production', 'Checks your first live FBR bill and QR', 'Trains your cashiers on FBR bills and returns', 'Sets up every branch and counter'])
          + '\n          <p class="utp-fgroup-foot">Help in Urdu or English on WhatsApp, phone or screen share.</p>\n        </article>\n      </div>\n')

offline = sec('', '', 'utp-off-title',
              '      <div class="utp-split">\n        <div>\n'
              + head('Load-shedding', 'utp-off-title', 'FBR POS integration during load-shedding', '', left=True)
              + '          <p class="utp-body">Light and internet go off in every city. FBR rules allow for it: bills made during an outage must be marked as offline and sent to FBR within 24 hours after the system is back. If a shop stays cut off from FBR for too long, it can face action.</p>\n          '
              + ul(['Billing keeps running offline on Windows and Android', 'Offline bills are kept safe on the device', 'They are reported to FBR when the internet returns', 'Connect your counters as soon as the internet is back', 'Keep a UPS for the router so short power cuts do not stop reporting'])
              + '\n        </div>\n        <div class="utp-band utp-band-fbr">\n          <div>\n            <span class="utp-eyebrow">For buyers</span>\n            <h2>Buyers can check your bill</h2>\n'
              + '            <p>Every FBR bill has a QR code. Buyers scan it with FBR\'s Tax Asaan app to see that the bill was reported. A verified bill builds trust with your customers.</p>\n'
              + '            <p>The Re 1 POS fee is paid by the buyer, shown on the bill and paid to FBR with your monthly sales tax return.</p>\n          </div>\n        </div>\n      </div>\n')

inds = [('Supermarkets and marts', 'https://uptrendpos.com/industries/grocery-store-pos-software/', 'grocery-store-pos-software'),
        ('Pharmacy chains', 'https://uptrendpos.com/industries/pharmacy-pos-software/', 'pharmacy-pos-software'),
        ('Clothing brands in malls', 'https://uptrendpos.com/industries/clothing-store-pos-software/', 'clothing-store-pos-software'),
        ('Shoe stores', 'https://uptrendpos.com/industries/shoe-store-pos-software/', 'shoe-store-pos-software'),
        ('Electronics showrooms', 'https://uptrendpos.com/industries/electronics-store-pos-software/', 'electronics-store-pos-software'),
        ('Mobile shops with card machines', 'https://uptrendpos.com/industries/mobile-shop-pos-software/', 'mobile-shop-pos-software'),
        ('Cosmetics stores', 'https://uptrendpos.com/industries/cosmetics-store-pos-software/', 'cosmetics-store-pos-software'),
        ('Furniture showrooms', 'https://uptrendpos.com/industries/furniture-shop-pos-software/', 'furniture-shop-pos-software'),
        ('Jewellery shops', 'https://uptrendpos.com/industries/jewellery-shop-pos-software/', 'jewellery-shop-pos-software')]
indsec = sec(' utp-alt', '', 'utp-ind-title',
             head('Who needs it', 'utp-ind-title', 'Retailers who often need FBR POS integration',
                  'Tier-1 is about how you sell, not what you sell. These shops are often Tier-1 because they sit in malls, take cards or are part of a chain.')
             + '      <div class="utp-chips">\n' + ''.join(f'        <a href="{u}" data-page="{s}">{n}</a>\n' for n, u, s in inds)
             + '        <a href="https://uptrendpos.com/industries/" data-page="industries">All 30+ business types</a>\n      </div>\n')

vs = sec('', '', 'utp-vs-title',
         head('POS integration vs digital invoicing', 'utp-vs-title', 'FBR POS integration is not the same as digital invoicing',
              'People mix these two up. Here is the simple difference.')
         + '      <div class="utp-duo">\n'
         + f'        <article class="utp-fgroup">\n          <div class="utp-fgroup-head">{ico("counter", "g")}<h3>FBR POS integration</h3></div>\n          '
         + ul(['For Tier-1 retailers selling at the counter', 'Every sale is reported to FBR as it happens', 'Bill shows FBR invoice number, QR and Re 1 fee', 'Under section 3(9A) of the Sales Tax Act', 'This is what UpTrendPos does today']) + '\n        </article>\n'
         + f'        <article class="utp-fgroup">\n          <div class="utp-fgroup-head">{ico("tax", "b")}<h3>Digital invoicing</h3></div>\n          '
         + ul(['For sales tax registered businesses, mostly business-to-business', 'Invoices to other registered buyers are sent to FBR', 'Separate rules under section 23 of the Sales Tax Act', 'Meeting one does not cover the other', 'Ask us if your business needs both']) + '\n        </article>\n      </div>\n')

cmp_rows = [('Making a bill', 'Bill twice: once in your POS, once for FBR', 'Bill once, FBR number comes back on its own'),
            ('Re 1 POS fee', 'Added by hand, often missed', 'Added and shown on every FBR bill'),
            ('QR code', 'Separate printout or no QR', 'Printed on the same receipt'),
            ('Internet goes off', 'Billing often stops', 'Billing runs, bills reported later'),
            ('Stock and udhaar', 'Not connected to FBR bills', 'Same bill updates stock and khata'),
            ('More counters', 'Each one set up again and again', 'Each counter with its own FBR details'),
            ('Help', 'Call centre or no one', 'Our team on WhatsApp in Urdu or English')]
cmpsec = sec(' utp-alt', '', 'utp-cmp-title',
             head('Why UpTrendPos', 'utp-cmp-title', 'Separate FBR app vs built-in FBR POS integration',
                  'Many shops run their POS and their FBR reporting as two different things. That doubles the work and the mistakes.')
             + '      <div class="utp-cmp-box utp-vs-box">\n        <table class="utp-cmp utp-vs">\n          <caption class="utp-sr">Separate FBR app compared with UpTrendPos</caption>\n'
             + '          <thead><tr><th scope="col">At your counter</th><th scope="col">Separate FBR app</th><th scope="col" class="is-rec">UpTrendPos</th></tr></thead>\n          <tbody>\n'
             + ''.join(f'            <tr><th scope="row">{a}</th><td>{b}</td><td class="is-rec">{c}</td></tr>\n' for a, b, c in cmp_rows)
             + '          </tbody>\n        </table>\n      </div>\n')

plan = ('  <section class="utp-sec" aria-labelledby="utp-plan-title">\n    <div class="utp-wrap">\n      <div class="utp-strip">\n        <div>\n'
        '          <h2 id="utp-plan-title">FBR POS integration comes with Enterprise and Custom</h2>\n'
        '          <p>Enterprise suits a mart with up to 2 branches and 6 users. Custom suits up to 3 branches and 9 users. Both include FBR invoices, barcode labels and the audit trail.</p>\n'
        '        </div>\n        <a class="utp-btn utp-btn-brand" href="https://uptrendpos.com/pos-software-pricing/" data-track="fbr_plans">See plans and prices</a>\n      </div>\n    </div>\n  </section>\n\n')

faqs = [
    ('What is FBR POS integration?', 'FBR POS integration means your POS sends every sale to FBR as it happens. FBR sends back an invoice number, and your bill prints it with a QR code. It is required for Tier-1 retailers under the Sales Tax Act, 1990, so FBR can see retail sales in real time.'),
    ('Who must get FBR POS integration?', 'Tier-1 retailers must integrate. You are Tier-1 if any one test applies: part of a chain, shop in an air-conditioned mall, electricity bills over Rs 1.2 million a year, wholesaler-cum-retailer, card machine at the counter, high 236G or 236H tax, or notified by FBR.'),
    ('How do I get FBR POS integration with UpTrendPos?', 'Register in IRIS and get your POS details from FBR for each counter. Then enter them in UpTrendPos under FBR settings, test in Sandbox and switch to Production. Our team does the UpTrendPos part with you on WhatsApp and checks your first live bill.'),
    ('What is the Re 1 POS fee?', 'It is a service fee of one rupee on every invoice from an FBR-integrated counter. The buyer pays it, it is shown on the bill, and you pay it to FBR with your monthly sales tax return. UpTrendPos adds it to each FBR bill on its own.'),
    ('What happens if internet or light goes off?', 'You keep billing. Offline bills are kept on the device and reported to FBR when the internet is back. FBR rules say offline bills must reach FBR within 24 hours after the system is restored, so reconnect your counters as soon as you can.'),
    ('What is the penalty for not integrating?', 'The penalty is Rs 500,000 for the first default, then Rs 1 million, Rs 2 million and Rs 3 million for later defaults. A non-integrated Tier-1 retailer also loses 60% of adjustable input tax, and FBR can seal the shop. Check the latest rules on fbr.gov.pk.'),
    ('Is UpTrendPos approved by FBR?', 'UpTrendPos is POS software with FBR POS integration built in. It uses the official FBR system with the details FBR gives you, and FBR rules route integration through a licensed integrator such as PRAL. We do not claim to be FBR or an FBR department.'),
    ('How can my customer check an FBR bill?', 'The customer scans the QR code on the bill with FBR\'s Tax Asaan app. The app shows whether the invoice was reported to FBR. This builds trust, because the buyer can see that the sales tax on the bill is real and recorded.'),
    ('How much does FBR POS integration cost?', 'It is included in the UpTrendPos Enterprise and Custom plans. FBR does not charge for integration itself, and PRAL offers its integration service free. See the <a href="https://uptrendpos.com/pos-software-pricing/">pricing page</a> for plan prices and a 14-day free trial.'),
    ('Can I use FBR on more than one counter or branch?', 'Yes. Register every counter in IRIS, then add each counter\'s FBR details in UpTrendPos. Each branch keeps its own stock and FBR setup, and the owner sees all branches from one account. Branch and user limits depend on your plan.'),
    ('I am not Tier-1. Do I need this?', 'Not for the Tier-1 rule. But if you are registered for sales tax, other FBR rules such as digital invoicing may apply to you. You can also turn on the Local GST line to show sales tax on bills without FBR reporting. Ask us what fits your shop.'),
]
faqsec = sec(' utp-alt', 'utp-faq', 'utp-faq-title',
             head('FAQ', 'utp-faq-title', 'FBR POS integration questions')
             + '      <div class="utp-faq-list">\n'
             + ''.join(f'        <details{" open" if n == 0 else ""}>\n          <summary>{q}</summary>\n          <p>{a}</p>\n        </details>\n' for n, (q, a) in enumerate(faqs))
             + '      </div>\n')

final = f'''  <section class="utp-final" aria-labelledby="utp-final-title">
    <div class="utp-wrap">
      <div class="utp-final-box">
        <h2 id="utp-final-title">Get FBR POS integration set up this week</h2>
        <p>Send us your Tier-1 result or your FBR details on WhatsApp. We set up UpTrendPos with you, test in Sandbox and check your first live FBR bill.</p>
        <div class="utp-cta">
          <a class="utp-btn utp-btn-primary" href="{wa('Hi, I want FBR POS integration with UpTrendPos')}" target="_blank" rel="noopener" data-track="fbr_final_whatsapp">{WA_SVG} Get FBR setup help</a>
          <a class="utp-btn utp-btn-ghost" href="https://live.uptrendpos.com/" target="_blank" rel="noopener" data-track="fbr_final_trial">Start 14-day free trial</a>
        </div>
        <div class="utp-contact">
          <a href="tel:+923192223292" data-track="fbr_final_call">Call 0319 2223292</a>
          <a href="mailto:sales@uptrendpos.com" data-track="fbr_final_email">sales@uptrendpos.com</a>
        </div>
        <p class="utp-final-note">UpTrendPos is a software company. We are not FBR and we do not give tax advice. FBR rules can change, so check <a href="https://www.fbr.gov.pk/" target="_blank" rel="noopener">fbr.gov.pk</a> or your tax advisor for your case.</p>
      </div>
    </div>
  </section>
'''

html = ('<div class="utp utp-fbr" id="utp-fbr-pos">\n\n' + hero + risk + checker + featsec + stepsec + anatomy + modesec + who + offline + indsec + vs + cmpsec + plan + faqsec + final + '</div>\n')
assert '<!--' not in html and '<style' not in html and '<script' not in html
(P / 'website_fbr_pos_integration_v1.html').write_text(html)
txt = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', re.sub(r'<svg.*?</svg>', '', html, flags=re.S)))
w = len(txt.split()); k = len(re.findall('FBR POS integration', txt, re.I))
print('words', w, 'kw', k, '%.2f%%' % (100 * k / w))
