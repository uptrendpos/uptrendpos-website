<?php
/**
 * 1.5.0 - REST layer for the daily automation (namespace utpk/v1). Logged-in users only (WPVibe connects as the admin).
 * Safety by design - this API can ONLY:
 *  - upload images named uptrendpos-<slug>.webp into the uploads root (same name = replaced in place, never "-1" copies);
 *  - write UpTrendPos page code into the HTML widget of a business-type page or a main page, and publish it;
 *  - start an UpdraftPlus backup and report when the last one finished;
 *  - remove media that nothing on the site uses: "-1/-2" duplicate copies and old uptrendpos-*.webp images.
 * It cannot delete pages, posts, users, plugins or settings, and cannot run any other code.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

const UTPK_IMG_RE = '/^uptrendpos-[a-z0-9]+(?:-[a-z0-9]+)*\.webp$/';

function utpk_api_can() {
	return current_user_can( 'publish_pages' ) && current_user_can( 'upload_files' );
}

add_action( 'rest_api_init', function () {
	$ns = 'utpk/v1';
	register_rest_route( $ns, '/status', array( 'methods' => 'GET', 'callback' => 'utpk_api_status', 'permission_callback' => 'utpk_api_can' ) );
	register_rest_route( $ns, '/media', array( 'methods' => 'POST', 'callback' => 'utpk_api_media', 'permission_callback' => 'utpk_api_can' ) );
	register_rest_route( $ns, '/page', array( 'methods' => 'POST', 'callback' => 'utpk_api_page', 'permission_callback' => 'utpk_api_can' ) );
	register_rest_route( $ns, '/backup', array( 'methods' => 'POST', 'callback' => 'utpk_api_backup', 'permission_callback' => 'utpk_api_can' ) );
	register_rest_route( $ns, '/media-cleanup', array( 'methods' => 'POST', 'callback' => 'utpk_api_cleanup', 'permission_callback' => 'utpk_api_can' ) );
	register_rest_route( $ns, '/replace', array( 'methods' => 'POST', 'callback' => 'utpk_api_replace', 'permission_callback' => 'utpk_api_can' ) );
	register_rest_route( $ns, '/source', array( 'methods' => 'GET', 'callback' => 'utpk_api_source', 'permission_callback' => 'utpk_api_can' ) ); // 1.7.0
	register_rest_route( $ns, '/font', array( 'methods' => 'POST', 'callback' => 'utpk_api_font', 'permission_callback' => 'utpk_api_can' ) ); // 1.7.0
	register_rest_route( $ns, '/check', array( 'methods' => 'GET', 'callback' => 'utpk_api_check', 'permission_callback' => 'utpk_api_can' ) ); // 1.7.0
	register_rest_route( $ns, '/self-update', array( 'methods' => 'POST', 'callback' => 'utpk_api_self_update', 'permission_callback' => 'utpk_api_can_update' ) );
} );

/** Plugin self-update needs a real administrator (update_plugins + install_plugins). */
function utpk_api_can_update() {
	return current_user_can( 'update_plugins' ) && current_user_can( 'install_plugins' );
}

/**
 * POST /self-update {version:"1.5.2"}
 * Installs THIS plugin from <asset_source>plugin/uptrendpos-site-kit-<version>.zip only, and only a newer
 * version. Same as Plugins > Upload > "Replace current with uploaded"; the plugin stays active.
 */
function utpk_api_self_update( WP_REST_Request $req ) {
	$ver = (string) $req->get_param( 'version' );
	if ( ! preg_match( '/^\d{1,2}\.\d{1,2}\.\d{1,3}$/', $ver ) ) {
		return new WP_Error( 'utpk_version', 'version must look like 1.5.2', array( 'status' => 400 ) );
	}
	if ( version_compare( $ver, UTPK_VERSION, '<=' ) ) {
		return new WP_Error( 'utpk_version', 'Version ' . $ver . ' is not newer than ' . UTPK_VERSION, array( 'status' => 409 ) );
	}
	$src = trim( (string) utpk_opt( 'asset_source' ) );
	if ( ! preg_match( '#^https://raw\.githubusercontent\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/[A-Za-z0-9_./-]+/$#', $src ) ) {
		return new WP_Error( 'utpk_source', 'Asset source is not set', array( 'status' => 400 ) );
	}
	$url = $src . 'plugin/uptrendpos-site-kit-' . $ver . '.zip';
	require_once ABSPATH . 'wp-admin/includes/file.php';
	require_once ABSPATH . 'wp-admin/includes/misc.php';
	require_once ABSPATH . 'wp-admin/includes/plugin.php';
	require_once ABSPATH . 'wp-admin/includes/class-wp-upgrader.php';
	$tmp = download_url( $url, 60 );
	if ( is_wp_error( $tmp ) ) {
		return new WP_Error( 'utpk_fetch', 'Could not download ' . $url, array( 'status' => 502 ) );
	}
	$zip = new ZipArchive();
	$ok  = true === $zip->open( $tmp );
	$top = $ok && $zip->numFiles ? strtok( (string) $zip->getNameIndex( 0 ), '/' ) : '';
	$main = $ok ? (string) $zip->getFromName( 'uptrendpos-site-kit/uptrendpos-site-kit.php' ) : '';
	if ( $ok ) {
		$zip->close();
	}
	if ( 'uptrendpos-site-kit' !== $top || false === strpos( $main, "define( 'UTPK_VERSION', '" . $ver . "' )" ) ) {
		@unlink( $tmp ); // phpcs:ignore
		return new WP_Error( 'utpk_zip', 'Zip is not UpTrendPos Site Kit ' . $ver, array( 'status' => 422 ) );
	}
	$up  = new Plugin_Upgrader( new WP_Ajax_Upgrader_Skin() );
	$res = $up->install( $tmp, array( 'overwrite_package' => true ) );
	@unlink( $tmp ); // phpcs:ignore
	if ( is_wp_error( $res ) || ! $res ) {
		return new WP_Error( 'utpk_install', is_wp_error( $res ) ? $res->get_error_message() : 'Install failed', array( 'status' => 500 ) );
	}
	if ( ! is_plugin_active( 'uptrendpos-site-kit/uptrendpos-site-kit.php' ) ) {
		activate_plugin( 'uptrendpos-site-kit/uptrendpos-site-kit.php' );
	}
	utpk_purge_caches();
	return array( 'installed' => $ver, 'from' => $url );
}

/* ---------------- helpers ---------------- */

function utpk_uploads() {
	$up = wp_get_upload_dir();
	return array( rtrim( $up['basedir'], '/' ), rtrim( $up['baseurl'], '/' ) );
}

function utpk_last_backup() {
	$o = get_option( 'updraft_last_backup' );
	return is_array( $o ) && ! empty( $o['backup_time'] ) ? (int) $o['backup_time'] : 0;
}

/* How many places use an attachment: page code (any post meta), post content, featured images, options. Revisions and trash ignored. */
function utpk_media_refs( $id, $file ) {
	global $wpdb;
	$like = '%' . $wpdb->esc_like( $file ) . '%';
	$n    = (int) $wpdb->get_var( $wpdb->prepare(
		"SELECT COUNT(*) FROM {$wpdb->postmeta} m JOIN {$wpdb->posts} p ON p.ID = m.post_id
		 WHERE m.meta_key NOT IN ('_wp_attached_file','_wp_attachment_metadata','_wp_attachment_backup_sizes','_wp_attachment_image_alt')
		 AND p.post_type <> 'revision' AND p.post_status NOT IN ('trash','auto-draft') AND m.meta_value LIKE %s", $like ) );
	$n   += (int) $wpdb->get_var( $wpdb->prepare(
		"SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type NOT IN ('revision','attachment') AND post_status IN ('publish','draft','private','future','pending') AND post_content LIKE %s", $like ) );
	$n   += (int) $wpdb->get_var( $wpdb->prepare(
		"SELECT COUNT(*) FROM {$wpdb->postmeta} m JOIN {$wpdb->posts} p ON p.ID = m.post_id WHERE m.meta_key = '_thumbnail_id' AND m.meta_value = %s AND p.post_status NOT IN ('trash','auto-draft') AND p.post_type <> 'revision'", (string) $id ) );
	$n   += (int) $wpdb->get_var( $wpdb->prepare(
		"SELECT COUNT(*) FROM {$wpdb->options} WHERE option_value LIKE %s OR ( option_name IN ('site_icon','site_logo','custom_logo') AND option_value = %s )", $like, (string) $id ) );
	return $n;
}

function utpk_regen_attachment( $id, $path ) {
	$old = wp_get_attachment_metadata( $id );
	if ( is_array( $old ) && ! empty( $old['sizes'] ) ) {
		$dir = dirname( $path );
		foreach ( $old['sizes'] as $s ) {
			if ( ! empty( $s['file'] ) && is_file( $dir . '/' . $s['file'] ) ) {
				wp_delete_file( $dir . '/' . $s['file'] );
			}
		}
	}
	if ( ! function_exists( 'wp_generate_attachment_metadata' ) ) {
		require_once ABSPATH . 'wp-admin/includes/image.php';
	}
	wp_update_attachment_metadata( $id, wp_generate_attachment_metadata( $id, $path ) );
	clean_post_cache( $id );
}


/* Files can also come from the public UpTrendPos assets repo set in Settings ("Asset source"), so the daily run sends a short URL, not the file. */
function utpk_fetch_asset( $url, $max ) {
	$src = trim( (string) utpk_opt( 'asset_source' ) );
	if ( '' === $src || 0 !== strpos( $url, $src ) || ! preg_match( '#^https://raw\.githubusercontent\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/#', $src ) || false !== strpos( substr( $url, strlen( $src ) ), '..' ) ) {
		return new WP_Error( 'utpk_src', 'URL is not inside the allowed asset source.', array( 'status' => 400 ) );
	}
	$res = wp_safe_remote_get( $url, array( 'timeout' => 30, 'limit_response_size' => $max + 1 ) );
	if ( is_wp_error( $res ) || 200 !== (int) wp_remote_retrieve_response_code( $res ) ) {
		return new WP_Error( 'utpk_fetch', 'Could not download the file from the asset source.', array( 'status' => 502 ) );
	}
	$body = (string) wp_remote_retrieve_body( $res );
	if ( strlen( $body ) > $max ) {
		return new WP_Error( 'utpk_size', 'File is too large.', array( 'status' => 400 ) );
	}
	return $body;
}

/* ---------------- GET /status ---------------- */

function utpk_api_urdu_list() {
	$out = array();
	if ( utpk_ur_home_id() ) {
		$out[] = array( 'en' => 'home', 'id' => utpk_ur_home_id(), 'status' => 'publish', 'url' => get_permalink( utpk_ur_home_id() ) );
	}
	$ids = get_posts( array( 'post_type' => 'page', 'post_status' => array( 'publish', 'draft', 'pending', 'private' ), 'numberposts' => -1, 'fields' => 'ids', 'suppress_filters' => true, 'meta_key' => '_utpk_lang', 'meta_value' => 'ur' ) );
	foreach ( $ids as $id ) {
		$out[] = array( 'en' => (string) get_post_meta( $id, '_utpk_en', true ), 'id' => (int) $id, 'status' => get_post_status( $id ), 'url' => get_permalink( $id ), 'title' => get_the_title( $id ) );
	}
	return $out;
}

function utpk_api_status() {
	delete_transient( 'utpk_dl_files' ); // 1.6.8: always look at the download folders again
	$types = array();
	foreach ( utpk_industries()['types'] as $t ) {
		$id      = utpk_find_page( $t['slug'] );
		$types[] = array(
			'slug'     => $t['slug'],
			'name'     => $t['name'],
			'page_id'  => $id,
			'status'   => $id ? get_post_status( $id ) : 'missing',
			'designed' => $id ? utpk_page_is_designed( $id ) : false,
			'live'     => utpk_is_live( $t['slug'] ),
		);
	}
	return array(
		'version'     => UTPK_VERSION,
		'time'        => time(),
		'last_backup' => utpk_last_backup(),
		'downloads'   => array( 'apk' => utpk_download( 'apk' ), 'exe' => utpk_download( 'exe' ) ), // 1.6.8
		'urdu'        => utpk_api_urdu_list(), // 1.7.0
		'urdu_font'   => array( 'url' => utpk_ur_font_url(), 'version' => (string) get_option( 'utpk_ur_font_ver', '' ) ),
		'types'       => $types,
	);
}

/* ---------------- POST /media {name, data (base64), alt} ---------------- */

function utpk_api_media( WP_REST_Request $r ) {
	$name = (string) $r->get_param( 'name' );
	$alt  = sanitize_text_field( (string) $r->get_param( 'alt' ) );
	if ( ! preg_match( UTPK_IMG_RE, $name ) ) {
		return new WP_Error( 'utpk_name', 'Only uptrendpos-<slug>.webp file names are allowed.', array( 'status' => 400 ) );
	}
	if ( $r->get_param( 'url' ) ) {
		$bin = utpk_fetch_asset( (string) $r->get_param( 'url' ), 1572864 );
		if ( is_wp_error( $bin ) ) {
			return $bin;
		}
	} else {
		$bin = base64_decode( (string) $r->get_param( 'data' ), true );
	}
	if ( false === $bin || strlen( $bin ) < 200 || strlen( $bin ) > 1572864 ) {
		return new WP_Error( 'utpk_data', 'Image data missing or over 1.5 MB.', array( 'status' => 400 ) );
	}
	$info = function_exists( 'getimagesizefromstring' ) ? @getimagesizefromstring( $bin ) : false; // phpcs:ignore WordPress.PHP.NoSilencedErrors
	if ( ! $info || 'image/webp' !== $info['mime'] || $info[0] < 50 || $info[1] < 50 ) {
		return new WP_Error( 'utpk_type', 'The data is not a WebP image.', array( 'status' => 400 ) );
	}
	list( $dir, $url ) = utpk_uploads();
	$path = $dir . '/' . $name;
	$same = is_file( $path ) && sha1_file( $path ) === sha1( $bin );
	if ( ! $same ) {
		$tmp = $path . '.utpk-tmp';
		if ( false === file_put_contents( $tmp, $bin ) || ! rename( $tmp, $path ) ) { // phpcs:ignore WordPress.WP.AlternativeFunctions
			return new WP_Error( 'utpk_write', 'Could not write the file.', array( 'status' => 500 ) );
		}
	}
	$id      = attachment_url_to_postid( $url . '/' . $name );
	$created = false;
	if ( ! $id ) {
		$id      = utpk_attachment_for( $url . '/' . $name, $alt );
		$created = true;
	} elseif ( ! $same ) {
		utpk_regen_attachment( $id, $path );
	}
	if ( $id && '' !== $alt ) {
		update_post_meta( $id, '_wp_attachment_image_alt', $alt );
	}
	if ( ! $same ) {
		do_action( 'litespeed_purge_url', $url . '/' . $name );
	}
	return array( 'id' => (int) $id, 'url' => $url . '/' . $name, 'replaced' => ! $same && ! $created, 'unchanged' => $same, 'created' => $created );
}

/* ---------------- POST /page {slug, html, publish} ---------------- */

function utpk_page_code_ok( $html ) {
	return ! ( strlen( $html ) > 409600 || ! preg_match( '#^\s*<div class="utp[ "]#', $html ) || false === strpos( $html, 'data-seo-title="' ) || preg_match( '#<script|<style|<!--|<iframe|<form|<object|<embed|javascript:|\son[a-z]+\s*=#i', $html ) );
}

function utpk_api_page( WP_REST_Request $r ) {
	$slug = sanitize_title( (string) $r->get_param( 'slug' ) );
	$html = (string) $r->get_param( 'html' );
	if ( '' === $html && $r->get_param( 'html_url' ) ) {
		$html = utpk_fetch_asset( (string) $r->get_param( 'html_url' ), 409600 );
		if ( is_wp_error( $html ) ) {
			return $html;
		}
	}
	$pub  = (bool) $r->get_param( 'publish' );
	if ( 'ur' === $r->get_param( 'lang' ) && 'home' !== $slug && 'ur' !== $slug ) {
		if ( ! utpk_page_code_ok( $html ) ) {
			return new WP_Error( 'utpk_html', 'The page code is not valid UpTrendPos page code.', array( 'status' => 400 ) );
		}
		return utpk_api_page_ur( $r, $slug, $html, $pub ); // 1.7.0: Urdu twin under /ur/
	}
	if ( 'ur' === $r->get_param( 'lang' ) ) {
		$slug = 'ur'; // the Urdu copy of Home is the core page /ur/
	}
	$ok   = isset( utpk_core_page_list()[ $slug ] );
	// 1.6.2: the front page (slug "home") may be written too, so site-wide facts such as plan prices stay editable through this route
	$ok   = $ok || ( 'home' === $slug && (int) get_option( 'page_on_front' ) === utpk_find_page( 'home' ) );
	foreach ( utpk_industries()['types'] as $t ) {
		$ok = $ok || $t['slug'] === $slug;
	}
	if ( ! $ok ) {
		return new WP_Error( 'utpk_slug', 'Only business-type pages and main UpTrendPos pages can be written.', array( 'status' => 400 ) );
	}
	if ( ! utpk_page_code_ok( $html ) ) {
		return new WP_Error( 'utpk_html', 'The page code is not valid UpTrendPos page code.', array( 'status' => 400 ) );
	}
	$id = utpk_find_page( $slug );
	return utpk_api_page_write( $id, $slug, $html, $pub );
}

/* 1.7.0 Urdu twin: slug = the English slug; title = the Urdu page name. Business types sit under
   the Urdu industries hub (publish it first), every other page under /ur/. */
function utpk_api_page_ur( WP_REST_Request $r, $slug, $html, $pub ) {
	$core = utpk_core_page_list();
	$type = false;
	foreach ( utpk_industries()['types'] as $t ) {
		$type = $type || $t['slug'] === $slug;
	}
	if ( ( ! isset( $core[ $slug ] ) && ! $type ) || 'ur' === $slug ) {
		return new WP_Error( 'utpk_slug', 'Only business-type pages and main UpTrendPos pages can get an Urdu page.', array( 'status' => 400 ) );
	}
	if ( ! utpk_find_page( $slug ) || 'publish' !== get_post_status( utpk_find_page( $slug ) ) ) {
		return new WP_Error( 'utpk_en', 'The English page must be live first.', array( 'status' => 400 ) );
	}
	if ( false === strpos( $html, 'utp-urdu' ) || false === strpos( $html, 'dir="rtl"' ) || false === strpos( $html, 'lang="ur"' ) ) {
		return new WP_Error( 'utpk_html', 'Urdu page code needs class utp-urdu, lang="ur" and dir="rtl" on the page block.', array( 'status' => 400 ) );
	}
	$id = utpk_ur_find( $slug );
	if ( ! $id ) {
		$title = trim( wp_strip_all_tags( (string) $r->get_param( 'title' ) ) );
		if ( '' === $title || ! preg_match( '/[\x{0600}-\x{06FF}]/u', $title ) ) {
			return new WP_Error( 'utpk_title', 'Send the Urdu page name as title.', array( 'status' => 400 ) );
		}
		$parent = $type ? utpk_ur_find( utpk_brand()['hub_slug'] ) : utpk_ur_home_id();
		if ( ! $parent || 'publish' !== get_post_status( $parent ) ) {
			return new WP_Error( 'utpk_parent', $type ? 'Publish the Urdu industries hub (/ur/industries/) first.' : 'The Urdu Home page /ur/ is not live.', array( 'status' => 400 ) );
		}
		$id = utpk_create_draft( $slug, $title, $parent, utpk_find_page( $slug ) );
		if ( $id ) {
			update_post_meta( $id, '_utpk_lang', 'ur' );
			update_post_meta( $id, '_utpk_en', $slug );
			if ( get_post_field( 'post_name', $id ) !== $slug ) {
				wp_update_post( array( 'ID' => $id, 'post_name' => $slug ) );
			}
		}
		if ( ! $id ) {
			return new WP_Error( 'utpk_page', 'The Urdu page could not be made.', array( 'status' => 500 ) );
		}
	}
	return utpk_api_page_write( $id, $slug, $html, $pub );
}

function utpk_api_page_write( $id, $slug, $html, $pub ) {
	if ( ! $id ) {
		$hub    = get_page_by_path( utpk_brand()['hub_slug'] );
		$parent = isset( utpk_core_page_list()[ $slug ] ) ? 0 : ( $hub ? (int) $hub->ID : 0 );
		$name   = utpk_core_page_list()[ $slug ] ?? $slug; // 1.6.8: core pages get their real title, not the slug
		foreach ( utpk_industries()['types'] as $t ) {
			if ( $t['slug'] === $slug ) {
				$name = $t['name'];
			}
		}
		$id = utpk_create_draft( $slug, $name, $parent, utpk_reference_page() );
	}
	if ( ! $id || 'trash' === get_post_status( $id ) ) {
		return new WP_Error( 'utpk_page', 'The page could not be found or made.', array( 'status' => 500 ) );
	}
	// put the code into the first HTML widget; keep every other layout setting as it is
	$raw  = get_post_meta( $id, '_elementor_data', true );
	$data = is_string( $raw ) ? json_decode( $raw, true ) : null;
	if ( ! is_array( $data ) || ! $data ) {
		$data = utpk_layout_from( utpk_reference_page() );
	}
	$set  = false;
	$walk = function ( $els ) use ( &$walk, &$set, $html ) {
		foreach ( $els as $k => $el ) {
			if ( ! $set && isset( $el['widgetType'] ) && 'html' === $el['widgetType'] ) {
				$els[ $k ]['settings']['html'] = $html;
				$set                           = true;
			} elseif ( ! empty( $el['elements'] ) ) {
				$els[ $k ]['elements'] = $walk( $el['elements'] );
			}
		}
		return $els;
	};
	$data = $walk( $data );
	if ( ! $set ) {
		$data = utpk_layout_from( 0 );
		$data = $walk( $data );
	}
	$saved = false;
	if ( class_exists( '\Elementor\Plugin' ) && isset( \Elementor\Plugin::$instance->documents ) ) {
		$doc = \Elementor\Plugin::$instance->documents->get( $id, false );
		if ( $doc ) {
			$saved = (bool) $doc->save( array( 'elements' => $data ) );
		}
	}
	if ( ! $saved ) {
		update_post_meta( $id, '_elementor_data', wp_slash( wp_json_encode( $data ) ) );
		delete_post_meta( $id, '_elementor_element_cache' );
		delete_post_meta( $id, '_elementor_css' );
	}
	update_post_meta( $id, '_elementor_edit_mode', 'builder' );
	if ( $pub && 'publish' !== get_post_status( $id ) ) {
		wp_update_post( array( 'ID' => $id, 'post_status' => 'publish' ) );
	} else {
		wp_update_post( array( 'ID' => $id ) ); // runs the normal save hooks (SEO, featured image)
	}
	utpk_page_html( $id, true );
	utpk_auto_page( $id );
	utpk_flush_live();
	utpk_purge_caches();
	return array(
		'id'        => (int) $id,
		'url'       => get_permalink( $id ),
		'status'    => get_post_status( $id ),
		'seo_title' => get_post_meta( $id, 'rank_math_title', true ),
		'keywords'  => get_post_meta( $id, 'rank_math_focus_keyword', true ),
		'robots'    => get_post_meta( $id, 'rank_math_robots', true ),
		'thumbnail' => (int) get_post_thumbnail_id( $id ),
		'elementor' => $saved ? 'document_save' : 'meta_write',
	);
}

/* ---------------- POST /replace {pairs:[{find,replace}], apply} ---------------- */

/**
 * 1.6.3 - site-wide plain-text fact change (e.g. "14-day" -> "7-day").
 * Only plain text: find/replace may not contain < or >, so no markup or script can be added.
 * Targets: the front page, every core page, every business-type page and every blog post.
 * Elementor pages: text inside HTML widgets. Other posts: post_content and excerpt. Plus Rank Math title/description.
 * Without apply:true it only reports what would change.
 */
function utpk_api_replace( WP_REST_Request $r ) {
	$pairs = $r->get_param( 'pairs' );
	$apply = (bool) $r->get_param( 'apply' );
	if ( ! is_array( $pairs ) || ! $pairs || count( $pairs ) > 20 ) {
		return new WP_Error( 'utpk_pairs', 'Send 1 to 20 pairs of {find, replace}.', array( 'status' => 400 ) );
	}
	$find = array();
	$repl = array();
	foreach ( $pairs as $p ) {
		$f = isset( $p['find'] ) ? (string) $p['find'] : '';
		$t = isset( $p['replace'] ) ? (string) $p['replace'] : '';
		if ( strlen( $f ) < 3 || strlen( $f ) > 300 || strlen( $t ) > 300 || $f === $t || preg_match( '/[<>]/', $f . $t ) ) {
			return new WP_Error( 'utpk_pairs', 'Each pair needs plain text: find 3-300 characters, replace up to 300, no < or >.', array( 'status' => 400 ) );
		}
		$find[] = $f;
		$repl[] = $t;
	}
	$swap = function ( $s, &$n ) use ( $find, $repl ) {
		$c   = 0;
		$out = str_replace( $find, $repl, (string) $s, $c );
		$n  += $c;
		return $out;
	};

	$ids   = array();
	$slugs = array_keys( utpk_core_page_list() );
	foreach ( utpk_industries()['types'] as $t ) {
		$slugs[] = $t['slug'];
	}
	foreach ( array_unique( $slugs ) as $slug ) {
		$id = utpk_find_page( $slug );
		if ( $id ) {
			$ids[ $id ] = $slug;
		}
	}
	foreach ( (array) get_posts( array( 'post_type' => 'page', 'post_status' => array( 'publish', 'draft' ), 'numberposts' => -1, 'fields' => 'ids', 'suppress_filters' => true, 'meta_key' => '_utpk_lang', 'meta_value' => 'ur' ) ) as $pid ) {
		$ids[ (int) $pid ] = 'ur/' . get_post_field( 'post_name', $pid ); // 1.7.0: Urdu pages too
	}
	$front = (int) get_option( 'page_on_front' );
	if ( $front ) {
		$ids[ $front ] = 'home';
	}
	foreach ( (array) get_posts( array( 'post_type' => 'post', 'post_status' => array( 'publish', 'draft', 'future', 'pending', 'private' ), 'numberposts' => -1, 'fields' => 'ids', 'suppress_filters' => true ) ) as $pid ) {
		$ids[ (int) $pid ] = (string) get_post_field( 'post_name', $pid );
	}

	$report = array( 'apply' => $apply, 'pages' => array(), 'total' => 0 );
	foreach ( $ids as $id => $slug ) {
		if ( 'trash' === get_post_status( $id ) ) {
			continue;
		}
		$n    = 0;
		$raw  = get_post_meta( $id, '_elementor_data', true );
		$data = is_string( $raw ) && '' !== $raw ? json_decode( $raw, true ) : null;
		$new_content = null;
		$new_excerpt = null;
		if ( is_array( $data ) && $data ) {
			$walk = function ( $els ) use ( &$walk, &$n, $swap ) {
				foreach ( $els as $k => $el ) {
					if ( isset( $el['widgetType'] ) && 'html' === $el['widgetType'] && isset( $el['settings']['html'] ) ) {
						$els[ $k ]['settings']['html'] = $swap( $el['settings']['html'], $n );
					}
					if ( ! empty( $el['elements'] ) ) {
						$els[ $k ]['elements'] = $walk( $el['elements'] );
					}
				}
				return $els;
			};
			$data = $walk( $data );
		} else {
			$data        = null;
			$new_content = $swap( get_post_field( 'post_content', $id, 'raw' ), $n );
			$new_excerpt = $swap( get_post_field( 'post_excerpt', $id, 'raw' ), $n );
		}
		$meta = array();
		foreach ( array( 'rank_math_title', 'rank_math_description' ) as $mk ) {
			$mv = get_post_meta( $id, $mk, true );
			if ( is_string( $mv ) && '' !== $mv ) {
				$c2 = 0;
				$nv = $swap( $mv, $c2 );
				if ( $c2 ) {
					$meta[ $mk ] = $nv;
					$n          += $c2;
				}
			}
		}
		if ( ! $n ) {
			continue;
		}
		$report['pages'][] = array( 'id' => (int) $id, 'slug' => $slug, 'type' => get_post_type( $id ), 'changes' => $n );
		$report['total']  += $n;
		if ( ! $apply ) {
			continue;
		}
		if ( null !== $data ) {
			$saved = false;
			if ( class_exists( '\Elementor\Plugin' ) && isset( \Elementor\Plugin::$instance->documents ) ) {
				$doc = \Elementor\Plugin::$instance->documents->get( $id, false );
				if ( $doc ) {
					$saved = (bool) $doc->save( array( 'elements' => $data ) );
				}
			}
			if ( ! $saved ) {
				update_post_meta( $id, '_elementor_data', wp_slash( wp_json_encode( $data ) ) );
				delete_post_meta( $id, '_elementor_element_cache' );
				delete_post_meta( $id, '_elementor_css' );
			}
			wp_update_post( array( 'ID' => $id ) ); // normal save hooks (SEO from the page code, featured image)
			utpk_page_html( $id, true );
			utpk_auto_page( $id );
		} else {
			wp_update_post( wp_slash( array( 'ID' => $id, 'post_content' => $new_content, 'post_excerpt' => $new_excerpt ) ) );
		}
		foreach ( $meta as $mk => $nv ) {
			update_post_meta( $id, $mk, $nv );
		}
	}
	if ( $apply && $report['total'] ) {
		utpk_flush_live();
		utpk_purge_caches();
	}
	return $report;
}

/* ---------------- POST /backup ---------------- */

/** Purge every page cache the site may run (LiteSpeed, WP-Optimize). */
function utpk_purge_caches() {
	do_action( 'litespeed_purge_all' );
	if ( function_exists( 'wpo_cache_flush' ) ) {
		wpo_cache_flush();
	}
}

function utpk_api_backup( WP_REST_Request $r = null ) {
	if ( ! class_exists( 'UpdraftPlus' ) && ! has_action( 'updraft_backup_all' ) ) {
		return new WP_Error( 'utpk_backup', 'UpdraftPlus is not active.', array( 'status' => 400 ) );
	}
	$before = utpk_last_backup();
	if ( $r && $r->get_param( 'now' ) ) {
		// Run the backup inside this request (WP-Cron may not fire on a site without visits).
		if ( function_exists( 'set_time_limit' ) ) {
			@set_time_limit( 600 ); // phpcs:ignore
		}
		do_action( 'updraft_backup_all' );
		$after = utpk_last_backup();
		return array( 'started' => true, 'done' => $after > $before, 'last_backup_before' => $before, 'last_backup' => $after );
	}
	if ( ! wp_next_scheduled( 'updraft_backup_all' ) ) {
		wp_schedule_single_event( time() + 5, 'updraft_backup_all' );
	}
	if ( function_exists( 'spawn_cron' ) ) {
		spawn_cron();
	}
	return array( 'started' => true, 'last_backup_before' => $before, 'hint' => 'Poll GET /utpk/v1/status until last_backup is newer than last_backup_before.' );
}

/* ---------------- POST /media-cleanup {apply, older_than_hours} ---------------- */

function utpk_api_cleanup( WP_REST_Request $r ) {
	global $wpdb;
	$apply = (bool) $r->get_param( 'apply' );
	$age   = max( 24, (int) ( $r->get_param( 'older_than_hours' ) ? $r->get_param( 'older_than_hours' ) : 48 ) );
	list( $dir, $url ) = utpk_uploads();
	$rows = $wpdb->get_results(
		"SELECT p.ID, p.post_date_gmt, m.meta_value AS file FROM {$wpdb->posts} p JOIN {$wpdb->postmeta} m ON m.post_id = p.ID AND m.meta_key = '_wp_attached_file'
		 WHERE p.post_type = 'attachment' AND m.meta_value LIKE 'uptrendpos-%' ORDER BY p.post_date_gmt ASC"
	);
	$by   = array();
	foreach ( $rows as $row ) {
		if ( preg_match( UTPK_IMG_RE, $row->file ) ) {
			$by[ $row->file ] = $row;
		}
	}
	$report = array( 'merged' => array(), 'deleted' => array(), 'kept_in_use' => array(), 'apply' => $apply );
	// 1) "-N" copies of a base file: the newest copy becomes the base file, then the copies go
	foreach ( $by as $file => $row ) {
		if ( ! preg_match( '/^(.+)-(\d{1,2})\.webp$/', $file, $m ) || ! isset( $by[ $m[1] . '.webp' ] ) ) {
			continue;
		}
		$base = $by[ $m[1] . '.webp' ];
		$group = array();
		foreach ( $by as $f2 => $r2 ) {
			if ( preg_match( '/^' . preg_quote( $m[1], '/' ) . '-\d{1,2}\.webp$/', $f2 ) ) {
				$group[ $f2 ] = $r2;
			}
		}
		if ( isset( $report['merged'][ $base->file ] ) ) {
			continue;
		}
		$newest = end( $group );
		$bpath  = $dir . '/' . $base->file;
		$npath  = $dir . '/' . $newest->file;
		$entry  = array( 'base' => $base->file, 'newest_copy' => $newest->file, 'copies' => array_keys( $group ), 'base_updated' => false );
		if ( $apply && is_file( $npath ) && ( ! is_file( $bpath ) || sha1_file( $npath ) !== sha1_file( $bpath ) ) ) {
			if ( copy( $npath, $bpath ) ) {
				utpk_regen_attachment( (int) $base->ID, $bpath );
				$entry['base_updated'] = true;
			}
		}
		$report['merged'][ $base->file ] = $entry;
		foreach ( $group as $f2 => $r2 ) {
			if ( utpk_media_refs( $r2->ID, $f2 ) > 0 ) {
				$report['kept_in_use'][] = $f2;
				continue;
			}
			if ( $apply ) {
				wp_delete_attachment( (int) $r2->ID, true );
			}
			$report['deleted'][] = $f2;
			unset( $by[ $f2 ] );
		}
	}
	// 2) old uptrendpos-*.webp images that nothing uses any more
	$cut = time() - $age * HOUR_IN_SECONDS;
	foreach ( $by as $file => $row ) {
		if ( in_array( $file, $report['deleted'], true ) || strtotime( $row->post_date_gmt . ' UTC' ) > $cut ) {
			continue;
		}
		if ( utpk_media_refs( $row->ID, $file ) > 0 ) {
			continue;
		}
		if ( $apply ) {
			wp_delete_attachment( (int) $row->ID, true );
		}
		$report['deleted'][] = $file;
	}
	if ( $apply && ( $report['deleted'] || $report['merged'] ) ) {
		utpk_purge_caches();
	}
	return $report;
}

/* ---------------- 1.7.0 POST /font {"file":"fonts/jameel-noori-nastaleeq-ur.woff2"} ---------------- */

/* Installs the Urdu page-text font subset from the asset repo into uploads/utpk/.
   The daily Urdu run rebuilds it from the text of every Urdu page, so new words never fall back. */
function utpk_api_font( WP_REST_Request $r ) {
	$file = (string) ( $r->get_param( 'file' ) ? $r->get_param( 'file' ) : 'fonts/jameel-noori-nastaleeq-ur.woff2' );
	if ( ! preg_match( '#^fonts/[a-z0-9-]+\.woff2$#', $file ) ) {
		return new WP_Error( 'utpk_font', 'Only fonts/<name>.woff2 from the asset repo.', array( 'status' => 400 ) );
	}
	$body = utpk_fetch_asset( trailingslashit( (string) utpk_opt( 'asset_source' ) ) . $file, 1572864 );
	if ( is_wp_error( $body ) ) {
		return $body;
	}
	if ( 'wOF2' !== substr( $body, 0, 4 ) || strlen( $body ) < 10000 ) {
		return new WP_Error( 'utpk_font', 'The file is not a WOFF2 font.', array( 'status' => 400 ) );
	}
	$up  = wp_upload_dir( null, false );
	$dir = trailingslashit( $up['basedir'] ) . 'utpk';
	if ( ! wp_mkdir_p( $dir ) ) {
		return new WP_Error( 'utpk_font', 'Could not make the font folder.', array( 'status' => 500 ) );
	}
	$path = $dir . '/jameel-noori-nastaleeq-ur.woff2';
	if ( false === file_put_contents( $path, $body ) ) { // phpcs:ignore WordPress.WP.AlternativeFunctions
		return new WP_Error( 'utpk_font', 'Could not save the font.', array( 'status' => 500 ) );
	}
	$ver = substr( md5( $body ), 0, 10 );
	update_option( 'utpk_ur_font_ver', $ver, false );
	utpk_purge_caches();
	return array( 'installed' => true, 'bytes' => strlen( $body ), 'version' => $ver, 'url' => utpk_ur_font_url() );
}

/* ---------------- 1.7.0 GET /check?path=/ur/industries/ ---------------- */

/* Loads one page of this site fresh (cache bypassed) and reports what search engines and visitors get:
   status, speed, head SEO, hreflang, language, headings, links, images, NAP and security headers. */
function utpk_api_check( WP_REST_Request $r ) {
	$path = '/' . ltrim( (string) $r->get_param( 'path' ), '/' );
	if ( preg_match( '#[\s<>"\\]|\.\.#', $path ) || 0 === strpos( $path, '//' ) ) {
		return new WP_Error( 'utpk_path', 'Send a site path like /ur/ or /industries/grocery-store-pos-software/.', array( 'status' => 400 ) );
	}
	$url = home_url( $path );
	$t0  = microtime( true );
	$res = wp_remote_get( add_query_arg( 'utpk_check', time(), $url ), array( 'timeout' => 30, 'redirection' => 0, 'headers' => array( 'Cache-Control' => 'no-cache' ), 'user-agent' => 'UpTrendPos-SiteKit-Check/' . UTPK_VERSION ) );
	$ms  = (int) round( ( microtime( true ) - $t0 ) * 1000 );
	if ( is_wp_error( $res ) ) {
		return new WP_Error( 'utpk_check', 'The page could not be loaded: ' . $res->get_error_message(), array( 'status' => 502 ) );
	}
	$code = (int) wp_remote_retrieve_response_code( $res );
	$html = (string) wp_remote_retrieve_body( $res );
	$hdr  = wp_remote_retrieve_headers( $res );
	$one  = function ( $re ) use ( $html ) {
		return preg_match( $re, $html, $m ) ? html_entity_decode( trim( $m[1] ), ENT_QUOTES, 'UTF-8' ) : '';
	};
	$all  = function ( $re ) use ( $html ) {
		preg_match_all( $re, $html, $m );
		return $m[1];
	};
	$alts = array();
	preg_match_all( '#<link\s[^>]*hreflang=["\']([^"\']+)["\'][^>]*href=["\']([^"\']+)["\']#i', $html, $hl, PREG_SET_ORDER );
	foreach ( $hl as $h ) {
		$alts[ $h[1] ] = $h[2];
	}
	$body  = preg_replace( '#<(script|style)\b.*?</\1>#is', '', $html );
	$h1    = $all( '#<h1\b[^>]*>(.*?)</h1>#is' );
	$imgs  = $all( '#(<img\b[^>]*>)#i' );
	$noalt = 0;
	$nowebp = 0;
	$bad    = array();
	foreach ( $imgs as $im ) {
		if ( ! preg_match( '#\salt=["\'][^"\']+["\']#i', $im ) ) {
			$noalt++;
			$bad[] = 'no alt: ' . substr( $im, 0, 160 );
		}
		if ( preg_match( '#\ssrc=["\']([^"\']+\.(jpe?g|png))(\?|["\'])#i', $im, $src ) ) {
			$nowebp++;
			$bad[] = 'not webp: ' . $src[1];
		}
	}
	$home  = untrailingslashit( home_url() );
	$hrefs = $all( '~<a\b[^>]*\shref=["\']([^"\'#][^"\']*)["\']~i' );
	$int   = 0;
	$to_ur = 0;
	$to_en = array();
	foreach ( $hrefs as $h ) {
		$h = html_entity_decode( $h );
		if ( 0 !== strpos( $h, $home ) && ( '' === $h || '/' !== $h[0] || 0 === strpos( $h, '//' ) ) ) {
			continue;
		}
		$p = (string) wp_parse_url( 0 === strpos( $h, $home ) ? substr( $h, strlen( $home ) ) : $h, PHP_URL_PATH );
		if ( preg_match( '#^/(wp-|downloadapk|downloaddesktop|feed)#', $p ) ) {
			continue;
		}
		$int++;
		if ( 0 === strpos( $p, '/ur/' ) ) {
			$to_ur++;
		} else {
			$to_en[] = '' === $p ? '/' : $p;
		}
	}
	$sec = array();
	foreach ( array( 'strict-transport-security', 'x-content-type-options', 'x-frame-options', 'referrer-policy', 'permissions-policy', 'content-security-policy' ) as $k ) {
		$sec[ $k ] = isset( $hdr[ $k ] ) ? ( is_array( $hdr[ $k ] ) ? implode( ', ', $hdr[ $k ] ) : (string) $hdr[ $k ] ) : '';
	}
	$text = wp_strip_all_tags( $body );
	return array(
		'url'          => $url,
		'status'       => $code,
		'location'     => (string) wp_remote_retrieve_header( $res, 'location' ),
		'ms'           => $ms,
		'html_kb'      => round( strlen( $html ) / 1024, 1 ),
		'lang'         => $one( '#<html\b[^>]*\slang=["\']([^"\']+)#i' ),
		'dir'          => $one( '#<html\b[^>]*\sdir=["\']([^"\']+)#i' ),
		'title'        => $one( '#<title[^>]*>(.*?)</title>#is' ),
		'description'  => $one( '#<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)#i' ),
		'robots'       => $one( '#<meta\s+name=["\']robots["\']\s+content=["\']([^"\']*)#i' ),
		'canonical'    => $one( '#<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']*)#i' ),
		'og_locale'    => $one( '#<meta\s+property=["\']og:locale["\']\s+content=["\']([^"\']*)#i' ),
		'hreflang'     => $alts,
		'h1'           => array_map( function ( $x ) { return trim( wp_strip_all_tags( html_entity_decode( $x, ENT_QUOTES, 'UTF-8' ) ) ); }, $h1 ),
		'h2_count'     => count( $all( '#<h2\b[^>]*>(.*?)</h2>#is' ) ),
		'jsonld_types' => array_values( array_unique( $all( '#"@type"\s*:\s*"([A-Za-z]+)"#' ) ) ),
		'images'       => count( $imgs ),
		'images_no_alt'=> $noalt,
		'images_not_webp' => $nowebp,
		'image_notes'  => array_slice( $bad, 0, 12 ),
		'css_files'    => count( $all( '#<link\b[^>]*rel=["\']stylesheet["\'][^>]*href=["\']([^"\']+)#i' ) ),
		'js_files'     => count( $all( '#<script\b[^>]*\ssrc=["\']([^"\']+)#i' ) ),
		'font_preload' => count( $all( '#<link\b[^>]*rel=["\']preload["\'][^>]*as=["\']font["\'][^>]*href=["\']([^"\']+)#i' ) ) + count( $all( '#<link\b[^>]*rel=["\']preload["\'][^>]*href=["\']([^"\']+\.woff2[^"\']*)#i' ) ),
		'links_internal' => $int,
		'links_to_ur'  => $to_ur,
		'links_to_en'  => array_values( array_unique( $to_en ) ),
		'nap'          => array( 'name' => false !== strpos( $text, 'UpTrendPos' ), 'phone' => false !== strpos( $text, '0319 2223292' ) || false !== strpos( $html, '923192223292' ), 'city' => false !== strpos( $text, 'Sahiwal' ) || false !== strpos( $text, 'ساہیوال' ) ),
		'security'     => $sec,
		'urdu_chars'   => preg_match_all( '/[\x{0600}-\x{06FF}]/u', $text ),
		'latin_words'  => preg_match_all( '/\b[A-Za-z]{4,}\b/', $text ),
	);
}

/* ---------------- 1.7.0 GET /source?slug=<slug>&lang=en|ur ---------------- */

/* Only the page code (HTML widget) of one UpTrendPos page, so a translation run reads 40 KB, not the whole post. */
function utpk_api_source( WP_REST_Request $r ) {
	$slug = sanitize_title( (string) $r->get_param( 'slug' ) );
	$ur   = 'ur' === $r->get_param( 'lang' );
	if ( 'home' === $slug ) {
		$id = $ur ? utpk_ur_home_id() : (int) get_option( 'page_on_front' );
	} else {
		$id = $ur ? utpk_ur_find( $slug ) : utpk_find_page( $slug );
	}
	if ( ! $id ) {
		return new WP_Error( 'utpk_source', 'No such page.', array( 'status' => 404 ) );
	}
	$html = (string) utpk_page_html( $id );
	$out  = array( 'slug' => $slug, 'lang' => $ur ? 'ur' : 'en', 'id' => (int) $id, 'status' => get_post_status( $id ), 'url' => get_permalink( $id ), 'title' => get_the_title( $id ), 'md5' => md5( $html ), 'bytes' => strlen( $html ) );
	if ( 'md5' !== $r->get_param( 'fields' ) ) {
		$out['html'] = $html;
	}
	if ( $r->get_param( 'pad' ) ) {
		$out['pad'] = str_repeat( '.', 90000 ); // 1.7.2: makes the connector save the reply to a file, so the page code is read from disk, never retyped
	}
	return $out;
}
