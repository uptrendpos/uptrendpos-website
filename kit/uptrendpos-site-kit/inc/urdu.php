<?php
/**
 * 1.6.8 Urdu copy of the Home page at /ur/ and the English <-> Urdu switch.
 *
 * - /ur/ is a normal UpTrendPos page (slug "ur") whose page code is the Home page in Urdu.
 * - On /ur/ the page is right-to-left (lang="ur-PK" dir="rtl"), the header and footer
 *   are shown in Urdu (one word map below) and the text uses Jameel Noori Nastaleeq,
 *   self-hosted as a small subset of only the letters the site uses.
 * - Every other page stays English. The switch ("اردو" / "English") shows in the header
 *   only after /ur/ is live, and Home and /ur/ point to each other with hreflang.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function utpk_is_ur() {
	return function_exists( 'utpk_current_slug' ) && 'ur' === utpk_current_slug();
}

function utpk_ur_ready() {
	return utpk_is_live( 'ur' );
}

/* <html lang="ur-PK" dir="rtl"> on /ur/ (runs after the en-PK filter). */
add_filter( 'language_attributes', function ( $out ) {
	if ( is_admin() || ! utpk_is_ur() ) {
		return $out;
	}
	$out = preg_replace( '/\s*dir="[a-z]+"/', '', $out );
	$out = preg_replace( '/lang="[A-Za-z-]+"/', 'lang="ur-PK" dir="rtl"', $out );
	return false === strpos( $out, 'lang=' ) ? trim( $out . ' lang="ur-PK" dir="rtl"' ) : $out;
}, 20 );

add_filter( 'body_class', function ( $c ) {
	if ( utpk_is_ur() ) {
		$c[] = 'utp-ur-mode';
	}
	return $c;
} );

/* Font faces: the full page subset on /ur/, a tiny one for the "اردو" switch label elsewhere. */
function utpk_ur_font_faces( $f ) {
	$range = 'unicode-range:U+0600-06FF,U+0750-077F,U+200C-200F,U+2066-2069,U+FB50-FDFF,U+FE70-FEFF;';
	if ( utpk_is_ur() ) {
		echo '<link rel="preload" href="' . esc_url( $f . 'jameel-noori-nastaleeq-ur.woff2?v=' . UTPK_VERSION ) . '" as="font" type="font/woff2" crossorigin>' . "\n";
		return "@font-face{font-family:'Jameel Noori Nastaleeq';font-style:normal;font-weight:400;font-display:swap;{$range}src:url(" . esc_url( $f . 'jameel-noori-nastaleeq-ur.woff2?v=' . UTPK_VERSION ) . ") format('woff2')}";
	}
	if ( utpk_ur_ready() ) {
		return "@font-face{font-family:'UTP Urdu Label';font-style:normal;font-weight:400;font-display:swap;{$range}src:url(" . esc_url( $f . 'jameel-noori-nastaleeq-label.woff2?v=' . UTPK_VERSION ) . ") format('woff2')}";
	}
	return '';
}

/* hreflang between Home (English) and /ur/ (Urdu). */
add_action( 'wp_head', function () {
	if ( ! utpk_front_ok() || ! utpk_ur_ready() ) {
		return;
	}
	if ( ! is_front_page() && ! utpk_is_ur() ) {
		return;
	}
	echo '<link rel="alternate" hreflang="en-PK" href="' . esc_url( home_url( '/' ) ) . '">' . "\n";
	echo '<link rel="alternate" hreflang="ur-PK" href="' . esc_url( home_url( '/ur/' ) ) . '">' . "\n";
	echo '<link rel="alternate" hreflang="x-default" href="' . esc_url( home_url( '/' ) ) . '">' . "\n";
}, 2 );

/* The switch: "اردو" on English pages, "English" on /ur/. */
function utpk_ur_switch_html( $extra = '' ) {
	if ( ! utpk_ur_ready() ) {
		return '';
	}
	$cls = trim( 'utn-lang ' . $extra );
	if ( utpk_is_ur() ) {
		return '<a class="' . esc_attr( $cls ) . '" href="' . utpk_u( '/' ) . '" hreflang="en" lang="en" data-track="lang_en" aria-label="Read this page in English">' . utpk_ic( 'globe', 16 ) . '<span>English</span></a>';
	}
	return '<a class="' . esc_attr( $cls . ' is-ur' ) . '" href="' . utpk_u( '/ur/' ) . '" hreflang="ur" lang="ur" data-track="lang_ur" aria-label="اردو میں پڑھیں (Urdu)">' . utpk_ic( 'globe', 16 ) . '<span>اردو</span></a>';
}

/* Header and footer words in Urdu. Keys are the exact escaped HTML the header and footer print. */
function utpk_ur_map() {
	return array(
		// top bar + header
		'Works offline · 7-day free trial'                    => 'آف لائن بھی چلتا ہے · <bdi>7</bdi> دن مفت آزمائش',
		'</svg>Login</a>'                                      => '</svg>لاگ اِن</a>',
		'aria-label="UpTrendPos home"'                         => 'aria-label="UpTrendPos ہوم"',
		'aria-label="Main"'                                    => 'aria-label="مین مینیو"',
		'>Industries <svg'                                     => '>کاروبار <svg',
		'>Daily needs and health<'                             => '>روزمرہ ضروریات اور صحت<',
		'>Fashion<'                                            => '>فیشن<',
		'>Electronics and solar<'                              => '>الیکٹرونکس اور سولر<',
		'>Grocery &amp; Kiryana<'                              => '>کریانہ اسٹور<',
		'>Pharmacy &amp; Medical<'                             => '>فارمیسی اور میڈیکل<',
		'>Cosmetics &amp; Beauty<'                             => '>کاسمیٹکس اور بیوٹی<',
		'>Clothing &amp; Garments<'                            => '>کپڑے اور گارمنٹس<',
		'>Tailoring &amp; Boutique<'                           => '>ٹیلر شاپ اور بوتیک<',
		'>Shoes &amp; Footwear<'                               => '>جوتوں کی دکان<',
		'>Solar Shop<'                                         => '>سولر شاپ<',
		'>Mobile &amp; Computer<'                              => '>موبائل اور کمپیوٹر<',
		'>Mobile, Computer &amp; Printer<'                     => '>موبائل، کمپیوٹر اور پرنٹر<',
		'>Electronics &amp; CCTV<'                             => '>الیکٹرونکس اور CCTV<',
		'>7,000+ products, udhaar<'                            => '><bdi>7,000+</bdi> پروڈکٹس، ادھار<',
		'>17,000+ medicines, expiry<'                          => '><bdi>17,000+</bdi> ادویات، ایکسپائری<',
		'>5,500+ products, expiry<'                            => '><bdi>5,500+</bdi> پروڈکٹس، ایکسپائری<',
		'>950+ products, sizes<'                               => '><bdi>950+</bdi> پروڈکٹس، سائز<',
		'>Orders and delivery dates<'                          => '>آرڈر اور ڈیلیوری کی تاریخیں<',
		'>200+ products, sizes<'                               => '><bdi>200+</bdi> پروڈکٹس، سائز<',
		'>1,100+ products, qist<'                              => '><bdi>1,100+</bdi> پروڈکٹس، قسطیں<',
		'>700+ products, IMEI<'                                => '><bdi>700+</bdi> پروڈکٹس، IMEI<',
		'>700+ products, IMEI, printers<'                      => '><bdi>700+</bdi> پروڈکٹس، IMEI، پرنٹرز<',
		'>1,100+ products, CCTV<'                              => '><bdi>1,100+</bdi> پروڈکٹس، CCTV<',
		'<span>Hardware, paint, auto parts, jewellery and more<small>+' => '<span>ہارڈویئر، پینٹ، آٹو پارٹس، جیولری اور بہت کچھ<small><bdi>+',
		' more business types</small>'                         => '</bdi> مزید کاروبار</small>',
		'</svg> 30+ business types</span>'                     => '</svg> <bdi>30+</bdi> قسم کے کاروبار</span>',
		'>Ready setup for your shop<'                          => '>آپ کی دکان کے لیے تیار سیٹ اپ<',
		'>Pick your business type at sign up. Fields, units and reports open ready for it.<' => '>سائن اپ پر اپنا کاروبار منتخب کریں۔ فیلڈز، یونٹس اور رپورٹس اسی کے مطابق تیار ملتی ہیں۔<',
		'>See all business types <svg'                         => '>تمام کاروبار دیکھیں <svg',
		'<strong>FBR POS integration</strong><small>FBR invoice number and QR on every bill</small>' => '<strong>FBR POS انٹیگریشن</strong><small>ہر بل پر FBR انوائس نمبر اور QR کوڈ</small>',
		'>FBR integration<'                                    => '>FBR انٹیگریشن<',
		'>Pricing<'                                            => '>قیمتیں<',
		'>Download<'                                           => '>ڈاؤن لوڈ<',
		'>About<'                                              => '>ہمارے بارے میں<',
		'>Contact<'                                            => '>رابطہ<',
		'aria-label="Free demo on WhatsApp"'                   => 'aria-label="واٹس ایپ پر مفت ڈیمو"',
		'>Start free trial<'                                   => '>مفت آزمائیں<',
		'aria-label="Open menu"'                               => 'aria-label="مینیو کھولیں"',
		'>Start 7-day free trial<'                             => '><bdi>7</bdi> دن مفت آزمائیں<',
		'</svg>Free demo on WhatsApp</a>'                      => '</svg>واٹس ایپ پر مفت ڈیمو</a>',
		'<p class="utn-dnote">Call <a'                         => '<p class="utn-dnote">کال کریں: <a',
		'</a> · Mon to Sat, 10 am to 7 pm</p>'                 => '</a> · پیر تا ہفتہ، صبح <bdi>10</bdi> سے شام <bdi>7</bdi> بجے</p>',
		'text=Hi%2C%20I%20want%20a%20free%20demo%20of%20UpTrendPos' => 'text=Assalam%20o%20Alaikum%2C%20mujhe%20UpTrendPos%20ka%20free%20demo%20chahiye',
		// footer
		'>Ready to run your shop on UpTrendPos?<'              => '>کیا آپ اپنی دکان UpTrendPos پر چلانے کے لیے تیار ہیں؟<',
		'>Start free for 7 days, or get a free demo for your type of shop on WhatsApp.<' => '><bdi>7</bdi> دن مفت شروع کریں، یا واٹس ایپ پر اپنی دکان کے حساب سے مفت ڈیمو لیں۔<',
		'</svg>Free demo</a>'                                  => '</svg>مفت ڈیمو</a>',
		'alt="UpTrendPos logo"'                                => 'alt="UpTrendPos لوگو"',
		'>POS and accounting software for Pakistani shops. Fast billing, stock, udhaar and FBR invoices, even when the internet is off.<' => '>پاکستانی دکانوں کے لیے POS اور اکاؤنٹنگ سافٹ ویئر۔ تیز بلنگ، اسٹاک، ادھار اور FBR انوائس، انٹرنیٹ بند ہو تب بھی۔<',
		'<li>Windows</li><li>Android</li><li>Web</li>'         => '<li>ونڈوز</li><li>اینڈرائیڈ</li><li>ویب</li>',
		'aria-label="Company"><p class="uf-h">Company<'        => 'aria-label="کمپنی"><p class="uf-h">کمپنی<',
		'>Home<'                                               => '>ہوم<',
		'>About us<'                                           => '>ہمارے بارے میں<',
		'>FBR POS integration<'                                => '>FBR POS انٹیگریشن<',
		'>Contact us<'                                         => '>رابطہ کریں<',
		'>Login<'                                              => '>لاگ اِن<',
		'aria-label="Business types"><p class="uf-h">Business types<' => 'aria-label="کاروبار"><p class="uf-h">کاروبار<',
		'>All 30+ business types<'                             => '>تمام <bdi>30+</bdi> کاروبار<',
		'>Get in touch<'                                       => '>رابطے میں رہیں<',
		'<span>Monday to Saturday, 10 am to 7 pm</span>'       => '<span>پیر تا ہفتہ، صبح <bdi>10</bdi> سے شام <bdi>7</bdi> بجے</span>',
		'>Support in Urdu and English on WhatsApp, phone and email.<' => '>واٹس ایپ، فون اور ای میل پر اردو اور انگریزی میں سپورٹ۔<',
		'</span> UpTrendPos. All rights reserved. Made in Sahiwal, Pakistan.</p>' => '</span> UpTrendPos۔ جملہ حقوق محفوظ ہیں۔ ساہیوال، پاکستان میں بنایا گیا۔</p>',
		'>Privacy Policy<'                                     => '>پرائیویسی پالیسی<',
		'>Terms &amp; Conditions<'                             => '>شرائط و ضوابط<',
		'>Support<'                                            => '>سپورٹ<',
		'>Blog<'                                               => '>بلاگ<',
	);
}

function utpk_ur_tr( $html ) {
	return strtr( $html, utpk_ur_map() );
}
