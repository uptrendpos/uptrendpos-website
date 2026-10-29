# UpTrendPos Website Build: Handoff (20 Oct 2026)

Read this first in a new chat. It records where the uptrendpos.com website work stands, the rules we follow, how to rebuild everything, and what comes next.

## 1. How to restore the workspace in a new chat
1. Upload `UpTrendPos_Website_Workspace_20Oct2026.zip` to the chat.
2. Ask Claude to unzip it to `/home/claude/site` (folder names inside the zip are already correct).
3. The tools need Python 3, Playwright with Chromium, Pillow and PHP for the lint check. These are already present in the Claude workspace.
4. All page HTML, the Design System, the SEO Snippet and the master plan are also saved as project docs (paths below). The zip is the full backup, including the builders and image generators.

## 2. Fixed setup on WordPress (never change)
- Each page = one Elementor **HTML widget** that holds only page HTML. No `<style>`, no `<script>`, no HTML comments, no JSON-LD inside the widget.
- **WPCode HTML snippet "UpTrendPos Design System"** (site-wide header) = all CSS + JS. Project doc `claude/UpTrendPos_Design_System.html`.
- **WPCode PHP snippet "UpTrendPos SEO Snippet"** (Run Everywhere) = schema merged into Rank Math, breadcrumbs, page images, FAQPage built from `.utp-faq-list`, automatic image ALT, fluentform shortcodes. Project doc `claude/UpTrendPos_SEO_Snippet.php`. Current version **2026-10-14c**.
- Every delivery = page HTML + full Design System + full SEO Snippet + images + Rank Math values, together.
- Design System edit points:
  - `UTP_LIVE_PAGES`: slugs of live pages. Links to other slugs show as plain text.
  - `UTP_LINKS`: download links.
- Theme page titles are hidden by the Design System. Still turn on Elementor "Hide Title" on every page.

## 3. Content rules (standing)
- Brand is always written **UpTrendPos**. Never write AGR / AGR Soft. The only exception is the Google Maps link on the Contact page.
- Very simple English for Pakistani readers. Talk with Abdul in Roman Urdu. All deliverables are in English.
- Only built features. If a feature is not built: say nothing, or add a grey "Coming soon" tag (`<em class="utp-ptag soon">`).
- Never say "FBR approved", "certified" or "licensed integrator". No FBR logo.
- No prices in page content except on the pricing page.
- One exact focus keyword per page, at 0.8–1.0% density. No cannibalization between pages.
- Plan tags:
  - `Enterprise+` = Enterprise and Custom plans. Used for FBR, qist/installments, barcode labels, profit/P&L and audit trail.
  - `Custom` = Custom plan only. Used for HRM attendance, salary and commission.
- Images must look real, never like "AI work". They are SVG UI/device scenes rendered to WebP 1200x900 (about 35–55 KB) with a subtle watermark.
- **Before planning any business-type page, ask Abdul how many catalog products are pre-loaded** and which vertical modules that category has.
- Industry pages follow template v3 (the Grocery v2 / Pharmacy structure), rendered by `industry.py`.

## 4. Pages done (all saved as project docs)

| Page | URL | Focus keyword | Project doc |
|---|---|---|---|
| Home v1/v2 | / | POS software in Pakistan | claude/website_home_v1.html |
| About | /about-uptrendpos/ | UpTrendPos | claude/website_about_v1.html |
| Pricing | /pos-software-pricing/ | POS software pricing | claude/website_pricing_v1.html |
| Contact | /contact-us/ | free POS software demo | claude/website_contact_v1.html |
| Downloads | /download-pos-software/ | download POS software | claude/website_downloads_page_v4.html |
| Footer | site-wide | - | claude/website_footer_v1.html |
| Industries hub | /industries/ | industry-specific POS software | claude/website_industries_hub_v1.html |
| Grocery v2 (7,000 products) | /industries/grocery-store-pos-software/ | grocery store POS software | claude/website_grocery_v2.html |
| Pharmacy (17,000+ medicines) | /industries/pharmacy-pos-software/ | pharmacy POS software | claude/website_pharmacy_v1.html |
| FBR POS Integration | /fbr-pos-integration/ | FBR POS integration | claude/website_fbr_pos_integration_v1.html |
| Tailor (0 catalog) | /industries/tailor-shop-pos-software/ (301 from /tailor-shop-software/) | tailor shop POS software | claude/website_tailor_v1.html |
| Mobile & Computer (700+) | /industries/mobile-shop-pos-software/ | mobile shop POS software | claude/website_mobile_shop_v1.html |
| Solar (600+ shared) | /industries/solar-shop-pos-software/ | solar shop POS software | claude/website_solar_v1.html |
| Electronics, Appliances & CCTV (600+ shared) | /industries/electronics-store-pos-software/ (CCTV section #utp-cctv) | electronics store POS software | claude/website_electronics_v1.html |
| Privacy | /privacy-policy/ | - | claude/website_privacy_v1.html |
| Terms | /terms-and-conditions/ | - | claude/website_terms_v1.html |
| Support | /support/ | - | claude/website_support_v1.html |

- `UTP_LIVE_PAGES` currently holds: industries, grocery-store-pos-software, pharmacy-pos-software, fbr-pos-integration, tailor-shop-pos-software, mobile-shop-pos-software, solar-shop-pos-software, electronics-store-pos-software.
- `UTP_LINKS`:
  - exe = https://uptrendpos.com/wp-content/uploads/UpTrendPOS_Setup_1.0.0.zip
  - apk = https://uptrendpos.com/downloadapk/app-release.apk. This is the public URL; the hstgr.io File Manager link Abdul gave needs a login.
- Full SEO record and Rank Math values: `claude/website_seo_master_plan.md`, sections 12 to 17.

## 5. Confirmed app facts used on the pages (14 Oct 2026)
- Catalogs:
  - Pharmacy: about 17,000 medicines, every plan.
  - Grocery: about 7,000 products.
  - Mobile & Computer: 700+ products.
  - Electronics/Solar/Appliances/CCTV: one shared 600+ catalog.
  - Tailor: 0.
  - All catalogs use the same flow: search, tick, add. They carry no prices or stock; the shop sets those through PO/GRN.
- FBR: built. Modes are Simulated, Sandbox and Production. Adds the Re 1 POS fee. A separate Local GST toggle works without FBR.
- Tailor:
  - Sizes saved per customer ID. An old register number can be typed in as the ID. Sizes update on the next order.
  - Referral customer.
  - Order status: booked > cutting/stitching > ready > delivered. Advance and balance.
  - Cutting and stitching masters come from employees. Karigars are **salaried HRM staff**; no per-piece rate or commission.
  - Workshop size slip. Thermal, A4 and WhatsApp slips.
  - Coming soon: customer-app status notifications, and ready-made suit sale on the same POS.
- Mobile:
  - IMEI/serial from purchase to sale, warranty lookup module, qist.
  - **No repair job card.** Buy-back is coming soon. The warranty date does **not** print on the bill.
- Electronics/Solar/Appliances/CCTV: serial tracking, warranty lookup and qist. **No installation/repair job cards** (S46 is not built).
- Common to all: offline-first, Quick Bill, calculator, Hold, udhaar khata, installments, report sharing everywhere, PO/GRN/PI, accounts, cash sessions, multi-login, quotations (S53, A4, convert to sale).

## 6. Rebuild commands (inside /home/claude/site)
- Pages:
  - `python3 build_<trade>.py` builds the trade page. Trades: tailor, mobile, solar, electronics, pharmacy, fbr, grocery_v2, legal. Each run prints the word count, keyword density and FAQ count.
  - `industry.py` is the shared renderer. To make a new industry page, copy `build_solar.py` or `build_mobile.py` and change only the content.
- Images:
  - `python3 hw/gen_<set>.py [name]` writes `hw/img/<name>.webp`. Sets: gen_ind (grocery/hub), gen_fbr_pharm, gen_tailor_mobile, gen_elec_solar.
- Checks:
  - `python3 preview/build.py <page_file_stem> ...` renders desktop (1366) and mobile (390) screenshots with the real Design System, and reports elements wider than the screen.
  - PHP lint: prepend `<?php` to the SEO Snippet and run `php -l`.

## 7. Next queue (2 pages a day)
- **Next pair: Electrical & LED Lighting + Clothing & Garments.** Before building, ask Abdul:
  - The catalog size for each.
  - Whether Electrical is its own category or part of the Electronics category.
- After that:
  - Shoes + Cosmetics
  - Baby + Hardware
  - Paint + Auto Parts
  - Tyre + Jewellery
  - Artificial Jewellery + Watch
  - Perfume + Bags
  - Toys + Sports
  - Stationery + Crockery
  - Furniture + Meat
  - Agri + Veterinary
  - Glass + Undergarments
  - Vape + Battery
  - Then the Features hub and blog.
- The full slug and keyword map is in master plan section 2/3.

## 8. Open items to raise with Abdul
- FBR:
  - The Simulated-mode local QR must be clearly marked "not an FBR invoice".
  - Confirm that offline FBR bills auto-report on reconnect.
  - Confirm the integration route through a licensed integrator (PRAL).
- Downloads page:
  - The Windows file is a .zip. Offered to add a line "open the zip, then run the setup" to the install steps. No answer yet.
  - Check on a phone that the APK public URL downloads.
- Grocery: confirm the 7,000 catalog uses the same search-and-tick flow (assumed).
- Home page industry list still says "Electronics & CCTV Shop". Optional rename to "Electronics, Appliances & CCTV".
- Legal business decisions still open:
  - Reply targets.
  - Whether support is included in paid plans.
  - Setup-fee refund rule.
  - Limited access after the trial.
  - Registered legal entity name.
- Favicon delivered (blue 512 + 4096 + pack). SVGs are in `claude/brand/UpTrendPos-Favicon-*.svg`. Abdul uploads the 512 PNG as the WordPress Site Icon.
