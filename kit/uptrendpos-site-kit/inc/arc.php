<?php
/**
 * Business-type card ribbon ("arc"): tall cards on a gently curved, endlessly moving track
 * (design reference: the industry cards under the ondial.ai hero, saved 11 Nov 2026).
 *
 * Added on output, so no page code changes are needed and new pages get it on their own:
 * - Home: inside the "30+ types of shops" section, between the heading and the full list
 * - Industries hub: right under the hero
 * - Every live business-type page: before "Related" (or before the final call to action)
 * Cards = live business-type pages only (each page's featured image, short name, one line).
 *
 * @package UpTrendPos_Site_Kit
 */

defined( 'ABSPATH' ) || exit;

/** All live business-type cards, top menu types first. Cached until the live list or version changes. */
function utpk_arc_cards() {
	static $cards = null;
	if ( null !== $cards ) {
		return $cards;
	}
	$live = utpk_live_slugs();
	$key  = 'utpk_arc_' . md5( UTPK_VERSION . '|' . implode( ',', $live ) );
	$hit  = get_transient( $key );
	if ( is_array( $hit ) ) {
		$cards = $hit;
		return $cards;
	}
	$d     = utpk_industries();
	$order = array();
	foreach ( (array) ( $d['menu']['columns'] ?? array() ) as $col ) {
		foreach ( (array) ( $col['items'] ?? array() ) as $it ) {
			$order[] = (string) ( $it['slug'] ?? '' );
		}
	}
	foreach ( $d['types'] as $t ) {
		$order[] = $t['slug'];
	}
	$cards = array();
	foreach ( array_unique( $order ) as $slug ) {
		$t = utpk_industry( $slug );
		if ( ! $t || ! in_array( $slug, $live, true ) ) {
			continue;
		}
		$id    = utpk_find_page( $slug );
		$thumb = $id ? (int) get_post_thumbnail_id( $id ) : 0;
		$src   = $thumb ? wp_get_attachment_image_src( $thumb, 'medium_large' ) : false;
		if ( ! $src ) {
			continue; // a card without a picture looks broken: wait until the page has its featured image
		}
		$cards[] = array(
			'slug'  => $slug,
			'url'   => utpk_industry_url( $slug ),
			'title' => (string) ( $t['short'] ?? $t['name'] ),
			'name'  => (string) $t['name'],
			'line'  => (string) ( $t['line'] ?? '' ),
			'group' => (string) ( $t['group'] ?? '' ),
			'img'   => (string) $src[0],
			'w'     => (int) $src[1],
			'h'     => (int) $src[2],
		);
	}
	set_transient( $key, $cards, 12 * HOUR_IN_SECONDS );
	return $cards;
}

/** The ribbon markup. $skip = slug of the page being viewed (left out). */
function utpk_arc_html( $skip = '' ) {
	$cards = array_values(
		array_filter(
			utpk_arc_cards(),
			function ( $c ) use ( $skip ) {
				return $c['slug'] !== $skip;
			}
		)
	);
	if ( count( $cards ) < 5 ) {
		return '';
	}
	$li = '';
	foreach ( $cards as $c ) {
		$li .= '<li class="utp-arc-card g-' . esc_attr( $c['group'] ) . '"><a href="' . esc_url( $c['url'] ) . '" data-page="' . esc_attr( $c['slug'] ) . '" data-track="arc_' . esc_attr( $c['slug'] ) . '">'
			. '<span class="utp-arc-t">' . esc_html( $c['title'] ) . '</span>'
			. '<span class="utp-arc-img"><img src="' . esc_url( $c['img'] ) . '" width="' . (int) $c['w'] . '" height="' . (int) $c['h'] . '" loading="lazy" decoding="async" alt="' . esc_attr( 'UpTrendPos for ' . $c['name'] ) . '"></span>'
			. '<span class="utp-arc-c">' . esc_html( $c['line'] ) . '</span>'
			. '</a></li>';
	}
	return '<div class="utp-arc" data-arc><ul class="utp-arc-track">' . $li . '</ul></div>';
}

/** Section wrapper used on the hub and the business-type pages. */
function utpk_arc_section( $skip, $eyebrow, $title, $text ) {
	$arc = utpk_arc_html( $skip );
	if ( '' === $arc ) {
		return '';
	}
	return '<section class="utp-sec utp-arc-sec" aria-labelledby="utp-arc-title"><div class="utp-wrap"><div class="utp-head">'
		. '<span class="utp-eyebrow">' . esc_html( $eyebrow ) . '</span><h2 id="utp-arc-title">' . esc_html( $title ) . '</h2><p>' . esc_html( $text ) . '</p>'
		. '</div></div>' . $arc . '</section>';
}

/** Put the ribbon into the page on output (idempotent). */
function utpk_insert_arc( $html ) {
	if ( false !== strpos( $html, 'class="utp-arc' ) || false === strpos( $html, 'class="utp ' ) && false === strpos( $html, 'class="utp"' ) ) {
		return $html;
	}
	$slug = utpk_current_slug();
	$hub  = utpk_brand()['hub_slug'];

	if ( is_front_page() ) {
		$at = strpos( $html, 'id="utp-industries"' );
		$at = false === $at ? false : strpos( $html, '<div class="utp-ind">', $at );
		if ( false !== $at ) {
			$arc = utpk_arc_html();
			return '' === $arc ? $html : substr_replace( $html, '</div>' . $arc . '<div class="utp-wrap utp-arc-after">', $at, 0 );
		}
		return $html;
	}

	if ( $slug === $hub ) {
		$at = strpos( $html, '<section class="utp-hero"' );
		$at = false === $at ? false : strpos( $html, '</section>', $at );
		if ( false !== $at ) {
			$sec = utpk_arc_section( '', 'Business types', 'Ready setups for every shop', 'Each card opens the full setup for that business: fields, units, reports and the daily flow.' );
			return '' === $sec ? $html : substr_replace( $html, $sec, $at + strlen( '</section>' ), 0 );
		}
		return $html;
	}

	if ( $slug && utpk_industry( $slug ) ) {
		$sec = utpk_arc_section( $slug, 'More business types', 'UpTrendPos for other shops too', 'Run more than one kind of business? Each one gets its own ready setup.' );
		if ( '' === $sec ) {
			return $html;
		}
		foreach ( array( '<section class="utp-sec utp-alt" aria-labelledby="utp-rel-title"', '<section class="utp-final"' ) as $mark ) {
			$at = strpos( $html, $mark );
			if ( false !== $at ) {
				return substr_replace( $html, $sec, $at, 0 );
			}
		}
	}
	return $html;
}
