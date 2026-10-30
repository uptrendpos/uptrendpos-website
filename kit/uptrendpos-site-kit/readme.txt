=== UpTrendPos Site Kit ===
Version: 1.5.1
Requires at least: 6.3
Requires PHP: 7.4
License: GPL-2.0-or-later

One plugin for the whole uptrendpos.com front end. It replaces the two WPCode snippets
"UpTrendPos Design System" (HTML) and "UpTrendPos SEO Snippet" (PHP).

== What it does ==
* Design system: all CSS and JS for the page designs, self-hosted Poppins font (no Google Fonts call).
* Header on every page: top bar, logo, Industries mega menu, FBR, Pricing, Download, About, Contact,
  WhatsApp button and "Start free trial". Mobile drawer with the same links.
* Footer on every page.
* Animated hero "stage" on every page: white UpTrendPos logo in the centre, six tool nodes with
  flowing data lines and one small problem -> fix card at a time. Each page picks its preset with
  <div class="utp-stage" data-stage="pharmacy">. Home has a dark blue hero; every other page a light one.
* Live pages are automatic: a page is "live" when it is published and set to index in Rank Math.
  The menu, footer, hub schema and every in-page link follow this on their own.
* Schema merged into Rank Math: Organization, SoftwareApplication with the 3 plan offers,
  WebPage (about, publisher, reviewedBy, lastReviewed, page image, audience), FAQPage from the
  page FAQ, industries hub CollectionPage + ItemList, BreadcrumbList for every page.
* Automatic image ALT text, Fluent Forms shortcode inside Elementor HTML widgets,
  Open Graph image fallback, /llms.txt, 301s for old URLs, clean head, lang="en-PK".
* UpTrendPos > SEO Health: checks every page and copies the SEO title, description,
  keywords and index setting from the page code into Rank Math with one click.
* UpTrendPos > Settings: download links (APK / Windows), page reviewer (EEAT), on/off switches.

== New page in future ==
1. Paste the page HTML into one Elementor HTML widget.
2. Publish.
3. UpTrendPos > SEO Health > tick the page > "Fill Rank Math from page code".
4. Purge the cache. Nothing else to paste anywhere.

== Changelog ==
= 1.5.2 (30 Oct 2026) =
* Catalog counts (Abdul, 30 Oct 2026): hero stages Cosmetics 5,500+, Mobile & Computer 700+, Grocery 7,000+, and a new
  catalog card for Clothing 950+, Shoes 200+ and Baby 350+; business-type lines with
  counts (Grocery 7,000+, Crockery 2,000+, Toys 1,000+, Clothing 950+, Bags 680+, Undergarments 400+, Baby 350+, Perfume 300+,
  Sports 250+, Shoes 200+, Stationery 200+, Watch 150+, Electronics and Solar 1,100+); menu sub-lines with counts.
* llms.txt facts: every catalog count plus the full catalog of 38,000+ products.
* Includes 1.5.1 (short Industries menu, guarded self-update endpoint).

= 1.5.1 (30 Oct 2026) =
* Industries mega menu, mobile menu and footer now use a FIXED short list of 9 top business types (registry "menu"), in 3 columns, centred under the header, with one "+N more business types" line. New business types no longer make the menu bigger; they show on Home, the Industries hub and "See all business types".
* POST utpk/v1/self-update {version}: installs a newer Site Kit only from <asset source>plugin/uptrendpos-site-kit-<version>.zip (administrators only; zip and version are checked). Lets future plugin updates go live without a manual upload.

= 1.5.0 (29 Oct 2026) =
* REST layer for the daily automation (utpk/v1, admin login only): status, image upload (same file name is
  replaced in place - no more "-1" copies), page code publish (through Elementor's own save, then SEO, featured
  image and cache purge), UpdraftPlus backup start, and media clean-up (merges "-1/-2" copies into the original
  file name and removes UpTrendPos images that nothing uses). It cannot delete pages, users, plugins or settings.
* Hero animation: a new business type can carry its own 6 items in the page code, so new pages need no plugin update.
= 1.4.0 (29 Oct 2026) =
* Home page and Industries hub always list every business type in data/industries.json. A type missing
  from the page code is added on output (linked once its page is live). No page re-paste needed.
* Missing pages are made for you: every business type or main page with no WordPress page gets a DRAFT
  page with the right URL, parent "Industries", the same Elementor layout as a designed page, one empty
  HTML widget, title hidden and noindex. Paste the page code and click Publish - SEO, index and featured
  image fill on their own. Runs after every plugin update and when a new business type is added; also a
  "Create missing pages now" button in SEO Health. A notice lists the drafts waiting for code.
* SEO Health card "Business type links" shows if Home or the hub code is behind the registry.
* New hero animations: Electrical & LED Lighting, Baby & Diaper Store.
= 1.3.1 (29 Oct 2026) =
* Automatic page setup: every time a page is saved, Rank Math gets the SEO title, description,
  focus keyword + secondary keywords and index setting from the page code. No button to click.
  A later Rank Math save can no longer empty these fields.
* Automatic featured image: the first picture in the page design becomes the featured image
  (also used for Facebook / WhatsApp previews). Pictures uploaded by File Manager are added to the
  Media Library on their own. A featured image you choose by hand is never replaced.
* On the first admin visit after this update, all designed pages are set up once.
* Two switches in UpTrendPos > Settings: "Auto SEO" and "Auto featured image".
* Installation fee removed from llms.txt (handled by the sales team, not the website).
* New: Shoes & Footwear and Vehicle Showroom hero animations; Vehicle Showroom in the Industries menu.
= 1.3.0 (29 Oct 2026) =
* New hero animations for the Clothing & Garments and Cosmetics & Beauty pages.
* Catalog counts in the hero animations: electronics, solar and CCTV 1,100+; mobile and computer 670+.
* Pricing page: style for the one-time installation fee line on each plan card.
= 1.2.1 (21 Oct 2026) =
* Fix: on phones, opening the menu after scrolling showed only a thin strip and the screen froze
  until the menu was closed. The scrolled header's blur effect trapped the menu panel; it is now
  switched off while the menu is open, so the panel always fills the screen.
= 1.2.0 (20 Oct 2026) =
* Light hero on every page except Home (Home keeps the dark blue hero). Header follows it.
* New orbit: white disc with the colour UpTrendPos logo, six floating tool nodes with labels,
  flowing data lines, turning colour ring. The active tool lights up with its card.
* Smaller cards, one at a time, on the left side (never under the WhatsApp button). On phones the
  card sits under the orbit, so it never covers a tool.
* No picture under the hero on any page (also hidden for old page code).
* Animation pauses when the hero is off screen or the tab is hidden.

= 1.1.0 (20 Oct 2026) =
* New hero animation: an atom with three orbits and the UpTrendPos core. Market-gap cards
  (problem -> UpTrendPos fix) change every few seconds. One set per page.
* Cleaner hero: smaller headline, underline instead of a yellow block, shorter lead.
* Staff commission now listed on the Enterprise plan (pricing stage, llms.txt).
* Old Elementor footer is hidden when the plugin footer is on, so the footer shows once.

= 1.0.0 (20 Oct 2026) =
* First version. Merges Design System (15 Oct) and SEO Snippet 2026-10-14c, adds header,
  mega menu, footer, hero stages, SEO Health screen, llms.txt, redirects.
