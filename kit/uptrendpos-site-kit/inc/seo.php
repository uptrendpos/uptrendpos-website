<?php
/**
 * Technical SEO that runs on its own for every page (old and new):
 * Rank Math helpers, Open Graph image fallback, llms.txt, 301s for old URLs,
 * clean <head>, en-PK language.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/* 1. The sticky "jump" bar on our pages counts as a table of contents in the Rank Math test. */
add_filter( 'rank_math/researches/toc_plugins', function ( $plugins ) {
	$plugins[ plugin_basename( UTPK_FILE ) ] = 'UpTrendPos Site Kit';
	return $plugins;
} );

/* 2. Keep template post types and utility pages out of the sitemap and the index. */
add_filter( 'rank_math/sitemap/exclude_post_type', function ( $exclude, $type ) {
	if ( in_array( $type, array( 'elementor-hf', 'elementor_library', 'e-landing-page', 'jkit-header', 'jkit-footer', 'jkit-template', 'wpcode' ), true ) ) {
		return true;
	}
	return $exclude;
}, 10, 2 );

function utpk_noindex_slugs() {
	return array( 'no-access', 'thank-you', 'cart', 'checkout', 'my-account', 'h1', 'sample-page' );
}

add_filter( 'rank_math/sitemap/posts_to_exclude', function ( $ids ) {
	foreach ( utpk_noindex_slugs() as $slug ) {
		$p = get_page_by_path( $slug );
		if ( $p ) {
			$ids[] = (int) $p->ID;
		}
	}
	return $ids;
} );

add_filter( 'rank_math/frontend/robots', function ( $robots ) {
	if ( is_page( utpk_noindex_slugs() ) || is_search() || is_404() ) {
		$robots['index']  = 'noindex';
		$robots['follow'] = 'follow';
	}
	return $robots;
} );

/* 3. Open Graph / Twitter image: when a page has no featured image and no Rank Math social image,
      use the first image in the page design. */
function utpk_og_image( $image ) {
	if ( ! is_singular() || ! is_object( $image ) || ! method_exists( $image, 'add_image' ) ) {
		return;
	}
	$id = get_queried_object_id();
	if ( has_post_thumbnail( $id ) || get_post_meta( $id, 'rank_math_facebook_image', true ) ) {
		return;
	}
	$src = utpk_page_image( $id );
	if ( '' !== $src ) {
		$image->add_image( $src );
	}
}
add_action( 'rank_math/opengraph/facebook/add_additional_images', 'utpk_og_image' );
add_action( 'rank_math/opengraph/twitter/add_additional_images', 'utpk_og_image' );

/* 4. Page language en-PK (English for Pakistan). */
add_filter( 'language_attributes', function ( $out ) {
	if ( is_admin() ) {
		return $out;
	}
	return preg_replace( '/lang="en(-[A-Z]{2})?"/', 'lang="en-PK"', $out );
} );

/* 5. /llms.txt for AI search engines (built from the live pages, nothing to edit). */
function utpk_llms_txt() {
	$b   = utpk_brand();
	$txt = "# UpTrendPos\n\n> UpTrendPos is POS and accounting software for Pakistani shops. It runs on Windows, Android and the web, keeps billing offline during load-shedding and syncs later, and covers billing, stock, udhaar khata (customer credit), purchases, double-entry accounts, installments (qist), multi-branch control and FBR invoices with QR code. Made by the UpTrendPos team in Sahiwal, Punjab, Pakistan.\n\n";
	$txt .= "Contact: " . $b['phone_show'] . " (call or WhatsApp), " . $b['email'] . ". Office: " . $b['street'] . ', ' . $b['city'] . ' ' . $b['postcode'] . ", Pakistan. Support Monday to Saturday, 10:00 to 19:00 PKT, in Urdu and English.\n\n";
	$txt .= "## Main pages\n";
	$core = array(
		array( '/', 'Home', 'POS software in Pakistan: overview, features, plans, FAQ' ),
		array( '/pos-software-pricing/', 'Pricing', 'Premium, Enterprise and Custom plans in PKR, 14-day free trial, plan comparison' ),
		array( '/download-pos-software/', 'Download', 'Windows app, Android APK and web app' ),
		array( '/fbr-pos-integration/', 'FBR POS integration', 'How FBR invoice numbers and QR codes work in UpTrendPos' ),
		array( '/industries/', 'Industries', 'POS software by business type' ),
		array( '/about-uptrendpos/', 'About', 'Who builds UpTrendPos' ),
		array( '/contact-us/', 'Contact', 'Free demo on WhatsApp, phone, email, office' ),
		array( '/support/', 'Support', 'Help channels, hours and reply targets' ),
	);
	foreach ( $core as $c ) {
		$slug = trim( $c[0], '/' );
		if ( '' !== $slug && ! utpk_is_live( $slug ) ) {
			continue;
		}
		$txt .= '- [' . $c[1] . '](' . home_url( $c[0] ) . '): ' . $c[2] . "\n";
	}
	$types = '';
	foreach ( utpk_live_industries() as $g ) {
		foreach ( $g['items'] as $t ) {
			$types .= '- [' . $t['name'] . ' POS software](' . utpk_industry_url( $t['slug'] ) . '): ' . $t['line'] . "\n";
		}
	}
	if ( '' !== $types ) {
		$txt .= "\n## Business types\n" . $types;
	}
	$txt .= "\n## Policies\n- [Privacy Policy](" . home_url( '/privacy-policy/' ) . ")\n- [Terms and Conditions](" . home_url( '/terms-and-conditions/' ) . ")\n";
	$txt .= "\n## Facts\n- Free trial: 14 days. No free plan.\n- Plans (monthly, PKR): Premium 2,000 (1 branch, 3 users), Enterprise 3,000 (2 branches, 6 users), Custom 6,000 (3 branches, 9 users). Unlimited invoices on all plans. Yearly billing: 10% off the first year.\n- Ready product catalogs (no prices or stock; the shop ticks what it sells and sets its own price): pharmacy 17,000+ medicines, grocery 7,000+, beauty and cosmetics 5,500+, crockery and household 2,000+, electronics, solar and CCTV 1,100+, toys and gifts 1,000+, clothing 950+, mobile and computer 700+, bags 680+, undergarments 400+, baby and diaper 350+, perfume 300+, sports 250+, shoes 200+, stationery 200+, watches 150+. Any shop can add products from the full UpTrendPos catalog of 38,000+ products by name or category.\n- FBR invoices, installments, barcode labels, staff commission, profit and loss and audit trail: Enterprise and Custom plans. Staff attendance and salaries: Custom plan.\n- Web app: " . $b['app'] . "\n";
	return $txt;
}

add_action( 'init', function () {
	if ( ! utpk_opt( 'llms' ) ) {
		return;
	}
	$uri = isset( $_SERVER['REQUEST_URI'] ) ? strtok( wp_unslash( $_SERVER['REQUEST_URI'] ), '?' ) : ''; // phpcs:ignore WordPress.Security.ValidatedSanitizedInput
	if ( '/llms.txt' === $uri ) {
		status_header( 200 );
		header( 'Content-Type: text/plain; charset=utf-8' );
		header( 'X-Robots-Tag: noindex' );
		echo utpk_llms_txt(); // phpcs:ignore WordPress.Security.EscapeOutput
		exit;
	}
}, 1 );

/* 6. 301 redirects for old URLs. Only used when the old URL returns 404, so a real page is never overridden. */
function utpk_redirects() {
	return array(
		'/tailor-shop-software'               => '/industries/tailor-shop-pos-software/',
		'/industries/tailor-shop-software'    => '/industries/tailor-shop-pos-software/',
		'/privacy-and-policy'                 => '/privacy-policy/',
		'/terms-conditions'                   => '/terms-and-conditions/',
		'/downloads'                          => '/download-pos-software/',
		'/download'                           => '/download-pos-software/',
		'/about-us'                           => '/about-uptrendpos/',
		'/about'                              => '/about-uptrendpos/',
		'/pricing'                            => '/pos-software-pricing/',
		'/contact'                            => '/contact-us/',
		'/fbr'                                => '/fbr-pos-integration/',
		'/fbr-integration'                    => '/fbr-pos-integration/',
	);
}

add_action( 'template_redirect', function () {
	if ( ! utpk_opt( 'redirects' ) || ! is_404() ) {
		return;
	}
	$path = isset( $_SERVER['REQUEST_URI'] ) ? untrailingslashit( strtok( wp_unslash( $_SERVER['REQUEST_URI'] ), '?' ) ) : ''; // phpcs:ignore WordPress.Security.ValidatedSanitizedInput
	$map  = utpk_redirects();
	if ( isset( $map[ $path ] ) ) {
		wp_safe_redirect( home_url( $map[ $path ] ), 301, 'UpTrendPos Site Kit' );
		exit;
	}
}, 1 );

/* 7. Clean <head> */
add_action( 'init', function () {
	if ( ! utpk_opt( 'cleanup' ) ) {
		return;
	}
	remove_action( 'wp_head', 'print_emoji_detection_script', 7 );
	remove_action( 'wp_print_styles', 'print_emoji_styles' );
	remove_action( 'admin_print_scripts', 'print_emoji_detection_script' );
	remove_action( 'admin_print_styles', 'print_emoji_styles' );
	remove_filter( 'the_content_feed', 'wp_staticize_emoji' );
	remove_filter( 'comment_text_rss', 'wp_staticize_emoji' );
	remove_filter( 'wp_mail', 'wp_staticize_emoji_for_email' );
	add_filter( 'emoji_svg_url', '__return_false' );
	remove_action( 'wp_head', 'wp_generator' );
	remove_action( 'wp_head', 'rsd_link' );
	remove_action( 'wp_head', 'wlwmanifest_link' );
	remove_action( 'wp_head', 'wp_shortlink_wp_head' );
	remove_action( 'template_redirect', 'wp_shortlink_header', 11 );
	remove_action( 'wp_head', 'wp_oembed_add_discovery_links' );
	add_filter( 'xmlrpc_enabled', '__return_false' );
} );
add_filter( 'the_generator', '__return_empty_string' );
