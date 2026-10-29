<?php
/**
 * 1.4.0 - full automation for business types (data/industries.json is the single list):
 *  A. Business-type lists on the Home page and the Industries hub are completed from the registry on output,
 *     so a new business type always shows (and links once its page is live). No page re-paste needed.
 *  B. Every business type and core page that has no WordPress page yet gets a DRAFT page made for it:
 *     right slug, parent "Industries", same Elementor layout as a designed page, one HTML widget, title hidden, noindex.
 *     The owner only opens it in Elementor, pastes the page code and clicks Publish (auto.php fills SEO + image).
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/* ---------- A. Lists ---------- */

function utpk_group_types() {
	$reg = utpk_industries();
	$out = array();
	foreach ( $reg['groups'] as $g ) {
		$out[ strtolower( html_entity_decode( $g['name'], ENT_QUOTES, 'UTF-8' ) ) ] = array();
	}
	$names = array();
	foreach ( $reg['groups'] as $g ) {
		$names[ $g['id'] ] = strtolower( $g['name'] );
	}
	foreach ( $reg['types'] as $t ) {
		if ( isset( $names[ $t['group'] ] ) ) {
			$out[ $names[ $t['group'] ] ][] = $t;
		}
	}
	return $out;
}

function utpk_group_key( $h3 ) {
	return strtolower( trim( html_entity_decode( wp_strip_all_tags( $h3 ), ENT_QUOTES, 'UTF-8' ) ) );
}

function utpk_fill_industry_lists( $html ) {
	if ( false === strpos( $html, 'utp-ind-list' ) && false === strpos( $html, 'utp-tgrid' ) ) {
		return $html;
	}
	$groups = utpk_group_types();
	// Home page: <div class="utp-ind-head">...<h3>Group</h3></div> <ul class="utp-ind-list"> ... </ul>
	$html = preg_replace_callback(
		'#(<h3>([^<]+)</h3></div>\s*<ul class="utp-ind-list">)(.*?)(</ul>)#s',
		function ( $m ) use ( $groups ) {
			$key = utpk_group_key( $m[2] );
			if ( empty( $groups[ $key ] ) ) {
				return $m[0];
			}
			$add = '';
			foreach ( $groups[ $key ] as $t ) {
				if ( false === strpos( $m[3], 'data-page="' . $t['slug'] . '"' ) ) {
					$add .= '<li><a href="' . esc_url( utpk_industry_url( $t['slug'] ) ) . '" data-page="' . esc_attr( $t['slug'] ) . '">' . esc_html( $t['name'] ) . '</a></li>';
				}
			}
			return $m[1] . $m[3] . $add . $m[4];
		},
		$html
	);
	// Industries hub: <h3>Group</h3><span class="utp-count">N types</span></div> <ul class="utp-tgrid"> ... </ul>
	$html = preg_replace_callback(
		'#<h3>([^<]+)</h3><span class="utp-count">\d+ types?</span>(</div>\s*<ul class="utp-tgrid">)(.*?)(</ul>)#s',
		function ( $m ) use ( $groups ) {
			$key = utpk_group_key( $m[1] );
			if ( empty( $groups[ $key ] ) ) {
				return $m[0];
			}
			$add = '';
			foreach ( $groups[ $key ] as $t ) {
				if ( false === strpos( $m[3], 'data-page="' . $t['slug'] . '"' ) ) {
					$add .= '<li><a class="utp-tcard" href="' . esc_url( utpk_industry_url( $t['slug'] ) ) . '" data-page="' . esc_attr( $t['slug'] ) . '"><strong>' . esc_html( $t['name'] ) . '</strong><span>' . esc_html( rtrim( $t['line'], '.' ) ) . '.</span></a></li>';
				}
			}
			$list = $m[3] . $add;
			$n    = substr_count( $list, '<li' );
			return '<h3>' . $m[1] . '</h3><span class="utp-count">' . $n . ' type' . ( 1 === $n ? '' : 's' ) . '</span>' . $m[2] . $list . $m[4];
		},
		$html
	);
	return $html;
}

/* Registry types that the saved page code does not list yet (shown in SEO Health). */
function utpk_missing_types_in_code( $post_id ) {
	$html = utpk_page_html( $post_id );
	$miss = array();
	foreach ( utpk_industries()['types'] as $t ) {
		if ( false === strpos( $html, 'data-page="' . $t['slug'] . '"' ) ) {
			$miss[] = $t['name'];
		}
	}
	return $miss;
}

/* ---------- B. Draft pages for anything that has no page yet ---------- */

function utpk_core_page_list() {
	return array(
		'about-uptrendpos'      => 'About UpTrendPos',
		'contact-us'            => 'Contact Us',
		'download-pos-software' => 'Download POS Software',
		'fbr-pos-integration'   => 'FBR POS Integration',
		'industries'            => 'Industries',
		'pos-software-pricing'  => 'POS Software Pricing Plans',
		'privacy-policy'        => 'Privacy Policy',
		'support'               => 'Support',
		'terms-and-conditions'  => 'Terms & Conditions',
	);
}

function utpk_find_page( $slug ) {
	$found = get_posts( array( 'post_type' => 'page', 'name' => $slug, 'post_status' => array( 'publish', 'draft', 'pending', 'private', 'future' ), 'numberposts' => 1, 'fields' => 'ids', 'suppress_filters' => true ) );
	return $found ? (int) $found[0] : 0;
}

/* Elementor layout copied from a designed page (same container settings), with a single empty HTML widget. */
function utpk_layout_from( $ref_id ) {
	$raw  = $ref_id ? get_post_meta( $ref_id, '_elementor_data', true ) : '';
	$data = is_string( $raw ) ? json_decode( $raw, true ) : null;
	$new  = function () {
		return substr( md5( wp_generate_uuid4() ), 0, 7 );
	};
	if ( is_array( $data ) && $data ) {
		$done = false;
		$walk = function ( $els ) use ( &$walk, &$done, $new ) {
			$out = array();
			foreach ( $els as $el ) {
				if ( isset( $el['widgetType'] ) && 'html' === $el['widgetType'] ) {
					if ( $done ) {
						continue; // keep one HTML widget only
					}
					$done                   = true;
					$el['settings']['html'] = '';
				}
				$el['id'] = $new();
				if ( ! empty( $el['elements'] ) ) {
					$el['elements'] = $walk( $el['elements'] );
				}
				$out[] = $el;
			}
			return $out;
		};
		$data = $walk( $data );
		if ( $done ) {
			return $data;
		}
	}
	return array(
		array(
			'id'       => $new(),
			'elType'   => 'container',
			'settings' => array( 'content_width' => 'full', 'padding' => array( 'unit' => 'px', 'top' => '0', 'right' => '0', 'bottom' => '0', 'left' => '0', 'isLinked' => true ) ),
			'elements' => array( array( 'id' => $new(), 'elType' => 'widget', 'widgetType' => 'html', 'settings' => array( 'html' => '' ), 'elements' => array() ) ),
			'isInner'  => false,
		),
	);
}

function utpk_reference_page() {
	foreach ( array( 'industries/clothing-store-pos-software', 'industries/pharmacy-pos-software', 'industries/grocery-store-pos-software' ) as $path ) {
		$p = get_page_by_path( $path );
		if ( $p && utpk_page_is_designed( $p->ID ) ) {
			return (int) $p->ID;
		}
	}
	return 0;
}

function utpk_create_draft( $slug, $title, $parent, $ref ) {
	$id = wp_insert_post( array( 'post_type' => 'page', 'post_status' => 'draft', 'post_title' => $title, 'post_name' => $slug, 'post_parent' => $parent, 'post_content' => '' ), true );
	if ( is_wp_error( $id ) || ! $id ) {
		return 0;
	}
	$GLOBALS['utpk_writing'] = true;
	update_post_meta( $id, '_elementor_edit_mode', 'builder' );
	update_post_meta( $id, '_elementor_template_type', 'wp-page' );
	if ( defined( 'ELEMENTOR_VERSION' ) ) {
		update_post_meta( $id, '_elementor_version', ELEMENTOR_VERSION );
	}
	update_post_meta( $id, '_elementor_data', wp_slash( wp_json_encode( utpk_layout_from( $ref ) ) ) );
	$settings = $ref ? get_post_meta( $ref, '_elementor_page_settings', true ) : array();
	$settings = is_array( $settings ) ? $settings : array();
	$settings['hide_title'] = 'yes';
	update_post_meta( $id, '_elementor_page_settings', $settings );
	$tpl = $ref ? get_post_meta( $ref, '_wp_page_template', true ) : '';
	if ( $tpl ) {
		update_post_meta( $id, '_wp_page_template', $tpl );
	}
	update_post_meta( $id, 'rank_math_robots', array( 'noindex' ) );
	update_post_meta( $id, '_utpk_autocreated', current_time( 'mysql' ) );
	$GLOBALS['utpk_writing'] = false;
	return (int) $id;
}

/* Returns the ids of the pages it made. */
function utpk_create_missing_pages() {
	$made = array();
	$ref  = utpk_reference_page();
	foreach ( utpk_core_page_list() as $slug => $title ) {
		if ( ! utpk_find_page( $slug ) ) {
			$id = utpk_create_draft( $slug, $title, 0, $ref );
			if ( $id ) {
				$made[] = $id;
			}
		}
	}
	$hub = get_page_by_path( utpk_brand()['hub_slug'] );
	$hub = $hub ? (int) $hub->ID : utpk_find_page( utpk_brand()['hub_slug'] );
	foreach ( utpk_industries()['types'] as $t ) {
		if ( utpk_find_page( $t['slug'] ) ) {
			continue;
		}
		$id = utpk_create_draft( $t['slug'], $t['name'], $hub, $ref );
		if ( $id ) {
			$made[] = $id;
		}
	}
	if ( $made ) {
		$old = (array) get_option( 'utpk_new_drafts', array() );
		update_option( 'utpk_new_drafts', array_values( array_unique( array_merge( $old, $made ) ) ), false );
	}
	return $made;
}

/* Runs once per plugin version and whenever data/industries.json changes. */
add_action( 'admin_init', function () {
	if ( ! utpk_opt( 'auto_pages' ) || ! current_user_can( 'publish_pages' ) || wp_doing_ajax() ) {
		return;
	}
	$sig = md5( UTPK_VERSION . wp_json_encode( utpk_industries()['types'] ) . wp_json_encode( utpk_core_page_list() ) );
	if ( get_option( 'utpk_pages_sig' ) === $sig ) {
		return;
	}
	update_option( 'utpk_pages_sig', $sig, false );
	utpk_create_missing_pages();
	utpk_flush_live();
}, 20 );

/* Notice: draft pages that are waiting for their page code. */
add_action( 'admin_notices', function () {
	if ( ! current_user_can( 'edit_pages' ) ) {
		return;
	}
	$ids = array_filter( (array) get_option( 'utpk_new_drafts', array() ), function ( $id ) {
		return 'draft' === get_post_status( $id ) && ! utpk_page_is_designed( $id );
	} );
	if ( ! $ids ) {
		return;
	}
	update_option( 'utpk_new_drafts', array_values( $ids ), false );
	echo '<div class="notice notice-info"><p><strong>UpTrendPos:</strong> ' . (int) count( $ids ) . ' page(s) are ready and waiting for their page code. Open one with Elementor, paste the code into the HTML widget and click <strong>Publish</strong>. SEO, index and featured image fill on their own.</p><p>';
	$links = array();
	foreach ( array_slice( $ids, 0, 40 ) as $id ) {
		$links[] = '<a href="' . esc_url( admin_url( 'post.php?post=' . (int) $id . '&action=elementor' ) ) . '">' . esc_html( get_the_title( $id ) ) . '</a>';
	}
	echo implode( ' · ', $links ) . '</p></div>'; // phpcs:ignore WordPress.Security.EscapeOutput
} );

add_action( 'admin_post_utpk_make_pages', function () {
	if ( ! current_user_can( 'publish_pages' ) ) {
		wp_die( 'Not allowed.' );
	}
	check_admin_referer( 'utpk_make_pages' );
	$made = utpk_create_missing_pages();
	utpk_flush_live();
	wp_safe_redirect( admin_url( 'admin.php?page=utpk-seo&utpk_made=' . count( $made ) ) );
	exit;
} );
