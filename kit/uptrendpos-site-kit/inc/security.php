<?php
/**
 * UpTrendPos Site Kit - security hardening (1.6.3).
 *
 * 1. HTTP security headers. Written into the root .htaccess (between
 *    "# BEGIN UpTrendPos Security Headers" markers) so they also reach pages
 *    served from the WP-Optimize page cache, which never runs PHP. If the
 *    .htaccess file cannot be written, the same headers are sent from PHP.
 * 2. User enumeration: anonymous /wp/v2/users REST calls and ?author=N
 *    archive lookups are closed.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'UTPK_HT_MARKER', 'UpTrendPos Security Headers' );

function utpk_security_headers() {
	return array(
		'Strict-Transport-Security' => 'max-age=31536000',
		'X-Content-Type-Options'    => 'nosniff',
		'X-Frame-Options'           => 'SAMEORIGIN',
		'Referrer-Policy'           => 'strict-origin-when-cross-origin',
		'Permissions-Policy'        => 'camera=(), microphone=(), geolocation=(), payment=(), usb=()',
		'Content-Security-Policy'   => "upgrade-insecure-requests; frame-ancestors 'self'; object-src 'none'; base-uri 'self'",
	);
}

function utpk_htaccess_path() {
	if ( ! function_exists( 'get_home_path' ) ) {
		require_once ABSPATH . 'wp-admin/includes/file.php';
	}
	return get_home_path() . '.htaccess';
}

/* Write (or refresh) the .htaccess block once per plugin version. */
function utpk_write_security_htaccess() {
	if ( ! function_exists( 'insert_with_markers' ) ) {
		require_once ABSPATH . 'wp-admin/includes/misc.php';
	}
	$file = utpk_htaccess_path();
	if ( ! ( file_exists( $file ) ? wp_is_writable( $file ) : wp_is_writable( dirname( $file ) ) ) ) {
		update_option( 'utpk_ht_ver', 'php-fallback', false );
		return false;
	}
	$lines = array( '<IfModule mod_headers.c>' );
	foreach ( utpk_security_headers() as $k => $v ) {
		$lines[] = '	Header always set ' . $k . ' "' . $v . '"';
	}
	$lines[] = '</IfModule>';
	$ok = insert_with_markers( $file, UTPK_HT_MARKER, $lines );
	update_option( 'utpk_ht_ver', $ok ? UTPK_VERSION : 'php-fallback', false );
	return $ok;
}

add_action( 'init', function () {
	$ver = get_option( 'utpk_ht_ver' );
	if ( UTPK_VERSION !== $ver && 'php-fallback' !== $ver ) {
		utpk_write_security_htaccess();
	}
}, 5 );

/* PHP fallback only when the .htaccess block could not be written (avoids double headers). */
add_action( 'send_headers', function () {
	if ( 'php-fallback' !== get_option( 'utpk_ht_ver' ) || headers_sent() ) {
		return;
	}
	foreach ( utpk_security_headers() as $k => $v ) {
		header( $k . ': ' . $v );
	}
} );

/* Remove the block when the plugin is deactivated. */
register_deactivation_hook( UTPK_FILE, function () {
	if ( ! function_exists( 'insert_with_markers' ) ) {
		require_once ABSPATH . 'wp-admin/includes/misc.php';
	}
	$file = utpk_htaccess_path();
	if ( file_exists( $file ) && wp_is_writable( $file ) ) {
		insert_with_markers( $file, UTPK_HT_MARKER, array() );
	}
	delete_option( 'utpk_ht_ver' );
} );

/* Close user enumeration for visitors (admins and the editor keep full access). */
add_filter( 'rest_endpoints', function ( $endpoints ) {
	if ( is_user_logged_in() ) {
		return $endpoints;
	}
	foreach ( array_keys( $endpoints ) as $route ) {
		if ( 0 === strpos( $route, '/wp/v2/users' ) ) {
			unset( $endpoints[ $route ] );
		}
	}
	return $endpoints;
} );

add_action( 'template_redirect', function () {
	if ( is_user_logged_in() ) {
		return;
	}
	if ( isset( $_GET['author'] ) || is_author() ) { // phpcs:ignore WordPress.Security.NonceVerification
		wp_safe_redirect( home_url( '/' ), 301, 'UpTrendPos Site Kit' );
		exit;
	}
}, 0 );
