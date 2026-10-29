"""Builds pages/website_grocery_v2.html from v1 (kept sections) + new full-depth sections."""
import re, pathlib
P = pathlib.Path('/home/claude/site/pages')
v1 = (P / 'website_grocery_v1.html').read_text()


def cut(start, end):
    a = v1.index(start); b = v1.index(end, a)
    return v1[a:b]


hero_ticker = cut('  <section class="utp-hero"', '  <nav class="utp-jump"')
usp = cut('  <section class="utp-sec utp-usp" id="utp-mobile"', '  <section class="utp-sec utp-alt" id="utp-setup"')
setup = cut('  <section class="utp-sec utp-alt" id="utp-setup"', '  <section class="utp-sec" aria-labelledby="utp-pain-title">')
offline = cut('  <section class="utp-sec utp-alt" aria-labelledby="utp-off-title">', '  <section class="utp-sec" id="utp-reports"')
reports = cut('  <section class="utp-sec" id="utp-reports"', '  <section class="utp-sec utp-alt" aria-labelledby="utp-fbr-title">')
plans = cut('  <section class="utp-sec" id="utp-plans"', '  <section class="utp-sec utp-alt" id="utp-faq"')
related_final = v1[v1.index('  <section class="utp-sec" aria-labelledby="utp-rel-title">'):]

# --- small edits to kept sections ---
hero_ticker = hero_ticker.replace(
    'UpTrendPos is grocery store POS software for kiryana shops and marts in Pakistan. Sell by carton, pack, piece or kg, keep every udhaar in a khata and get stock and expiry alerts. Start on your phone with a small Type-C printer, or on a PC. Billing keeps running when the internet is off.',
    'UpTrendPos is grocery store POS software for kiryana shops, general stores and marts in Pakistan. Sell by carton, pack, piece or kg, keep every udhaar in a khata and get stock and expiry alerts. Start on your phone with a small Type-C printer, or on a PC. Billing keeps running when the internet is off.')
offline = offline.replace('class="utp-sec utp-alt" aria-labelledby="utp-off-title"', 'class="utp-sec" aria-labelledby="utp-off-title"')
setup = setup.replace('class="utp-sec utp-alt" id="utp-setup"', 'class="utp-sec" id="utp-setup"')
reports = reports.replace('class="utp-sec" id="utp-reports"', 'class="utp-sec utp-alt" id="utp-reports"')
reports = reports.replace('        </ol>\n      </div>\n    </div>\n  </section>',
    '        </ol>\n        <p class="utp-more-h">More reports in the app</p>\n        <ul class="utp-mini-chips">\n'
    + ''.join(f'          <li>{x}</li>\n' for x in ['Sales history', 'Profit and loss', 'Monthly closing', 'Day book', 'Stock valuation', 'Batch and expiry', 'Expenses by category', 'Supplier payables', 'Cash sessions', 'Trial balance', 'Balance sheet', 'Cash flow'])
    + '        </ul>\n      </div>\n    </div>\n  </section>')
plans = plans.replace('class="utp-sec" id="utp-plans"', 'class="utp-sec utp-alt" id="utp-plans"')

ICON = {
    'bill': '<path d="M6 2h12v20l-3-2-3 2-3-2-3 2z"/><path d="M9 7h6M9 11h6M9 15h4"/>',
    'box': '<path d="M21 8l-9-5-9 5 9 5 9-5z"/><path d="M3 8v8l9 5 9-5V8M12 13v8"/>',
    'book': '<path d="M4 4h11a3 3 0 0 1 3 3v13H7a3 3 0 0 1-3-3z"/><path d="M8 8h6M8 12h6"/>',
    'truck': '<path d="M3 6h11v10H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    'chart': '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    'shield': '<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    'phone': '<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>',
    'printer': '<path d="M6 9V3h12v6"/><rect x="3" y="9" width="18" height="8" rx="2"/><path d="M7 14h10v7H7z"/>',
    'pc': '<rect x="2" y="4" width="20" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>',
    'scan': '<path d="M3 7V4h3M21 7V4h-3M3 17v3h3M21 17v3h-3M7 8v8M10 8v8M13 8v8M16 8v8"/>',
    'tag': '<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8.5" r="1.5"/>',
    'store': '<path d="M3 9l2-5h14l2 5"/><path d="M3 9h18v11H3zM9 20v-6h6v6"/>',
    'cart': '<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.5 12h11.5l2-8H6.2"/>',
    'branch': '<circle cx="6" cy="5" r="2"/><circle cx="6" cy="19" r="2"/><circle cx="18" cy="12" r="2"/><path d="M6 7v10M8 12h8"/>',
    'call': '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    'cash': '<rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18M7 15h3"/>',
    'clock': '<circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.5 2.5M9 2h6"/>',
    'qr': '<path d="M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h3v3h-3zM20 14v6h-3"/>',
}


def ico(name, cls, size='sm'):
    return (f'<div class="utp-ico {size} {cls}"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[name]}</svg></div>')


def plan(txt):
    return f' <em class="utp-ptag">{txt}</em>'


def ul(items, cls='utp-feat'):
    return f'<ul class="{cls}">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


def head(eyebrow, hid, h2, p, left=False):
    return (f'      <div class="utp-head{" left" if left else ""}">\n        <span class="utp-eyebrow">{eyebrow}</span>\n'
            f'        <h2 id="{hid}">{h2}</h2>\n' + (f'        <p>{p}</p>\n' if p else '') + '      </div>\n')


jump = '''  <nav class="utp-jump" aria-label="On this page">
    <div class="utp-wrap">
      <ul>
        <li><a href="#utp-problems">Problems</a></li>
        <li><a href="#utp-mobile">Phone billing</a></li>
        <li><a href="#utp-features">Features</a></li>
        <li><a href="#utp-hardware">Hardware</a></li>
        <li><a href="#utp-process">How it works</a></li>
        <li><a href="#utp-reports">Reports</a></li>
        <li><a href="#utp-faq">FAQ</a></li>
      </ul>
    </div>
  </nav>

'''

pains = [
    ('Udhaar gets lost in the register', 'Pages tear, names get mixed and customers argue about the total.', 'Every credit sale goes into the customer khata on its own.'),
    ('Long lines at rush hour', 'Writing and adding bills by hand is slow, so customers leave.', 'Scan or search, and the bill is ready in seconds.'),
    ('Stock expires on the shelf', 'Biscuits, oil and milk packs expire before anyone sees them.', 'Expiry alerts show what to sell first or return.'),
    ('Wrong prices and missing bills', 'Old rates, double billing and lost slips eat your profit.', 'One price list, and every bill is saved with its own number.'),
    ('Cash does not match', 'At night the drawer is short and nobody knows why.', 'Cash sessions show what each cashier collected.'),
    ('No idea of real profit', 'Sales look good, but expenses and udhaar hide the real number.', 'Profit, expenses and udhaar on one screen, every day.'),
]
problems = ('  <section class="utp-sec" id="utp-problems" aria-labelledby="utp-pain-title">\n    <div class="utp-wrap">\n'
            + head('The problems', 'utp-pain-title', 'Common problems kiryana store owners face without POS software',
                   'Running a grocery store in Pakistan is hard work. You sell hundreds of items, deal with daily rush, distributors, rate changes and udhaar. When all of this is on paper, mistakes happen every day. Good grocery store POS software fixes these problems first.')
            + '      <ul class="utp-pain c3">\n'
            + ''.join(f'        <li>\n          <span class="utp-tag">The problem</span>\n          <h3>{h}</h3>\n          <p>{p}</p>\n          <p class="utp-fix">{f}</p>\n        </li>\n' for h, p, f in pains)
            + '      </ul>\n    </div>\n  </section>\n\n')

caps = [
    ('bill', 'b', 'Make fast, correct bills', ['Bill a full trolley in seconds at rush hour', 'Right price every time, no calculator', 'Print it or send it on WhatsApp']),
    ('box', 'g', 'See your stock live', ['Stock goes down with every sale', 'Stock goes up when goods arrive', 'Alerts before items run out or expire']),
    ('book', 'y', 'Keep every udhaar safe', ['Credit sales go to the khata on their own', 'Take full or part payments', 'Send the statement on WhatsApp']),
    ('truck', 't', 'Handle suppliers and purchases', ['Purchase orders and goods received', 'What you owe each distributor', 'Returns to the supplier on record']),
    ('chart', 'n', 'Know your daily profit', ['Sales, expenses and profit for the day', 'This week and this month side by side', 'Reports on your phone, anywhere']),
    ('branch', 'b', 'Grow to more counters and branches', ['Staff logins for every cashier', 'Each branch keeps its own stock', 'The owner sees everything in one account']),
]
capsec = ('  <section class="utp-sec utp-alt" aria-labelledby="utp-cap-title">\n    <div class="utp-wrap">\n'
          + head('With UpTrendPos', 'utp-cap-title', 'What you can do with our grocery store POS software',
                 'UpTrendPos is complete grocery store POS software made for Pakistani shops. Billing, stock, udhaar, purchases and accounts are all connected, so you enter each thing only once.')
          + '      <div class="utp-fgrid">\n'
          + ''.join(f'        <article class="utp-fcard">\n          {ico(i, c)}\n          <h3>{h}</h3>\n          {ul(l, "utp-feat sm")}\n        </article>\n' for i, c, h, l in caps)
          + '      </div>\n    </div>\n  </section>\n\n')

groups = [
    ('bill', 'b', 'Billing at the counter', [
        'Barcode scanning with any USB scanner', 'Search items by name in a few letters', 'Sell by carton, pack, piece or kg',
        'Discount on the bill', 'Cash, bank or udhaar payment', 'Thermal receipt or A4 invoice with your logo',
        'Bill on WhatsApp as a picture or PDF', 'Returns and bill edits keep the same invoice number']),
    ('box', 'g', 'Stock and inventory', [
        'Live stock that moves with every sale and purchase', 'Low stock and out of stock alerts', 'Expiring and expired item alerts',
        'Batch-wise stock and expiry report', 'Demand list of items to reorder', 'Damage, sample and stock audit entries',
        'Stock value at cost and at sale price', 'Categories, brands and units']),
    ('book', 'y', 'Udhaar khata and customers', [
        'Every credit sale goes to the customer ledger', 'Full or part payments, any time', 'Opening udhaar for your old customers',
        'Khata statement as PDF, print or WhatsApp', 'Udhaar age: 0-7, 8-15, 16-30 and 30+ days', 'Each customer\'s bills and payments in one place',
        'Installments (kist) for big items' + plan('Enterprise+')]),
    ('truck', 't', 'Suppliers and purchases', [
        'Supplier records and supplier ledger', 'Purchase order, goods received (GRN) and purchase invoice', 'Purchase returns to the supplier',
        'Supplier payments and balance due', 'Credit days per supplier and payable age', 'Print purchase orders and GRN on A4',
        'Average cost updates on its own, so profit stays right']),
    ('chart', 'n', 'Reports and accounts', [
        'Daily sales report and sales history', 'Profit dashboard' + plan('Enterprise+'), 'Profit and loss and monthly closing' + plan('Enterprise+'),
        'Expenses by category', 'Day book, trial balance and balance sheet', 'Cash flow, receivables and payables', 'Reports as PDF to save or share']),
    ('shield', 'g', 'Staff, branches and safety', [
        'Staff logins with their own access', 'Open and close cash sessions per shift', 'Cashier records of what each person collected',
        'Audit trail of deletes and changes' + plan('Enterprise+'), 'Period lock so closed days stay closed', 'Backup and restore',
        'More branches with their own stock and prices', 'Attendance, salary and staff commission' + plan('Custom')]),
]
featsec = ('  <section class="utp-sec" id="utp-features" aria-labelledby="utp-feat-title">\n    <div class="utp-wrap">\n'
           + head('Features', 'utp-feat-title', 'Grocery store POS software features, in full detail',
                  'Here is everything a kiryana store or mart gets in UpTrendPos. All of it is built and working in the app today. Choose Grocery and Kiryana when you sign up, and these tools open ready for your shop.')
           + '      <div class="utp-fgroups">\n'
           + ''.join(f'        <article class="utp-fgroup">\n          <div class="utp-fgroup-head">{ico(i, c)}<h3>{h}</h3></div>\n          {ul(l, "utp-checks")}\n        </article>\n' for i, c, h, l in groups)
           + '      </div>\n      <p class="utp-note"><em class="utp-ptag">Enterprise+</em> means Enterprise and Custom plans. Everything else is in every plan of our grocery store POS software. <a class="utp-link" href="https://uptrendpos.com/pos-software-pricing/" data-track="gro_feat_pricing">See what each plan includes</a></p>\n    </div>\n  </section>\n\n')

hw = [
    ('phone', 'g', 'Android phone', 'Start here. Billing, udhaar, stock and reports all run on the phone.'),
    ('printer', 'y', 'Small Type-C printer', 'Plugs into the phone with a USB Type-C cable and prints receipts.'),
    ('pc', 'b', 'Windows PC or laptop', 'Windows 10 or 11 for a busy counter with many items.'),
    ('bill', 't', '80mm receipt printer', 'A thermal printer by USB for the PC counter. No ink needed.'),
    ('scan', 'n', 'USB barcode scanner', 'Plug and play. Scan packed items and bill in seconds.'),
    ('tag', 'g', 'Barcode label printer', 'Print price stickers for loose and packed items.' + plan('Enterprise+')),
]
hwsec = ('  <section class="utp-sec utp-alt" id="utp-hardware" aria-labelledby="utp-hw-title">\n    <div class="utp-wrap">\n'
         + head('Hardware', 'utp-hw-title', 'Grocery store POS hardware you need to get started',
                'You do not need a costly branded machine. Our grocery store POS software works with common devices from any computer market in Pakistan. Start with a phone and add the rest when your shop grows.')
         + '      <div class="utp-split utp-hw-split">\n        <figure class="utp-figure utp-figure-img">\n'
         + '          <img src="https://uptrendpos.com/wp-content/uploads/uptrendpos-grocery-pos-hardware.webp" width="1200" height="900" loading="lazy" decoding="async" alt="Grocery store POS hardware for a kiryana shop: Android phone, Type-C receipt printer, Windows PC, 80mm thermal printer and barcode scanner">\n'
         + '        </figure>\n        <ul class="utp-hwlist">\n'
         + ''.join(f'          <li>{ico(i, c)}<div><h3>{h}</h3><p>{p}</p></div></li>\n' for i, c, h, p in hw)
         + '        </ul>\n      </div>\n      <p class="utp-note">Already have a printer or scanner? <a class="utp-link" href="https://wa.me/923192223292?text=Hi%2C%20will%20my%20printer%20and%20scanner%20work%20with%20UpTrendPos%3F" target="_blank" rel="noopener" data-track="gro_hw_check">Send us the model on WhatsApp</a> and we will tell you if it works with our grocery store POS software.</p>\n    </div>\n  </section>\n\n')

steps = [
    ('Buy stock', 'Make a purchase order. When goods arrive, save the GRN. Stock goes up and the supplier ledger updates.'),
    ('Sell at the counter', 'Scan or search the item, pick the unit (carton, pack, piece or kg) and choose cash or udhaar.'),
    ('Print or send the bill', 'Print a receipt, or send the bill on WhatsApp as a picture or PDF.'),
    ('Collect udhaar', 'When a customer pays, save the payment. The khata updates and you can send the new statement.'),
    ('See your profit', 'Sales, expenses and profit go into your accounts on their own. Check the day report at night.'),
]
procsec = ('  <section class="utp-sec" id="utp-process" aria-labelledby="utp-proc-title">\n    <div class="utp-wrap">\n'
           + head('How it works', 'utp-proc-title', 'How grocery store POS software works, from stock-in to profit',
                  'This is the full daily cycle of a kiryana store in our grocery store POS software. Each step feeds the next one, so stock, udhaar and accounts always match.')
           + '      <div class="utp-proc">\n        <figure class="utp-figure utp-figure-img">\n'
           + '          <img src="https://uptrendpos.com/wp-content/uploads/uptrendpos-grocery-pos-process.webp" width="1200" height="900" loading="lazy" decoding="async" alt="How kiryana store software works: buy stock, sell at the counter, print or send the bill, collect udhaar and see profit">\n'
           + '        </figure>\n        <ol class="utp-rep">\n'
           + ''.join(f'          <li><strong>{h}</strong><span>{p}</span></li>\n' for h, p in steps)
           + '        </ol>\n      </div>\n'
           + '      <p class="utp-note">Getting started with our grocery store POS software takes four steps: sign up, add your items, connect your printer and make your first bill. Send us your item list in Excel or a clear photo and our team helps you load it.</p>\n    </div>\n  </section>\n\n')

bens = [
    ('Faster checkout', 'Customers do not wait at rush hour, so fewer walk away.'),
    ('No udhaar forgotten', 'Every rupee of credit is on record with the date and the bill.'),
    ('Less money lost to expiry', 'You see expiring items in time to sell them first or return them.'),
    ('The right stock order', 'The demand list tells you what to buy before the shelf is empty.'),
    ('Cash that matches', 'Each shift has its own cash session, so shortages show up the same day.'),
    ('Real profit, every day', 'Sales, cost and expenses come together, so you know what you earned.'),
]
bensec = ('  <section class="utp-sec utp-alt" aria-labelledby="utp-ben-title">\n    <div class="utp-wrap">\n'
          + head('Benefits', 'utp-ben-title', 'Top benefits of UpTrendPos in your grocery store, every day',
                 'Small changes at the counter add up to real money by the end of the month. This is what shop owners get from grocery store POS software that fits their shop.')
          + '      <ol class="utp-rep c2">\n'
          + ''.join(f'        <li><strong>{h}</strong><span>{p}</span></li>\n' for h, p in bens)
          + '      </ol>\n    </div>\n  </section>\n\n')

sec_items = ['Each shop\'s data is kept separate from every other shop', 'Staff only see what their login allows',
             'Audit trail of deletes and changes' + plan('Enterprise+'), 'Period lock stops changes to closed days',
             'Backup and restore for your shop data', 'Bills save on the device first, then sync to your account']
fbr_items = ['FBR invoice number and QR code on each bill' + plan('Enterprise+'), 'Buyers can check the bill on the FBR verification site',
             'Add your FBR POS details once, then every bill is reported', 'The FBR POS service fee is added to the bill as the rule says',
             'Your shop name, logo and address on thermal or A4 invoices', 'Not on FBR POS? Keep it off and bill as normal']
duo = ('  <section class="utp-sec" aria-labelledby="utp-safe-title">\n    <div class="utp-wrap">\n'
       + head('Safety and FBR', 'utp-safe-title', 'Safe shop data and FBR-ready invoices',
              'Your sales, udhaar and supplier records are business secrets. Bigger stores also need FBR invoices. Our grocery store POS software takes care of both.')
       + '      <div class="utp-duo">\n'
       + f'        <article class="utp-fgroup">\n          <div class="utp-fgroup-head">{ico("shield", "g")}<h3>Your shop data stays yours</h3></div>\n          {ul(sec_items, "utp-checks")}\n        </article>\n'
       + f'        <article class="utp-fgroup utp-fgroup-dark">\n          <div class="utp-fgroup-head">{ico("qr", "y")}<h3>FBR-ready receipts for marts</h3></div>\n          {ul(fbr_items, "utp-checks")}\n'
       + '          <p class="utp-fgroup-foot">Read more about the <a href="https://uptrendpos.com/fbr-pos-integration/" data-page="fbr-pos-integration">FBR invoice and QR code on every receipt</a>, or the rules on the official <a href="https://fbr.gov.pk/" target="_blank" rel="noopener">Federal Board of Revenue website</a>.</p>\n        </article>\n'
       + '      </div>\n    </div>\n  </section>\n\n')

segs = [
    ('store', 'g', 'Small kiryana shop', 'Run the whole shop on a phone. Print with a Type-C printer or send bills on WhatsApp, and keep the udhaar khata.'),
    ('cart', 'b', 'General store and mini mart', 'Barcode billing, stock and expiry alerts, and a separate login for each helper at the counter.'),
    ('pc', 'n', 'Supermarket and departmental store', 'Many counters, cash sessions per shift, barcode labels and FBR invoices for a Tier-1 store.'),
    ('truck', 't', 'Wholesale kiryana', 'Sell by carton and bag, give quotations first, and keep udhaar for the shopkeepers you supply.'),
    ('branch', 'y', 'Grocery chain with branches', 'Each branch keeps its own stock and prices. The owner sees all branches from one account.'),
    ('call', 'g', 'Phone order and home delivery shop', 'Take the order on a call, send the bill on WhatsApp, and collect cash or add it to the khata.'),
]
segsec = ('  <section class="utp-sec utp-alt" aria-labelledby="utp-seg-title">\n    <div class="utp-wrap">\n'
          + head('Every grocery business', 'utp-seg-title', 'Grocery store POS software for every kind of grocery business',
                 'From a one-man kiryana shop in a street to a supermarket with many counters, UpTrendPos grocery store POS software fits the way you sell.')
          + '      <div class="utp-fgrid">\n'
          + ''.join(f'        <article class="utp-fcard">\n          {ico(i, c)}\n          <h3>{h}</h3>\n          <p>{p}</p>\n        </article>\n' for i, c, h, p in segs)
          + '      </div>\n    </div>\n  </section>\n\n')

faqs = [
    ('Which is the best grocery store POS software in Pakistan?',
     'The best grocery store POS software is the one that fits a kiryana counter. Check five things: it sells by pack, piece and kg, keeps udhaar, works offline, prints from a phone, and your staff find it easy. UpTrendPos does all five, and you can test it free for 14 days.'),
    ('Is UpTrendPos good for a small kiryana shop?',
     'Yes. A small shop can run the full system on one Android phone. Make bills, keep the udhaar khata and check stock on the phone. Add a small Type-C printer for paper receipts, or send bills on WhatsApp. You can move to a PC later without losing any data.'),
    ('Can I print receipts from my phone without a computer?',
     'Yes. Connect a small thermal receipt printer to your Android phone with a USB Type-C cable, make the bill and tap Print. No computer, laptop or tablet is needed. Message us before you buy a printer and we will tell you which one works well.'),
    ('I have no printer. How does my customer get a bill?',
     'Send the bill on WhatsApp. After the sale, tap Send and the bill goes to the customer as a picture or a PDF. You can also send khata statements to udhaar customers and share your day report from the same phone, with no printer at all.'),
    ('Does it work during load-shedding or without internet?',
     'Yes. Cash billing keeps running on the Windows and Android apps when the internet or light goes. Bills save on the device and sync on their own later, with no double entries. Udhaar sales need internet so that every device shows the same khata.'),
    ('Can I sell atta by bag and sugar by kg?',
     'Yes. Set the units for each item once, such as carton, pack, piece or kg. At the counter, pick the unit and type the quantity, like 2.5 kg. The bill and your stock both use the right unit, so the stock count stays correct.'),
    ('How does this kiryana store software keep udhaar?',
     'Every credit sale goes into that customer\'s khata on its own. You see the total each customer owes and how old the udhaar is. When they pay, save a full or part payment and send the updated statement on WhatsApp, so there is no argument.'),
    ('Can it track expiry dates of grocery items?',
     'Yes. Add the expiry date when stock comes in. The dashboard shows expiring and expired items, and the batch-wise report lists each batch with its date. Sell the oldest stock first, or return it to the supplier before it becomes a loss.'),
    ('Does UpTrendPos support FBR invoices?',
     'Yes, on the Enterprise and Custom plans. If your store is registered with FBR for POS, add your FBR details once. Each bill then prints an FBR invoice number and a QR code that buyers can check. Shops not on FBR POS can keep it off.'),
    ('How much does grocery store POS software cost?',
     'It depends on your plan. Premium suits one shop, Enterprise suits a busy mart and Custom suits two or three branches. You can pay monthly or yearly, and every new shop gets a 14-day free trial first. See all prices on our <a href="https://uptrendpos.com/pos-software-pricing/">pricing page</a>.'),
    ('Can I use more than one counter or branch?',
     'Yes. Add more counters with separate staff logins, and each branch keeps its own stock and prices. The owner sees every counter and branch from one account. Branch and user limits depend on your plan, and we can quote for more.'),
]
faqsec = ('  <section class="utp-sec" id="utp-faq" aria-labelledby="utp-faq-title">\n    <div class="utp-wrap">\n'
          + head('FAQ', 'utp-faq-title', 'Grocery store POS software questions', '')
          + '      <div class="utp-faq-list">\n'
          + ''.join(f'        <details{" open" if n == 0 else ""}>\n          <summary>{q}</summary>\n          <p>{a}</p>\n        </details>\n' for n, (q, a) in enumerate(faqs))
          + '      </div>\n    </div>\n  </section>\n\n')

related_final = related_final.replace('<section class="utp-sec" aria-labelledby="utp-rel-title">', '<section class="utp-sec utp-alt" aria-labelledby="utp-rel-title">')

html = ('<div class="utp utp-gro" id="utp-grocery">\n\n' + hero_ticker + jump + problems + usp + capsec + featsec + hwsec + setup
        + procsec + offline.replace('class="utp-sec" aria-labelledby="utp-off-title"', 'class="utp-sec utp-alt" aria-labelledby="utp-off-title"')
        + bensec.replace('class="utp-sec utp-alt" aria-labelledby="utp-ben-title"', 'class="utp-sec" aria-labelledby="utp-ben-title"')
        + reports + duo + segsec + plans.replace('class="utp-sec utp-alt" id="utp-plans"', 'class="utp-sec" id="utp-plans"')
        + faqsec.replace('class="utp-sec" id="utp-faq"', 'class="utp-sec utp-alt" id="utp-faq"')
        + related_final.replace('class="utp-sec utp-alt" aria-labelledby="utp-rel-title"', 'class="utp-sec" aria-labelledby="utp-rel-title"'))
(P / 'website_grocery_v2.html').write_text(html)
print('ok', len(html))

# alternate backgrounds strictly: problems alt, usp plain, then toggle
html = (P / 'website_grocery_v2.html').read_text()
state = {'alt': True}
def fix(m):
    cls = m.group(1).replace(' utp-alt', '')
    if 'utp-usp' in cls:
        state['alt'] = True
        return f'<section class="{cls}"'
    out = cls + (' utp-alt' if state['alt'] else '')
    state['alt'] = not state['alt']
    return f'<section class="{out}"'
html = re.sub(r'<section class="(utp-sec[^"]*)"', fix, html)
(P / 'website_grocery_v2.html').write_text(html)
print(re.findall(r'<section class="(utp-sec[^"]*)"', html))

# --- 14 Oct: ~7,000-product grocery catalog (confirmed by Abdul) ---
html = (P / 'website_grocery_v2.html').read_text()
TK = re.search(r'<li><span class="utp-tk-ic">.*?</span>', html).group(0)
edits = [
    ('kiryana shops, general stores and marts in Pakistan. Sell by carton,',
     'kiryana shops, general stores and marts in Pakistan. Start with about 7,000 grocery products already loaded. Sell by carton,'),
    ('<ul class="utp-mq-track">\n', '<ul class="utp-mq-track">\n        ' + TK + '7,000 products ready</li>\n'),
    ('<ul class="utp-checks"><li>Live stock that moves with every sale and purchase</li>',
     '<ul class="utp-checks"><li>Ready catalog of about 7,000 grocery products</li><li>Live stock that moves with every sale and purchase</li>'),
    ('        <details>\n          <summary>Can I print receipts from my phone without a computer?</summary>',
     '        <details>\n          <summary>Do I need to enter all my grocery products myself?</summary>\n          <p>No. UpTrendPos comes with a catalog of about 7,000 grocery products. Search, pick the items you sell and add them to your shop. Then set your own prices and stock when goods arrive. Missing an item? Add it yourself in a minute.</p>\n        </details>\n'
     '        <details>\n          <summary>Can I print receipts from my phone without a computer?</summary>'),
]
for a, b in edits:
    assert html.count(a) == 1, a
    html = html.replace(a, b)
(P / 'website_grocery_v2.html').write_text(html)
t = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', re.sub(r'<svg.*?</svg>', '', html, flags=re.S)))
w = len(t.split()); k = len(re.findall('grocery store POS software', t, re.I))
print('grocery words', w, 'kw', k, '%.2f%%' % (100 * k / w), 'faqs', html.count('<summary>'))
