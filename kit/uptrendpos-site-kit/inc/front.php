<?php
/**
 * Front end: fonts, CSS, JS, body classes, header with Industries mega menu, footer,
 * live-page link control and automatic image ALT text.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/* =========================================================================
 * 1. Helpers
 * ========================================================================= */

function utpk_front_ok() {
	if ( is_admin() || is_feed() || wp_doing_ajax() || ( defined( 'REST_REQUEST' ) && REST_REQUEST ) ) {
		return false;
	}
	return true;
}

function utpk_in_editor_preview() {
	return isset( $_GET['elementor-preview'] ) || ( isset( $_GET['action'] ) && 'elementor' === $_GET['action'] ); // phpcs:ignore WordPress.Security.NonceVerification
}

function utpk_current_has_hero() {
	if ( ! is_singular() ) {
		return false;
	}
	return false !== strpos( utpk_page_html( get_queried_object_id() ), 'utp-hero' );
}

/* 1.2: only the home page keeps the dark navy hero; every other page has a light hero. */
function utpk_current_dark_hero() {
	if ( ! utpk_current_has_hero() ) {
		return false;
	}
	return ( function_exists( 'is_front_page' ) && is_front_page() ) || 1 === preg_match( '/class="utp utp-home[\s"]/', utpk_page_html( get_queried_object_id() ) );
}

function utpk_u( $path ) {
	return esc_url( home_url( $path ) );
}

function utpk_ic( $id, $size = 20 ) {
	return '<svg class="utk-i" width="' . (int) $size . '" height="' . (int) $size . '" aria-hidden="true"><use href="#utk-' . esc_attr( $id ) . '"/></svg>';
}

function utpk_wa_link( $text ) {
	return 'https://wa.me/' . utpk_brand()['wa'] . '?text=' . rawurlencode( $text );
}

/* =========================================================================
 * 2. Fonts, CSS, JS
 * ========================================================================= */

add_action( 'wp_head', function () {
	if ( ! utpk_front_ok() ) {
		return;
	}
	$f = UTPK_URL . 'assets/fonts/';
	echo "\n<!-- UpTrendPos Site Kit " . esc_html( UTPK_VERSION ) . " -->\n";
	echo '<link rel="preload" href="' . esc_url( $f . 'poppins-latin-400-normal.woff2' ) . '" as="font" type="font/woff2" crossorigin>' . "\n";
	echo '<link rel="preload" href="' . esc_url( $f . 'poppins-latin-700-normal.woff2' ) . '" as="font" type="font/woff2" crossorigin>' . "\n";
	$faces = '';
	foreach ( array( 400, 500, 600, 700, 800 ) as $w ) {
		$faces .= "@font-face{font-family:'Poppins';font-style:normal;font-weight:{$w};font-display:swap;src:url(" . esc_url( $f . 'poppins-latin-' . $w . '-normal.woff2' ) . ") format('woff2')}";
	}
	echo '<style id="utpk-fonts">' . $faces . '</style>' . "\n"; // phpcs:ignore WordPress.Security.EscapeOutput
	echo '<meta name="theme-color" content="#0A1838">' . "\n";
	if ( ! has_site_icon() ) {
		echo '<link rel="icon" href="' . esc_url( UTPK_URL . 'assets/img/icon-512.png' ) . '" sizes="512x512">' . "\n";
	}
	if ( utpk_opt( 'hide_theme_hf' ) && ! utpk_in_editor_preview() ) {
		$css = '';
		if ( utpk_opt( 'header' ) ) {
			$css .= 'body.utp-site #site-header,body.utp-site .site-header:not(.utp-nav),body.utp-site [data-elementor-type="header"],body.utp-site [data-elementor-type="jkit-header"],body.utp-site .jkit-header,body.utp-site #jkit-header,body.utp-site .elementor-location-header,body.utp-site header.ehf-header,body.utp-site #masthead:not(.utp-nav){display:none!important}';
		}
		if ( utpk_opt( 'footer' ) ) {
			$css .= 'body.utp-site #site-footer,body.utp-site .site-footer:not(.utp-foot),body.utp-site [data-elementor-type="footer"],body.utp-site [data-elementor-type="jkit-footer"],body.utp-site .jkit-footer,body.utp-site #jkit-footer,body.utp-site .elementor-location-footer,body.utp-site footer.ehf-footer,body.utp-site #colophon{display:none!important}';
		}
		echo '<style id="utpk-hide-theme">' . $css . '</style>' . "\n"; // phpcs:ignore WordPress.Security.EscapeOutput
	}
}, 1 );

function utpk_js_config() {
	return array(
		'live'   => utpk_live_slugs(),
		'img'    => UTPK_URL . 'assets/img/',
		'motion' => (bool) utpk_opt( 'motion' ),
		'links'  => array(
			'apk'           => (string) utpk_opt( 'apk' ),
			'apkVersion'    => (string) utpk_opt( 'apk_version' ),
			'apkSize'       => (string) utpk_opt( 'apk_size' ),
			'apkMinAndroid' => (string) utpk_opt( 'apk_min' ),
			'exe'           => (string) utpk_opt( 'exe' ),
			'exeVersion'    => (string) utpk_opt( 'exe_version' ),
			'exeSize'       => (string) utpk_opt( 'exe_size' ),
			'updated'       => (string) utpk_opt( 'updated' ),
		),
	);
}

function utpk_enqueue() {
	wp_enqueue_style( 'utpk', UTPK_URL . 'assets/css/utp.css', array(), UTPK_VERSION );
	wp_enqueue_script( 'utpk', UTPK_URL . 'assets/js/utp.js', array(), UTPK_VERSION, array( 'in_footer' => true, 'strategy' => 'defer' ) );
	wp_add_inline_script( 'utpk', 'window.UTPK=' . wp_json_encode( utpk_js_config() ) . ';', 'before' );
}
add_action( 'wp_enqueue_scripts', 'utpk_enqueue', 20 );
add_action( 'elementor/preview/enqueue_styles', 'utpk_enqueue' );
add_action( 'elementor/editor/after_enqueue_styles', function () {
	wp_enqueue_style( 'utpk', UTPK_URL . 'assets/css/utp.css', array(), UTPK_VERSION );
} );

add_filter( 'body_class', function ( $c ) {
	$c[] = 'utp-site';
	if ( utpk_current_has_hero() ) {
		$c[] = 'utp-has-hero';
	}
	if ( utpk_opt( 'header' ) && ! utpk_in_editor_preview() ) {
		$c[] = 'utp-has-nav';
	}
	if ( ! utpk_opt( 'motion' ) ) {
		$c[] = 'utp-no-motion';
	}
	return $c;
} );

/* =========================================================================
 * 3. Icon sprite (header, menu, footer)
 * ========================================================================= */

function utpk_sprite() {
	$i = array(
		'chev'     => '<path d="M6 9l6 6 6-6"/>',
		'arrow'    => '<path d="M5 12h14M13 6l6 6-6 6"/>',
		'mail'     => '<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3.5 6.5l8.5 6.5 8.5-6.5"/>',
		'phone'    => '<path d="M5 4h3.5l1.7 4.3-2.2 1.4a11 11 0 0 0 6.3 6.3l1.4-2.2L20 15.5V19a1 1 0 0 1-1 1A16 16 0 0 1 4 5a1 1 0 0 1 1-1z"/>',
		'user'     => '<circle cx="12" cy="8" r="3.6"/><path d="M4.5 20a7.5 7.5 0 0 1 15 0"/>',
		'pin'      => '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
		'clock'    => '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
		'offline'  => '<path d="M2 8.5a15 15 0 0 1 20 0M5.5 12a10 10 0 0 1 13 0M9 15.5a5 5 0 0 1 6 0"/><path d="M3 3l18 18"/>',
		'qr'       => '<path d="M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h3v3h-3zM20 14v6h-3"/>',
		'grid'     => '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
		'shield'   => '<path d="M12 3l7.5 3v5.5c0 4.5-3.2 8.2-7.5 9.5-4.3-1.3-7.5-5-7.5-9.5V6z"/><path d="M8.8 12l2.2 2.2 4.2-4.4"/>',
		'download' => '<path d="M12 3v12M7 10l5 5 5-5M5 21h14"/>',
		'cart'     => '<path d="M3 4h2.2l2.3 11.2a1.5 1.5 0 0 0 1.5 1.2h8.6a1.5 1.5 0 0 0 1.5-1.1L21 8H6.2"/><circle cx="9.5" cy="20" r="1.3"/><circle cx="17" cy="20" r="1.3"/>',
		'meat'     => '<path d="M15.5 4.5a5 5 0 0 1 0 7.1l-4 4a3 3 0 0 1-4.2 0l-.9-.9a3 3 0 0 1 0-4.2l4-4a5 5 0 0 1 5.1-2z"/><path d="M7 16l-3 3M5 21l-2-2"/>',
		'cup'      => '<path d="M4 8h13v5a6 6 0 0 1-6 6h-1a6 6 0 0 1-6-6z"/><path d="M17 10h1.5a2.5 2.5 0 0 1 0 5H17M7 3v2M11 3v2M15 3v2"/>',
		'cloud'    => '<path d="M7 18a4.5 4.5 0 0 1-.4-9A6 6 0 0 1 18 9.5a4 4 0 0 1-.5 8.5z"/>',
		'pill'     => '<rect x="3" y="8.5" width="18" height="7" rx="3.5" transform="rotate(-45 12 12)"/><path d="M9.5 9.5l5 5"/>',
		'spark'    => '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 16l.8 2.2L22 19l-2.2.8L19 22l-.8-2.2L16 19l2.2-.8z"/>',
		'baby'     => '<circle cx="12" cy="8" r="4"/><path d="M6 21a6 6 0 0 1 12 0M10.5 8h.01M13.5 8h.01"/>',
		'drop'     => '<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/>',
		'shirt'    => '<path d="M8 3l4 3 4-3 5 4-3 4-2-1v11H8V10l-2 1-3-4z"/>',
		'shoe'     => '<path d="M3 17h18v-2.5c0-1-1-1.7-2-1.9l-5-1-3-4H7v3H3z"/><path d="M3 17v2h18v-2"/>',
		'scissors' => '<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M8.1 8.1L20 20M8.1 15.9L20 4"/>',
		'bag'      => '<path d="M5 8h14l-1 13H6z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/>',
		'watch'    => '<circle cx="12" cy="12" r="5.5"/><path d="M12 9.5V12l1.5 1.5M9 6.8L9.6 3h4.8l.6 3.8M9 17.2l.6 3.8h4.8l.6-3.8"/>',
		'gem'      => '<path d="M6 3h12l3 6-9 12L3 9z"/><path d="M3 9h18M9 3l3 6 3-6M12 9v12"/>',
		'tv'       => '<rect x="2" y="5" width="20" height="13" rx="2"/><path d="M8 21h8M12 18v3"/>',
		'sun'      => '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
		'bulb'     => '<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>',
		'mobile'   => '<rect x="6.5" y="2.5" width="11" height="19" rx="2.5"/><path d="M11 18.5h2"/>',
		'battery'  => '<rect x="2" y="7" width="17" height="10" rx="2"/><path d="M22 11v2M6 10v4M10 10v4"/>',
		'hammer'   => '<path d="M14 6l4 4M3 21l9-9M12.5 4.5l4-1.5 4.5 4.5-1.5 4-3 0-4-4z"/>',
		'brush'    => '<path d="M14.5 4.5l5 5L11 18l-5-5z"/><path d="M6 13c-2 0-3 1.5-3 3.2 0 1.6-.5 2.6-1 3.3 3 .2 6.2-.6 7-3.5"/>',
		'window'   => '<rect x="4" y="3" width="16" height="18" rx="1.5"/><path d="M12 3v18M4 12h16"/>',
		'sofa'     => '<path d="M4 11V8a3 3 0 0 1 3-3h10a3 3 0 0 1 3 3v3"/><path d="M2 13a2 2 0 0 1 4 0v2h12v-2a2 2 0 0 1 4 0v5H2zM5 18v2M19 18v2"/>',
		'car'      => '<path d="M5 16h14v-4l-2-5H7l-2 5z"/><path d="M3 12h18M5 16v3M19 16v3"/><circle cx="8" cy="13.5" r=".8"/><circle cx="16" cy="13.5" r=".8"/>',
		'tyre'     => '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/><path d="M12 3v5M12 16v5M3 12h5M16 12h5"/>',
		'gift'     => '<rect x="3" y="8" width="18" height="13" rx="2"/><path d="M3 12h18M12 8v13M12 8c-2-4-6-4-6-1.5S10 8 12 8c2 0 6 1 6-1.5S14 4 12 8"/>',
		'ball'     => '<circle cx="12" cy="12" r="9"/><path d="M12 7l4 3-1.5 4.5h-5L8 10z"/><path d="M12 3v4M21 10l-5 0M15 21l-.5-6.5M9 21l.5-6.5M3 10h5"/>',
		'book'     => '<path d="M4 4h11a3 3 0 0 1 3 3v13H7a3 3 0 0 1-3-3z"/><path d="M8 8h6M8 12h6"/>',
		'leaf'     => '<path d="M5 21c0-9 6-15 16-16-1 10-7 16-16 16zM5 21l8-8"/>',
		'paw'      => '<circle cx="7" cy="10" r="2"/><circle cx="17" cy="10" r="2"/><circle cx="9.5" cy="5.5" r="2"/><circle cx="14.5" cy="5.5" r="2"/><path d="M12 12c-3 0-5 3.5-5 5.5 0 1.5 1.2 2.5 2.7 2.5.9 0 1.5-.5 2.3-.5s1.4.5 2.3.5c1.5 0 2.7-1 2.7-2.5 0-2-2-5.5-5-5.5z"/>',
	);
	$fill = array(
		'wa' => '<path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38a9.9 9.9 0 0 0 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91A9.9 9.9 0 0 0 12.04 2zm0 18.15c-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.25-8.24 2.2 0 4.27.86 5.83 2.42a8.18 8.18 0 0 1 2.41 5.83c0 4.54-3.7 8.23-8.24 8.23zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.12-.17.25-.64.81-.78.97-.14.17-.29.19-.54.06-.25-.12-1.05-.39-1.99-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.02-.38.11-.51.11-.11.25-.29.37-.43.13-.15.17-.25.25-.42.08-.17.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.22.25-.86.85-.86 2.07s.89 2.4 1.01 2.56c.12.17 1.75 2.67 4.23 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.67-1.18.21-.58.21-1.07.14-1.18-.06-.1-.22-.16-.47-.28z"/>',
		'fb' => '<path d="M14 8h3V4h-3c-2.8 0-4.5 1.8-4.5 4.6V11H7v4h2.5v9h4v-9H17l.5-4h-4V8.8c0-.5.3-.8.5-.8z"/>',
		'ig' => '<path d="M12 7.2A4.8 4.8 0 1 0 12 16.8 4.8 4.8 0 0 0 12 7.2zm0 7.9a3.1 3.1 0 1 1 0-6.2 3.1 3.1 0 0 1 0 6.2zM17 5.8a1.1 1.1 0 1 0 0 2.3 1.1 1.1 0 0 0 0-2.3zM21.5 7.6c-.1-1.5-.4-2.9-1.5-4-1.1-1.1-2.5-1.4-4-1.5-1.6-.1-6.4-.1-8 0-1.5.1-2.9.4-4 1.5S2.6 6.1 2.5 7.6c-.1 1.6-.1 6.4 0 8 .1 1.5.4 2.9 1.5 4s2.5 1.4 4 1.5c1.6.1 6.4.1 8 0 1.5-.1 2.9-.4 4-1.5s1.4-2.5 1.5-4c.1-1.6.1-6.4 0-8zm-2 9.8a3.2 3.2 0 0 1-1.8 1.8c-1.3.5-4.3.4-5.7.4s-4.4.1-5.7-.4a3.2 3.2 0 0 1-1.8-1.8c-.5-1.3-.4-4.3-.4-5.7s-.1-4.4.4-5.7a3.2 3.2 0 0 1 1.8-1.8C7.6 3.7 10.6 3.8 12 3.8s4.4-.1 5.7.4a3.2 3.2 0 0 1 1.8 1.8c.5 1.3.4 4.3.4 5.7s.1 4.4-.4 5.7z"/>',
		'yt' => '<path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12 31 31 0 0 0 1 16.8a3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1c.4-1.6.5-3.2.5-4.8s-.1-3.2-.5-4.8zM9.7 15.1V8.9l5.8 3.1-5.8 3.1z"/>',
		'in' => '<path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.5h4V21H3zM9.5 9.5h3.8v1.6h.1c.5-1 1.8-2 3.8-2 4 0 4.8 2.6 4.8 6V21h-4v-5.2c0-1.3 0-2.9-1.8-2.9s-2 1.4-2 2.8V21h-4z"/>',
	);
	$out = '<svg xmlns="http://www.w3.org/2000/svg" style="position:absolute;width:0;height:0;overflow:hidden" aria-hidden="true" focusable="false">';
	foreach ( $i as $k => $p ) {
		$out .= '<symbol id="utk-' . $k . '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">' . $p . '</symbol>';
	}
	foreach ( $fill as $k => $p ) {
		$out .= '<symbol id="utk-' . $k . '" viewBox="0 0 24 24" fill="currentColor">' . $p . '</symbol>';
	}
	return $out . '</svg>';
}

/* =========================================================================
 * 4. Header with Industries mega menu
 * ========================================================================= */

function utpk_live_industries() {
	$d    = utpk_industries();
	$out  = array();
	foreach ( $d['groups'] as $g ) {
		$items = array();
		foreach ( $d['types'] as $t ) {
			if ( $t['group'] === $g['id'] && utpk_is_live( $t['slug'] ) ) {
				$items[] = $t;
			}
		}
		if ( $items ) {
			$out[] = array( 'group' => $g, 'items' => $items );
		}
	}
	return $out;
}

/**
 * Fixed short list for the header mega menu, mobile drawer and footer (registry "menu").
 * Only live pages show. New business types never grow the menu; they live on Home and the hub.
 * Falls back to the first 3 live groups x 3 types when the registry has no "menu" list.
 */
function utpk_menu_industries() {
	$d    = utpk_industries();
	$out  = array();
	if ( ! empty( $d['menu']['columns'] ) && is_array( $d['menu']['columns'] ) ) {
		foreach ( $d['menu']['columns'] as $col ) {
			$items = array();
			foreach ( (array) ( $col['items'] ?? array() ) as $it ) {
				$t = utpk_industry( (string) ( $it['slug'] ?? '' ) );
				if ( ! $t || ! utpk_is_live( $t['slug'] ) ) {
					continue;
				}
				if ( ! empty( $it['label'] ) ) {
					$t['name'] = $it['label'];
				}
				if ( ! empty( $it['line'] ) ) {
					$t['line'] = $it['line'];
				}
				$items[] = $t;
				if ( count( $items ) >= 4 ) {
					break;
				}
			}
			if ( $items ) {
				$out[] = array( 'group' => array( 'name' => (string) ( $col['name'] ?? '' ) ), 'items' => $items );
			}
			if ( count( $out ) >= 3 ) {
				break;
			}
		}
		return $out;
	}
	foreach ( array_slice( utpk_live_industries(), 0, 3 ) as $g ) {
		$g['items'] = array_slice( $g['items'], 0, 3 );
		$out[]      = $g;
	}
	return $out;
}

/** Live business-type slugs (published + index). */
function utpk_live_slugs_of_types() {
	$out = array();
	foreach ( utpk_industries()['types'] as $t ) {
		if ( utpk_is_live( $t['slug'] ) ) {
			$out[] = $t['slug'];
		}
	}
	return $out;
}

function utpk_current_slug() {
	return is_singular() ? (string) get_post_field( 'post_name', get_queried_object_id() ) : '';
}

function utpk_header_html() {
	$b      = utpk_brand();
	$cur    = utpk_current_slug();
	$groups = utpk_menu_industries();
	$hub    = utpk_is_live( $b['hub_slug'] ) ? home_url( '/' . $b['hub_slug'] . '/' ) : home_url( '/#utp-industries' );
	$logo_c = UTPK_URL . 'assets/img/logo-color.webp';
	$logo_w = UTPK_URL . 'assets/img/logo-white.webp';
	$demo   = utpk_wa_link( 'Hi, I want a free demo of UpTrendPos' );

	$nav = array(
		array( 'fbr-pos-integration', 'FBR integration' ),
		array( 'pos-software-pricing', 'Pricing' ),
		array( 'download-pos-software', 'Download' ),
		array( 'about-uptrendpos', 'About' ),
		array( 'contact-us', 'Contact' ),
	);

	$mega = '';
	foreach ( $groups as $g ) {
		$mega .= '<div class="utn-grp"><p class="utn-gh">' . esc_html( $g['group']['name'] ) . '</p>';
		foreach ( $g['items'] as $t ) {
			$on    = $cur === $t['slug'] ? ' aria-current="page"' : '';
			$mega .= '<a href="' . esc_url( utpk_industry_url( $t['slug'] ) ) . '"' . $on . ' data-track="menu_' . esc_attr( $t['slug'] ) . '"><span class="mi mi-' . esc_attr( $t['group'] ) . '">' . utpk_ic( $t['icon'], 20 ) . '</span><span><strong>' . esc_html( $t['name'] ) . '</strong><small>' . esc_html( $t['line'] ) . '</small></span></a>';
		}
		$mega .= '</div>';
	}

	$h  = '<header class="utp-nav' . ( utpk_current_has_hero() ? ( utpk_current_dark_hero() ? ' is-dark' : ' is-light' ) : ' is-solid is-static' ) . '" id="utp-nav">';
	$h .= '<div class="utn-top"><div class="utn-top-in"><div class="l">';
	$h .= '<a href="' . esc_url( 'https://wa.me/' . $b['wa'] ) . '" target="_blank" rel="noopener" data-track="top_whatsapp">' . utpk_ic( 'wa', 15 ) . esc_html( $b['phone_show'] ) . '</a>';
	$h .= '<a class="hide-m" href="mailto:' . esc_attr( $b['email'] ) . '">' . utpk_ic( 'mail', 15 ) . esc_html( $b['email'] ) . '</a>';
	$h .= '</div><div class="r"><span class="utn-badge hide-m"><i></i>Works offline · 14-day free trial</span>';
	$h .= '<a href="' . esc_url( $b['app'] ) . '" target="_blank" rel="noopener" data-track="top_login">' . utpk_ic( 'user', 15 ) . 'Login</a></div></div></div>';

	$h .= '<div class="utn-in">';
	$h .= '<a class="utn-logo" href="' . utpk_u( '/' ) . '" aria-label="UpTrendPos home"><img class="lc" src="' . esc_url( $logo_c ) . '" width="600" height="120" alt="UpTrendPos"><img class="lw" src="' . esc_url( $logo_w ) . '" width="600" height="120" alt="" aria-hidden="true"></a>';
	$h .= '<nav class="utn-nav" aria-label="Main"><ul class="utn-menu">';
	$h .= '<li class="has-mega"><button type="button" class="utn-mbtn" aria-expanded="false" aria-controls="utn-mega">Industries ' . utpk_ic( 'chev', 14 ) . '</button>';
	$in_menu = 0;
	foreach ( $groups as $g ) {
		$in_menu += count( $g['items'] );
	}
	$more = max( 0, count( utpk_live_slugs_of_types() ) - $in_menu );
	$more_link = $more ? '<a class="utn-more" href="' . esc_url( $hub ) . '" data-track="menu_more_types"><span>Hardware, paint, auto parts, jewellery and more<small>+' . (int) $more . ' more business types</small></span>' . utpk_ic( 'arrow', 16 ) . '</a>' : '';
	$h .= '<div class="utn-mega" id="utn-mega"><div class="utn-mega-main">' . ( $mega ? '<div class="utn-mega-grid">' . $mega . '</div>' : '' ) . $more_link . '</div>';
	$h .= '<div class="utn-mega-side"><span class="utn-side-k">' . utpk_ic( 'grid', 16 ) . ' 30+ business types</span><p class="utn-side-t">Ready setup for your shop</p><p class="utn-side-p">Pick your business type at sign up. Fields, units and reports open ready for it.</p>';
	$h .= '<a class="utn-side-btn" href="' . esc_url( $hub ) . '" data-track="menu_all_types">See all business types ' . utpk_ic( 'arrow', 16 ) . '</a>';
	if ( utpk_is_live( 'fbr-pos-integration' ) ) {
		$h .= '<a class="utn-side-fbr" href="' . utpk_u( '/fbr-pos-integration/' ) . '" data-track="menu_fbr"><span>' . utpk_ic( 'qr', 18 ) . '</span><span><strong>FBR POS integration</strong><small>FBR invoice number and QR on every bill</small></span></a>';
	}
	$h .= '</div></div></li>';
	foreach ( $nav as $n ) {
		if ( 'fbr-pos-integration' === $n[0] && ! utpk_is_live( $n[0] ) ) {
			continue;
		}
		$on = $cur === $n[0] ? ' aria-current="page"' : '';
		$h .= '<li><a href="' . utpk_u( '/' . $n[0] . '/' ) . '"' . $on . '>' . esc_html( $n[1] ) . '</a></li>';
	}
	$h .= '</ul></nav>';
	$h .= '<div class="utn-cta"><a class="utn-wa" href="' . esc_url( $demo ) . '" target="_blank" rel="noopener" aria-label="Free demo on WhatsApp" data-track="nav_whatsapp">' . utpk_ic( 'wa', 22 ) . '</a>';
	$h .= '<a class="utn-btn" href="' . esc_url( $b['app'] ) . '" target="_blank" rel="noopener" data-track="nav_trial">Start free trial</a>';
	$h .= '<button class="utn-burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="utn-drawer"><span></span></button></div>';
	$h .= '</div>';

	/* Mobile drawer */
	$h .= '<div class="utn-drawer" id="utn-drawer"><details class="utn-acc"><summary>Industries ' . utpk_ic( 'chev', 16 ) . '</summary><div class="utn-acc-in">';
	foreach ( $groups as $g ) {
		$h .= '<p class="utn-gh">' . esc_html( $g['group']['name'] ) . '</p>';
		foreach ( $g['items'] as $t ) {
			$h .= '<a href="' . esc_url( utpk_industry_url( $t['slug'] ) ) . '"><span class="mi mi-' . esc_attr( $t['group'] ) . '">' . utpk_ic( $t['icon'], 18 ) . '</span>' . esc_html( $t['name'] ) . '</a>';
		}
	}
	$h .= '<a class="utn-all" href="' . esc_url( $hub ) . '">See all business types ' . utpk_ic( 'arrow', 16 ) . '</a></div></details>';
	foreach ( $nav as $n ) {
		if ( 'fbr-pos-integration' === $n[0] && ! utpk_is_live( $n[0] ) ) {
			continue;
		}
		$h .= '<a class="utn-dl" href="' . utpk_u( '/' . $n[0] . '/' ) . '">' . esc_html( $n[1] ) . utpk_ic( 'arrow', 16 ) . '</a>';
	}
	$h .= '<div class="utn-dcta"><a class="utn-btn" href="' . esc_url( $b['app'] ) . '" target="_blank" rel="noopener" data-track="drawer_trial">Start 14-day free trial</a>';
	$h .= '<a class="utn-btn line" href="' . esc_url( $demo ) . '" target="_blank" rel="noopener" data-track="drawer_whatsapp">' . utpk_ic( 'wa', 18 ) . 'Free demo on WhatsApp</a></div>';
	$h .= '<p class="utn-dnote">Call <a href="tel:' . esc_attr( $b['phone_tel'] ) . '">' . esc_html( $b['phone_show'] ) . '</a> · Mon to Sat, 10 am to 7 pm</p></div>';
	$h .= '</header>';
	return $h;
}

/* =========================================================================
 * 5. Footer
 * ========================================================================= */

function utpk_footer_html() {
	$b     = utpk_brand();
	$types = array();
	foreach ( utpk_menu_industries() as $g ) {
		foreach ( $g['items'] as $t ) {
			$types[] = $t;
		}
	}
	$types = array_slice( $types, 0, 8 );
	$hub   = utpk_is_live( $b['hub_slug'] ) ? home_url( '/' . $b['hub_slug'] . '/' ) : home_url( '/#utp-industries' );
	$demo  = utpk_wa_link( 'Hi, I want a free demo of UpTrendPos' );

	$f  = '<footer class="utp-foot" id="utp-footer"><div class="uf-wrap">';
	$f .= '<div class="uf-cta"><div class="uf-cta-copy"><p class="uf-cta-title">Ready to run your shop on UpTrendPos?</p><p class="uf-cta-text">Start free for 14 days, or get a free demo for your type of shop on WhatsApp.</p></div>';
	$f .= '<div class="uf-cta-btns"><a class="uf-btn uf-btn-yellow" href="' . esc_url( $b['app'] ) . '" target="_blank" rel="noopener" data-track="footer_trial">Start free trial</a>';
	$f .= '<a class="uf-btn uf-btn-line" href="' . esc_url( $demo ) . '" target="_blank" rel="noopener" data-track="footer_whatsapp">' . utpk_ic( 'wa', 18 ) . 'Free demo</a></div></div>';

	$f .= '<div class="uf-grid"><div class="uf-brand"><a class="uf-logo" href="' . utpk_u( '/' ) . '" aria-label="UpTrendPos home"><img src="' . esc_url( UTPK_URL . 'assets/img/logo-white.webp' ) . '" width="600" height="120" loading="lazy" decoding="async" alt="UpTrendPos logo"></a>';
	$f .= '<p class="uf-about">POS and accounting software for Pakistani shops. Fast billing, stock, udhaar and FBR invoices, even when the internet is off.</p>';
	$f .= '<ul class="uf-platforms"><li>Windows</li><li>Android</li><li>Web</li></ul><ul class="uf-social">';
	foreach ( array( array( 'fb', 'Facebook', 0 ), array( 'ig', 'Instagram', 1 ), array( 'yt', 'YouTube', 2 ), array( 'in', 'LinkedIn', 3 ) ) as $s ) {
		$f .= '<li><a href="' . esc_url( $b['same_as'][ $s[2] ] ) . '" target="_blank" rel="noopener" aria-label="UpTrendPos on ' . esc_attr( $s[1] ) . '" data-track="footer_' . esc_attr( strtolower( $s[1] ) ) . '">' . utpk_ic( $s[0], 18 ) . '</a></li>';
	}
	$f .= '</ul></div>';

	$f .= '<nav class="uf-col" aria-label="Company"><p class="uf-h">Company</p><ul>';
	$company = array( array( '/', 'Home' ), array( '/about-uptrendpos/', 'About us' ), array( '/pos-software-pricing/', 'Pricing' ), array( '/download-pos-software/', 'Download' ) );
	if ( utpk_is_live( 'fbr-pos-integration' ) ) {
		$company[] = array( '/fbr-pos-integration/', 'FBR POS integration' );
	}
	$company[] = array( '/contact-us/', 'Contact us' );
	foreach ( $company as $c ) {
		$f .= '<li><a href="' . utpk_u( $c[0] ) . '">' . esc_html( $c[1] ) . '</a></li>';
	}
	$f .= '<li><a href="' . esc_url( $b['app'] ) . '" target="_blank" rel="noopener">Login</a></li></ul></nav>';

	$f .= '<nav class="uf-col" aria-label="Business types"><p class="uf-h">Business types</p><ul>';
	foreach ( $types as $t ) {
		$f .= '<li><a href="' . esc_url( utpk_industry_url( $t['slug'] ) ) . '">' . esc_html( $t['name'] ) . '</a></li>';
	}
	$f .= '<li><a class="uf-more" href="' . esc_url( $hub ) . '">All 30+ business types</a></li></ul></nav>';

	$f .= '<div class="uf-col uf-contact"><p class="uf-h">Get in touch</p><ul>';
	$f .= '<li>' . utpk_ic( 'pin', 18 ) . '<a href="' . esc_url( $b['map'] ) . '" target="_blank" rel="noopener" data-track="footer_map">' . esc_html( $b['street'] . ', ' . $b['city'] . ' ' . $b['postcode'] . ', ' . $b['country_name'] ) . '</a></li>';
	$f .= '<li>' . utpk_ic( 'phone', 18 ) . '<a href="tel:' . esc_attr( $b['phone_tel'] ) . '">' . esc_html( $b['phone_show'] ) . '</a></li>';
	$f .= '<li>' . utpk_ic( 'mail', 18 ) . '<a href="mailto:' . esc_attr( $b['email'] ) . '">' . esc_html( $b['email'] ) . '</a></li>';
	$f .= '<li>' . utpk_ic( 'clock', 18 ) . '<span>Monday to Saturday, 10 am to 7 pm</span></li>';
	$f .= '</ul><p class="uf-note">Support in Urdu and English on WhatsApp, phone and email.</p></div></div>';

	$f .= '<div class="uf-bottom"><p>&copy; <span data-utp-year>' . esc_html( gmdate( 'Y' ) ) . '</span> UpTrendPos. All rights reserved. Made in Sahiwal, Pakistan.</p><ul class="uf-legal">';
	$f .= '<li><a href="' . utpk_u( '/privacy-policy/' ) . '">Privacy Policy</a></li><li><a href="' . utpk_u( '/terms-and-conditions/' ) . '">Terms &amp; Conditions</a></li><li><a href="' . utpk_u( '/support/' ) . '">Support</a></li>';
	$f .= '</ul></div></div></footer>';
	return $f;
}

add_action( 'wp_body_open', function () {
	if ( ! utpk_front_ok() ) {
		return;
	}
	echo utpk_sprite(); // phpcs:ignore WordPress.Security.EscapeOutput
	if ( utpk_opt( 'header' ) && ! utpk_in_editor_preview() ) {
		echo utpk_header_html(); // phpcs:ignore WordPress.Security.EscapeOutput
	}
}, 5 );

add_action( 'wp_footer', function () {
	if ( ! utpk_front_ok() || utpk_in_editor_preview() ) {
		return;
	}
	if ( ! did_action( 'wp_body_open' ) ) {
		echo utpk_sprite(); // phpcs:ignore WordPress.Security.EscapeOutput -- theme without wp_body_open
	}
	if ( utpk_opt( 'footer' ) ) {
		echo utpk_footer_html(); // phpcs:ignore WordPress.Security.EscapeOutput
	}
}, 5 );

/* =========================================================================
 * 6. One output pass for every front-end page:
 *    a) links to pages that are not live yet become plain text (or are removed)
 *    b) images with no ALT get one (file name, then focus keyword, then page title)
 * ========================================================================= */

function utpk_gate_html( $html ) {
	if ( false === strpos( $html, 'data-page="' ) ) {
		return $html;
	}
	return preg_replace_callback(
		'#<a\b([^>]*?)\sdata-page="([a-z0-9-]+)"([^>]*)>(.*?)</a>#is',
		function ( $m ) {
			if ( utpk_is_live( $m[2] ) ) {
				return $m[0];
			}
			$attrs = $m[1] . ' ' . $m[3];
			if ( false !== strpos( $attrs, 'data-hide-until-live' ) ) {
				return '';
			}
			$class = preg_match( '/\sclass="([^"]*)"/i', ' ' . $attrs, $c ) ? ' class="' . $c[1] . '"' : '';
			return '<span' . $class . '>' . $m[4] . '</span>';
		},
		$html
	);
}

function utpk_alt_from_file( $src ) {
	$path = (string) wp_parse_url( $src, PHP_URL_PATH );
	$name = pathinfo( $path, PATHINFO_FILENAME );
	$name = preg_replace( '/-(scaled|rotated|e\d+|\d+x\d+)$/i', '', $name );
	$name = preg_replace( '/-(scaled|\d+x\d+)$/i', '', $name );
	$name = preg_replace( '/[-_.+]+/', ' ', $name );
	$name = preg_replace( '/\s*\d+$/', '', $name );
	$name = trim( preg_replace( '/\s+/', ' ', $name ) );
	$letters = preg_replace( '/[^a-z]/i', '', $name );
	if ( strlen( $letters ) < 4 || ( preg_match( '/^(img|image|photo|pic|picture|screenshot|screen shot|dsc|whatsapp image|pos|untitled|logo|banner|icon|design|frame|group|copy|new|final)( .*)?$/i', $name ) && str_word_count( $name ) < 3 ) ) {
		return '';
	}
	$name = ucwords( strtolower( $name ) );
	$name = preg_replace( '/\bUptrendpos\b/i', 'UpTrendPos', $name );
	$name = preg_replace( '/\bUptrend Pos\b/i', 'UpTrendPos', $name );
	return $name;
}

function utpk_alt_fill_html( $html ) {
	if ( false === stripos( $html, '<img' ) ) {
		return $html;
	}
	$id      = is_singular() ? get_queried_object_id() : 0;
	$keyword = '';
	$title   = 'UpTrendPos';
	if ( $id ) {
		$kw      = (string) get_post_meta( $id, 'rank_math_focus_keyword', true );
		$keyword = trim( (string) strtok( $kw, ',' ) );
		$t       = trim( wp_strip_all_tags( get_the_title( $id ) ) );
		if ( '' !== $t && ! is_front_page() ) {
			$title = $t . ' - UpTrendPos';
		}
	}
	$state = array( 'used_kw' => false, 'n' => 0 );
	return preg_replace_callback(
		'#<img\b[^>]*>#i',
		function ( $m ) use ( $keyword, $title, &$state ) {
			$tag = $m[0];
			if ( preg_match( '/\saria-hidden\s*=\s*["\']true["\']|\srole\s*=\s*["\']presentation["\']/i', $tag ) ) {
				return $tag;
			}
			$has_alt = preg_match( '/\salt\s*=\s*(["\'])(.*?)\1/is', $tag, $a );
			if ( $has_alt && '' !== trim( $a[2] ) ) {
				return $tag;
			}
			if ( preg_match( '/\sclass\s*=\s*["\'][^"\']*\blw\b/i', $tag ) ) {
				return $tag; // second (white) header logo is decorative
			}
			$src = '';
			if ( preg_match( '/\ssrc\s*=\s*(["\'])(.*?)\1/is', $tag, $s ) && 0 !== strpos( $s[2], 'data:' ) ) {
				$src = $s[2];
			}
			$alt = $src ? utpk_alt_from_file( $src ) : '';
			if ( '' === $alt ) {
				if ( '' !== $keyword && ! $state['used_kw'] ) {
					$alt              = ( false !== stripos( $keyword, 'uptrendpos' ) ) ? $keyword : $keyword . ' - UpTrendPos';
					$state['used_kw'] = true;
				} else {
					$state['n']++;
					$alt = $title . ( $state['n'] > 1 ? ' ' . $state['n'] : '' );
				}
			}
			$alt = esc_attr( $alt );
			if ( $has_alt ) {
				return preg_replace( '/\salt\s*=\s*(["\'])(.*?)\1/is', ' alt="' . $alt . '"', $tag, 1 );
			}
			return preg_replace( '#\s*/?>$#', ' alt="' . $alt . '"$0', $tag, 1 );
		},
		$html
	);
}

function utpk_output_pass( $html ) {
	if ( ! is_string( $html ) || '' === $html ) {
		return $html;
	}
	if ( utpk_opt( 'auto_lists' ) ) {
		$html = utpk_fill_industry_lists( $html );
	}
	if ( utpk_opt( 'gate' ) ) {
		$html = utpk_gate_html( $html );
	}
	if ( utpk_opt( 'alt' ) ) {
		$html = utpk_alt_fill_html( $html );
	}
	return $html;
}

add_action( 'template_redirect', function () {
	if ( ! utpk_front_ok() || utpk_in_editor_preview() || function_exists( 'utp_alt_fill_html' ) ) {
		return; // old WPCode snippet still active: it already runs its own ALT pass
	}
	ob_start( 'utpk_output_pass' );
}, 0 );

/* New image uploads get an ALT from the file name when the ALT is empty */
add_action( 'add_attachment', function ( $post_id ) {
	if ( ! utpk_opt( 'alt' ) || ! wp_attachment_is_image( $post_id ) ) {
		return;
	}
	$alt = get_post_meta( $post_id, '_wp_attachment_image_alt', true );
	if ( '' !== trim( (string) $alt ) ) {
		return;
	}
	$new = utpk_alt_from_file( wp_get_attachment_url( $post_id ) );
	if ( '' !== $new ) {
		update_post_meta( $post_id, '_wp_attachment_image_alt', sanitize_text_field( $new ) );
	}
} );

/* =========================================================================
 * 7. Fluent Forms shortcode inside Elementor HTML widgets (contact page form)
 * ========================================================================= */

add_filter( 'elementor/widget/render_content', function ( $content, $widget ) {
	if ( function_exists( 'utp_schema_config' ) ) {
		return $content; // old WPCode snippet still active and already does this
	}
	if ( is_object( $widget ) && method_exists( $widget, 'get_name' ) && 'html' === $widget->get_name() && false !== strpos( $content, '[fluentform' ) ) {
		$content = preg_replace_callback(
			'/\[fluentform\b[^\]]*\]/',
			function ( $m ) {
				return do_shortcode( $m[0] );
			},
			$content
		);
	}
	return $content;
}, 10, 2 );
