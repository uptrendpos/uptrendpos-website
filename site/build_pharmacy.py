"""Builds pages/website_pharmacy_v1.html (industry template v3, same structure as grocery v2, pharmacy-only content)."""
import pathlib, re
from build_fbr import ico as _ico, ICON, ul, head, wa, WA_SVG, UP
P = pathlib.Path('/home/claude/site/pages')
ICON.update({
    'pill': '<rect x="3" y="9" width="18" height="6" rx="3" transform="rotate(-45 12 12)"/><path d="M8.5 8.5l7 7"/>',
    'search': '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.5-4.5"/>',
    'clock': '<circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.5 2.5M9 2h6"/>',
    'truck': '<path d="M3 6h11v10H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    'book': '<path d="M4 4h11a3 3 0 0 1 3 3v13H7a3 3 0 0 1-3-3z"/><path d="M8 8h6M8 12h6"/>',
    'chart': '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    'bill': '<path d="M6 2h12v20l-3-2-3 2-3-2-3 2z"/><path d="M9 7h6M9 11h6M9 15h4"/>',
    'rx': '<path d="M5 3h6a4 4 0 0 1 0 8H5zM5 11v10M9 11l10 10M19 13l-6 6"/>',
    'rack': '<path d="M4 3v18M20 3v18M4 8h16M4 14h16M4 20h16"/>',
    'store': '<path d="M3 9l2-5h14l2 5"/><path d="M3 9h18v11H3zM9 20v-6h6v6"/>',
    'hosp': '<rect x="3" y="4" width="18" height="17" rx="2"/><path d="M12 8v8M8 12h8"/>',
    'leaf': '<path d="M5 21c0-9 6-15 16-16-1 10-7 16-16 16zM5 21l8-8"/>',
    'printer': '<path d="M6 9V3h12v6"/><rect x="3" y="9" width="18" height="8" rx="2"/><path d="M7 14h10v7H7z"/>',
    'pc': '<rect x="2" y="4" width="20" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>',
    'scan': '<path d="M3 7V4h3M21 7V4h-3M3 17v3h3M21 17v3h-3M7 8v8M10 8v8M13 8v8M16 8v8"/>',
    'tag': '<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8.5" r="1.5"/>',
})
ico = _ico


def plan(txt):
    return f' <em class="utp-ptag">{txt}</em>'


def section(cls, sid, hid, inner):
    idattr = f' id="{sid}"' if sid else ''
    return f'  <section class="utp-sec{cls}"{idattr} aria-labelledby="{hid}">\n    <div class="utp-wrap">\n{inner}    </div>\n  </section>\n\n'


TICK = '<span class="utp-tk-ic"><svg width="14" height="14" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 10.5l3.2 3.2L15 6.8"/></svg></span>'

hero = f'''  <section class="utp-hero" aria-labelledby="utp-h1">
    <div class="utp-wrap utp-hero-grid">
      <div class="utp-hero-copy">
        <nav class="utp-crumb" aria-label="Breadcrumb">
          <ol>
            <li><a href="https://uptrendpos.com/">Home</a></li>
            <li><a href="https://uptrendpos.com/industries/" data-page="industries">Industries</a></li>
            <li><span aria-current="page">Pharmacy &amp; Medical Store</span></li>
          </ol>
        </nav>
        <p class="utp-kicker">Pharmacy &amp; medical store</p>
        <h1 id="utp-h1">Pharmacy POS software for <span class="utp-hl">medical stores.</span></h1>
        <p class="utp-lead">UpTrendPos is pharmacy POS software for medical stores in Pakistan. Pick from 17,000+ medicines already loaded, search by salt or brand, sell by box, strip or tablet, and get batch and expiry alerts. Billing keeps running when the internet is off.</p>
        <div class="utp-cta">
          <a class="utp-btn utp-btn-primary" href="https://live.uptrendpos.com/" target="_blank" rel="noopener" data-track="ph_hero_trial">Start 14-day free trial</a>
          <a class="utp-btn utp-btn-ghost" href="{wa('Hi, I want a free demo of UpTrendPos for my medical store')}" target="_blank" rel="noopener" data-track="ph_hero_whatsapp"><svg width="20" height="20" viewBox="0 0 24 24" fill="#25D366" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2z"/></svg> Free pharmacy demo</a>
        </div>
        <p class="utp-smart-note">Medicine catalog in every plan · Demo in Urdu or English</p>
        <ul class="utp-ticks">
          <li>17,000+ medicines loaded</li>
          <li>Batch and expiry alerts</li>
          <li>Works offline</li>
        </ul>
      </div>
      <figure class="utp-hero-img">
        <img src="{UP}uptrendpos-pharmacy-pos-software.webp" width="1200" height="900" fetchpriority="high" decoding="async" alt="Pharmacy POS software at a medical store counter: medicines with pack, batch and expiry, Rx badges, receipt printer, scanner and expiry alerts on phone">
      </figure>
    </div>
  </section>

  <div class="utp-ticker" aria-label="Pharmacy highlights">
    <div class="utp-marquee">
      <ul class="utp-mq-track">
''' + ''.join(f'        <li>{TICK}{x}</li>\n' for x in ['17,000+ medicines loaded', 'Search by salt or brand', 'Box, strip or tablet', 'Batch and expiry alerts', 'Rx and controlled checks', 'Rack number on every item', 'Bills on WhatsApp', 'FBR invoice and QR']) + '''      </ul>
    </div>
  </div>

  <nav class="utp-jump" aria-label="On this page">
    <div class="utp-wrap">
      <ul>
        <li><a href="#utp-problems">Problems</a></li>
        <li><a href="#utp-catalog">Medicine catalog</a></li>
        <li><a href="#utp-features">Features</a></li>
        <li><a href="#utp-hardware">Hardware</a></li>
        <li><a href="#utp-process">How it works</a></li>
        <li><a href="#utp-reports">Reports</a></li>
        <li><a href="#utp-faq">FAQ</a></li>
      </ul>
    </div>
  </nav>

'''

pains = [('Typing thousands of medicines', 'A new medical store can spend weeks entering medicine names by hand. Most pharmacy software in Pakistan starts you with an empty list.', 'Pick from 17,000+ medicines already loaded. Search, tick and add.'),
         ('Wrong strength given', 'Two strengths of one medicine look the same in a quick search.', 'Strength and form show on every search result, so the right one is picked.'),
         ('Expiry found too late', 'Syrups, drops and injections expire on the shelf before anyone checks.', 'Batch-wise expiry alerts show what expires in the next 30 days.'),
         ('Box, strip or tablet mix-up', 'Selling loose tablets from a strip breaks the stock count.', 'Set packing once, like 1 box = 10 strips. Sell any unit, stock stays right.'),
         ('Controlled medicine without a check', 'A busy counter can sell a controlled medicine without looking at the prescription.', 'Rx items show a red badge. Controlled items need a "prescription checked" tick.'),
         ('Medicine not found on the shelf', 'Helpers waste time looking through racks while the customer waits.', 'Every item keeps its rack number, shown right at billing.')]
problems = section(' utp-alt', 'utp-problems', 'utp-pain-title',
                   head('The problems', 'utp-pain-title', 'Common problems medical store owners face without POS software',
                        'A medical store sells thousands of items with batches, expiry dates and strict rules. Paper registers and simple billing apps cannot keep up. Good pharmacy POS software fixes these problems first.')
                   + '      <ul class="utp-pain c3">\n'
                   + ''.join(f'        <li>\n          <span class="utp-tag">The problem</span>\n          <h3>{h}</h3>\n          <p>{p}</p>\n          <p class="utp-fix">{f}</p>\n        </li>\n' for h, p, f in pains)
                   + '      </ul>\n')

usp = f'''  <section class="utp-sec utp-usp" id="utp-catalog" aria-labelledby="utp-cat-title">
    <div class="utp-wrap">
      <div class="utp-head">
        <span class="utp-eyebrow">Ready on day one</span>
        <h2 id="utp-cat-title">17,000+ medicines already loaded in our pharmacy POS software</h2>
        <p>The hardest part of starting a medical store system is entering the medicines. With UpTrendPos you skip it. The medicine catalog comes with every plan.</p>
      </div>

      <div class="utp-usp-row">
        <figure class="utp-figure utp-figure-img">
          <img src="{UP}uptrendpos-pharmacy-medicine-catalog.webp" width="1200" height="900" loading="lazy" decoding="async" alt="Medical store software medicine catalog: search paracetamol, tick the medicines you sell and add them to your pharmacy">
        </figure>
        <div class="utp-usp-copy">
          <span class="utp-num">1</span>
          <h3>Search, tick and add the medicines you sell</h3>
          <p>Type a medicine or salt name, tick the ones you keep, and add them to your pharmacy in one go. Each medicine comes with its form, strength and salt. Not in the list? Add your own product in a minute.</p>
          {ul(['17,000+ medicines in a global catalog, in every plan', 'Comes from the internet once, then works offline and online', 'You set your own price, stock, packing and rack when stock comes in', 'On the next order, your rack, alert level and settings come back as they were'], 'utp-feat')}
        </div>
      </div>

      <div class="utp-usp-row rev">
        <figure class="utp-figure utp-figure-img">
          <img src="{UP}uptrendpos-pharmacy-salt-search-expiry.webp" width="1200" height="900" loading="lazy" decoding="async" alt="Search medicines by salt to see every brand with strength and Rx badge, and batch-wise expiry alerts on phone">
        </figure>
        <div class="utp-usp-copy">
          <span class="utp-num">2</span>
          <h3>Search by salt, sell the right strength, catch expiry early</h3>
          <p>A customer asks for a salt, not a brand? Search the salt and see every brand you have, with strength, form and stock. Expiry alerts show each batch that will expire soon, so you sell it first or return it to the distributor.</p>
          {ul(['Search by medicine, salt, brand, batch or barcode', 'Strength and form chips on every result', 'Red Rx badge, and a prescription tick for controlled medicines', 'Batch-wise expiry list for the next 30 days'], 'utp-feat')}
        </div>
      </div>
    </div>
  </section>

'''

caps = [('pill', 'g', 'Start fast', ['Pick medicines from the catalog', 'No long data entry', 'Add your own items any time']),
        ('bill', 'b', 'Bill in seconds', ['Search by salt or brand', 'Sell by box, strip or tablet', 'Print or send the bill on WhatsApp']),
        ('clock', 'y', 'Stop expiry losses', ['Batch and expiry on every purchase', 'Oldest batch sells first', 'Alerts before items expire']),
        ('rx', 'n', 'Sell safely', ['Rx badge on prescription medicines', 'Prescription tick for controlled items', 'DRAP registration number on record']),
        ('truck', 't', 'Handle distributors', ['Purchase orders and stock received', 'Returns of expired stock', 'What you owe each distributor']),
        ('chart', 'g', 'Know your profit', ['Sales and profit every day', 'Stock value at cost', 'Reports on your phone'])]
capsec = section(' utp-alt', '', 'utp-cap-title',
                 head('With UpTrendPos', 'utp-cap-title', 'What you can do with our pharmacy POS software',
                      'UpTrendPos is complete pharmacy POS software made for Pakistani medical stores. The catalog, billing, batches, purchases and accounts all work together.')
                 + '      <div class="utp-fgrid">\n'
                 + ''.join(f'        <article class="utp-fcard">\n          {ico(i, c)}\n          <h3>{h}</h3>\n          {ul(l, "utp-feat sm")}\n        </article>\n' for i, c, h, l in caps)
                 + '      </div>\n')

groups = [
    ('pill', 'g', 'Medicine catalog and product details', ['17,000+ medicine global catalog in every plan', 'Add your own medicines and products', 'Dosage form, strength and generic salt', 'Rx status, age group and therapeutic class', 'DRAP registration number field', '16 product types: tablets, syrups, injections, cold-chain, surgical, devices and more', 'Add your own options to any dropdown']),
    ('bill', 'b', 'Billing at the counter', ['Search by medicine, salt, brand, batch or barcode', 'Strength and form shown on search results', 'Sell by box, strip or tablet', 'Hold a bill and serve the next customer', 'Quick bill and calculator on the counter', 'Cash, bank or udhaar payment', 'Thermal receipt or A4 invoice, or send on WhatsApp', 'Returns and bill edits keep the same invoice number']),
    ('clock', 'y', 'Batch, expiry and stock', ['Batch number and expiry date on every purchase', 'Oldest expiry sells first (FEFO)', 'Expiring in 30 days and expired alerts', 'Rack or shelf number on every item', 'Low stock alert level per item', 'Demand list of what to reorder', 'Damage, expired and stock audit entries', 'Stock value at cost and sale price']),
    ('truck', 't', 'Distributors and purchases', ['Purchase order, goods received (GRN) and purchase invoice', 'Packing per purchase, like 1 box = 10 strips', 'Return expired or damaged stock to the distributor', 'Distributor ledger and balance due', 'Credit days and payable age per distributor', 'Print purchase orders and GRN on A4', 'Average cost updates on its own, so profit stays right']),
    ('book', 'n', 'Customers and udhaar', ['Khata for regular customers and patients', 'Credit accounts for clinics and doctors you supply', 'Full or part payments, any time', 'Khata statement as PDF, print or WhatsApp', 'Udhaar age: 0-7, 8-15, 16-30 and 30+ days', 'Customer bills and payments in one place']),
    ('shield', 'b', 'Reports, staff and safety', ['Daily sales report and sales history', 'Profit dashboard and profit and loss' + plan('Enterprise+'), 'Batch-wise stock and expiry report', 'Staff logins and cash sessions per shift', 'Audit trail of deletes and changes' + plan('Enterprise+'), 'More branches with their own stock', 'Backup and restore']),
]
featsec = section('', 'utp-features', 'utp-feat-title',
                  head('Features', 'utp-feat-title', 'Pharmacy POS software features, in full detail',
                       'Here is everything a medical store or pharmacy gets in UpTrendPos. All of it is built and working in the app today. Choose Pharmacy when you sign up and these tools open ready for you.')
                  + '      <div class="utp-fgroups">\n'
                  + ''.join(f'        <article class="utp-fgroup">\n          <div class="utp-fgroup-head">{ico(i, c)}<h3>{h}</h3></div>\n          {ul(l, "utp-checks")}\n        </article>\n' for i, c, h, l in groups)
                  + '      </div>\n      <p class="utp-note"><em class="utp-ptag">Enterprise+</em> means Enterprise and Custom plans. Everything else is in every plan of our pharmacy POS software. <a class="utp-link" href="https://uptrendpos.com/pos-software-pricing/" data-track="ph_feat_pricing">See what each plan includes</a></p>\n')

hw = [('pc', 'b', 'Windows PC or laptop', 'For the main counter with many medicines and fast billing.'),
      ('phone', 'g', 'Android phone', 'For a small medical store, or for the owner to check sales and expiry from home.'),
      ('bill', 't', '80mm receipt printer', 'A thermal printer by USB for the counter. No ink needed.'),
      ('printer', 'y', 'Small Type-C printer', 'Plugs into the phone with a USB Type-C cable to print receipts.'),
      ('scan', 'n', 'USB barcode scanner', 'Scan the barcode on the medicine box and bill in seconds.'),
      ('tag', 'g', 'Barcode label printer', 'Print stickers for items that have no barcode.' + plan('Enterprise+'))]
hwsec = section(' utp-alt', 'utp-hardware', 'utp-hw-title',
                head('Hardware', 'utp-hw-title', 'Pharmacy POS hardware you need',
                     'You do not need costly machines. Our pharmacy POS software works with common devices from any computer market in Pakistan. Start with what you have.')
                + '      <div class="utp-split utp-hw-split">\n        <figure class="utp-figure utp-figure-img">\n'
                + f'          <img src="{UP}uptrendpos-pharmacy-pos-hardware.webp" width="1200" height="900" loading="lazy" decoding="async" alt="Pharmacy POS hardware: Windows PC, barcode scanner, receipt printer, owner phone and cold-chain items">\n'
                + '        </figure>\n        <ul class="utp-hwlist">\n'
                + ''.join(f'          <li>{ico(i, c)}<div><h3>{h}</h3><p>{p}</p></div></li>\n' for i, c, h, p in hw)
                + '        </ul>\n      </div>\n      <p class="utp-note">Already have a printer or scanner? <a class="utp-link" href="' + wa('Hi, will my printer and scanner work with UpTrendPos for my pharmacy?') + '" target="_blank" rel="noopener" data-track="ph_hw_check">Send us the model on WhatsApp</a> and we will check it.</p>\n')

steps = [('Pick your medicines', 'Search the 17,000+ catalog, tick the medicines you sell and add them. Add any missing product yourself.'),
         ('Receive stock', 'Save the GRN from your distributor with batch, expiry, packing, rack, cost and sale price.'),
         ('Sell at the counter', 'Search by salt or brand, choose box, strip or tablet, and check the Rx badge before you save.'),
         ('Watch the alerts', 'See expiring batches, low stock and the demand list. Return expired stock to the distributor.'),
         ('See your profit', 'Sales, cost and expenses go into your accounts on their own. Check the day report at night.')]
procsec = section('', 'utp-process', 'utp-proc-title',
                  head('How it works', 'utp-proc-title', 'How pharmacy POS software works, from catalog to profit',
                       'This is the full daily cycle of a medical store in UpTrendPos pharmacy POS software. Each step feeds the next, so batches, stock and accounts always match.')
                  + '      <div class="utp-proc">\n        <figure class="utp-figure utp-figure-img">\n'
                  + f'          <img src="{UP}uptrendpos-pharmacy-pos-process.webp" width="1200" height="900" loading="lazy" decoding="async" alt="How medical store software works: pick medicines, receive stock, sell fast, get alerts and see profit">\n'
                  + '        </figure>\n        <ol class="utp-rep">\n'
                  + ''.join(f'          <li><strong>{h}</strong><span>{p}</span></li>\n' for h, p in steps)
                  + '        </ol>\n      </div>\n')

offline = section(' utp-alt', '', 'utp-off-title',
                  head('Load-shedding ready', 'utp-off-title', 'Keep your medical store billing during load-shedding',
                       'Medical stores stay open late, and many run 24 hours. Light and internet can go at any time. Our pharmacy POS software is built offline-first: bills save on your PC or phone and sync to your account when the internet is back.')
                  + '''      <div class="utp-sync-row">
        <div class="utp-node"><strong>Your counter</strong><span>Bills and stock save on the device, even offline</span></div>
        <span class="utp-arrow" aria-hidden="true"></span>
        <div class="utp-node cloud"><strong>Your account</strong><span>Sales sync when the internet is back</span></div>
        <span class="utp-arrow" aria-hidden="true"></span>
        <div class="utp-node"><strong>Owner's phone</strong><span>Check sales and expiry from home</span></div>
      </div>
      <p class="utp-sync-note">Cash bills work offline. Udhaar sales need internet, so the khata stays the same on every device.</p>
''')

bens = [('Faster counter', 'Salt search and strength chips cut the time to find the right medicine.'),
        ('Less expiry loss', 'You see expiring batches in time to sell them first or return them.'),
        ('Safer selling', 'Rx and controlled medicines are flagged before the bill is saved.'),
        ('Right stock, right time', 'Low stock alerts and the demand list make ordering simple.'),
        ('Fewer mistakes', 'Packing is set once, so box, strip and tablet sales never break stock.'),
        ('Real profit', 'Cost, sales and expenses come together, so you know what you earn.')]
bensec = section('', '', 'utp-ben-title',
                 head('Benefits', 'utp-ben-title', 'Top benefits of UpTrendPos for your medical store',
                      'Small changes at the counter save money every month. This is what pharmacy owners get from pharmacy POS software that fits the way they work.')
                 + '      <ol class="utp-rep c2">\n' + ''.join(f'        <li><strong>{h}</strong><span>{p}</span></li>\n' for h, p in bens) + '      </ol>\n')

reports = section(' utp-alt', 'utp-reports', 'utp-rep-title',
                  head('Reports', 'utp-rep-title', 'Reports a pharmacy owner checks every day',
                       'Our pharmacy POS software keeps these reports ready. Check them from the counter or from home. Send any report to yourself or your partner on WhatsApp.')
                  + '      <ol class="utp-rep c2">\n'
                  + '        <li><strong>Sales and profit today</strong><span>Bills, sales, profit and cash in the drawer, with this week and this month.</span></li>\n'
                  + '        <li><strong>Expiry by batch</strong><span>Every batch that expires in the next 30 days, and what has already expired.</span></li>\n'
                  + '        <li><strong>Low stock and demand list</strong><span>What is low, what is out, and what to order from each distributor.</span></li>\n'
                  + '        <li><strong>Distributor payables</strong><span>What you owe each distributor and how old each bill is.</span></li>\n'
                  + '      </ol>\n      <p class="utp-more-h">More reports in the app</p>\n      <ul class="utp-mini-chips">\n'
                  + ''.join(f'        <li>{x}</li>\n' for x in ['Sales history', 'Batch-wise stock', 'Stock valuation', 'Profit and loss', 'Monthly closing', 'Day book', 'Customer khata', 'Expenses by category', 'Cash sessions', 'Trial balance'])
                  + '      </ul>\n')

duo = section('', '', 'utp-safe-title',
              head('Safety, DRAP and FBR', 'utp-safe-title', 'Safe records, DRAP details and FBR-ready bills',
                   'Medicine records must be correct and safe. Bigger pharmacies and chains also need FBR invoices. Our pharmacy POS software handles both.')
              + '      <div class="utp-duo">\n'
              + f'        <article class="utp-fgroup">\n          <div class="utp-fgroup-head">{ico("shield", "g")}<h3>Correct and safe records</h3></div>\n          '
              + ul(['Each shop\'s data is kept separate from every other shop', 'Staff only see what their login allows', 'DRAP registration number saved on each medicine', 'Batch and expiry kept from purchase to sale', 'Audit trail of deletes and changes' + plan('Enterprise+'), 'Backup and restore for your shop data'])
              + '\n          <p class="utp-fgroup-foot utp-light">Check medicine registration rules on the <a href="https://www.dra.gov.pk/" target="_blank" rel="noopener">Drug Regulatory Authority of Pakistan</a> website.</p>\n        </article>\n'
              + f'        <article class="utp-fgroup utp-fgroup-dark">\n          <div class="utp-fgroup-head">{ico("qr", "y")}<h3>FBR-ready bills for pharmacy chains</h3></div>\n          '
              + ul(['FBR invoice number and QR code on each bill' + plan('Enterprise+'), 'Re 1 FBR POS fee added on its own', 'Each counter with its own FBR details', 'Billing keeps running offline, reported later', 'Not on FBR POS? Keep it off and bill as normal'])
              + '\n          <p class="utp-fgroup-foot">See how <a href="https://uptrendpos.com/fbr-pos-integration/" data-page="fbr-pos-integration">FBR POS integration works in UpTrendPos</a>.</p>\n        </article>\n      </div>\n')

segs = [('store', 'g', 'Retail medical store', 'One counter, fast salt search, expiry alerts and a khata for regular customers.'),
        ('branch', 'b', 'Pharmacy chain', 'Each branch with its own stock and batches, FBR bills, and one owner view.'),
        ('hosp', 'n', 'Hospital or clinic pharmacy', 'Busy counter, Rx and controlled checks, and credit accounts for departments or doctors.'),
        ('truck', 't', 'Medicine distributor counter', 'Sell by box and carton, and keep udhaar for the pharmacies you supply.'),
        ('leaf', 'y', 'Herbal and homeopathic store', 'Use the herbal and homeopathic product type for these items.'),
        ('hosp', 'g', 'Surgical and medical devices', 'Surgical items, devices and test kits, each with its own product type.')]
segsec = section(' utp-alt', '', 'utp-seg-title',
                 head('Every pharmacy', 'utp-seg-title', 'Pharmacy POS software for every kind of medical business',
                      'From a small medical store near a clinic to a chain with many branches, UpTrendPos pharmacy POS software fits the way you work.')
                 + '      <div class="utp-fgrid">\n'
                 + ''.join(f'        <article class="utp-fcard">\n          {ico(i, c)}\n          <h3>{h}</h3>\n          <p>{p}</p>\n        </article>\n' for i, c, h, p in segs)
                 + '      </div>\n')

plans = section('', 'utp-plans', 'utp-plan-title',
                head('Plans', 'utp-plan-title', 'Which plan fits your pharmacy?', 'Every plan includes the 17,000+ medicine catalog and unlimited bills. Plans change by branches, users and a few advanced tools.')
                + '''      <div class="utp-fgrid">
        <article class="utp-fcard utp-fit">
          <p class="utp-fit-tag">Premium</p>
          <h3>One medical store</h3>
          <p>One branch and up to 3 users. Catalog, billing, batches, expiry, purchases, udhaar and accounts.</p>
        </article>
        <article class="utp-fcard utp-fit is-rec">
          <p class="utp-fit-tag">Enterprise</p>
          <h3>A busy pharmacy</h3>
          <p>Up to 2 branches and 6 users. Adds FBR invoices, barcode labels, profit reports and audit trail.</p>
        </article>
        <article class="utp-fcard utp-fit">
          <p class="utp-fit-tag">Custom</p>
          <h3>A pharmacy chain</h3>
          <p>Up to 3 branches and 9 users, with every module, including staff attendance, salary and commission.</p>
        </article>
      </div>
      <p class="utp-center"><a class="utp-btn utp-btn-brand" href="https://uptrendpos.com/pos-software-pricing/" data-track="ph_plans">Compare UpTrendPos plans</a></p>
''')

faqs = [
    ('Which is the best pharmacy POS software in Pakistan?', 'The best pharmacy POS software is the one built for a medical store counter. Check five things: medicines already loaded, salt search, batch and expiry alerts, box-strip-tablet selling and offline billing. UpTrendPos does all five, and you can test it free for 14 days.'),
    ('Do I need to type all medicines myself?', 'No. UpTrendPos has a global catalog of 17,000+ medicines in every plan. Search, tick the ones you sell and add them to your pharmacy. If a product is missing, add it yourself in a minute. You then set your own prices and stock.'),
    ('Does the medicine catalog include prices?', 'No. The catalog gives you medicine names, form, strength and salt. You set your own cost, sale price, stock, packing, rack and expiry when stock comes in through a GRN. On your next order, your saved rack and alert levels come back as they were.'),
    ('Can I search medicines by salt or generic name?', 'Yes. Type the salt and you see every brand you have with that salt, with strength, form and stock. You can also search by brand, batch or barcode. This helps when a customer asks for a cheaper brand of the same medicine.'),
    ('How does this medical store software track expiry?', 'Enter the batch and expiry date when stock comes in. The dashboard shows expiring and expired items, and the batch-wise report lists every batch with its date. The oldest batch sells first, and you can return expired stock to the distributor.'),
    ('Can I sell by box, strip and single tablet?', 'Yes. Set the packing when you buy, for example 1 box = 10 strips and 1 strip = 10 tablets. At the counter, sell a box, a strip or loose tablets. The bill and your stock both use the right unit, so the stock count stays correct.'),
    ('How are prescription and controlled medicines handled?', 'Prescription medicines show a red Rx badge on search and on the bill. Controlled medicines need the cashier to tick "prescription checked" before the bill can be saved. This keeps the counter fast while making sure the check is never skipped.'),
    ('Does it work during load-shedding?', 'Yes. Our pharmacy POS software keeps cash billing running on the Windows and Android apps when the internet or light goes. Bills save on the device and sync on their own later, with no double entries. Udhaar sales need internet so every device shows the same khata.'),
    ('Does UpTrendPos support FBR invoices for pharmacies?', 'Yes, on the Enterprise and Custom plans. If your pharmacy is a Tier-1 retailer, add your FBR details once. Each bill then prints an FBR invoice number, QR code and the Re 1 POS fee. Pharmacies not on FBR POS can keep it off.'),
    ('How much does pharmacy POS software cost?', 'It depends on your plan. Premium suits one medical store, Enterprise suits a busy pharmacy and Custom suits a small chain. Every plan includes the medicine catalog. Pay monthly or yearly after a 14-day free trial. See all prices on our <a href="https://uptrendpos.com/pos-software-pricing/">pricing page</a>.'),
    ('Can I run more than one counter or branch?', 'Yes. UpTrendPos pharmacy POS software lets you add counters with separate staff logins, and each branch keeps its own stock, batches and prices. The owner sees every branch from one account. Branch and user limits depend on your plan, and we can quote for more.'),
]
faqsec = section(' utp-alt', 'utp-faq', 'utp-faq-title',
                 head('FAQ', 'utp-faq-title', 'Pharmacy POS software questions')
                 + '      <div class="utp-faq-list">\n'
                 + ''.join(f'        <details{" open" if n == 0 else ""}>\n          <summary>{q}</summary>\n          <p>{a}</p>\n        </details>\n' for n, (q, a) in enumerate(faqs))
                 + '      </div>\n')

related = section('', '', 'utp-rel-title',
                  head('Related', 'utp-rel-title', 'Also selling these? See their setup')
                  + '''      <div class="utp-chips">
        <a href="https://uptrendpos.com/industries/veterinary-store-pos-software/" data-page="veterinary-store-pos-software">Veterinary Store</a>
        <a href="https://uptrendpos.com/industries/cosmetics-store-pos-software/" data-page="cosmetics-store-pos-software">Cosmetics &amp; Beauty Store</a>
        <a href="https://uptrendpos.com/industries/baby-store-pos-software/" data-page="baby-store-pos-software">Baby &amp; Diaper Store</a>
        <a href="https://uptrendpos.com/industries/grocery-store-pos-software/" data-page="grocery-store-pos-software">Grocery &amp; Kiryana Store</a>
        <a href="https://uptrendpos.com/industries/" data-page="industries">All 30+ business types</a>
      </div>
''')

final = f'''  <section class="utp-final" aria-labelledby="utp-final-title">
    <div class="utp-wrap">
      <div class="utp-final-box">
        <h2 id="utp-final-title">Try UpTrendPos in your medical store for 14 days</h2>
        <p>Pick your medicines from the catalog today and make your first bill, or message us and we will set it up with you. Simple pharmacy POS software, made for Pakistani medical stores.</p>
        <div class="utp-cta">
          <a class="utp-btn utp-btn-primary" href="https://live.uptrendpos.com/" target="_blank" rel="noopener" data-track="ph_final_trial">Start 14-day free trial</a>
          <a class="utp-btn utp-btn-ghost" href="https://uptrendpos.com/contact-us/" data-track="ph_final_contact">Book a free demo</a>
        </div>
        <div class="utp-contact">
          <a href="tel:+923192223292" data-track="ph_final_call">Call 0319 2223292</a>
          <a href="mailto:sales@uptrendpos.com" data-track="ph_final_email">sales@uptrendpos.com</a>
        </div>
      </div>
    </div>
  </section>
'''

setups = section('', 'utp-setup', 'utp-setup-title',
                 head('Your setup', 'utp-setup-title', 'Start small, grow when you are ready',
                      'Our pharmacy POS software works on a phone, a phone with a small printer, or a full counter PC. All use the same account.')
                 + f'''      <div class="utp-cards">
        <article class="utp-card">
          {ico('phone', 'g').replace('utp-ico sm', 'utp-ico')}
          <h3>Phone only</h3>
          <p class="utp-best">For a small medical store run by the owner</p>
          {ul(['Android phone with the UpTrendPos app', 'Bills on WhatsApp as a picture or PDF', 'Catalog, expiry alerts and day report'], 'utp-feat')}
        </article>
        <article class="utp-card is-rec">
          <span class="utp-rec">Easy first step</span>
          {ico('printer', 'y').replace('utp-ico sm', 'utp-ico')}
          <h3>Phone and Type-C printer</h3>
          <p class="utp-best">For a busy small store that needs receipts</p>
          {ul(['Everything in phone only', 'Small thermal printer by USB Type-C cable', 'Paper receipt for every customer'], 'utp-feat')}
        </article>
        <article class="utp-card">
          {ico('pc', 'b').replace('utp-ico sm', 'utp-ico')}
          <h3>Counter PC</h3>
          <p class="utp-best">For pharmacies with many items and staff</p>
          {ul(['Windows PC with the UpTrendPos app', 'USB barcode scanner and 80mm printer', 'Owner checks sales and expiry on the phone'], 'utp-feat')}
        </article>
      </div>
''')

def alt_pass(h):
    n = [0]
    def f(m):
        cls = m.group(1).replace(' utp-alt', '')
        n[0] += 1
        return '<section class="utp-sec' + cls + (' utp-alt' if n[0] % 2 else '') + '"'
    return re.sub(r'<section class="utp-sec([^"]*)"', f, h)


html = alt_pass('<div class="utp utp-gro utp-ph" id="utp-pharmacy">\n\n' + hero + problems + usp + capsec + featsec + hwsec + setups + procsec + offline + bensec + reports + duo + segsec + plans + faqsec + related + final + '</div>\n')
assert '<!--' not in html and '<style' not in html and '<script' not in html
(P / 'website_pharmacy_v1.html').write_text(html)
txt = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', re.sub(r'<svg.*?</svg>', '', html, flags=re.S)))
w = len(txt.split()); k = len(re.findall('pharmacy POS software', txt, re.I))
print('words', w, 'kw', k, '%.2f%%' % (100 * k / w))
