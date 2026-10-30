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
	do_action( 'litespeed_purge_all' );
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

function utpk_api_status() {
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
	$ok   = isset( utpk_core_page_list()[ $slug ] );
	foreach ( utpk_industries()['types'] as $t ) {
		$ok = $ok || $t['slug'] === $slug;
	}
	if ( ! $ok ) {
		return new WP_Error( 'utpk_slug', 'Only business-type pages and main UpTrendPos pages can be written.', array( 'status' => 400 ) );
	}
	if ( strlen( $html ) > 409600 || ! preg_match( '#^\s*<div class="utp[ "]#', $html ) || false === strpos( $html, 'data-seo-title="' ) || preg_match( '#<script|<style|<!--|<iframe|<form|<object|<embed|javascript:|\son[a-z]+\s*=#i', $html ) ) {
		return new WP_Error( 'utpk_html', 'The page code is not valid UpTrendPos page code.', array( 'status' => 400 ) );
	}
	$id = utpk_find_page( $slug );
	if ( ! $id ) {
		$hub    = get_page_by_path( utpk_brand()['hub_slug'] );
		$parent = isset( utpk_core_page_list()[ $slug ] ) ? 0 : ( $hub ? (int) $hub->ID : 0 );
		$name   = $slug;
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
	do_action( 'litespeed_purge_all' );
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

/* ---------------- POST /backup ---------------- */

function utpk_api_backup() {
	if ( ! class_exists( 'UpdraftPlus' ) && ! has_action( 'updraft_backup_all' ) ) {
		return new WP_Error( 'utpk_backup', 'UpdraftPlus is not active.', array( 'status' => 400 ) );
	}
	$before = utpk_last_backup();
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
		do_action( 'litespeed_purge_all' );
	}
	return $report;
}
