# UpTrendPos - Website Content Handoff: What We Are Building for Shop Owners

**For:** the website design and content chat (pages, sections, copy, FAQs, ads)
**Prepared:** 27 Oct 2026, from the 23-27 Oct planning sessions (roadmap V4)
**Scope:** customer side only - what a shop owner, cashier, manager or their customers will see and use. The UpTrendPos admin side is not part of this file and must not appear on the website.
**Companion docs:** `UpTrendPos_App_Features_Oct2026.md` (features already in the app today), `website_pricing_v1.html` (pricing page), `HANDOFF_Website_SiteKit_v1_20Oct2026.md` (site design kit).

---

## 0. Rules for using this file

1. **Status labels decide the wording.** Every feature below carries one label. Use the matching wording on the site:

| Label | Meaning | Website wording |
|---|---|---|
| LIVE | in the app today | present tense: "UpTrendPos does ..." |
| LAUNCH | being built now, part of the national launch (retail stage) | "New", "Coming with the launch", or present tense only after Abdul confirms it is live |
| NEXT | stage 2 (wholesale, distribution, online selling) | "Coming soon" |
| LATER | stage 3 (manufacturing) | mention only as "on our roadmap" or leave out |

   Never describe a LAUNCH, NEXT or LATER feature as available today. When in doubt, ask Abdul which items have gone live.
2. **Brand:** always "UpTrendPos" (this spelling and casing). Never mention or link AGR / AGR Soft. Never name competitors on the website.
3. **Language:** very simple, point-to-point English for Pakistani shop owners. Short sentences. Prices in "Rs".
4. **Links:** demo and sign-up = live.uptrendpos.com. Shop online stores live on `<shopname>.uptrendpos.store`.
5. **No technical words on pages:** no database, server, RLS, sync queue, token, edge function. Say "your data", "internet", "your counters".

---

## 1. Plans, prices and free trial (LAUNCH)

| | Premium | Enterprise | Custom |
|---|---|---|---|
| One line | For one shop with one or two counters | For busy shops, FBR billing and up to 2 branches | For bigger shops that need every tool and more staff |
| Monthly | Rs 2,000 / month | Rs 3,000 / month | Rs 6,000 / month |
| Yearly | Rs 24,000 / year | Rs 36,000 / year | Rs 72,000 / year |
| Branches / locations | 1 | 2 | more (set per deal) |
| Counters (devices) | 2 | more | most |
| Cloud storage for photos and documents | 2 GB | 10 GB | 50 GB |
| FBR Digital Invoicing | - | Included | Included |
| Free trial | 14 days, all Premium features | 14 days, all Enterprise features | 14 days, all Custom features (or on request) |

- **Each plan has its own free trial.** The old single "demo" is gone. During the trial the shop sees exactly the features of the plan it chose, so what they test is what they buy.
- Reminders come before the trial ends. If the shop does not buy, the account pauses. **Data is never deleted**; buying the plan opens everything again as it was.
- **Honest pricing rule (use on the pricing page):** the monthly card says "Rs 2,000 / month - billed monthly. Rs 24,000 a year." Any first-year discount is shown as a separate line. No hidden fees.
- **Installation charges are NOT mentioned on the website** (decision 29 Oct 2026): no amounts, no fee lines. The sales team quotes and manages installation charges manually per client after engagement.
- Extra branch, extra user, extra storage and the Online Store can be added later as add-ons.
- Wholesale and distribution plans use the same sign-up and trial flow (NEXT; prices not decided yet - do not publish).

## 2. Sign-up and getting started (LAUNCH)

- Sign up from the website or with our team. Steps: your business details -> your business type and category -> choose a plan -> start free trial or pay now -> your shop is ready.
- Mobile number is verified by code. One free trial per number / business.
- **Welcome email** with your shop name, login steps, download links for Android, Windows and web, and support contact. It never contains a password.
- Pay now and the POS works the same day.
- Category-based setup: choosing your business category switches on the right features (for example batch and expiry for pharmacy, IMEI for mobile shops, kitchen screens for restaurants). Changing category later shows what will change before applying it.
- Start checklist on the home screen guides a new owner through the first steps.

## 3. Works without internet (LAUNCH)

**Main message:** "Only your first login needs internet. After that, sell, manage stock and see your reports without internet."

- Every counter (Android, Windows) keeps working when the internet goes down: sales, returns, stock, customer accounts, printing.
- **Full reports on every counter, offline.** All retail reports and all dashboards open without internet for that branch. Only a few items need internet by nature and say so clearly ("Needs internet"): online store orders, all-branches combined view, bank statement import, budgets, CRM, FBR reconciliation.
- When the internet comes back, everything sends automatically. FBR invoices made offline are sent as soon as the internet returns (FBR requires upload within 24 hours).
- Each report shows "Data up to <time>", so the owner knows how fresh the figures are.
- **How long offline (plan rules, say simply on the FAQ):**
  - Monthly plan: connect at least once before your month ends to stay active.
  - Yearly plan: connect at least once every 3 months; renewal reminders start about 20 days before the year ends.
  - If a counter stays offline too long it signs out, but **nothing on it is lost**. Connect, sign in, and it continues where it stopped.
- Safe against tampering: changing the computer's date does not extend a plan.

## 4. Security for shop owners (LAUNCH)

- **Two-step login (2FA)** for owners and staff with any authenticator app; 10 recovery codes to print and keep.
- Owner can require 2FA for admins or for every staff login.
- "Recent security activity": sign-ins, failed sign-ins, password changes, new devices; see and close active sessions.
- **Field-level permissions:** hide cost price, profit, discounts or customer phone numbers from chosen staff; per-user branch and location access.
- Data on the shop's computer is encrypted.
- **Nothing posted can be deleted.** Mistakes are corrected with a reversal, so the books always show the full history (owner-friendly message: "No one can secretly delete a sale").
- Approval rules: big discounts, credit over limit or large payments can require the owner's approval. One approvals inbox.
- Restricted documents: mark a document private so only chosen users can see it.

## 5. New look: clear colours and a dashboard for every module (LAUNCH)

- New UpTrendPos visual design across the app: cleaner screens, larger readable numbers, dark mode, works on phone, tablet and desktop.
- **Every module has its own colour** so staff always know where they are (Sales blue, Purchases purple, Inventory teal, Accounts green, and so on). Money colours always mean the same thing: green = money in / profit, red = money out / loss, amber = due soon.
- **Dashboards (owner home + 7 module dashboards):**

| Dashboard | What the owner sees |
|---|---|
| Home | net sales, gross profit and margin, cash in hand, bank balance, receivables, payables, stock value; 30-day sales with profit line; pending approvals and alerts |
| Sales | sales by channel and by hour, new vs returning customers, top customers and products, overdue customers, "customer concentration risk" (warns if a few customers make most of your sales), salesperson leaderboard |
| Purchases | payables due, GRNs pending, top suppliers, supplier lead time (days from order to delivery), stock on order |
| Inventory | dead stock (no movement 30 / 60 / 90 days), stock turnover with colour targets, ABC analysis, stock health ring (healthy / low / out / over), near expiry, stock by location |
| Accounts | profit and loss trend, margins, current ratio, cash flow, tax payable summary, cheques due in the next 7 days, bank balances |
| Installments | active plans, overdue amount, recovery rate, top defaulters, upcoming 7 days |
| Cash and Cheques | cash in hand, over / short this month, cheques in hand and under collection, bounced cheques |
| HR | headcount, present today, on leave, payroll this month, advances |

- Each tile opens the full report behind it. Cashiers see only what their role allows (no money dashboards for a cashier).

## 6. Reports, alerts and morning briefing (LAUNCH)

- **84 retail reports** in one Report Center with filters, export, saved views; all work offline for the branch.
- New reports include running cost (movement by movement), daily stock, serial trace (search an IMEI, engine or chassis number to see who it was bought from and sold to), area-wise customers and sales, FBR submitted invoices.
- **55 ready alerts**, switched on by the owner, sent in the app (and by email / WhatsApp where set). Examples:
  - Stock: low stock, out of stock on a selling item, negative stock, batch near expiry, transfer arriving short.
  - Sales: customer over credit limit, invoice overdue, **sold below cost**, installments in arrears.
  - Tills: cash over / short at shift close, shift left open, a counter not sending its data.
  - Banking: cheque due, cheque bounced, bank balance too low for issued cheques, books check found a problem.
  - Online shop: new order, payment problem, cash-on-delivery money not received from the courier.
  - Plan: trial ending, renewal due.
- **Owner's morning briefing:** yesterday's key numbers and today's to-dos at a time the owner chooses; evening summary of unread alerts.

## 7. Retail upgrades (LAUNCH)

- **Promotions:** percent off, amount off, fixed price, buy X get Y, basket offers with minimum spend; dates, times, days, branches, and channel (counter, invoice, online); usage caps; a receipt code on the bill; **"Test a basket"** screen shows which offers apply and why.
- **Loyalty:** points, stamps (buy 9, get the 10th free), cashback as store credit, spend tiers; gift cards and store credit.
- **Price lists** that switch automatically by sale type (cash, credit, installment, wholesale).
- **Customer who is also a supplier:** one combined statement and a "set-off" to net what you owe against what they owe.
- **Charge a stock shortage to an employee** (recovered through payroll), with owner PIN.
- Customer quick-add at the POS with photo and thumb-impression image; CNIC mask; areas and routes; credit limit; customer-specific prices.
- **Installments:** guarantors register (CNIC, cheque no, balance guaranteed), recovery report, plans by tenure, top defaulters.
- **Printing:** paper size per form, logo, tax breakdown, signature line, bank details, customer's balance on credit invoices, **"DUPLICATE" mark on every reprint**, branch NTN / STRN on invoices, share by WhatsApp.
- **POS settings:** quick-key pages, weighing scale and tare presets, scan behaviour, hide zero-stock items, cash denominations, receipt header and footer.
- Tax handled per product line (inclusive or exclusive, with a worked example on screen); tax-exempt buyer needs a reason and certificate number, so no invoice goes out untaxed by mistake.
- Purchases: supplier quotation, purchase order with approval and expected delivery, bonus quantity that correctly lowers your cost, pending-to-receive register.
- Stock always moves with the sale, so profit is always right.

## 8. Godown and warehouse (Block A = LAUNCH, rest = NEXT)

**Message:** "Add a godown without buying a distribution system."

LAUNCH (retail shops with a godown):
- Warehouse and "hold / damaged" locations alongside your shops.
- **Transfers with "on the way" status:** goods leave one place, the other place confirms receipt, short and damaged items are recorded.
- Quality check on receiving: chosen items wait in "QC hold" until approved.
- **Delivery note:** sell now, deliver later, with a pending-deliveries list.
- Damaged or returned stock can never be sold by mistake.
- Each user only works in the locations they are allowed.

NEXT (bigger stores and wholesalers):
- Racks and bins, put-away rules, auto replenishment (min / max) from godown to shop.
- **Stock reserved for orders** so the same stock is never promised twice.
- Pick list -> pack -> delivery challan -> delivered, with proof of delivery and freight.
- Internal requisitions (a branch asks the godown for stock), ABC classes and cycle counting (blind counts).
- Warehouse dashboard and **18 warehouse reports**, offline at the warehouse.

## 9. Wholesale, distribution and B2B (NEXT)

- Order booker app flow with route days and journey plans; delivery next day on a van with a **load sheet**; day-end settlement of the delivery man.
- **Van sales** with van stock, offline credit allowance, and field cash collection that works without signal.
- Schemes and discounts from principals (10+1, slabs), principal claims, market returns.
- Credit control: limits, overdue holds, approvals.
- B2B order to cash: enquiry, quotation with revisions, sales order, dispatch, invoice; field service for installed equipment.
- Import and foreign currency (USD payables, landed cost, exchange gain / loss).
- B2B tax and FBR Digital Invoicing for business buyers.
- **CRM:** leads, follow-ups, deals, assigned to salespeople.
- **55 distribution reports** plus the 18 warehouse reports.

## 10. Restaurants, cafes and fast food (LAUNCH)

Core restaurant POS (dine-in, takeaway, delivery, floor plan, kitchen order tickets and kitchen screens, token board, reservations, call centre, own riders with cash-on-delivery settlement, Foodpanda-type aggregators, menu with modifiers and combos, recipes and food cost) plus these additions:
- **Order Control:** one live board of every order (counter, waiter, call centre, QR): not sent to kitchen, in kitchen, ready, late, not billed yet.
- Ready item notes ("No onion", "Extra spicy") printed on the kitchen ticket.
- Kitchen sections (kitchen, bar, desserts) each with a target time; late orders turn colour.
- **Kitchen print station:** a PC near the kitchen printer prints new orders by itself - works on the shop's own network even without internet.
- **Guest feedback** with ratings (food, service, speed, cleanliness) and comments.
- Reports by channel and time of day (breakfast, lunch, dinner, late night).
- **Live command centre** full-screen mode for a manager's TV.
- Loyalty with stamps and cashback.
- Kitchen staff mark items "finished" with their own PIN on a shared tablet.
- Floor designer with furniture, walls, doors; saved layout versions.

## 11. Salons, spas, barbers and repair shops (LAUNCH)

- **One-tap setup** for Beauty Salon and Spa, Barber Shop, Wellness Spa, Phone and Computer Repair: services with prices and durations, staff and resources ready.
- **Booking desk:** day view, booked / in service / done / no-show, walk-in queue with tokens (W-17).
- No-show tracking with weekly no-show rate; slot size, opening hours, overbooking setting.
- Staff profiles with calendar colour, skills and "bookable" switch; staff become employees for payroll, attendance and commission.
- Services dashboard: bookings today, walk-ins waiting, top services, staff performance.
- **Quick job card** for repairs: customer, priority, promised time, then add parts and labour.
- Installation jobs, repair tickets, warranty registration and warranty claims.

## 12. Online store and selling online (NEXT)

**Your own online store (Online Store add-on):**
- A website for your shop at `<yourshop>.uptrendpos.store`, or connect your own domain.
- Products, prices and stock come straight from your POS: no double entry.
- **7 designs:** Classic (general retail), Tech (electronics, solar, mobiles - spec tables, compare, WhatsApp quote), Fresh (grocery - quick add, delivery slots), Care (pharmacy - prescription upload), Style (fashion - colours, size guide), Bites (restaurant menu with deals), Trade (wholesale - prices after login, request a quote).
- Edit colours, logo, banners, homepage sections, pages (about, contact, returns, privacy) from the app.
- Checkout with mobile number code; **Cash on Delivery on from day one**. JazzCash, Easypaisa and card payments can be switched on with the shop's own merchant account - **money goes straight to the shop's account**, UpTrendPos never holds it.
- Orders arrive in the app: verify by call or WhatsApp confirmation link, pack, dispatch, invoice; order tracking page for the customer.
- If the plan ends the store shows "temporarily unavailable" - nothing is deleted.

**Selling on other channels (Channels add-on):**
- Connect Shopify, WooCommerce and Daraz: products and stock sync both ways with safety buffers, orders come in automatically.
- **Couriers:** Leopards, TCS, PostEx and Trax first (more like M&P, BlueEx, Call Courier, Daewoo after). Book, print labels, track, all from the app; rules pick the best courier per city.
- Failed delivery desk (re-attempt, hold, return), returned parcels graded sellable / damaged.
- **Cash Truth:** see how much COD money is still with each courier, what was deducted, and what reached your bank. Remittances matched automatically; short payments become claims with deadlines.
- Fake-order protection: customer risk score from their own past refusals, duplicate order checks, automatic rules (hold, ask for advance payment, require confirmation).
- Ecommerce reports: courier scorecards, return rate by city, product profit after courier cost, true ecommerce profit (sales tax is never counted as income).

## 13. Backups for shops (LAUNCH)

- Your data is kept safely online and backed up daily by UpTrendPos.
- The Windows POS also keeps a daily encrypted backup on the shop's own computer or USB, so sales made offline are protected until they are sent.
- On request, our support team can give a shop a full copy of its own data.

## 14. Manufacturing (LATER)

On the roadmap after the distribution stage: recipes / bill of materials, production orders, raw material issue, finished goods, cost per unit, quality checks, batch tracing. Do not promote yet; at most "Manufacturing - on our roadmap".

---

## 15. Selling points (use across pages)

1. **Works without internet** - only the first login needs internet; full reports on every counter.
2. **Your books are always right** - every sale updates stock and accounts at once; nothing can be secretly deleted; sales tax is kept apart from your income.
3. **One app for the whole business** - counter, godown, accounts, staff, online store, couriers.
4. **Made for Pakistan** - FBR Digital Invoicing, Urdu, cash-on-delivery, JazzCash / Easypaisa, local couriers, installments with guarantors.
5. **Clear and colourful** - every module has its own colour and dashboard; numbers you can read at a glance.
6. **Safe** - two-step login, staff permissions down to single fields, encrypted shop data, daily backups.
7. **Honest pricing** - each plan has its own free trial; price shown monthly and yearly; no hidden fees.
8. **Grows with you** - start with one shop; add branches, a godown, wholesale and an online store when you need them.

## 16. Suggested website use

| Page / section | Content from this file |
|---|---|
| Home | Selling points 1-8; dashboards screenshot strip; "Start your free trial" |
| Pricing | Section 1 table + honest pricing line + trial FAQ |
| Features: Offline POS | Section 3 |
| Features: Reports and dashboards | Sections 5, 6 |
| Features: Security | Section 4, 13 |
| Features: Inventory and godown | Section 7 (stock items) + Section 8 LAUNCH part |
| Industry: Restaurant | Section 10 |
| Industry: Salon / repair | Section 11 |
| Industry: Grocery, pharmacy, electronics, mobile | Section 7 + relevant category items |
| Coming soon: Online Store, Wholesale and Distribution | Sections 9, 12 (labelled "Coming soon") |
| FAQ | trial, offline limits, data safety, FBR, payment money flow, what happens when a plan ends |

## 17. Claims to avoid

- Do not say "free plan" or "free forever" (trial only).
- Do not say "unlimited offline" - say "only the first login needs internet" and give the plan rule in the FAQ.
- Do not list NEXT / LATER features as available.
- Do not promise a delivery date for coming features.
- Do not name or compare with specific competitors.
- Do not mention installation charges or their amounts anywhere on the website (sales team handles them per client).
