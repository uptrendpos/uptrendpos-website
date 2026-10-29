# UpTrendPos Website SEO Master Plan (v1, 12 Oct 2026)

## 1. Standing rules for every page
- Brand name is always "UpTrendPos" (never UpTrendPOS / Uptrend POS) in titles, meta, content and alt text.
- Very simple English. Short sentences, point to point. Write for a Pakistani shop owner, not a native English reader.
- One exact focus keyword per page. It must appear in: SEO title (at the start), meta description, URL slug, H1, first paragraph, at least one H2, one image alt, and about 0.8 to 1.2 percent of the body text. No two pages share a focus keyword (no cannibalization).
- Only built features. No fake numbers, no fake reviews, no "No.1 / Pakistan's first / best" claims, no prices in content except on the pricing page.
- EEAT: real company (UpTrendPos team, Sahiwal; never mention AGR / AGR Soft), real phone 0319 2223292, sales@uptrendpos.com, honest limits ("depends on your plan"), outbound link to an official source (FBR, DRAP, Microsoft, etc.).
- Links inside the page code: home, pricing, download page, contact, 2 to 3 related industry pages, the industries hub, and at least one outbound authority link.
- Design: vidzvalley.com style + logo blue #024691 / green #2FA455 / ad yellow #FAE814 with navy #10224A text, Poppins. Yellow is a background only, always with navy text.
- Code: page widget holds HTML content only. All CSS and JS live once in the WPCode snippet "UpTrendPos Design System". No HTML comments, no style or script tags inside a page widget. Schema comes from Rank Math, not from the widget.
- Rank Math score is checked inside the Elementor editor (Rank Math tab), not on the WordPress edit screen.
- Every page stays noindex until it is designed. On launch day: switch to index, add its slug to UTP_LIVE_PAGES in the snippet, purge cache, request indexing in Search Console.

## 2. Core pages
| Page | URL | Focus keyword | SEO title | Status |
|---|---|---|---|---|
| Home | / | POS software in Pakistan | POS Software in Pakistan: Easy & FBR Ready \| UpTrendPos | v1 code ready (12 Oct) |
| Downloads | /download-pos-software/ (301 from /downloads/) | download POS software | Download POS Software for PC, Android & Web \| UpTrendPos | v4 code ready (12 Oct) |
| Industries hub | /industries/ | industry-specific POS software | Industry-Specific POS Software for 30+ Shops \| UpTrendPos | Day 2 |
| Pricing | /pos-software-pricing/ | POS software pricing | POS Software Pricing in Pakistan: 3 Easy Plans \| UpTrendPos | full page v1 code ready (13 Oct) - replaces block v3 |
| About | /about-uptrendpos/ (confirmed live 13 Oct) | UpTrendPos | About UpTrendPos \| POS Software Company in Pakistan | v1 done (12 Oct) |
| Contact | /contact-us/ | free POS software demo | Free POS Software Demo on WhatsApp \| Contact UpTrendPos | v1 code ready (13 Oct) |

## 3. Industry pages (32) - locked slugs and focus keywords
SEO title pattern: "<Focus keyword in Title Case> in Pakistan | UpTrendPos" (max 60 characters).

| # | Card name | Slug under /industries/ | Focus keyword | Exists? |
|---|---|---|---|---|
| 1 | Grocery & Kiryana Store | grocery-store-pos-software | grocery store POS software | yes |
| 2 | Pharmacy & Medical Store | pharmacy-pos-software | pharmacy POS software | yes |
| 3 | Clothing & Garments | clothing-store-pos-software | clothing store POS software | yes |
| 4 | Shoes & Footwear | shoe-store-pos-software | shoe store POS software | yes |
| 5 | Tailoring & Boutique | tailor-shop-pos-software (was tailor-shop-software, 301) | tailor shop POS software | yes - change slug |
| 6 | Cosmetics & Beauty Store | cosmetics-store-pos-software | cosmetics store POS software | yes |
| 7 | Baby & Diaper Store | baby-store-pos-software | baby store POS software | yes |
| 8 | Undergarments & Hosiery | undergarments-shop-pos-software | undergarments shop POS software | new |
| 9 | Electronics & CCTV Shop | electronics-store-pos-software | electronics store POS software | yes |
| 10 | Solar Shop | solar-shop-pos-software | solar shop POS software | yes |
| 11 | Electrical & LED Lighting | electrical-store-pos-software | electrical store POS software | new |
| 12 | Mobile & Computer Shop | mobile-shop-pos-software | mobile shop POS software | new |
| 13 | Battery Shop | battery-shop-pos-software | battery shop POS software | new |
| 14 | Hardware, Sanitary & Building Material | hardware-store-pos-software | hardware store POS software | new |
| 15 | Paint Store | paint-store-pos-software | paint store POS software | new |
| 16 | Glass & Aluminium Shop | glass-shop-pos-software | glass shop POS software | new |
| 17 | Auto Spare Parts | auto-parts-pos-software | auto parts POS software | new |
| 18 | Tyre Shop | tyre-shop-pos-software | tyre shop POS software | new |
| 19 | Jewellery & Gold Shop | jewellery-shop-pos-software | jewellery shop POS software | new |
| 20 | Artificial Jewellery Shop | artificial-jewellery-shop-pos-software | artificial jewellery shop POS software | new |
| 21 | Watch Shop | watch-shop-pos-software | watch shop POS software | new |
| 22 | Perfume & Attar Shop | perfume-shop-pos-software | perfume shop POS software | new |
| 23 | Bags & Luggage | bag-shop-pos-software | bag shop POS software | new |
| 24 | Toys & Gift Shop | toy-shop-pos-software | toy shop POS software | new |
| 25 | Sports Goods | sports-shop-pos-software | sports shop POS software | new |
| 26 | Stationery & Book Shop | stationery-shop-pos-software | stationery shop POS software | new |
| 27 | Crockery & Household Shop | crockery-shop-pos-software | crockery shop POS software | new |
| 28 | Furniture Shop | furniture-shop-pos-software | furniture shop POS software | new |
| 29 | Poultry, Meat & Seafood | meat-shop-pos-software | meat shop POS software | new |
| 30 | Agri Inputs (Seed, Fertilizer & Pesticides) | fertilizer-shop-pos-software | fertilizer shop POS software | new |
| 31 | Veterinary Store | veterinary-store-pos-software | veterinary store POS software | new |
| 32 | Vape & Pan Shop | vape-shop-pos-software | vape shop POS software | new |

Note: the ads list says "Electronics, Solar & CCTV" as one business type. On the website it is two pages (Electronics & CCTV, Solar Shop) because people search for them separately. Total = 31 business types, 32 pages.

Cannibalization guards: Clothing (readymade) vs Tailor (stitching orders) vs Undergarments; Electronics/CCTV vs Electrical/LED; Hardware vs Paint vs Glass; Jewellery (gold rate) vs Artificial Jewellery; Pharmacy vs Veterinary. Each page must describe its own workflow, not a copy of another page.

## 4. Two pages a day (re-planned 13 Oct 2026 after the Blueprint v2 merge)
| Day | Pages | Status |
|---|---|---|
| 1 (12 Oct) | Home + Downloads | done |
| extra (12 Oct) | About | done |
| 2 (13 Oct) | Pricing + Industries hub | done (hub v1 13 Oct) |
| 3 | Grocery & Kiryana (done early 13 Oct) + FBR POS Integration | FBR page = Blueprint "win the FBR cluster first" |
| 4 | Pharmacy & Medical + Tailoring & Boutique | |
| 5 | Mobile & Computer + Electronics & CCTV | |
| 6 | Solar Shop + Electrical & LED Lighting | |
| 7 | Clothing & Garments + Shoes & Footwear | |
| 8 | Cosmetics & Beauty + Baby & Diaper | |
| 9 | Hardware, Sanitary & Building Material (Contact done early, 13 Oct) | |
| 10 | Paint Store + Auto Spare Parts | |
| 11 | Tyre Shop + Jewellery & Gold | |
| 12 | Artificial Jewellery + Watch Shop | |
| 13 | Perfume & Attar + Bags & Luggage | |
| 14 | Toys & Gift + Sports Goods | |
| 15 | Stationery & Book + Crockery & Household | |
| 16 | Furniture + Poultry, Meat & Seafood | |
| 17 | Agri Inputs + Veterinary Store | |
| 18 | Glass & Aluminium + Undergarments & Hosiery | |
| 19 | Vape & Pan + Battery Shop | |
| 20 | FBR Digital Invoicing (product page only if live in production, else guide + waitlist) + Features hub | |
| 21-23 | 6 feature pages: Offline POS, Inventory, Udhaar Khata, Installments, Accounting, Multi-Branch | |
| 24 | Privacy Policy + Terms | |
| 25 | Support + custom 404 | |
| after | Blog: 12 guides, 2 per week (Blueprint 10.1) | |

## 5. Industry page template v2 (same for all 32; Blueprint 8.1 merged)
1. Visible breadcrumb: Home > Industries > Page (Rank Math breadcrumbs ON, gives BreadcrumbList schema).
2. Hero: kicker, H1 with focus keyword, 40-60 word direct answer, 2 CTAs (Start free trial + WhatsApp demo), compliance ticks (text only: Works offline / FBR-ready invoices / Windows, Android and Web), watermarked trade-specific image (WebP, keyword alt).
3. H2 Problems this shop faces (4 real pains in the owner's words, each with the fix).
4. H2 Features built for this shop (6 x H3, at least 60% trade-specific, only what the app has for that vertical).
5. H2 How it works at your counter (3-4 steps).
6. H2 Keep billing during load-shedding (paragraph written fresh for this trade).
7. H2 Reports this owner checks daily (3 named reports).
8. H2 FBR-ready receipts (retail pages only, about 80 words + link to the FBR POS page with anchor "FBR invoice and QR code on every receipt").
9. H2 Which plan fits this shop (plan-fit line + link "compare UpTrendPos plans" to Pricing).
10. Customer story (only when real, with permission).
11. H2 FAQs: 6, answers 40-60 words, first sentence is the answer. Pattern: best [trade] software in Pakistan / offline in load-shedding / track [expiry, IMEI, measurements, kist] / how much does it cost (link Pricing) / udhaar customers / more than one branch or counter.
12. Related business types (3 ring links + hub) + final CTA.
Words 1,200-1,800. Internal links 3-6 in body, never two identical exact-match anchors to one URL. Outbound 1-2 regulator links only (fbr.gov.pk, DRAP for pharmacy, etc.).
Secondary keywords: add the Pakistani phrasing as Rank Math secondary keywords and use them in H2/FAQ, never in the title: "medical store software", "kiryana store software", "garments shop software", "mobile shop software", "udhaar khata", "kist", "hisab kitab".

## 6. Open items found on 12 Oct
- Junk page "h1" is published (default SEO title) - move to Trash or Draft.
- Industries hub has the default title %title% and %excerpt% - set on Day 2.
- Tailor page SEO title "Tailor Shop POS Software for Boutiques in Pakistan" has no brand and is 50+ characters; change to "Tailor Shop POS Software in Pakistan | UpTrendPos" with the new slug.
- Pricing, Privacy, Support, Terms titles/meta use "UpTrendPOS"; Pricing title has "2026"; Support meta claims "24/7" - align.
- Live homepage claims to remove: "Pakistan's first", "100+ startups", "30-day free trial" (real = 14 days), "free basic plan", "PRAL Sales Tax Compliant", visible editor notes in two FAQ answers, several H1 tags.
- Customer logos and 4 testimonials on the live homepage: keep only if they are real customers who agreed. Send names and permission, and a real testimonials section will be added.
- Official address (confirmed by Abdul): House No 193/A, Umer Block, Shadab Town, Sahiwal 57000, Punjab, Pakistan - use it everywhere (footer, schema, Rank Math Local SEO, contact page).
- Two snippet plugins are installed (WPCode and Code Snippets). Use WPCode only.

## 7. Pricing page v1 (13 Oct 2026)
- Plans (updated by Abdul 13 Oct 2026): Premium Rs 2,000/mo, Rs 24,000/yr (1 branch, 3 users); Enterprise Rs 3,000/mo, Rs 36,000/yr (2 branches, 6 users, Recommended); Custom Rs 6,000/mo, Rs 72,000/yr (3 branches, 9 users). Unlimited invoices on all.
- Yearly toggle shows 10% off the first year (Rs 21,600 / 32,400 / 64,800), taken from Abdul's own pricing block. Admin yearly fee is still 12x monthly - sales must apply the 10% by hand until admin supports it.
- One-time setup fee mentioned without an amount. 14-day free trial. No free plan.
- Compare table follows the admin module flags exactly (Premium locks barcode labels, FBR, installments, share links, white-label, P&L, audit, attendance, commission, payroll; Enterprise locks staff commission, attendance and payroll; Custom has all).
- 6 watermarked hardware images (WebP, 28-58 KB) uploaded to /wp-content/uploads/: uptrendpos-pos-hardware-set, -windows-pc-pos, -thermal-receipt-printer, -barcode-scanner, -android-tablet-pos, -android-phone-pos. Generator: site/hw/gen_hw.py.
- Schema: SEO snippet price range now 2000-6000, offerCount 3.

## 8. Blueprint v2 (1 Oct 2026) merged on 13 Oct 2026
Source: UpTrendPos_SEO_Implementation_Blueprint.docx (Blueprint v2). Rule: where the blueprint and a later decision differ, the later decision stays. Everything this plan already does beyond the blueprint stays too.

### 8.1 Already done (blueprint item -> our state)
- Bot block / robots.txt -> fixed 3 Oct (single User-agent * group + sitemap).
- One H1, keyword-first titles 50-60, metas 140-158, self canonical -> applied on Home, Downloads, About, Pricing.
- Claim audit -> removed "Pakistan's first", iOS, PRA/SRB, 30-day trial, 100+ startups, free plan, fake rating, unverified counters.
- Schema graph (Organization, WebSite, SoftwareApplication, FAQPage from visible FAQs), no aggregateRating -> UpTrendPos SEO Snippet.
- Static HTML prices, FAQs and compare table (no JS-loaded content) -> Pricing v1.
- Single plan ladder that matches Super Admin -> Pricing v1 (Premium / Enterprise / Custom).
- WebP images with width/height and descriptive file names -> pricing hardware images (watermarked, our extra).
- Lead tracking -> data-track CTA events + (13 Oct) automatic utp_contact_click for every WhatsApp, call and email link.

### 8.2 Kept as OUR decision (blueprint item not used)
- Brand spelling "UpTrendPos" everywhere (blueprint said UpTrendPOS) - Abdul's 12 Oct rule.
- Industry slugs /industries/<x>-pos-software/ (blueprint said /pos-software-for-<x>/) - locked 12 Oct.
- No AGR / AGR Soft anywhere (blueprint About title "by AGR Soft" dropped).
- Pricing focus "POS software pricing", no "2026" in title, no free plan (blueprint: "POS software price in Pakistan", free plan). Use "POS software price in Pakistan" as a SECONDARY keyword on Pricing.
- Downloads slug /download-pos-software/ (blueprint /download/).
- 32 industry pages from the admin category list. Blueprint pages for Automotive hub, Car Showroom, EV, Motorcycle, Restaurant, Apparel are ON HOLD until those verticals are active in Super Admin.
- Industry focus keywords stay "<trade> POS software"; the blueprint's "<trade> software" phrasing becomes the secondary keyword.

### 8.3 Pending - page work (built into the schedule above)
- FBR POS Integration page (Day 3): 1,800-2,200 words, outline from Blueprint 7.2, cited FBR facts from Blueprint 7.1 (re-check every SRO on fbr.gov.pk), annotated receipt image (own invoice no, FBR number, QR, Re 1 fee), returns = credit note only, never "FBR approved / certified / licensed integrator", no FBR logo. Need from Abdul/Hamza: is FBR production live for customers, and current live slug of the FBR page.
- FBR Digital Invoicing page (Day 20, conditional on production status).
- Features hub + 6 feature pages (Days 20-23).
- Contact page (Day 9): demo form (name, business type, city, phone), support hours, onboarding steps, contact FAQs, map, links to Pricing and Download.
- Privacy, Terms, Support, custom 404 (Days 24-25).
- Blog: 12 guides (Blueprint 10.1), named author, last-updated date, cited sources, app screenshots.
- Home v2 later: grow from about 1,450 to about 2,500 words with H2s for accounting, "UpTrendPos vs register vs basic billing app" table, data safety (confirmed controls only), hardware; FAQ answers to 40-60 words.
- Pricing v1.1 (small): add secondary keyword "POS software price in Pakistan" in one H2 + one FAQ, onboarding timeline, "Are there hidden charges?" FAQ, FAQ answers to 40-60 words, one Offer per plan in schema.

### 8.4 Pending - site-wide (not page design)
- Rank Math: enable breadcrumbs; add secondary keywords per page; site language en-PK (via SEO Snippet filter if WP has no en-PK).
- OG image 1200x630 per page (generate with the hardware image generator, watermarked) + Twitter summary_large_image.
- Header: Industries mega menu, Features, FBR, Pricing, Resources, Contact, Login (live.uptrendpos.com), button "Start Free". Footer: all money pages + NAP identical to Google Business Profile.
- Mobile sticky bottom bar with WhatsApp + Call (ready to add to the Design System snippet on approval).
- live.uptrendpos.com: noindex on login and app routes.
- Check one host version: https://uptrendpos.com with 301 from www and http.
- Search Console + Bing Webmaster: verify, submit sitemap_index.xml, request indexing for each page as it goes live.
- GTM: map utp_cta_click, utp_download_click, utp_contact_click to GA4 key events.
- Core Web Vitals targets: LCP < 2.5s on 4G, INP < 200ms, CLS < 0.1.

### 8.5 Pending - authority (off-page)
- Google Business Profile (Software company, real address, photos, weekly posts, review link to every onboarded shop).
- Directories: SoftwareSuggest, GoodFirms, Capterra/GetApp, TechnologyCounter (same description + screenshots).
- Google Play listing optimised for "POS software" and "billing app".
- YouTube: one Urdu demo per industry page, embedded on that page.
- One press story (ProPakistani / TechJuice / Business Recorder) + 3 partner links (hardware sellers, tax consultants).
- Backlink gap vs Oscar POS, Moneypex, LookPOS, XStak. No paid link packages or PBNs.
- Real numbers (shops, cities, invoices) and case studies only from real data with an as-of date.

### 8.6 Standing rules added from the blueprint
- FAQ answers 40-60 words, first sentence is the direct answer (AI Overviews lift these).
- Compliance badges are text only; never an official FBR logo; never "FBR approved / certified / licensed integrator".
- Security claims only for confirmed controls: tenant-separated data, role-based access with PIN, audit trail (Enterprise+), backup and restore.
- Pakistani search phrasing (software, kiryana, medical store, udhaar, khata, kist) goes in H2s, body and FAQs; English head term stays in title and H1.
- Every money page within 2 clicks of Home.

## 9. Contact page v1 (13 Oct 2026)
- Root "utp utp-ct". Sections: hero (WhatsApp + call CTAs, watermarked demo image), 4 contact cards (WhatsApp, phone, email, office/Maps), demo form card + "what you see in a demo", 4 next steps, "keep ready" list + FBR details band (fbr.gov.pk), office band with Google Maps embed, 7 FAQs (40-60 words), final CTA.
- Fluent Forms: form id 1 ([fluentform id="1"]). Use the Fluent Forms widget or a Shortcode widget with [fluentform id="1"] in the SAME Elementor container, directly under the HTML widget. The Design System JS moves the form into the designed card on the live page (not in the editor) and hides the empty widget. Suggested fields: Name, WhatsApp number, Business type (dropdown), City, Message (optional).
- Keyword "free POS software demo" 8x (0.94%, 852 words). Meta: "Book a free POS software demo on WhatsApp or call 0319 2223292. See UpTrendPos for your shop type and get help with setup, prices and FBR."
- Image watermark made softer on all images (13 Oct, Abdul): diagonal text 3% opacity, centre logo 4.5%, small corner logo.
- Map embed uses the exact pin 30.64995021748812, 73.1160202245369 (no business name shown); Office card and "Get directions" button open Abdul's Google Maps place link.
- 13 Oct (fix): the shortcode [fluentform id="1"] now sits inside the contact page code (form card). The UpTrendPos SEO Snippet runs it inside Elementor HTML widgets, so no separate Fluent Forms widget is needed (remove it if added).

## 10. Home v2 + About v1.1 (13 Oct 2026, Abdul's request)
- Home order: hero > ticker > "Is your shop still running on a register?" problem cards as an auto-running slider (8 cards) > Businesses that trust UpTrendPos > industries (moved right under the logos) > features > offline > hardware (new, uses uptrendpos-pos-hardware-set.webp, links Pricing #utp-hardware) > FBR band > "Paper register vs POS software in Pakistan" table (new) > steps > about > plans > FAQ (answers 40-60 words, real prices) > final CTA. Keyword 17x (0.91%, 1,866 words).
- About: hero is now image uptrendpos-about-made-in-pakistan.webp (1200x900); story image uptrendpos-register-to-pos-software.webp (paper register vs udhaar khata on phone); office link uses the exact pin 30.64995021748812,73.1160202245369; FAQ answers 40-60 words. Brand keyword 1.58%.
- Pricing: hardware section now has id="utp-hardware" (linked from Home).
- 13 Oct (follow-up): Home has ONE slider only. The blue ticker was merged into the white problem-card slider (now 12 cards: the 8 problems + devices, branches, 30+ shop types, free updates) placed right under the hero; the blue ticker stays on About and Pricing.
- 13 Oct (final home order, Abdul): hero > Businesses that trust UpTrendPos (logo slider) > 30+ shop types > "Is your shop still running on a register?" card slider > features > offline > hardware > FBR > register vs app > steps > about > plans > FAQ > final. Sliders are kept apart (never two in a row).

## 11. Global footer v1 (13 Oct 2026)
- File: claude/website_footer_v1.html. Paste into ONE HTML widget inside the site-wide footer template (Jeg Kit > Footer, condition Entire Site). CSS and JS live in the Design System snippet.
- Root class is "utp-foot" (NOT "utp"), so it never interferes with page layout code on pages without our design (blog, legal pages).
- Sections: CTA row (free trial + WhatsApp demo), brand (white logo uptrendpos-logo-white.png, short line, Windows/Android/Web chips, Facebook/Instagram/YouTube/LinkedIn), Company links, Business types (live-gated via UTP_LIVE_PAGES, plain text until live; "All 30+ business types" goes to Home #utp-industries), Get in touch (address -> exact map pin, phone, email), bottom bar (auto year, Privacy, Terms, Support).
- Legal URLs assumed: /privacy-policy/, /terms-and-conditions/, /support/ - confirm with Abdul.
- Footer links use p.uf-h labels (no H tags) so page heading structure stays clean.


## 12. Industries hub v1 + Grocery & Kiryana v1 (13 Oct 2026)
- Files: claude/website_industries_hub_v1.html (root "utp utp-hub") and claude/website_grocery_v1.html (root "utp utp-gro"). Design System updated the same day (industry-page CSS + UTP_LIVE_PAGES now has 'industries' and 'grocery-store-pos-software').
- Hub: slug /industries/, focus "industry-specific POS software", title "Industry-Specific POS Software for 30+ Shops | UpTrendPos" (57), meta "Industry-specific POS software for 30+ shop types in Pakistan. Pick your business type and get ready units, fields and reports. Works offline." (142). Keyword 12x (0.91%, 1,320 words). Sections: breadcrumb hero + image, 3 steps, 32 type cards in 7 groups (each with a one-line trade feature, live-gated links), not-listed callout, 8 core features, basic billing app vs industry-specific table, local team + facts, 6 FAQs, final CTA.
- Grocery: slug /industries/grocery-store-pos-software/, focus "grocery store POS software", title "Grocery Store POS Software in Pakistan | UpTrendPos" (51), meta "Grocery store POS software for kiryana shops in Pakistan. Bill on your phone, print with a Type-C printer, send bills on WhatsApp and track udhaar." (147). H1 changed to "Grocery store POS software for kiryana shops." Keyword 16x (0.87%, 1,845 words). Secondary keywords: kiryana store software, udhaar khata, kiryana POS.
- Grocery USP (Abdul): phone-only shops - bill on Android, print with a small thermal printer by USB Type-C, or with no printer send bill (picture/PDF), khata statement and day report on WhatsApp. Sections: hero, blue ticker, jump nav, USP rows (2 images), 3 setups (phone / phone + Type-C printer / counter PC), 4 problems, 6 features, 4 counter steps, load-shedding sync row (cash offline, udhaar needs internet), 3 daily reports + image, FBR band (gated link to /fbr-pos-integration/ - confirm slug), plan fit (no prices), 8 FAQs, related ring (pharmacy, baby, crockery, meat, hub), final CTA.
- Images (WebP 1200x900, 39-45 KB, same soft watermark, official logo): uptrendpos-industry-specific-pos-software, uptrendpos-grocery-store-pos-software, uptrendpos-mobile-pos-type-c-thermal-printer, uptrendpos-send-bill-on-whatsapp, uptrendpos-grocery-daily-reports. Generator: claude/industry_images_generator.py. Upload to /wp-content/uploads/ with the same names.
- Image policy (Abdul 13 Oct: site must not look like AI work): no AI photo-real people or shops. Use device/UI scenes now; replace with real photos of a real kiryana counter (with the owner's permission) and real app screenshots using the SAME file names, so no code change is needed.
- Sada Hisab /industries/ audit (13 Oct): 10 blog-style cards, no visible H1, no FAQs, card images named Gemini_Generated_Image (AI), blank alts, pharmacy in meta but no pharmacy card, bakery card excerpt says grocery, "1st" superlative. Their grocery page: ~1,200 words, cloud-only, no offline, no udhaar, no mobile printing, no WhatsApp bill, bakery copy-paste alt text. Our edge = phone + Type-C printing, WhatsApp bills, udhaar khata, offline, 8 FAQs, honest claims.
- Legal URLs found live: /privacy-and-policy/ and /terms-conditions/ (footer links /privacy-policy/ and /terms-and-conditions/ were broken). Recommended: change the two page slugs to /privacy-policy/ and /terms-and-conditions/ + 301 from the old slugs (footer then needs no change). /support/ is correct. Titles/metas: "Privacy Policy | UpTrendPos", "Terms and Conditions | UpTrendPos", "Support and Help Center | UpTrendPos"; remove "24/7" from Support meta (page says Mon-Sat 10-7); Terms mention a Free plan after trial while Pricing says no free plan - Abdul to decide and align.

- 13 Oct (v2, Abdul): Grocery page rebuilt to Sada Hisab depth and beyond = claude/website_grocery_v2.html (replaces v1; same slug, title, meta and focus keyword). 3,097 words, keyword 26x (0.84%), 11 FAQs (40-51 words). New sections: 6 problems (problem + fix), "what you can do" 6 cards, 6 feature groups with 7-8 checklist items each and plan tags (Enterprise+ / Custom), hardware tree image + 6-item hardware list, stock-in-to-profit process image + 5 steps, 6 numbered benefits, more-reports chips, safety + FBR duo cards, 6 grocery business types (small kiryana, mini mart, supermarket, wholesale kiryana, chain, phone order/delivery). Kept: hero, ticker, phone USP rows, 3 setups, load-shedding sync row, daily reports, plan fit, related, final CTA. No SRB/PRA claims (Sada Hisab claims them; we only do FBR).
- New images: uptrendpos-grocery-pos-hardware.webp, uptrendpos-grocery-pos-process.webp (generator claude/industry_images_generator.py). Upload all 7 industry images.
- UpTrendPos SEO Snippet v2026-10-13e: hub = CollectionPage + ItemList of LIVE industry pages (published + not noindex, automatic), BreadcrumbList when Rank Math has none, page image (primaryImageOfPage) from config, audience map for all 32 slugs, SoftwareApplication featureList. Standing rule (Abdul 13 Oct): every page delivery includes the page HTML + full Design System + full SEO Snippet + images + Rank Math values together.
- Featured image: set the page's hero WebP as the WordPress Featured Image so Rank Math uses it for og:image.


## 13. Industry template v3 = Grocery v2 structure (STANDING, Abdul 13 Oct 2026)
Every other /industries/ page follows claude/website_grocery_v2.html: long page, complete spec detail, so an owner of that trade gets everything on one page. Same design classes, same section order, written fresh for each trade.
1. Hero: breadcrumb, kicker, H1 with exact focus keyword, 40-60 word direct answer, 2 CTAs, 3 ticks, trade hero image.
2. Blue ticker (8 trade points) + jump nav.
3. 6 problems of THIS trade (problem line + fix line).
4. Trade USP rows (2 image rows) - the 1-2 things this trade cares about most (pharmacy: salt search + 17,000 medicines; tailor: measurements + delivery dates; mobile: kist + warranty).
5. "What you can do" 6 cards (3 lines each).
6. Features in full detail: 6 groups x 7-8 checklist items, plan tags (Enterprise+ / Custom). At least 60% trade-specific; only built features.
7. Hardware for this trade (tree image + 6-item list).
8. Setups (phone / phone + Type-C printer / counter PC) - keep for retail trades, adapt wording.
9. Process image + 5 steps (trade workflow, e.g. tailor: measurement > order > stitching > ready > delivery).
10. Load-shedding block written fresh for the trade.
11. 6 numbered benefits.
12. Daily reports (3) + more-reports chips.
13. Safety + FBR duo cards (FBR only for retail trades).
14. 6 sub-types of this trade (e.g. pharmacy: retail chemist, hospital pharmacy counter, wholesale medicine, chain...).
15. Plan fit (no prices) + 10-11 FAQs (40-60 words, first sentence answers) + related ring (3-4 + hub) + final CTA.
Length 2,500-3,200 words, focus keyword 0.8-1.0%, 2 new images per page (hardware tree + process) besides the hero.
Cannibalization guards: one exact focus keyword per page; never reuse another page's H1/H2 wording; problems, USP, features, process and sub-types must be about that trade only; shared blocks (load-shedding, safety, setups) must be re-written in the trade's own words; pairs to watch: Clothing vs Tailor vs Undergarments, Electronics/CCTV vs Electrical/LED vs Solar vs Mobile vs Battery, Hardware vs Paint vs Glass, Jewellery vs Artificial Jewellery, Pharmacy vs Veterinary vs Cosmetics vs Baby, Grocery vs Meat vs Crockery.


## 14. Legal + Support pages v1 (13 Oct 2026)
- Slugs now live (Abdul moved them): /privacy-policy/, /terms-and-conditions/, /support/ - footer links correct, add 301s from /privacy-and-policy/ and /terms-conditions/ if not done.
- Files: claude/website_privacy_v1.html, claude/website_terms_v1.html (root "utp utp-legal": small hero + last updated chips, sticky contents list, "short version" card, numbered sections, tables, contact block) and claude/website_support_v1.html (root "utp utp-sup": 4 channels, priority/reply-target table, details checklist + stay-safe card, 6 quick-fix cards, included vs not included, data/export/deletion, escalation band, 6 FAQs).
- Rank Math: Privacy = focus "UpTrendPos privacy policy", title "Privacy Policy | UpTrendPos", meta "Read the UpTrendPos privacy policy: what data we collect, why, who we share it with, how we protect it and how you can export or delete it." Terms = focus "UpTrendPos terms and conditions", title "Terms and Conditions | UpTrendPos", meta "UpTrendPos terms and conditions for the web, Android and Windows apps: trial, plans, payments, refunds, offline use, FBR and your data." Support = focus "UpTrendPos support", title "Support and Help Center | UpTrendPos", meta "Get UpTrendPos support on WhatsApp, phone or email in Urdu or English. Monday to Saturday, 10 am to 7 pm. Quick fixes and reply times." All three index.
- Removed: "POS Software" as provider name (now UpTrendPos + Sahiwal address), "moves to the Free plan" (now "limited access", data kept), 24/7 claim. Added: data roles, website visitors, WhatsApp/SMS sharing, data location, breach notice, retention table, privacy request process (30-day aim), PECA 2016 + ETO 2002, setup fee, taxes on invoice, hardware/third-party services, indemnity, force majeure, general clauses, support priorities, quick fixes, scope, escalation, security reporting, anti-fraud note.
- Business decisions Abdul must confirm: reply targets (2 working hours / same day / 1 day / 3 days), "support included in every paid plan", setup fee non-refundable once work starts, limited-access wording after trial, registered legal entity name (if any, add it in Terms section 1 - no AGR per standing rule).
- SEO Snippet v2026-10-13f: Home > page breadcrumbs for the 3 pages; Organization gets a customer-support ContactPoint with Mon-Sat 10:00-19:00 hours.

## 15. FBR POS Integration v1 + Pharmacy v1 + Grocery v2.1 (14 Oct 2026)
- **FBR page** `/fbr-pos-integration/` (root page, not under /industries/). Focus keyword "FBR POS integration" (0.98%). Root `utp utp-fbr`. Highest-intent lead page.
  - Sections: hero (receipt image), dark risk band (Rs 500k to 3m penalty, 60% input tax, sealing, 24-hour offline rule, with sources), interactive Tier-1 checker (7 FBR booklet categories, ticks go into the WhatsApp message, dataLayer `utp_tier1_check`), 9 features, 5 steps + image, invoice anatomy, Practice/Sandbox/Production table, "you keep ready / our team does", load-shedding + buyer verification, retailer chips, POS integration vs digital invoicing, separate FBR app vs built-in table, plan strip, 11 FAQs, final CTA + disclaimer.
  - Honesty rules: never "FBR approved / certified / licensed integrator", no FBR logo. Integration goes through a licensed integrator (PRAL, free). Practice bills are NOT FBR invoices. Penalties shown with section numbers + "not tax advice".
- **Pharmacy page** `/industries/pharmacy-pos-software/`. Focus "pharmacy POS software" (0.87%); secondary "medical store software", "pharmacy software in Pakistan". Template v3. Root `utp utp-gro utp-ph`.
  - Unique angle vs grocery: 17,000+ medicine catalog (every plan, search + tick, no prices or stock, own items allowed), salt search with strength/form chips, Rx badge + controlled "prescription checked" tick, batch/expiry/FEFO, box-strip-tablet packing via GRN, rack number, DRAP Reg No, 16 product types, distributor returns. 11 FAQs.
- **Grocery v2.1**: ~7,000-product catalog added (lead, ticker, stock feature list, new FAQ = 12 FAQs). 0.82%.
- **Standing rule:** before planning any business-type page, ask Abdul how many catalog products are pre-loaded.
- Images (gen_fbr_pharm.py): uptrendpos-fbr-pos-invoice-qr, uptrendpos-fbr-pos-integration-steps, uptrendpos-pharmacy-pos-software, -medicine-catalog, -salt-search-expiry, -pos-hardware, -pos-process.
- Design System: risk band + checker CSS/JS; UTP_LIVE_PAGES now also `pharmacy-pos-software`, `fbr-pos-integration`.
- SEO Snippet 2026-10-14a: `simple_pages` + new `page_images` for fbr-pos-integration; pharmacy image in `industry_pages`.
- Open with Abdul: Simulated-mode QR must say "not an FBR invoice"; confirm offline FBR bills auto-report on reconnect; confirm integrator route (PRAL); confirm grocery catalog uses the same search-and-tick flow.

## 16. Tailoring & Boutique v1 + Mobile & Computer Shop v1 (14 Oct 2026)
- Both built with the shared renderer `industry.py` (template v3) - content lives in build_tailor.py / build_mobile.py, so every next industry page = one content file.
- **Tailor** `/industries/tailor-shop-pos-software/` (old slug /tailor-shop-software/ -> 301). Focus "tailor shop POS software" (0.86%), secondary "tailor shop software", "tailoring software", boutique. Catalog: ZERO pre-loaded (no catalog claim). Root `utp utp-gro utp-tl`. 11 FAQs.
  - Built (Abdul 14 Oct): sizes per customer (shalwar kameez, coat, waistcoat...), unique ID + phone, old register number typed as customer ID, size update on next order, referral customer, all search, stitching order with delivery date, status booked > cutting > stitching > ready > delivered, advance/balance, cutting + stitching master from employees, per-piece/commission (shown as Custom plan = Staff Commission module), order slip thermal/A4/WhatsApp, separate workshop size slip (like kitchen print), udhaar + accounts as standard.
  - Coming soon (tagged on page with `.utp-ptag.soon`): customer app with a notification at every status; ready-made suits + fabric sale on the same counter. Remove the tag when shipped.
- **Mobile** `/industries/mobile-shop-pos-software/` (new page). Focus "mobile shop POS software" (0.87%), secondary "mobile shop software", "computer shop", IMEI. Catalog: 700+ mobile and computer products. Root `utp utp-gro utp-mb`. 11 FAQs.
  - Built: IMEI/serial from purchase (GRN) to sale, warranty lookup module, qist (Customer Installments = Enterprise+), quick bill, calculator, PO/GRN, vendors, customers, accounts, backup, FBR, multi-login, cash sessions, WhatsApp + thermal invoices.
  - NOT in this vertical: repair job cards (separate category) - never claim. Buy-back: coming soon tag. Easyload: not claimed.
- Images (hw/gen_tailor_mobile.py): uptrendpos-tailor-shop-pos-software, -tailor-customer-measurements, -tailor-order-tracking, -tailor-shop-pos-hardware, -tailor-shop-pos-process; uptrendpos-mobile-shop-pos-software, -mobile-shop-product-catalog, -mobile-shop-imei-warranty-installments, -mobile-shop-pos-hardware, -mobile-shop-pos-process.
- Design System: `.utp-ptag.soon` style; UTP_LIVE_PAGES + tailor-shop-pos-software, mobile-shop-pos-software. SEO Snippet 2026-10-14b: page images for both.

## 17. Solar Shop v1 + Electronics, Appliances & CCTV v1 (14 Oct 2026)
- **Page split decision (Claude, approved to proceed by Abdul):** the app has ONE category "Electronics/Solar/Home Appliances/CCTV" with one 600+ catalog (click to add). Website = 2 pages, not 4: Solar (own search intent, biggest growth market, own ad audience) + Electronics page that also covers Home Appliances and CCTV (same catalog/features; 4 near-identical pages = doorway/thin-content risk and split authority). CCTV ads land on `/industries/electronics-store-pos-software/#utp-cctv`. A separate CCTV page only if Search Console later shows demand.
- No slug change, no redirect. WordPress title of the electronics page -> "POS Software for Electronics, Home Appliances & CCTV Shop". Hub card renamed "Electronics, Appliances & CCTV"; hub "job cards" claims removed from both cards (job cards / installation are NOT built for this category).
- Built for this category (Abdul 14 Oct): serial number tracking, warranty lookup, qist (shown Enterprise+ as Customer Installments is plan-locked), plus all common modules; quotations (S53 universal, A4, convert to sale) used for solar systems and CCTV kits. Warranty does NOT print on the bill.
- **Solar** `/industries/solar-shop-pos-software/`: focus "solar shop POS software" (0.84%), root `utp utp-gro utp-sl`, custom sections "What you sell" (#utp-solar-items) + "Quote to sale" (#utp-quote). 11 FAQs.
- **Electronics** `/industries/electronics-store-pos-software/`: focus "electronics store POS software" (0.88%), secondary home appliance / CCTV, root `utp utp-gro utp-el`, custom sections "What you sell" (#utp-trades) + "CCTV shop software" (#utp-cctv). 11 FAQs.
- Renderer: industry.py now supports `custom` sections + `order` (helpers split_section, groups_section).
- Images (hw/gen_elec_solar.py): uptrendpos-solar-shop-pos-software, -solar-shop-product-catalog, -solar-shop-serial-warranty-installments, -solar-shop-quotation, -solar-shop-pos-hardware, -solar-shop-pos-process; uptrendpos-electronics-store-pos-software, -electronics-store-product-catalog, -electronics-store-serial-warranty-installments, -electronics-store-pos-hardware, -electronics-store-pos-process, uptrendpos-cctv-shop-quotation.
- Design System: UTP_LIVE_PAGES + solar-shop-pos-software, electronics-store-pos-software. SEO Snippet 2026-10-14c: images + names/audience for both.
