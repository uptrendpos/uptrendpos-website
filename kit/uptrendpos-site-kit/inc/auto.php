<?php
/**
 * Automatic page setup (1.3.1).
 * When a page is saved (WordPress editor or Elementor), the plugin reads the page code and:
 *  1. fills Rank Math: SEO title, description, focus keyword + secondary keywords, index / noindex;
 *  2. sets the featured image from the first picture in the page design (and makes it a Media Library item if it is not one yet).
 * The page code (data-seo-* on the root div) is the source of truth, so a later Rank Math save cannot empty these fields.
 * A featured image chosen by hand is never replaced.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

const UTPK_SEO_KEYS = array( 'rank_math_title', 'rank_math_description', 'rank_math_focus_keyword', 'rank_math_robots' );

/* Rank Math values that the page code asks for, keyed by meta key. */
function utpk_code_meta( $post_id ) {
	$seo = utpk_page_seo( $post_id, true );
	$out = array();
	if ( ! empty( $seo['title'] ) ) {
		$out['rank_math_title'] = sanitize_text_field( $seo['title'] );
	}
	if ( ! empty( $seo['desc'] ) ) {
		$out['rank_math_description'] = sanitize_text_field( $seo['desc'] );
	}
	if ( ! empty( $seo['kw'] ) ) {
		// Rank Math keeps the focus keyword first and the secondary keywords after it, comma separated (max 5).
		$kws = array_slice( array_values( array_filter( array_map( 'trim', explode( ',', $seo['kw'] ) ) ) ), 0, 5 );
		$out['rank_math_focus_keyword'] = sanitize_text_field( implode( ',', $kws ) );
	}
	if ( isset( $seo['robots'] ) && in_array( $seo['robots'], array( 'index', 'noindex' ), true ) ) {
		$out['rank_math_robots'] = array( $seo['robots'] );
	}
	return $out;
}

function utpk_apply_code_meta( $post_id ) {
	$GLOBALS['utpk_writing'] = true;
	$n                       = 0;
	foreach ( utpk_code_meta( $post_id ) as $k => $v ) {
		if ( get_post_meta( $post_id, $k, true ) !== $v ) {
			update_post_meta( $post_id, $k, $v );
			$n++;
		}
	}
	$GLOBALS['utpk_writing'] = false;
	return $n;
}

/* Find the Media Library item for an uploads URL, or register the file that is already on the server as one. */
function utpk_attachment_for( $src, $alt = '' ) {
	$id = attachment_url_to_postid( $src );
	if ( $id ) {
		return $id;
	}
	$up  = wp_get_upload_dir();
	$rel = '';
	if ( 0 === strpos( $src, $up['baseurl'] . '/' ) ) {
		$rel = substr( $src, strlen( $up['baseurl'] ) + 1 );
	} elseif ( false !== ( $p = strpos( $src, '/wp-content/uploads/' ) ) ) {
		$rel = substr( $src, $p + strlen( '/wp-content/uploads/' ) );
	}
	$rel  = ltrim( (string) strtok( $rel, '?' ), '/' );
	$file = $up['basedir'] . '/' . $rel;
	if ( '' === $rel || false !== strpos( $rel, '..' ) || ! file_exists( $file ) ) {
		return 0;
	}
	$type = wp_check_filetype( $file );
	if ( empty( $type['type'] ) || 0 !== strpos( $type['type'], 'image/' ) ) {
		return 0;
	}
	$title = str_replace( 'Uptrendpos', 'UpTrendPos', ucwords( trim( preg_replace( '/[-_]+/', ' ', pathinfo( $file, PATHINFO_FILENAME ) ) ) ) );
	$id    = wp_insert_attachment( array( 'guid' => $up['baseurl'] . '/' . $rel, 'post_mime_type' => $type['type'], 'post_title' => $title, 'post_status' => 'inherit' ), $file, 0, true );
	if ( is_wp_error( $id ) || ! $id ) {
		return 0;
	}
	update_attached_file( $id, $rel );
	if ( ! function_exists( 'wp_generate_attachment_metadata' ) ) {
		require_once ABSPATH . 'wp-admin/includes/image.php';
	}
	wp_update_attachment_metadata( $id, wp_generate_attachment_metadata( $id, $file ) );
	if ( '' !== $alt ) {
		update_post_meta( $id, '_wp_attachment_image_alt', sanitize_text_field( $alt ) );
	}
	return (int) $id;
}

function utpk_auto_thumb( $post_id ) {
	if ( ! utpk_opt( 'auto_thumb' ) ) {
		return;
	}
	$auto = (int) get_post_meta( $post_id, '_utpk_auto_thumb', true );
	$cur  = (int) get_post_thumbnail_id( $post_id );
	if ( $cur && $cur !== $auto ) {
		return; // chosen by hand: keep it
	}
	$src = utpk_page_image( $post_id, true );
	if ( '' === $src ) {
		return;
	}
	$alt = '';
	if ( preg_match( '#<img\b[^>]*\ssrc="' . preg_quote( $src, '#' ) . '"[^>]*\salt="([^"]*)"#i', utpk_page_html( $post_id, true ), $m ) ) {
		$alt = html_entity_decode( $m[1], ENT_QUOTES, 'UTF-8' );
	}
	$id = utpk_attachment_for( $src, $alt );
	if ( $id && $id !== $cur ) {
		set_post_thumbnail( $post_id, $id );
		update_post_meta( $post_id, '_utpk_auto_thumb', $id );
	}
}

function utpk_auto_page( $post_id ) {
	$post_id = (int) $post_id;
	if ( ! $post_id || 'page' !== get_post_type( $post_id ) || wp_is_post_revision( $post_id ) || wp_is_post_autosave( $post_id ) ) {
		return;
	}
	if ( ! utpk_page_is_designed( $post_id ) ) {
		return;
	}
	if ( utpk_opt( 'auto_seo' ) && utpk_apply_code_meta( $post_id ) ) {
		utpk_flush_live();
	}
	utpk_auto_thumb( $post_id );
}

/* Run after every save: WordPress editor, quick edit, REST and Elementor. */
add_action( 'save_post_page', function ( $post_id ) {
	if ( defined( 'DOING_AUTOSAVE' ) && DOING_AUTOSAVE ) {
		return;
	}
	utpk_auto_page( $post_id );
}, 100 );

add_action( 'elementor/document/after_save', function ( $document ) {
	if ( is_object( $document ) && method_exists( $document, 'get_main_id' ) ) {
		utpk_auto_page( $document->get_main_id() );
	}
}, 100 );

/* Rank Math saves its sidebar right after Elementor. If it tries to write a different SEO value
   for a page whose code carries one, the value from the page code is kept. */
function utpk_guard_meta( $check, $object_id, $meta_key, $meta_value ) {
	if ( ! empty( $GLOBALS['utpk_writing'] ) || ! in_array( $meta_key, UTPK_SEO_KEYS, true ) || ! utpk_opt( 'auto_seo' ) ) {
		return $check;
	}
	if ( 'page' !== get_post_type( $object_id ) ) {
		return $check;
	}
	$want = utpk_code_meta( $object_id );
	if ( ! isset( $want[ $meta_key ] ) || maybe_unserialize( $meta_value ) === $want[ $meta_key ] ) {
		return $check;
	}
	$GLOBALS['utpk_writing'] = true;
	update_post_meta( $object_id, $meta_key, $want[ $meta_key ] );
	$GLOBALS['utpk_writing'] = false;
	return true; // skip the other value
}
add_filter( 'update_post_metadata', 'utpk_guard_meta', 10, 4 );
add_filter( 'add_post_metadata', 'utpk_guard_meta', 10, 4 );

/* After a plugin update: set up every designed page once, so nothing needs a click. */
add_action( 'admin_init', function () {
	if ( get_option( 'utpk_auto_done' ) === UTPK_VERSION || ! current_user_can( 'edit_pages' ) ) {
		return;
	}
	update_option( 'utpk_auto_done', UTPK_VERSION, false );
	$ids = get_posts( array( 'post_type' => 'page', 'post_status' => array( 'publish', 'draft', 'private' ), 'numberposts' => -1, 'fields' => 'ids', 'suppress_filters' => true ) );
	foreach ( $ids as $id ) {
		utpk_auto_page( $id );
	}
	utpk_flush_live();
} );
