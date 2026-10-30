# Handoff: catalog counts and the social-post design for the UpTrendPos website

30 Oct 2026 · For the website design chat · Source: Abdul (catalogs inserted in the system)

This handoff covers two things for every website page:

1. **Right numbers.** Ready catalog counts per business type.
2. **The same clean look as the daily social posts.** Those posts were approved on 30 Oct 2026, and their colours and style may also be reused for ads.

---

## 1. Ready catalog counts (source of truth from 30 Oct 2026)

How the catalogs work:
- They carry no prices and no stock. The owner searches, ticks the products the shop sells and adds them, then sets their own stock and price.
- **Full catalog is LIVE.** Any shop can search the whole UpTrendPos catalog by name or by category and add any product. For example, a pharmacy can also add grocery, baby diapers and general-store items.

### 1.1 Large catalogs (H1, hero stat and title are fine)

| Business type | System category | Count | Website page |
|---|---|---|---|
| Pharmacy & Medical Store | pharmacy | **17,000+** medicines | /industries/pharmacy-pos-software/ |
| Grocery & Kiryana | grocery | **7,000+** | /industries/grocery-store-pos-software/ |
| Cosmetics & Beauty | catalog_cosmetics_beauty_retail | **5,500+** (was 5,000+) | /industries/cosmetics-store-pos-software/ |
| Crockery, Household & Plastic | catalog_crockery_household_plastic_shop | **2,000+** | /industries/crockery-shop-pos-software/ (queued) |
| Electronics, Solar, Appliances & CCTV | one shared catalog | **1,100+** | solar-shop + electronics-store pages |
| Toys & Gift Shop | catalog_toys_gift_shop | **1,000+** | /industries/toy-shop-pos-software/ (queued) |

### 1.2 Mid-size catalogs (hero stat card or lead line)

| Business type | System category | Count | Website page |
|---|---|---|---|
| Clothing & Garments | catalog_clothing_garments | **950+** | /industries/clothing-store-pos-software/ |
| Mobile & Computer | catalog_mobile_computer_shop | **700+** (was 670+) | /industries/mobile-shop-pos-software/ |
| Bags & Luggage | Bags Luggage | **680+** | /industries/bag-shop-pos-software/ (queued) |
| Undergarments & Hosiery | Undergarments hosiery | **400+** | /industries/undergarments-shop-pos-software/ (queued) |
| Baby & Diaper Store | catalog_baby_diaper_store | **350+** | /industries/baby-store-pos-software/ |
| Perfume & Attar | catalog_perfume_attar_shop | **300+** | /industries/perfume-shop-pos-software/ (queued) |
| Sports Goods | catalog_sports_goods | **250+** | /industries/sports-shop-pos-software/ (queued) |
| Shoes & Footwear | catalog_shoes_footwear | **200+** | /industries/shoe-store-pos-software/ |
| Stationery & Book Shop | catalog_stationery_bookshop | **200+** | /industries/stationery-shop-pos-software/ (queued) |
| Watch Shop | catalog_watch_shop | **150+** | /industries/watch-shop-pos-software/ (queued) |
| Gift Shop | Gift Shop (separate admin category) | **150+** | merged into the Toys & Gift page |

### 1.3 Small starter lists (one line in the body only, never in the H1, title or hero)

| Business type | Count | Website page |
|---|---|---|
| Furniture | 70+ | /industries/furniture-shop-pos-software/ |
| LED Lighting | 50+ (Electrical has no confirmed count) | /industries/electrical-store-pos-software/ |
| Veterinary | 50+ | /industries/veterinary-store-pos-software/ (queued) |
| Vape & Pan | 50+ | /industries/vape-shop-pos-software/ (queued) |

### 1.4 No ready catalog (keep "your shop starts with an empty list")

Tailoring, Hardware & Sanitary, Paint, Auto Parts, Tyre, Battery, Jewellery & Gold, Artificial Jewellery, Glass & Aluminium, Meat, Agri Inputs, Vehicle Showroom, and Electrical (non-LED).

### 1.5 Rules
- Write counts exactly as listed, with a "+".
- Never write a total such as "38,000+ products". The categories may share items, so first confirm the unique total from the database.
- Abdul will post new or changed counts in chat. Update this table first, then the pages.

---

## 2. Website fixes needed now (live pages say the wrong thing)

These pages are live and say **"your shop starts with an empty list"**, which is now wrong.

| Priority | Page | Builder | Change |
|---|---|---|---|
| 1 | Clothing & Garments | site/build_clothing.py | Replace the empty-list lines and FAQ with "950+ clothing products already loaded: search, tick, add, set your own price". Add a hero stat card. Keep the variant generator story. |
| 1 | Baby & Diaper Store | site/build_baby.py | 350+, same pattern. The FAQ "No. Your shop starts with an empty list…" becomes "Yes. 350+ baby and diaper products are already loaded…". |
| 1 | Shoes & Footwear | site/build_shoes.py | 200+, same pattern (keep "add your own seasonal designs" as the second line). |
| 2 | Cosmetics & Beauty | site/build_cosmetics.py | 5,000+ → **5,500+** everywhere, including the image text in hw/gen_fashion_beauty.py. |
| 2 | Mobile & Computer | site/build_mobile.py | 670+ → **700+** everywhere, including images and llms.txt facts. |
| 3 | Furniture | site/build_furniture.py | Add one line: "A starter list of 70+ furniture items is ready; add your own models." The FAQ answer changes from "No…" to that line. |
| 3 | Electrical & LED | site/build_electrical.py | One line: "50+ LED lighting items are ready to add." The rest of the electrical stock is added by the owner. |
| 3 | Home page + Industries hub | kit data/industries.json `line` | Grocery "7,000+ products ready", Pharmacy "17,000+ medicines", Cosmetics "5,500+ products, shades, expiry", Mobile "700+ products, IMEI, qist", Clothing "950+ products, size x colour", Crockery "2,000+ products", Toys "1,000+ toys and gifts" and so on. Plugin data change → Site Kit release. |
| 3 | Mega menu lines | kit data/industries.json `menu` | Cosmetics "5,500+ products, expiry". Pharmacy and Grocery lines are already right. |

Already done in the repo (30 Oct 2026), so the 5 AM daily page automation now uses the counts:
- `site/automation/queue.json`: queued types carry their counts (perfume 300+, watch 150+, bags 680+, crockery 2,000+, undergarments 400+, toys 1,000+, sports 250+, stationery 200+, veterinary 50+, vape 50+, furniture 70+).
- `site/automation/FACTS.md`: catalog rule updated (count → catalog wording; under 150 = one line only; full catalog is live; no totals).

---

## 3. Design guide: bring the social-post look into the website

The 30 Oct posts work because of a few strict choices. Reuse them on the website, inside the existing Site Kit tokens (Poppins, navy #10224A, logo blue #024691, green #1E8A43, yellow #FAE814).

### 3.1 Palette

| Role | Social post value | Website token / rule |
|---|---|---|
| Text | #10224A navy | same |
| Sub text | #4A5873 | same |
| Page background | linear 170deg #FFFFFF → #F2F7FF → #E8F0FD, plus 2 soft circles (yellow 35% top-right, accent 10% bottom-left), plus an accent dot grid (28 px) | Inner pages only. The home hero stays dark blue (20 Oct rule). |
| Accent per trade (headline word, badge dot, icon gradient) | Pharmacy #0A7FD0→#3FD0C9 · Grocery/Full catalog #1E8A43→#47C683 · Cosmetics #E0457B→#FF9A62 · Solar/Electronics #E8663C→#F7B731 · Mobile #0884F6→#5CC8FF · Hardware/Auto #024691→#2F9BFF · Agri/Vet #2E8B3E→#A6D84A · Jewellery #B7791F→#F7B731 · Fashion #6D3FD1→#A77BFF | One accent per industry page (CSS variable `--acc1/--acc2` on the page root). Never more than 1 accent plus yellow on a page. |
| Status pills | ok #E7F7EE/#1E8A43 · warn #FFF4D6/#B7791F · bad #FDECEC/#D64545 · info #E6F0FF/#0A5BC4 | Use for "Added", "Expires in 12 days", "Synced", "Due". |
| Yellow | stat card #FAE814→#FFD43B with navy text | Yellow is only ever a background with navy text (existing contrast rule). |

### 3.2 Components to add to the Site Kit (one CSS each, reusable on every page)
1. **Kicker pill:** a white pill, 1.5 px accent border at 30%, a 12 px accent dot with a 5 px halo, CAPS, letter-spacing 2px. It replaces plain text kickers.
2. **One-line headline with a coloured second half:** `Every Medicine. <em>Every Rupee.</em>` with `em` in the accent colour. It is one line on desktop and may wrap only on mobile. Keep it at 36 characters or less.
3. **Phone mockup:** dark frame, 48 px radius.
   - Header in the accent gradient, with the title and a sub-line.
   - Search field, then 4-5 item rows: tick square in green gradient, item name and pack, and "Added"/"Add" on the right.
   - Yellow button.
   - This is THE way to show the ready catalog: "search, tick, add".
4. **Catalog stat card:** yellow gradient, a 44 px bold number (e.g. "950+") and a one-line label ("clothing products in the catalog"). Put it next to the phone, never alone.
5. **Info card:** white, radius 26, soft shadow `0 20px 50px rgba(10,43,108,.15)`.
   - 44 px accent-gradient icon square plus a bold title and a grey sub-line.
   - Key-value rows with 1 px #EEF2F8 dividers, right side bold or a status pill.
   - Use it for "You only set: stock and price / shelf number / low-stock alert".
6. **Floating chip:** a white pill with a round tinted icon, e.g. "A pharmacy can add grocery too". At most 2 per section.
7. **3 icon tiles row:** white, 1.5 px #E2E9F4 border, radius 22, 52 px gradient icon square plus a one-line label. Use them to close a section.
8. **Navy contact pill:** WhatsApp green circle + "+92 319 2223292 | uptrendpos.com" on navy. Use it as the closing strip of a section on mobile.

### 3.3 New sections the website should get
- **"Ready catalog" section on every industry page with a count** (sections 1.1 and 1.2):
  - phone (search for a real trade word, e.g. "lawn suit", "school bag", "dinner set") plus the stat card plus the "You only set" card;
  - text: "<count> <trade> products already loaded. Search, tick, add, then set your own stock and price. Sell something new? Add it in seconds."
- **"Full catalog" band on the Home page and the Industries hub:**
  - headline "Sell More Than One Category.";
  - sub-line "Add any product from the full UpTrendPos catalog by name or category";
  - a grid of count chips (Medicines 17,000+, Grocery 7,000+, Beauty 5,500+, Crockery 2,000+, Solar & Electronics 1,100+, Toys 1,000+, Clothing 950+, Mobile 700+ …);
  - the example "a pharmacy adds diapers and grocery too".
- **Count badges on hub cards:** a small yellow pill "950+ products" on each card that has a catalog (none for zero-catalog types).

### 3.4 Layout rules that keep it clean (from the approved posts)
- Few elements, generous spacing. The hero has one phone plus 2 cards at most, and blocks never overlap except one deliberate chip.
- Everything stays inside a 64 px safe margin on desktop sections (16 px gutter on mobile). Cards stack under the phone below 768 px.
- Mockup data:
  - Pakistani names, Rs amounts that add up;
  - generic product names (no brands: "Paracetamol 500 mg", not a brand name);
  - no fake prices for the plans.
- One headline idea per section; the sub-line explains it in 8-10 words.
- Check every page at 1366 px and 390 px. A headline must never break into a 1-word last line.

### 3.5 Wording rules shared with the posts
- Brand: UpTrendPos.
- Never write: "ready-made", "Smart", "One POS", "Free plan", "certified", "FBR approved", "Pakistan's first", or a total catalog size.
- Offline: "cash bills work offline; udhaar and qist need internet".
- "Free demo" stays on the website (CTAs) but is NOT used inside social post images or captions (Abdul, 30 Oct 2026).
