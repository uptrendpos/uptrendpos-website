# UpTrendPos website facts for the daily automation (source of truth)

Write ONLY what is on this list or in the queue entry's `specials`. If a feature is not here, leave it out or tag it `soon()` (grey "Coming soon"). Never guess.

## Every business type gets (built, every plan unless tagged)
- Billing: scan barcode (USB scanner or phone camera), search by name, quick bill and calculator, hold a bill, discount on the bill, cash / bank / udhaar.
- Thermal receipt (80mm, or small Type-C printer plugged into the phone) or A4 invoice with logo; bill on WhatsApp as picture or PDF.
- Returns and bill edits keep the same invoice number.
- Units (UOM): carton / box / pack / piece / kg / gram / meter / litre on one bill, stock always in the selling unit.
- Variant generator: two dimensions (e.g. size x colour, shade x size, model x colour) make all items in one go, each with its own stock and price.
- Categories and brands; add your own products. Ready catalog: use the queue entry's `catalog` value (Abdul, 30 Oct 2026). If it is a count (e.g. "300+"), say "<count> <trade> products already loaded: search, tick and add the ones you sell, then set your own stock and price" and follow the catalog wording pattern of site/build_cosmetics.py / build_mobile.py (counts under 150 = one line only, never in the H1, title or hero). If it is 0, say "your shop starts with an empty list, you add only what you sell". Any shop can also add products from the full UpTrendPos catalog of 38,000+ products by name or category (live; total confirmed by Abdul 30 Oct 2026, more coming). Never write a higher total.
- Batch number and expiry date on purchase; expiring/expired alerts; batch-wise stock and expiry report (only where it fits the trade).
- Low stock alerts; demand list (what to reorder).
- Inventory movements: damage, sample, adjustment, stock audit.
- Purchases: purchase order, goods received (GRN), purchase invoice; supplier ledger and balance due; average cost updates on its own; returns to supplier; A4 print of PO/GRN.
- A4 quotation with logo, send on WhatsApp, convert to a sale in one tap.
- Customers: list with phone, udhaar khata, payments on the ledger, statements as PDF / print / WhatsApp.
- Staff: own login and access per staff member; cash sessions (open/close drawer per shift); cashier records.
- Accounts: double-entry accounts and reports, expenses, profit and loss, trial balance, day book, monthly closing, stock valuation, AR aging.
- Offline-first: Windows and Android keep billing without internet and sync later. Say: "Cash bills work offline. Udhaar (and qist) need internet, so every device shows the same balance."
- Backup and restore; each shop's data kept separate.
- Windows, Android and web (live.uptrendpos.com). 14-day free trial.

## Plan tags (use `plan('Enterprise+')` exactly)
- Enterprise+ (Enterprise and Custom): FBR invoice number + QR code (Re 1 POS fee added on its own, each counter its own FBR details), barcode label printing, customer installments (qist) incl. guarantor, profit dashboard, audit trail, staff commission rules and report, bills without the UpTrendPos badge.
- Custom only: staff attendance and salary (payroll).
- Plan text: Premium = one branch, up to 3 users. Enterprise = up to 2 branches, 6 users. Custom = up to 3 branches, 9 users. Prices only on the pricing page (never in industry pages).

## Coming soon (only with `soon()`)
Season sale offers / promotions, loyalty points, special price lists per customer group, stock transfer between branches, salon/service booking, repair job cards, registration/documents tracking, second serial per unit, buy-back / trade-in, delivery scheduling.

## Never write
- Installation / setup charges or any fee besides plan prices (decision 29 Oct 2026).
- "Free plan", "free forever", "unlimited offline", "certified", "FBR approved", "licensed integrator", "Pakistan's first / No. 1", customer counts, iOS app.
- Competitor names (ElOERP, Sada Hisab, any other) or comparisons by name. AGR / AGR Soft.
- Real product brand names in copy or mockups (use generic names). Health claims. Anything that targets minors.
- Serial tracking / warranty lookup for a type unless its queue `specials` says so (only electronics, solar, mobile, vehicle have them).

## Style
- Very simple English for Pakistani shop owners, short sentences, "you / your shop", Rs for money, Pakistani examples (udhaar, khata, qist, kiryana, Eid rush, load-shedding).
- Brand always "UpTrendPos".
- Template v3 (industry.py): problems (6, pain -> fix), usp (2 rows with images), caps (6), features (6 groups), hardware (6), setups (3), process (5 steps + one line that says what changes on its own), offline, benefits (6), reports (4 + chips), duo (safety + FBR), segments (6), plans (3), faq (11), related (4 live/registry slugs), final.
- Focus keyword density 0.80-0.95%, 2,500-3,000 words, keyword in H1, lead, first image ALT, title (<=60) and description (120-160).
- Images: 4 per page, names `uptrendpos-<trade>-<topic>.webp`, never ending in `-<digits>`; built from the helpers in hw/gen_shoes_vehicle.py, hw/gen_electrical_baby.py, hw/gen_fashion_beauty.py (variant_tablet, unit_tablet, phone_list, phone_kv, counter_monitor, five_steps, hardware_scene). Pakistani names, Rs amounts that add up, no brands.
- Hero: `stage_items` = 6 x [problem, icon, colour, fix title, fix line, short label]; icons from: box clock wa bolt book qr search pill cal shield scissors ruler doc sync check star pin users layers store offline printer phone chart scan tv globe bell gem spark sun tag; colours b g y t.
