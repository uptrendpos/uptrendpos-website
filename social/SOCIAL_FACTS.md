# UpTrendPos daily social post: facts and rules (source of truth)

One post a day, one business type, English image + English captions. The same image and structure go to Facebook, Instagram and LinkedIn. Abdul uploads it himself.

Read this file together with `site/automation/FACTS.md` (the website's allowed-features list). If a feature is in neither file, or in the calendar entry's `idea`, or in that business's website page (`page` in the calendar entry), leave it out.

## Brand and contact (never change)
- Brand: **UpTrendPos**. Never write "UP Trend POS", "UptrendPOS", AGR or AGR Soft.
- Phone and WhatsApp: +92 319 2223292. Website: uptrendpos.com. Live app to try: live.uptrendpos.com.
- Socials: facebook.com/uptrendpos, instagram.com/uptrendpos, linkedin.com/company/uptrendpos, tiktok.com/@uptrendpos, youtube.com/@UpTrendPos.

## Loaded catalogs (Abdul, 30 Oct 2026: inserted in the system; highlight whenever the business has one)
The catalogs hold no prices or stock. The owner sets stock and price.

**Large catalogs (headline or stat):**

| Business | Count | How to say it |
|---|---|---|
| Pharmacy & Medical Store | 17,000+ | "17,000+ medicines pre-loaded" |
| Grocery & Kiryana | 7,000+ | "7,000+ grocery products ready" |
| Cosmetics & Beauty | 5,500+ | "5,500+ makeup, skin and hair care products" |
| Crockery, Household & Plastic | 2,000+ | "2,000+ crockery and household products" |
| Electronics, Solar, Appliances & CCTV | 1,100+ | one shared catalog: "1,100+ solar, electronics and CCTV products" |
| Toys & Gift Shop | 1,000+ | "1,000+ toys and gift items" |

**Mid-size catalogs (stat card or sub-line):**

| Business | Count |
|---|---|
| Clothing & Garments | 950+ |
| Mobile & Computer | 700+ |
| Bags & Luggage | 680+ |
| Undergarments & Hosiery | 400+ |
| Baby & Diaper Store | 350+ |
| Perfume & Attar | 300+ |
| Sports Goods | 250+ |
| Shoes & Footwear | 200+ |
| Stationery & Book Shop | 200+ |
| Watch Shop | 150+ |
| Gift Shop (admin category) | 150+ |

**Small starter catalogs (one small line only, never the headline):**

| Business | Count |
|---|---|
| Furniture | 70+ |
| LED Lighting | 50+ (the Electrical part has no confirmed count) |
| Veterinary | 50+ |
| Vape & Pan | 50+ (not posted) |

- No count for: Tailoring, Hardware/Sanitary, Paint, Auto Parts, Tyre, Battery, Jewellery, Artificial Jewellery, Glass, Meat, Agri Inputs, Vehicle Showroom, Electrical (non-LED). Never invent one; use the type's own strengths (variants, units, udhaar, quotations, qist).
- **Full catalog total: 38,000+ products (confirmed by Abdul, 30 Oct 2026; more are coming).** Use "38,000+ products" as the headline or stat on full-catalog days, and in captions. Never round it up or invent a higher total; Abdul will give the new number.
- **Full catalog is LIVE (Abdul, 30 Oct 2026).** Any shop can search the whole UpTrendPos catalog by category or by name and add any product to its own shop. Example: a pharmacy also adds grocery, baby diapers and general-store items. Use this as the main message on `full-catalog` days, and as one line or chip on other days where it fits.
- New counts: Abdul adds them in chat. Update this table and `calendar.json` when he does.
- Flow wording: "search, tick, add to your shop, set your own stock and price".

## Product stage (30 Oct 2026)
- Retail business types are ready and are the only ones posted.
- Not built yet, so never post them: warehouse, distribution, manufacturing, restaurant/food/bakery, salon booking, repair job cards.
- Vape & Pan is left out of social posts on purpose, because Meta restricts vape content.

## Plan wording
- Never put prices, plan names, "% off", discounts or fees in the image.
- These features are Enterprise and Custom only: FBR invoice + QR, barcode label printing, qist (installments), profit dashboard, audit trail and staff commission. If the hero shows one of them, the captions add one plain line: "Available on Enterprise and Custom plans."
- Staff attendance and salary (payroll) is Custom only.

## Never write
- "Free demo" (image or captions: the website already says it many times), "Free plan", "free forever", "ready-made", "One POS", "Smart", "certified", "FBR approved", "Pakistan's first/No. 1", "unlimited offline", iOS app, customer counts, competitor names, installation or setup fees.
- Real brand names in mockups, for example Panadol or Pampers. Use generic names such as "Paracetamol 500 mg" or "Baby Diapers Size 4".
- Health claims.
- Fake buttons or "Swipe" UI, except an in-app phone button that is part of the mockup.
- Offline wording: say "cash bills work offline". Udhaar and qist need internet.

## Design (the approved 30 Oct 2026 light post style; the same palette may be reused for ads)
- 4:5. The master is 2160x2700 (4K). The upload copy is 1640x2048, with a 1 px edge pad and no stretch. This is the Meta rule, and LinkedIn takes the same file.
- Layout:
  - White logo card top left.
  - Pill badge top right. CAPS, at most 30 characters.
  - One-line headline: navy, with the second half in `<em>` in the accent colour. At most 36 characters.
  - One-line sub-line in grey. Use `<b>` for one key phrase.
  - Hero canvas of 952x700 with app-screen mockups.
  - 3 white icon tiles.
  - Navy footer pill: WhatsApp icon + "+92 319 2223292 | uptrendpos.com". This is automatic. Never write "Free demo" anywhere in the image (Abdul, 30 Oct 2026).
- Accent `c1`/`c2`: pick one colour family per post. Avoid repeating the previous day's accent.
  - Pharmacy: `#0A7FD0`/`#3FD0C9`.
  - Grocery and full catalog: `#1E8A43`/`#47C683`.
  - Cosmetics: `#E0457B`/`#FF9A62`.
  - Solar and electronics: `#E8663C`/`#F7B731`.
  - Mobile: `#0884F6`/`#5CC8FF`.
  - Fashion: `#6D3FD1`/`#A77BFF` or `#E0457B`.
  - Hardware and auto: `#024691`/`#2F9BFF`.
  - Agri and veterinary: `#2E8B3E`/`#A6D84A`.
  - Jewellery: `#B7791F`/`#F7B731`.
- Neat and clean: few elements and generous spacing. Mockup data uses Pakistani names and Rs amounts that add up.
- Proven hero layouts (design px inside the 952x700 canvas):
  1. **Phone + right column.**
     - Phone `x 40, y 0, w 380, h 700`, with at most 5 rows. Add a `search` or a `banner` plus a `button`, at most 4 rows when both are used.
     - Right column `x 470, w 480`:
       - Stat card: about 140 tall.
       - Card height: about 90, plus 46 per row, plus about 70 for a balance box.
     - Leave at least 24 px between blocks. Chips are about 64 tall.
  2. **One wide table card** (`table`, `x 20, w 912, y 70`), with 4-5 rows and a centred `chip` at `y 0` marked `"overlap": true`.
  3. **Two cards side by side:** left `x 40, w 560`; right `x 632, w 320`.
- Examples to copy: `social/examples/*.json`. Icons are Tabler outline names. `post.py` stops with "ICON MISSING" if a name does not exist.

## Captions (write `captions.md` with 3 sections)
1. **Facebook:**
   - Hook line and 3-5 short benefit lines (✅).
   - One Roman Urdu line.
   - CTA: "WhatsApp +92 319 2223292".
   - **No links** (Facebook limits reach for them).
   - 6-8 hashtags.
2. **Instagram:**
   - Same core text, with "Try it live: live.uptrendpos.com".
   - The CTA phone.
   - 12-15 hashtags at the end.
3. **LinkedIn:**
   - 3 short professional paragraphs: the problem for that business type, how UpTrendPos solves it, and the CTA.
   - Link https://uptrendpos.com and live.uptrendpos.com.
   - 3-5 hashtags.

Hashtags:
- Always #UpTrendPos #POSSoftware #Pakistan.
- Add trade tags (#PharmacyPakistan #KiryanaStore #SolarPakistan …) and the city mix #Sahiwal #Lahore #Karachi.
- No competitor or brand tags.

Every caption ends with the same CTA phone. No prices.
