/* UpTrendPos Site Kit 1.2 - front-end script (header, hero stages, page tools, tracking) */
(function () {
  'use strict';

  var CFG = window.UTPK || {};
  var LIVE = CFG.live || [];
  var L = CFG.links || {};
  var MOTION = CFG.motion !== false;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }
  function push(o) { window.dataLayer = window.dataLayer || []; window.dataLayer.push(o); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  /* ================= Icons for the hero stages ================= */
  var I = {
    box: '<path d="M21 8l-9-5-9 5 9 5 9-5z"/><path d="M3 8v8l9 5 9-5V8M12 13v8"/>',
    clock: '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
    wa: '<path fill="currentColor" stroke="none" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.4.1-.6.3-.2.2-.8.8-.8 2s.8 2.3.9 2.5c.1.2 1.6 2.5 4 3.5 1.5.6 2 .7 2.8.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/>',
    bolt: '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
    book: '<path d="M4 4h11a3 3 0 0 1 3 3v13H7a3 3 0 0 1-3-3z"/><path d="M8 8h6M8 12h6"/>',
    qr: '<path d="M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h3v3h-3zM20 14v6h-3"/>',
    search: '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.5-4.5"/>',
    pill: '<rect x="3" y="8.5" width="18" height="7" rx="3.5" transform="rotate(-45 12 12)"/><path d="M9.5 9.5l5 5"/>',
    cal: '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    shield: '<path d="M12 3l7.5 3v5.5c0 4.5-3.2 8.2-7.5 9.5-4.3-1.3-7.5-5-7.5-9.5V6z"/><path d="M8.8 12l2.2 2.2 4.2-4.4"/>',
    scissors: '<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M8.1 8.1L20 20M8.1 15.9L20 4"/>',
    ruler: '<path d="M3 17L17 3l4 4L7 21z"/><path d="M7 13l2 2M10 10l2 2M13 7l2 2"/>',
    doc: '<path d="M6 2h9l5 5v15H6z"/><path d="M14 2v6h6M9 13h8M9 17h6"/>',
    sync: '<path d="M19.5 8A8 8 0 0 0 5 7.5M4.5 16a8 8 0 0 0 14.5.5"/><path d="M19.5 3.5V8H15M4.5 20.5V16H9"/>',
    check: '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    star: '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
    pin: '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    users: '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17.5" cy="9" r="2.5"/><path d="M16 14.2a5 5 0 0 1 5.5 5.8"/>',
    layers: '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
    store: '<path d="M3 9l2-5h14l2 5"/><path d="M3 9h18v11H3zM9 20v-6h6v6"/>',
    offline: '<path d="M2 8.5a15 15 0 0 1 20 0M5.5 12a10 10 0 0 1 13 0M9 15.5a5 5 0 0 1 6 0"/><path d="M3 3l18 18"/>',
    printer: '<path d="M6 9V3h12v6"/><rect x="3" y="9" width="18" height="8" rx="2"/><path d="M7 14h10v7H7z"/>',
    phone: '<rect x="6.5" y="2.5" width="11" height="19" rx="2.5"/><path d="M11 18.5h2"/>',
    chart: '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    scan: '<path d="M3 7V4h3M21 7V4h-3M3 17v3h3M21 17v3h-3M7 8v8M10 8v8M13 8v8M16 8v8"/>',
    tv: '<rect x="2" y="5" width="20" height="13" rx="2"/><path d="M8 21h8M12 18v3"/>',
    globe: '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.5 3.8 5.6 3.8 9s-1.3 6.5-3.8 9c-2.5-2.5-3.8-5.6-3.8-9S9.5 5.5 12 3z"/>',
    bell: '<path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z"/><path d="M10 20a2 2 0 0 0 4 0"/>',
    gem: '<path d="M6 3h12l3 6-9 12L3 9z"/><path d="M3 9h18M9 3l3 6 3-6"/>',
    spark: '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/>',
    tag: '<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8.5" r="1.5"/>',
    sun: '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>'
  };
  function ic(k, s) {
    return '<svg width="' + (s || 18) + '" height="' + (s || 18) + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + (I[k] || I.check) + '</svg>';
  }

  /* ================= Hero stage: "UpTrendPos atom" =================
     Each page shows 6 market gaps. One gap = [problem, icon, colour, solution title, solution line].
     The 6 icons ride the 3 orbits as electrons; the gap cards take turns (2 on screen at most). */
  var C = { b: '#2F7BD9', g: '#22c55e', y: '#FAE814', t: '#2FA9B0' };
  var P = {
    home: [['Typing thousands of products by hand', 'pill', 'b', 'Ready catalogs, one click', '17,000+ medicines, 5,500+ beauty, 1,100+ electronics', 'Ready catalogs'],
      ['No printer at a small counter', 'printer', 'g', 'Print from your phone', 'Thermal printer by USB Type-C cable', 'Phone printing'],
      ['Paper bills get lost', 'wa', 'y', 'WhatsApp invoices', 'With your e-signature and invoice style', 'WhatsApp bills'],
      ['Light or internet goes off', 'offline', 'b', 'Billing keeps working offline', 'Saved on the device, synced later', 'Works offline'],
      ['Qist written in a diary', 'cal', 'g', 'Installments with receipts', 'A receipt for every payment, a certificate at the end', 'Qist receipts'],
      ['Staff change stock without asking', 'shield', 'y', 'Manager PIN approvals', 'Stock reversals need the manager PIN', 'Manager PIN']],
    grocery: [['Typing every item by hand', 'box', 'b', '7,000+ products ready', 'Search, tick and add to your shop', '7,000+ products'],
      ['Carton, pack and piece prices', 'layers', 'g', 'Loose and pack sale', 'Carton, pack, piece or kg on one bill', 'Loose + pack'],
      ['Udhaar written in a register', 'book', 'y', 'Udhaar khata', 'Every credit sale in the customer ledger', 'Udhaar khata'],
      ['No printer at the counter', 'printer', 'b', 'Print from your phone', 'Small thermal printer by Type-C cable', 'Phone printing'],
      ['Stock runs out without warning', 'box', 'g', 'Low stock + demand list', 'Know what to reorder in time', 'Low stock alerts'],
      ['No barcode scanner', 'scan', 'y', 'Phone camera scanner', 'Scan barcodes inside the app', 'Camera scanner']],
    pharmacy: [['Weeks of typing medicine names', 'pill', 'b', '17,000+ medicines loaded', 'Search, tick and add in one go', '17,000+ medicines'],
      ['Customer asks for a salt, not a brand', 'search', 'g', 'Salt search', 'Every brand of the same salt', 'Salt search'],
      ['Expired stock found too late', 'clock', 'y', 'Batch and expiry alerts', 'Sell or return before the date', 'Expiry alerts'],
      ['Rx medicine sold without a check', 'shield', 'b', 'Rx and controlled checks', 'A prescription tick on the bill', 'Rx checks'],
      ['Hunting for the right shelf', 'layers', 'g', 'Rack and shelf number', 'Set once on the GRN, shown at sale', 'Rack and shelf'],
      ['FBR rules for big pharmacies', 'qr', 'y', 'FBR invoice + QR code', 'On the Enterprise and Custom plans', 'FBR + QR code']],
    tailor: [['Sizes lost in an old register', 'ruler', 'b', 'Sizes by customer ID', 'Old register numbers work as the ID', 'Sizes by ID'],
      ['Who is cutting, who is stitching?', 'scissors', 'g', 'Order status', 'Booked, cutting, stitching, ready, delivered', 'Order status'],
      ['Workshop gets the wrong size', 'doc', 'y', 'Workshop size slip', 'Thermal, A4 or WhatsApp slip', 'Size slip'],
      ['Advance and balance mixed up', 'book', 'b', 'Advance and balance', 'Collect the rest at delivery', 'Advance + balance'],
      ['Forgotten delivery dates', 'cal', 'g', 'Delivery dates', 'Every order with its own date', 'Delivery dates'],
      ['Customers keep calling for updates', 'wa', 'y', 'Slip on WhatsApp', 'Send the order slip in one tap', 'WhatsApp slip']],
    mobile: [['Hours typing phone models', 'phone', 'b', '700+ products ready', 'Phones, accessories and computers', '700+ products'],
      ['Which IMEI did we sell?', 'qr', 'g', 'IMEI from purchase to sale', 'Saved on the GRN, picked at sale', 'IMEI tracking'],
      ['Warranty claims without proof', 'shield', 'y', 'Warranty lookup', 'Find the bill by IMEI or serial', 'Warranty lookup'],
      ['Qist written in a diary', 'cal', 'b', 'Qist plans', 'Advance, monthly dues and receipts', 'Qist plans'],
      ['No printer at the counter', 'printer', 'g', 'Print from your phone', 'Thermal printer by Type-C cable', 'Phone printing'],
      ['Paper bills get lost', 'wa', 'y', 'WhatsApp invoices', 'Bill as a picture or PDF', 'WhatsApp bills']],
    solar: [['Days typing panels and inverters', 'sun', 'b', '1,100+ products ready', 'Panels, inverters, batteries, wire', '1,100+ products'],
      ['Which inverter did we sell him?', 'qr', 'g', 'Serial on every unit', 'From purchase to sale', 'Serial numbers'],
      ['Quotes on paper get lost', 'doc', 'y', 'A4 quotations', 'Send on WhatsApp, convert to a sale', 'A4 quotations'],
      ['Warranty claims without proof', 'shield', 'b', 'Warranty lookup', 'Bill, customer and date by serial', 'Warranty lookup'],
      ['Systems sold on a diary', 'cal', 'g', 'Solar on qist', 'Advance, markup and monthly dues', 'Solar on qist'],
      ['Wire stock never matches', 'layers', 'y', 'Wire by the meter', 'Sell any length on the bill', 'Wire by meter']],
    electronics: [['Typing every appliance model', 'tv', 'b', '1,100+ products ready', 'Electronics, appliances and CCTV', '1,100+ products'],
      ['Serial numbers on paper', 'qr', 'g', 'Serial tracking', 'From purchase to sale', 'Serial tracking'],
      ['Warranty fights at the counter', 'shield', 'y', 'Warranty lookup', 'Proof in seconds', 'Warranty lookup'],
      ['CCTV kits quoted on paper', 'doc', 'b', 'CCTV quotations', 'A4 quote, convert to a sale', 'CCTV quotes'],
      ['AC and fridge on qist', 'cal', 'g', 'Qist plans', 'Every due date tracked', 'Qist plans'],
      ['Light goes off at rush time', 'offline', 'y', 'Billing keeps working offline', 'Synced when back online', 'Works offline']],
    clothing: [['Typing every design by hand', 'box', 'g', '950+ products ready', 'Search, tick, add, set your price', '950+ products'],
      ['Which size is left?', 'layers', 'b', 'Stock per size and colour', 'Own stock for every size', 'Size stock'],
      ['Typing one design 12 times', 'box', 'g', 'Variant generator', 'Colour x size in one go', 'Variants'],
      ['Prices written by hand', 'tag', 'y', 'Barcode tags', 'Size and price on the tag', 'Barcode tags'],
      ['Exchanges spoil the stock', 'sync', 'b', 'Exchange on the same bill', 'Stock fixed on its own', 'Easy exchange'],
      ['Long queues in the Eid rush', 'scan', 'y', 'Scan and bill fast', 'Hold bills, add counters', 'Fast billing']],
    cosmetics: [['Weeks of typing products', 'spark', 'b', '5,500+ products ready', 'Makeup, skin and hair care', '5,500+ products'],
      ['Expired creams on the shelf', 'clock', 'g', 'Batch and expiry alerts', 'Sell first or return', 'Expiry alerts'],
      ['Which shade is left?', 'layers', 'y', 'Stock for every shade', 'Low stock and demand list', 'Shade stock'],
      ['Testers vanish from stock', 'box', 'b', 'Sample and damage entries', 'Stock and cost stay right', 'Testers'],
      ['Wrong price at the counter', 'scan', 'g', 'Barcode billing', 'Fixed price on every bill', 'Barcode billing'],
      ['Udhaar kept in a diary', 'book', 'y', 'Udhaar khata', 'Statement on WhatsApp', 'Udhaar khata']],
    shoes: [['Typing every shoe by hand', 'box', 'g', '200+ products ready', 'Search, tick, add, set your price', '200+ products'],
      ['Ten boxes opened for one size', 'box', 'b', 'Pairs for every size', 'Know in seconds if a 42 is there', 'Size stock'],
      ['Typing size by size', 'layers', 'g', 'Variant generator', 'Colour x size in one go', 'Variants'],
      ['Prices written on the box', 'tag', 'y', 'Box labels', 'Barcode, size and price', 'Box labels'],
      ['Size swaps spoil the count', 'sync', 'b', 'Swap on the same bill', 'Stock fixed on its own', 'Size swap'],
      ['Rush when schools open', 'scan', 'y', 'Scan and bill fast', 'Hold bills, add counters', 'Fast billing']],
    vehicle: [['Which chassis did we sell?', 'qr', 'b', 'Chassis on every unit', 'From purchase to sale', 'Chassis no.'],
      ['Qist kept in a diary', 'cal', 'g', 'Qist with a guarantor', 'Advance, monthly dues, guarantor', 'Qist plans'],
      ['Warranty claims without proof', 'shield', 'y', 'Warranty lookup', 'Bill and date by chassis', 'Warranty lookup'],
      ['Models and colours mixed up', 'layers', 'b', 'Model year x colour', 'Own units for each', 'Variants'],
      ['Quotes lost on paper', 'doc', 'g', 'A4 quotations', 'Send on WhatsApp, convert to a sale', 'A4 quotes'],
      ['Cash short after a big day', 'users', 'y', 'Cash sessions', 'Who sold and who took cash', 'Cash control']],
    electrical: [['Wire stock never matches', 'bolt', 'b', 'Wire by the meter', 'Buy by coil, sell by meter', 'Wire by meter'],
      ['Open boxes, lost pieces', 'box', 'g', 'Box to piece', 'Sell one or the full box', 'Box to piece'],
      ['Quotes lost on paper', 'doc', 'y', 'A4 quotes', 'Send on WhatsApp, convert to a sale', 'A4 quotes'],
      ['Electricians\' udhaar in a diary', 'book', 'b', 'Udhaar khata', 'Statement on WhatsApp', 'Udhaar khata'],
      ['Fused bulbs never counted', 'shield', 'g', 'Damage entries', 'Stock and cost stay right', 'Damage'],
      ['Many models of one LED', 'layers', 'y', 'Watt x colour', 'Own stock for each model', 'LED models']],
    baby: [['Typing every item by hand', 'box', 'g', '350+ products ready', 'Search, tick, add, set your price', '350+ products'],
      ['Loose pieces never counted', 'box', 'b', 'Pack or piece', 'Stock kept in pieces', 'Pack or piece'],
      ['The right size is out', 'layers', 'g', 'Stock for every size', 'Newborn to XL', 'Diaper sizes'],
      ['Expired baby food', 'clock', 'y', 'Batch and expiry alerts', 'Sell first or return', 'Expiry alerts'],
      ['Wrong price at the counter', 'scan', 'b', 'Barcode billing', 'Fixed price on every bill', 'Barcode billing'],
      ['Regular mothers on credit', 'book', 'y', 'Udhaar khata', 'Statement on WhatsApp', 'Udhaar khata']],
    fbr: [['Fines for bills without FBR', 'qr', 'b', 'FBR invoice number', 'Printed on every bill', 'FBR invoice no.'],
      ['Buyers cannot check the bill', 'search', 'g', 'QR code to verify', 'The buyer scans it to check', 'QR to verify'],
      ['Forgetting the Re 1 fee', 'bolt', 'y', 'Re 1 POS fee added', 'On its own, on every bill', 'Re 1 POS fee'],
      ['Going live without testing', 'shield', 'b', 'Sandbox mode', 'Test bills before production', 'Sandbox mode'],
      ['Two counters, one setup', 'store', 'g', 'Own POS ID per counter', 'Separate FBR details for each', 'POS ID per counter'],
      ['Who changed the bill?', 'doc', 'y', 'Audit trail', 'Deletes and changes logged', 'Audit trail']],
    pricing: [['Paying before you try', 'check', 'b', '14-day free trial', 'Test every feature first', '14-day trial'],
      ['Limits on bills', 'doc', 'g', 'Unlimited invoices', 'On every plan', 'Unlimited bills'],
      ['Stuck on a small plan', 'layers', 'y', 'Move up any time', 'Your data stays the same', 'Move up any time'],
      ['Staff commission done by hand', 'users', 'b', 'Staff commission', 'Now on Enterprise and Custom', 'Staff commission'],
      ['Second shop, second software', 'store', 'g', 'Up to 3 branches', 'Own stock and prices for each', 'Up to 3 branches'],
      ['Paying for every update', 'star', 'y', 'Free updates', 'New features on every plan', 'Free updates']],
    downloads: [['Stuck on one computer', 'store', 'b', 'Windows app', 'Full counter with scanner and printer', 'Windows app'],
      ['Owner away from the shop', 'phone', 'g', 'Android app', 'Sell and check sales on the phone', 'Android app'],
      ['No install allowed', 'globe', 'y', 'Web app', 'live.uptrendpos.com in any browser', 'Web app'],
      ['Internet drops all day', 'offline', 'b', 'Works offline', 'Bills save on the device', 'Works offline'],
      ['Data different on each device', 'sync', 'g', 'Auto sync', 'One account everywhere', 'Auto sync'],
      ['No barcode scanner', 'scan', 'y', 'Phone camera scanner', 'Scan barcodes inside the app', 'Camera scanner']],
    about: [['Foreign software, foreign rules', 'pin', 'b', 'Built in Sahiwal', 'For how Pakistani shops work', 'Made in Sahiwal'],
      ['No one to call for help', 'wa', 'g', 'Help in Urdu and English', 'WhatsApp, phone, email and tickets', 'Urdu + English'],
      ['One app does not fit every shop', 'layers', 'y', '30+ business types', 'Ready fields, units and catalogs', '30+ business types'],
      ['Paying for every update', 'star', 'b', 'Free updates', 'New features on every plan', 'Free updates'],
      ['Missing important events', 'bell', 'g', 'In-app notifications', 'For owner, staff, customers and vendors', 'Notifications'],
      ['Profit is a guess', 'chart', 'y', 'Double-entry accounts', 'Trial balance and profit and loss', 'Real accounts']],
    hub: [['Pharmacy and medical store', 'pill', 'b', '17,000+ medicines ready', 'Batch, expiry and salt search', 'Pharmacy'],
      ['Beauty and cosmetics', 'spark', 'g', '5,500+ beauty items ready', 'Add to your shop in one click', 'Beauty'],
      ['Electronics, solar and CCTV', 'sun', 'y', '1,100+ products ready', 'Serials and warranty lookup', 'Electronics + solar'],
      ['Mobile and computer shop', 'phone', 'b', '700+ products ready', 'IMEI from purchase to sale', 'Mobile shop'],
      ['Tailoring and boutique', 'scissors', 'g', 'Sizes by customer ID', 'Orders and delivery dates', 'Tailor shop'],
      ['Jewellery and more', 'gem', 'y', 'Tools for your trade', 'Gold rate, warranty, variants and more', 'Jewellery']],
    contact: [['Not sure which plan fits', 'wa', 'b', 'Free demo on WhatsApp', 'Made for your shop type', 'WhatsApp demo'],
      ['Staff prefer Urdu', 'users', 'g', 'Urdu or English', 'We talk the way you like', 'Urdu or English'],
      ['Setup feels hard', 'check', 'y', 'Setup help', 'Products, printer and staff training', 'Setup help'],
      ['Far from Sahiwal', 'pin', 'b', 'Help in every city', 'WhatsApp, phone and email', 'Every city'],
      ['An issue after you buy', 'doc', 'g', 'Support tickets', 'Raise a ticket inside the app', 'Support tickets'],
      ['Busy all day at the shop', 'clock', 'y', 'Mon to Sat, 10 to 7', 'Pakistan time', 'Mon to Sat']]
  };

  /* Where the plugin images live (the nucleus logo). */
  var IMG = CFG.img || (function () {
    var sc = document.currentScript && document.currentScript.src;
    return sc ? sc.replace(/js\/utp\.js.*$/, 'img/') : '';
  })();

  /* 1.2 stage: a white UpTrendPos nucleus, 6 floating tool nodes around it with flowing data lines,
     and one small "problem -> fix" card at a time. The active node lights up with its card. */
  function buildStage(el) {
    var key = el.getAttribute('data-stage') || 'home';
    var gaps = P[key];
    if (!gaps) { // 1.5: a new business type carries its own 6 items in the page code (no plugin update needed)
      try { gaps = JSON.parse(el.getAttribute('data-stage-items') || 'null'); } catch (e) { gaps = null; }
    }
    if (!gaps || !gaps.length) gaps = P.home;
    var compact = el.clientWidth && el.clientWidth < 460;
    if (compact) el.classList.add('is-compact');
    var cs = getComputedStyle(el);
    var cw = parseFloat(cs.getPropertyValue('--cw')) || 560, ch = parseFloat(cs.getPropertyValue('--ch')) || 540;
    var R = parseFloat(cs.getPropertyValue('--R')) || 196;
    var cx = cw / 2, cy = parseFloat(cs.getPropertyValue('--cy')) || ch / 2;
    var h = '<div class="at-canvas" aria-hidden="true"><span class="at-glow"></span><span class="at-dust">';
    for (var d = 0; d < 22; d++) {
      var x = (d * 37 % 97) + 1.5, y = (d * 53 % 91) + 4;
      h += '<i style="left:' + x + '%;top:' + y + '%;animation-delay:' + ((d * 0.71) % 5).toFixed(2) + 's"></i>';
    }
    h += '</span><span class="at-ring r1"></span><span class="at-ring r3"></span><div class="at-spin"><span class="at-ring r2"></span>';
    h += '<svg class="at-lines" width="' + cw + '" height="' + ch + '" viewBox="0 0 ' + cw + ' ' + ch + '">';
    var nodes = '';
    gaps.forEach(function (gp, i) {
      var ang = -90 + i * 60, rad = ang * Math.PI / 180;
      var nx = (cx + R * Math.cos(rad)).toFixed(1), ny = (cy + R * Math.sin(rad)).toFixed(1);
      h += '<line class="at-line" data-i="' + i + '" x1="' + cx + '" y1="' + cy + '" x2="' + nx + '" y2="' + ny + '" style="--c:' + C[gp[2]] + '"/>';
      nodes += '<span class="at-node ' + gp[2] + '" data-i="' + i + '" style="left:' + nx + 'px;top:' + ny + 'px;--i:' + i + ';--c:' + C[gp[2]] + '"><span class="at-node-in">'
        + '<span class="at-dot">' + ic(gp[1], 22) + '</span><span class="at-lab">' + esc(gp[5] || gp[3]) + '</span></span></span>';
    });
    h += '</svg>' + nodes + '</div>';
    h += '<span class="at-wave"></span><span class="at-wave w2"></span>';
    h += '<div class="at-nuc"><span class="at-nuc-ring"></span><span class="at-nuc-in">'
      + (IMG ? '<img src="' + IMG + 'logo-stacked.svg" width="1816" height="1370" alt="" decoding="async">' : '<b>UpTrend POS</b>') + '</span></div>';
    gaps.forEach(function (gp, i) {
      h += '<div class="at-card ' + (i % 2 ? 'b' : 'a') + '" data-i="' + i + '"><p class="q">' + esc(gp[0]) + '</p><div class="a2"><span class="ic' + (gp[2] === 'y' ? ' y' : '') + '" style="--c:' + C[gp[2]] + '">' + ic(gp[1], 16) + '</span><span><strong>' + esc(gp[3]) + '</strong><small>' + esc(gp[4]) + '</small></span></div></div>';
    });
    h += '</div>';
    el.innerHTML = h;
    function fit() {
      el.style.setProperty('--s', (el.clientWidth / cw).toFixed(4));
    }
    fit();
    if (window.ResizeObserver) new ResizeObserver(fit).observe(el);
    else window.addEventListener('resize', fit);

    var parts = el.querySelectorAll('.at-node,.at-line,.at-card');
    var cur = -1;
    function show(i) {
      cur = i;
      parts.forEach(function (n) { n.classList.toggle('on', +n.getAttribute('data-i') === i); });
    }
    show(0);
    var still = reduce || !MOTION;
    if (still) { el.classList.add('is-still'); return; }
    var timer = null, visible = true;
    function play() { if (!timer && visible) timer = setInterval(function () { show((cur + 1) % gaps.length); }, 3600); }
    function stop() { clearInterval(timer); timer = null; }
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (l) {
        visible = l[0].isIntersecting;
        el.classList.toggle('is-paused', !visible);
        if (visible) play(); else stop();
      }).observe(el);
    }
    document.addEventListener('visibilitychange', function () { if (document.hidden) stop(); else play(); });
    play();
  }

  ready(function () {
    var body = document.body;
    var inEditor = body.classList.contains('elementor-editor-active') || /elementor-preview/.test(location.search);

    /* ================= Header ================= */
    var nav = document.getElementById('utp-nav');
    if (nav) {
      var isStatic = nav.classList.contains('is-static');
      var onScroll = function () { if (!isStatic) nav.classList.toggle('is-solid', window.scrollY > 12); };
      onScroll();
      window.addEventListener('scroll', onScroll, { passive: true });

      var mBtn = nav.querySelector('.utn-mbtn');
      var mega = mBtn && document.getElementById(mBtn.getAttribute('aria-controls'));
      var setMega = function (open) {
        if (!mega) return;
        mega.classList.toggle('is-open', open);
        mBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
      };
      if (mBtn && mega) {
        var li = mBtn.parentNode, t;
        var hoverable = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
        mBtn.addEventListener('click', function (e) { e.stopPropagation(); setMega(hoverable ? true : !mega.classList.contains('is-open')); });
        if (hoverable) {
          li.addEventListener('mouseenter', function () { clearTimeout(t); setMega(true); });
          li.addEventListener('mouseleave', function () { t = setTimeout(function () { setMega(false); }, 180); });
        }
        document.addEventListener('click', function (e) { if (!li.contains(e.target)) setMega(false); });
        document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { setMega(false); setMenu(false); } });
        li.addEventListener('focusout', function (e) { if (!li.contains(e.relatedTarget)) setMega(false); });
      }

      var burger = nav.querySelector('.utn-burger');
      var setMenu = function (open) {
        nav.classList.toggle('is-menu', open);
        if (open) nav.classList.remove('is-hidden');
        if (burger) {
          burger.setAttribute('aria-expanded', open ? 'true' : 'false');
          burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
        }
        document.documentElement.style.overflow = open ? 'hidden' : '';
      };
      if (burger) burger.addEventListener('click', function () { setMenu(!nav.classList.contains('is-menu')); });
      nav.querySelectorAll('.utn-drawer a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
      window.addEventListener('resize', function () { if (window.innerWidth > 1060) setMenu(false); });

      nav.querySelectorAll('a').forEach(function (a) {
        a.addEventListener('click', function () {
          var h = a.getAttribute('href') || '';
          var kind = a.getAttribute('data-track') || 'nav_link';
          push({ event: (h.indexOf('wa.me/') !== -1 || h.indexOf('tel:') === 0 || h.indexOf('mailto:') === 0) ? 'utp_contact_click' : 'utp_cta_click', utp_target: kind, utp_page: location.pathname });
        });
      });
    }

    /* ================= Old footer template still on the page: hide it with its wrapper ================= */
    document.querySelectorAll('div.utp-foot').forEach(function (old) {
      var box = old.closest('[data-elementor-type], footer, .site-footer') || old;
      if (box.querySelector && box.querySelector('#utp-nav, footer.utp-foot') && box !== old) box = old;
      box.style.display = 'none';
    });

    /* ================= Footer ================= */
    var foot = document.querySelector('footer.utp-foot') || document.querySelector('.utp-foot');
    if (foot) {
      foot.querySelectorAll('[data-utp-year]').forEach(function (y) { y.textContent = new Date().getFullYear(); });
      foot.querySelectorAll('a').forEach(function (a) {
        a.addEventListener('click', function () {
          var h = a.getAttribute('href') || '';
          var kind = a.getAttribute('data-track') || (h.indexOf('tel:') === 0 ? 'footer_call' : (h.indexOf('mailto:') === 0 ? 'footer_email' : 'footer_link'));
          push({ event: (h.indexOf('tel:') === 0 || h.indexOf('mailto:') === 0 || h.indexOf('wa.me/') !== -1) ? 'utp_contact_click' : 'utp_cta_click', utp_target: kind, utp_page: location.pathname });
        });
      });
    }

    var root = document.querySelector('.utp');
    if (!root) return;

    /* ================= Full width + no gap above the page ================= */
    function layout() {
      root.style.setProperty('--utp-vw', document.documentElement.clientWidth + 'px');
      if (!nav) return;
      root.style.marginTop = '';
      var ab = document.getElementById('wpadminbar');
      var top = root.getBoundingClientRect().top + window.scrollY - (ab ? ab.offsetHeight : 0);
      if (top > 0 && top < 300) root.style.marginTop = (-top) + 'px';
    }
    layout();
    window.addEventListener('load', layout);
    var rt;
    window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(layout, 120); });

    /* ================= Hero stages ================= */
    root.querySelectorAll('.utp-stage[data-stage]').forEach(buildStage);

    /* ================= Scroll reveal + showcase tilt ================= */
    var canMove = MOTION && !reduce && !inEditor && 'IntersectionObserver' in window;
    var show = root.querySelectorAll('.utp-showcase');
    if (canMove) {
      var sel = '.utp-head,.utp-fcard,.utp-fgroup,.utp-step,.utp-tcard,.utp-rep li,.utp-hw-card,.utp-plan,.utp-usp-row,.utp-split>.utp-figure,.utp-band,.utp-partner,.utp-strip,.utp-callout,.utp-cmp-box,.utp-faq-list,.utp-reviewed,.utp-final-box,.utp-ind-group,.utp-tgroup,.utp-duo>*,.utp-checker,.utp-risk,.utp-hwlist li,.utp-card,.utp-node,.utp-stats li,.utp-doc-sec';
      var els = Array.prototype.filter.call(root.querySelectorAll(sel), function (e) { return !e.closest('.utp-hero') && !e.closest('.utp-marquee'); });
      els.forEach(function (e) {
        var sib = 0, s = e.previousElementSibling;
        while (s && sib < 6) { if (s.className === e.className) sib++; s = s.previousElementSibling; }
        e.style.setProperty('--rv-d', (sib * 0.07) + 's');
        e.classList.add('utp-rv');
      });
      var io = new IntersectionObserver(function (list) {
        list.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
      els.forEach(function (e) { io.observe(e); });
      show.forEach(function (e) { io.observe(e); });
      setTimeout(function () { els.forEach(function (e) { if (e.getBoundingClientRect().top < window.innerHeight) e.classList.add('in'); }); }, 900);
    } else {
      show.forEach(function (e) { e.classList.add('in'); });
    }

    /* ================= Endless scroll strips ================= */
    if (!reduce) {
      root.querySelectorAll('.utp-marquee').forEach(function (box) {
        var track = box.querySelector('.utp-mq-track');
        if (!track || track.getAttribute('data-ready')) return;
        var items = Array.prototype.slice.call(track.children);
        function addCopy() {
          items.forEach(function (li) {
            var c = li.cloneNode(true);
            c.setAttribute('aria-hidden', 'true');
            c.querySelectorAll('img').forEach(function (im) { im.setAttribute('alt', ''); });
            c.querySelectorAll('a').forEach(function (a) { a.setAttribute('tabindex', '-1'); });
            track.appendChild(c);
          });
        }
        var guard = 0;
        while (track.scrollWidth < box.offsetWidth && guard < 10) { addCopy(); guard++; }
        Array.prototype.slice.call(track.children).forEach(function (li) {
          var c = li.cloneNode(true);
          c.setAttribute('aria-hidden', 'true');
          c.querySelectorAll('img').forEach(function (im) { im.setAttribute('alt', ''); });
          c.querySelectorAll('a').forEach(function (a) { a.setAttribute('tabindex', '-1'); });
          track.appendChild(c);
        });
        track.style.setProperty('--utp-mq', Math.max(20, Math.round(track.scrollWidth / 2 / 45)) + 's');
        track.setAttribute('data-ready', '1');
      });
    }

    /* ================= Links to pages that are not live (backup; the server already does this) ================= */
    if (LIVE.length) {
      root.querySelectorAll('a[data-page]').forEach(function (a) {
        var slug = a.getAttribute('data-page');
        if (LIVE.indexOf(slug) !== -1) return;
        if (a.hasAttribute('data-hide-until-live')) { a.parentNode.removeChild(a); return; }
        var s = document.createElement('span');
        s.className = a.className;
        s.innerHTML = a.innerHTML;
        a.parentNode.replaceChild(s, a);
      });
    }

    /* ================= Downloads page ================= */
    var ua = navigator.userAgent || '';
    var os = 'other';
    if (/Android/i.test(ua)) os = 'android';
    else if (/iPhone|iPad|iPod/i.test(ua) || (/Macintosh/i.test(ua) && navigator.maxTouchPoints > 1)) os = 'ios';
    else if (/Windows/i.test(ua)) os = 'windows';
    var isDl = root.id === 'utp-downloads';
    var target = 'web';
    if (isDl) {
      var meta = function (v, s) {
        var p = [];
        if (v) p.push('Version ' + v);
        if (s) p.push(s);
        if (L.updated) p.push('Updated ' + L.updated);
        return p.join(' · ');
      };
      ['apk', 'exe'].forEach(function (key) {
        root.querySelectorAll('[data-dl="' + key + '"]').forEach(function (a) {
          if (L[key]) { a.setAttribute('href', L[key]); a.removeAttribute('aria-disabled'); }
          else { a.setAttribute('href', '#utp-get'); a.setAttribute('aria-disabled', 'true'); a.textContent = 'Coming soon'; }
        });
      });
      var mApk = root.querySelector('[data-meta="apk"]'), mExe = root.querySelector('[data-meta="exe"]');
      if (mApk) mApk.textContent = meta(L.apkVersion, L.apkSize);
      if (mExe) mExe.textContent = meta(L.exeVersion, L.exeSize);
      var rApk = root.querySelector('[data-req="apk"]');
      if (rApk && L.apkMinAndroid) rApk.textContent = L.apkMinAndroid;
      if (os === 'android' && L.apk) target = 'apk';
      if (os === 'windows' && L.exe) target = 'exe';
      var smart = document.getElementById('utp-smart'), smartText = document.getElementById('utp-smart-text'), smartNote = document.getElementById('utp-smart-note');
      if (smart && smartText) {
        if (target === 'apk') { smart.href = L.apk; smartText.textContent = 'Download for Android'; if (smartNote) smartNote.textContent = (meta(L.apkVersion, L.apkSize) || 'Android APK') + ' · 14-day free trial'; }
        else if (target === 'exe') { smart.href = L.exe; smartText.textContent = 'Download for Windows'; if (smartNote) smartNote.textContent = (meta(L.exeVersion, L.exeSize) || 'Windows 10 / 11') + ' · 14-day free trial'; }
      }
      if (os === 'ios') { var ios = document.getElementById('utp-ios'); if (ios) ios.classList.add('is-rec'); }
      else {
        var recKey = target === 'apk' ? 'android' : (target === 'exe' ? 'windows' : 'web');
        var card = root.querySelector('.utp-card[data-os="' + recKey + '"]');
        if (card) card.classList.add('is-rec');
      }
    }

    /* ================= Tabs ================= */
    var tabs = root.querySelectorAll('[role="tab"]');
    function openTab(name) {
      tabs.forEach(function (t) {
        var on = t.getAttribute('data-tab') === name;
        t.setAttribute('aria-selected', on ? 'true' : 'false');
        var pan = document.getElementById(t.getAttribute('aria-controls'));
        if (pan) pan.hidden = !on;
      });
    }
    tabs.forEach(function (t) { t.addEventListener('click', function () { openTab(t.getAttribute('data-tab')); }); });
    if (tabs.length) {
      var want = os === 'android' ? 'android' : (os === 'windows' ? 'windows' : 'web');
      var has = root.querySelector('[role="tab"][data-tab="' + want + '"]');
      openTab(has ? want : tabs[0].getAttribute('data-tab'));
    }

    /* ================= Pricing: monthly / yearly ================= */
    var billBtns = root.querySelectorAll('[data-bill]');
    function setBill(mode) {
      billBtns.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-bill') === mode ? 'true' : 'false'); });
      root.querySelectorAll('.utp-amt[data-' + mode + '], .utp-bill-note[data-' + mode + ']').forEach(function (el) { el.textContent = el.getAttribute('data-' + mode); });
    }
    billBtns.forEach(function (b) {
      b.addEventListener('click', function () {
        setBill(b.getAttribute('data-bill'));
        push({ event: 'utp_cta_click', utp_target: 'billing_' + b.getAttribute('data-bill'), utp_page: location.pathname });
      });
    });

    /* ================= Branded images: no right-click save or drag ================= */
    root.querySelectorAll('.utp-hw-card img, .utp-hero-img img, .utp-showcase img').forEach(function (im) {
      im.addEventListener('contextmenu', function (e) { e.preventDefault(); });
      im.addEventListener('dragstart', function (e) { e.preventDefault(); });
    });

    /* ================= Contact page: move a separate Fluent Forms widget into the form card ================= */
    var slot = root.querySelector('#utp-form-slot');
    if (slot && !inEditor && !slot.querySelector('form')) {
      var ff = document.querySelector('.fluentform_wrapper_' + (slot.getAttribute('data-form-id') || '1'));
      if (ff && root.contains(ff)) ff = null;
      if (!ff) document.querySelectorAll('.fluentform').forEach(function (f) { if (!ff && !root.contains(f)) ff = f; });
      if (ff) {
        var holder = ff.closest('.elementor-widget');
        slot.innerHTML = '';
        slot.appendChild(ff);
        if (holder && !holder.contains(root)) holder.style.display = 'none';
      }
    }

    /* ================= FBR page: Tier-1 checker ================= */
    root.querySelectorAll('[data-utp-checker]').forEach(function (box) {
      var msg = box.querySelector('.utp-check-msg'), res = box.querySelector('.utp-check-result'), wa = box.querySelector('[data-utp-check-wa]');
      var base = wa ? wa.getAttribute('href').split('?text=')[0] : '';
      box.addEventListener('change', function () {
        var on = [];
        box.querySelectorAll('input[type="checkbox"]:checked').forEach(function (c) { on.push(c.value); });
        if (msg) msg.textContent = msg.getAttribute(on.length ? 'data-yes' : 'data-none');
        if (res) res.classList.toggle('is-yes', on.length > 0);
        if (wa) {
          var t = on.length ? 'Hi, I checked the Tier-1 list on your website. True for my shop: ' + on.join(', ') + '. I need FBR POS integration.' : 'Hi, I checked the Tier-1 list on your website and need help with FBR POS integration';
          wa.setAttribute('href', base + '?text=' + encodeURIComponent(t));
        }
        push({ event: 'utp_tier1_check', utp_ticks: on.length, utp_page: location.pathname });
      });
    });

    /* ================= Lead + click tracking (GTM / GA4) ================= */
    root.querySelectorAll('a[href^="tel:"], a[href^="mailto:"], a[href*="wa.me/"]').forEach(function (a) {
      if (a.hasAttribute('data-track')) return;
      a.addEventListener('click', function () {
        var h = a.getAttribute('href') || '';
        push({ event: 'utp_contact_click', utp_target: h.indexOf('tel:') === 0 ? 'call' : (h.indexOf('mailto:') === 0 ? 'email' : 'whatsapp'), utp_page: location.pathname });
      });
    });
    root.querySelectorAll('[data-track]').forEach(function (a) {
      a.addEventListener('click', function () {
        if (a.getAttribute('aria-disabled') === 'true') return;
        var t = a.getAttribute('data-track');
        if (a.id === 'utp-smart') t = 'hero_' + target;
        var h = a.getAttribute('href') || '';
        var contact = h.indexOf('wa.me/') !== -1 || h.indexOf('tel:') === 0 || h.indexOf('mailto:') === 0;
        push({ event: isDl ? 'utp_download_click' : (contact ? 'utp_contact_click' : 'utp_cta_click'), utp_target: t, utp_page: location.pathname });
      });
    });
  });
})();
