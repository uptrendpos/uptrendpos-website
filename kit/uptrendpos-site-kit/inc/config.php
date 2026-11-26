<?php
/**
 * Brand data, settings, the business-type registry and the "live page" list.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/* =========================================================================
 * 1. Brand data (fixed facts, used by the header, footer and schema)
 * ========================================================================= */

function utpk_brand() {
	return array(
		'name'          => 'UpTrendPos',
		'alt_name'      => 'UpTrend POS',
		'tagline'       => 'POS and accounting software for Pakistani shops',
		'phone'         => '+92-319-2223292',
		'phone_tel'     => '+923192223292',
		'phone_show'    => '0319 2223292',
		'wa'            => '923192223292',
		'email'         => 'sales@uptrendpos.com',
		'street'        => 'House No 193/A, Umer Block, Shadab Town',
		'city'          => 'Sahiwal',
		'region'        => 'Punjab',
		'postcode'      => '57000',
		'country'       => 'PK',
		'country_name'  => 'Pakistan',
		'lat'           => 30.64995021748812,
		'lng'           => 73.1160202245369,
		'map'           => 'https://www.google.com/maps/search/?api=1&query=30.64995021748812%2C73.1160202245369',
		'app'           => 'https://live.uptrendpos.com/',
		'partners'      => 'https://partners.uptrendpos.com/',
		'same_as'       => array(
			'https://www.facebook.com/uptrendpos',
			'https://www.instagram.com/uptrendpos/',
			'https://www.youtube.com/@UpTrendPos',
			'https://www.linkedin.com/company/uptrendpos',
		),
		'support_days'  => array( 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' ),
		'support_open'  => '10:00',
		'support_close' => '19:00',
		/* Plans: name => monthly price in PKR (pricing page is the only page that shows prices) */
		'plans'         => array(
			'Premium'    => 1000,
			'Enterprise' => 2000,
			'Custom'     => 5000,
		),
		'hub_slug'      => 'industries',
	);
}

/* =========================================================================
 * 2. Settings (UpTrendPos > Settings)
 * ========================================================================= */

function utpk_defaults() {
	return array(
		'header'         => 1,  // print the UpTrendPos header on every page
		'footer'         => 1,  // print the UpTrendPos footer on every page
		'hide_theme_hf'  => 1,  // hide the theme / Jeg Kit / Elementor header and footer templates
		'motion'         => 1,  // hero stage + scroll reveal animations
		'schema'         => 1,  // schema merged into Rank Math
		'alt'            => 1,  // automatic image ALT text
		'gate'           => 1,  // links to pages that are not live become plain text
		'cleanup'        => 1,  // remove emoji, generator, RSD, shortlink, oEmbed tags
		'llms'           => 1,  // serve /llms.txt
		'redirects'      => 1,  // 301 old URLs that now 404
		'auto_seo'       => 1,  // fill Rank Math from the page code on every save
		'auto_thumb'     => 1,  // featured image from the first picture in the page design
		'auto_lists'     => 1,  // Home + Industries hub business lists completed from data/industries.json
		'auto_pages'     => 1,  // draft pages made for business types / core pages that have no page yet
		'apk'            => 'https://uptrendpos.com/downloadapk/app-release.apk',
		'apk_version'    => '',
		'apk_size'       => '',
		'apk_min'        => '',
		'exe'            => '', // 1.6.8: the file in /downloaddesktop/ is used; the old media-library zip was removed
		'exe_version'    => '',
		'exe_size'       => '',
		'updated'        => '',
		'reviewer_name'  => '',
		'reviewer_title' => '',
		'reviewer_url'   => '',
		'live_extra'     => '',
		'asset_source'   => '',  // https://raw.githubusercontent.com/<owner>/<repo>/main/ - the only place the automation may download files from
	);
}

function utpk_options() {
	static $o = null;
	if ( null === $o ) {
		$o = wp_parse_args( (array) get_option( 'utpk', array() ), utpk_defaults() );
	}
	return $o;
}

function utpk_opt( $key ) {
	$o = utpk_options();
	return isset( $o[ $key ] ) ? $o[ $key ] : '';
}

/* =========================================================================
 * 3. Business types registry (data/industries.json)
 * ========================================================================= */

function utpk_industries() {
	static $d = null;
	if ( null === $d ) {
		$raw = file_get_contents( UTPK_DIR . 'data/industries.json' ); // phpcs:ignore WordPress.WP.AlternativeFunctions
		$d   = json_decode( (string) $raw, true );
		if ( ! is_array( $d ) ) {
			$d = array( 'groups' => array(), 'types' => array() );
		}
	}
	return $d;
}

function utpk_industry( $slug ) {
	foreach ( utpk_industries()['types'] as $t ) {
		if ( $t['slug'] === $slug ) {
			return $t;
		}
	}
	return null;
}

function utpk_industry_url( $slug ) {
	return home_url( '/' . utpk_brand()['hub_slug'] . '/' . $slug . '/' );
}

/* =========================================================================
 * 4. Live pages = published + not "noindex" in Rank Math (automatic).
 *    Menu, footer, hub schema and in-page links all read this list, so a
 *    new page goes live everywhere the moment it is published and indexed.
 * ========================================================================= */

function utpk_live_slugs() {
	static $live = null;
	if ( null !== $live ) {
		return $live;
	}
	$cached = get_transient( 'utpk_live' );
	if ( is_array( $cached ) ) {
		$live = $cached;
	} else {
		$live = array();
		$ids  = get_posts(
			array(
				'post_type'        => 'page',
				'post_status'      => 'publish',
				'numberposts'      => -1,
				'fields'           => 'ids',
				'suppress_filters' => true,
			)
		);
		foreach ( (array) $ids as $id ) {
			$robots = get_post_meta( $id, 'rank_math_robots', true );
			if ( is_array( $robots ) && in_array( 'noindex', $robots, true ) ) {
				continue;
			}
			$live[] = (string) get_post_field( 'post_name', $id );
		}
		set_transient( 'utpk_live', $live, DAY_IN_SECONDS );
	}
	foreach ( preg_split( '/[\s,]+/', (string) utpk_opt( 'live_extra' ) ) as $extra ) {
		$extra = sanitize_title( $extra );
		if ( '' !== $extra ) {
			$live[] = $extra;
		}
	}
	$live = array_values( array_unique( $live ) );
	return $live;
}

function utpk_is_live( $slug ) {
	return in_array( $slug, utpk_live_slugs(), true );
}

function utpk_flush_live() {
	delete_transient( 'utpk_live' );
	delete_transient( 'utpk_ur_twins' ); // 1.7.0
}
add_action( 'save_post_page', 'utpk_flush_live' );
add_action( 'deleted_post', 'utpk_flush_live' );
add_action( 'transition_post_status', 'utpk_flush_live' );
add_action( 'updated_post_meta', function ( $mid, $pid, $key ) {
	if ( 'rank_math_robots' === $key ) {
		utpk_flush_live();
	}
}, 10, 3 );
add_action( 'added_post_meta', function ( $mid, $pid, $key ) {
	if ( 'rank_math_robots' === $key ) {
		utpk_flush_live();
	}
}, 10, 3 );
add_action( 'update_option_utpk', 'utpk_flush_live' );

/* =========================================================================
 * 5. Page HTML helpers (reads the Elementor HTML widgets of a page)
 * ========================================================================= */

function utpk_page_html( $post_id, $fresh = false ) {
	static $cache = array();
	$post_id = (int) $post_id;
	if ( ! $fresh && isset( $cache[ $post_id ] ) ) {
		return $cache[ $post_id ];
	}
	$html = '';
	$raw  = get_post_meta( $post_id, '_elementor_data', true );
	if ( is_string( $raw ) && '' !== $raw ) {
		$data = json_decode( $raw, true );
		if ( is_array( $data ) ) {
			array_walk_recursive(
				$data,
				function ( $v, $k ) use ( &$html ) {
					if ( 'html' === $k && is_string( $v ) ) {
						$html .= $v;
					}
				}
			);
		}
	}
	if ( '' === $html ) {
		$html = (string) get_post_field( 'post_content', $post_id );
	}
	$cache[ $post_id ] = $html;
	return $html;
}

/* SEO values written in the page code: <div class="utp ..." data-seo-title="" data-seo-desc="" data-seo-kw="" data-seo-robots=""> */
function utpk_page_seo( $post_id, $fresh = false ) {
	$html = utpk_page_html( $post_id, $fresh );
	$out  = array();
	if ( ! preg_match( '#<div\b[^>]*\bclass="utp\b[^"]*"[^>]*>#i', $html, $m ) ) {
		return $out;
	}
	foreach ( array( 'title', 'desc', 'kw', 'robots' ) as $k ) {
		if ( preg_match( '/\sdata-seo-' . $k . '="([^"]*)"/i', $m[0], $a ) ) {
			$out[ $k ] = trim( html_entity_decode( $a[1], ENT_QUOTES, 'UTF-8' ) );
		}
	}
	if ( isset( $out['kw'] ) ) {
		$out['kw'] = implode( ',', array_slice( array_values( array_filter( array_map( 'trim', explode( ',', $out['kw'] ) ) ) ), 0, 5 ) );
	}
	return $out;
}

function utpk_page_is_designed( $post_id ) {
	return false !== strpos( utpk_page_html( $post_id ), 'class="utp ' ) || false !== strpos( utpk_page_html( $post_id ), 'class="utp"' );
}

/* First uploaded image in the page code (used as the page image for schema and Open Graph) */
function utpk_page_image( $post_id, $fresh = false ) {
	$html = utpk_page_html( $post_id, $fresh );
	$html = preg_replace( '#<div class="utp-marquee utp-logos".*?</ul>#is', '', $html ); // customer logos are not page images
	if ( preg_match_all( '#<img\b[^>]*\ssrc="([^"]+)"#i', $html, $m ) ) {
		foreach ( $m[1] as $src ) {
			if ( 0 === strpos( $src, 'data:' ) ) {
				continue;
			}
			if ( false !== strpos( $src, '/wp-content/uploads/' ) && ! preg_match( '#/pos\d+\.|logo#i', $src ) ) {
				return $src;
			}
		}
	}
	return '';
}

/* =========================================================================
 * 1.6.8 Download files: the newest file in the /downloadapk/ and /downloaddesktop/
 * folders of the site (uploaded with the file manager, not the media library).
 * A file found there always wins over the link saved in the settings.
 * ========================================================================= */

function utpk_download_files() {
	static $out = null;
	if ( null !== $out ) {
		return $out;
	}
	$cached = get_transient( 'utpk_dl_files' );
	if ( is_array( $cached ) ) {
		return $out = $cached;
	}
	$out  = array();
	$dirs = array(
		'apk' => array( 'downloadapk', array( 'apk' ) ),
		'exe' => array( 'downloaddesktop', array( 'exe', 'msi', 'msix', 'zip' ) ),
	);
	foreach ( $dirs as $key => $d ) {
		$dir = trailingslashit( ABSPATH . $d[0] );
		if ( ! is_dir( $dir ) ) {
			continue;
		}
		$best = '';
		$time = 0;
		foreach ( (array) scandir( $dir ) as $f ) {
			$ext = strtolower( pathinfo( (string) $f, PATHINFO_EXTENSION ) );
			if ( '.' === $f[0] || ! in_array( $ext, $d[1], true ) || ! is_file( $dir . $f ) ) {
				continue;
			}
			$m = (int) filemtime( $dir . $f );
			if ( $m >= $time ) {
				$time = $m;
				$best = $f;
			}
		}
		if ( '' !== $best ) {
			$out[ $key ] = array(
				'url'  => home_url( '/' . $d[0] . '/' . rawurlencode( $best ) ),
				'file' => $best,
				'size' => size_format( (int) filesize( $dir . $best ), 1 ),
				'date' => wp_date( 'j M Y', $time ),
			);
		}
	}
	set_transient( 'utpk_dl_files', $out, HOUR_IN_SECONDS );
	return $out;
}

/* Link, size and date for one app ('apk' or 'exe'): the folder file first, then the settings. */
function utpk_download( $key ) {
	$f   = utpk_download_files();
	$opt = (string) utpk_opt( $key );
	if ( ! empty( $f[ $key ] ) ) {
		$size = (string) utpk_opt( $key . '_size' );
		return array( 'url' => $f[ $key ]['url'], 'size' => '' !== $size ? $size : $f[ $key ]['size'], 'date' => $f[ $key ]['date'], 'file' => $f[ $key ]['file'] );
	}
	return array( 'url' => $opt, 'size' => (string) utpk_opt( $key . '_size' ), 'date' => '', 'file' => '' );
}
add_action( 'update_option_utpk', function () {
	delete_transient( 'utpk_dl_files' );
} );
