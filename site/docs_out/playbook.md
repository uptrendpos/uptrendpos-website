# UpTrendPos - Website Content Strategy Playbook (benchmarked on ElOERP)

**For:** the website design and content chat (every new page, section, FAQ, ad copy)
**Prepared:** 27 Oct 2026
**Use with:** `HANDOFF_Website_Content_Customer_Features_27Oct2026.md` (WHAT to say + status labels) and `HANDOFF_Website_SiteKit_v1_20Oct2026.md` (HOW it looks). This file = HOW to write and structure the words.

**Internal only.** ElOERP (eloerp.net) is studied here for its content method, not its design and not its wording. On the website: never name it, never copy its sentences, never compare. Every line we publish is written fresh for UpTrendPos.

---

## 1. What ElOERP does well (the method we adopt)

| # | Their technique | Example of the pattern (theirs, for study only) | Why it works |
|---|---|---|---|
| 1 | **Every module headline is an outcome, not a feature name** | Kicker "Accounting" -> H2 "Your books close themselves." | Owner reads the result he wants, not a menu label |
| 2 | **Business flows shown as a short step strip** | Quotation -> Order -> Invoice -> Delivery Note -> Return | Shows the software follows the shop's real work, step by step |
| 3 | **"What happens automatically" line under each flow** | "Each confirmation posts revenue, COGS and stock - no double entry" | Proves connection between modules in one sentence |
| 4 | **Pain -> Fix grid on industry pages** | "Cash drawer never matches the books" -> "Every sale posts to stock and accounts the instant you charge" | Owner recognises his own problem first |
| 5 | **Claim headlines + reassurance** | "It keeps selling when the internet drops" | Removes fear before it is asked |
| 6 | **Small mock scenarios inside screenshots** | Basket of 4 items, Z-report with variance 0, rice priced 3 ways | Shows the feature working in a real shop |
| 7 | **Fixed feature-block formula** | Bold title + 2-4 word benefit; or title + one sentence | Scannable; every block reads the same |
| 8 | **Industry page = modules re-told for that shop** | Same modules, retail use case written next to each | One engine, many stories |
| 9 | **Industry FAQ in the shop owner's own words** | "Do I need special barcode hardware?" | Answers real objections |
| 10 | **Two CTAs everywhere + microcopy** | "Start free trial" + "Book a demo" / "No credit card required - Cancel anytime" | Low-risk next step |

## 2. Where we beat them (do these on every page)

| Their gap | Our rule |
|---|---|
| Jargon inside bullets (GRN, COGS, WAC, AR aging, IPC) | Plain words only. "Goods received", "cost of goods", "who owes you". Technical term at most in brackets once |
| Fake "placeholder logos" and testimonials missing on industry pages | Only real proof: real counts (catalog sizes, report counts, business types). Testimonials only from real shops with permission |
| Mixed "$" and unlabeled numbers in mockups | Always "Rs", Pakistani items, Pakistani names, Pakistani tax (17%/18% as applicable) |
| CTA label not matching destination ("Watch a 2-min demo" opens a booking page) | Every CTA says exactly where it goes |
| No FAQ on module pages | Every module page and every industry page ends with 5-7 FAQs |
| English only, global tone | Simple Pakistani-shop English; Urdu versions later; local examples (udhaar, kiryana, godown, installments with guarantor) |
| Offline explained with technical words (branch server, queued sales replayed) | "Only your first login needs internet. Sell, manage stock and see reports without internet." |
| Pricing hidden behind "Book a demo" | Honest plan prices on page (monthly + yearly). Installation charges are never on the website; the sales team handles them per client (29 Oct 2026) |

## 3. Copy formulas (write every block like this)

**F1 - Module section**
```
KICKER:   Module name (Sales / Godown / Accounts ...)
H2:       Outcome in 3-7 words ("Your stock count is always right.")
INTRO:    1-2 short sentences: what changes for the owner.
FLOW:     3-5 step strip (see Section 4)
AUTO:     "What happens by itself:" one line
BLOCKS:   3-4 x  **Feature title** - one plain sentence
CTA:      "See <module> in the live demo"  -> live.uptrendpos.com
```

**F2 - Pain -> Fix card (industry pages, 4 cards)**
```
Pain (owner's words, 1 line):  "Udhaar customers forget what they owe."
Fix (1 line, starts with UpTrendPos action): "Every credit sale goes to the customer's account; send the balance on WhatsApp in one tap."
```

**F3 - Feature tile (grids)**: `**Feature name**` + 2-4 word result. e.g. **Works offline** - Never stops selling.

**F4 - Claim headline + proof line**: Claim in 4-7 words, then one line of proof. e.g. "No one can secretly delete a sale." / "Mistakes are fixed with a reversal, so your books keep the full history."

**F5 - FAQ**: question exactly as an owner would ask it on WhatsApp; answer in 2-3 sentences, first word answers it ("Yes." / "No." / "Rs 2,000 a month.").

**F6 - Mock scenario (for screenshots and examples)**: real Pakistani basket in Rs, e.g. 2 x Dalda 1kg, 1 x Surf Excel, 3 x Nestle milk; totals that add up exactly; variance 0 on Z-report must be mathematically correct.

**Writing rules:** sentences under 15 words; one idea per sentence; active voice ("UpTrendPos sends..."); "you / your shop" not "the user"; numbers as digits; no em-dash overload.

## 4. UpTrendPos flow library (ready to use - respect status labels)

Status label decides wording (LIVE = present tense; LAUNCH = "New / with the launch" until Abdul confirms live; NEXT = "Coming soon"; LATER = roadmap only). Confirm each flow's label from the main handoff before publishing.

| Flow | Steps (strip) | "What happens by itself" line | Label (per handoff) |
|---|---|---|---|
| Counter sale | Scan -> Charge (cash / card / udhaar / split) -> Receipt prints | Stock drops and the sale goes into your accounts at the same moment | LIVE core |
| Offline selling | Internet goes -> Keep selling -> Internet comes back -> Everything sends | FBR invoices made offline are sent as soon as the internet returns | LAUNCH (full-offline reports) |
| Buying stock | Purchase order -> Owner approves -> Goods received -> Supplier bill -> Payment | Bonus quantity lowers your real cost; supplier balance updates itself | LAUNCH (approval, bonus qty) |
| Godown to shop | Send stock -> "On the way" -> Shop confirms -> Short / damaged recorded | Damaged stock can never be sold by mistake | LAUNCH |
| Sell now, deliver later | Sale -> Delivery note -> Pending deliveries list -> Delivered | Customer pays once; stock leaves only when delivered | LAUNCH |
| Installment sale | Sale -> Down payment -> Plan + guarantor -> Monthly recovery | Overdue installments raise an alert and show in the defaulters list | LIVE base + LAUNCH reports |
| Udhaar / credit | Credit sale -> Customer account -> Reminder -> Payment received | Over-limit credit needs the owner's approval | LIVE + LAUNCH approval |
| Shift close | Open with cash float -> Sell all day -> Count cash -> Close | Cash over / short is recorded and alerts the owner | LAUNCH alerts |
| Day start for owner | Morning briefing -> Alerts -> Approvals inbox | Yesterday's numbers arrive at the time you choose | LAUNCH |
| Promotions | Create offer -> Test a basket -> Goes live on dates / branches | Receipt shows the offer code; caps stop overuse | LAUNCH |
| Restaurant order | Order (counter / waiter / QR) -> Kitchen ticket -> Ready -> Bill | Late orders change colour on the Order Control board | LAUNCH additions |
| Repair job | Job card -> Add parts + labour -> Ready -> Invoice -> Warranty | Parts used leave stock; warranty is registered with the sale | LAUNCH |
| Salon booking | Booking or walk-in token -> In service -> Done -> Bill | Staff commission and no-show rate tracked | LAUNCH |
| Free trial | Business details -> Category -> Plan -> 14-day trial -> Buy | Data is never deleted; buying opens everything as it was | LAUNCH |
| Online store order | Customer orders -> Confirm by WhatsApp -> Pack -> Courier -> Delivered | COD money tracked until it reaches your bank (Cash Truth) | NEXT - "Coming soon" |
| Order booker / van sale | Route day -> Order booked -> Load sheet -> Deliver -> Day-end settlement | Field cash collected offline, settled at day end | NEXT - "Coming soon" |

## 5. Page templates

**Module / feature page (e.g. Offline POS, Inventory & Godown, Reports & Dashboards, Security)**
1. Hero: outcome H1 + one-line sub + 2 CTAs (Start free trial / Open live demo) + 3 reassurance chips
2. Flow strip (Section 4) with the "by itself" line
3. 3-4 outcome sections (F1), each with a Rs mock scenario screenshot
4. Feature tile grid (F3), 6-12 tiles
5. "Works with" strip (hardware / Android / Windows / web)
6. FAQ (F5), 5-7 questions
7. Closing CTA (outcome line + 2 buttons)

**Industry page (grocery, pharmacy, solar, mobile, tailor, restaurant ...)**
1. Hero: "<Industry> POS software in Pakistan" + outcome sub-line
2. Pain -> Fix grid (F2), 4 cards in that trade's own words
3. "How a day runs" flow strip for that trade
4. 3-4 module sections re-told for that trade (same engine, trade examples)
5. Trade-specific fields (batch/expiry, IMEI, sizes/colours, measurements)
6. **Proof numbers** (real only): e.g. Solar ready-made catalog 1,100+ items; Computer & Mobile catalog 670+ items; 30+ business types; 84 retail reports; 55 alerts (LAUNCH counts - confirm live first)
7. FAQ in that trade's words
8. Closing CTA

**Home page**: outcome H1 -> 8 selling points (handoff Section 15) as F4 blocks -> module sections (F1, short) -> industries grid -> honest pricing teaser -> FAQ -> CTA.

## 6. Site-map ideas taken from their structure (content only)

- Separate pages per module (Inventory, Purchasing, POS, Offline POS, Sales, Accounting, FBR invoicing, HR & Payroll, Dashboards, Alerts, Roles & Permissions, Multi-branch) - each is also an SEO landing page.
- Solutions by industry + by size (single shop / multi-branch / wholesale).
- Compliance hub (FBR Digital Invoicing) as its own page - we already have `website_fbr_pos_integration_v1.html`.
- Security & trust page (2FA, field permissions, no-delete, backups).
- Resources later: guides, case studies (real only).

## 7. Checklist before any page goes live

- [ ] Every feature checked against the handoff status label
- [ ] No competitor name, no copied sentence
- [ ] No technical word (database, server, sync, token, RLS, GRN without explanation)
- [ ] All money in Rs; mock totals add up
- [ ] Every CTA goes where its label says
- [ ] FAQ present (5-7)
- [ ] Proof numbers are real and current
- [ ] Brand spelled "UpTrendPos"; no AGR / AGR Soft
