<?php
/**
 * Plugin Name:       UpTrendPos Site Kit
 * Plugin URI:        https://uptrendpos.com/
 * Description:       One plugin for the whole uptrendpos.com front end: design system (CSS, JS, self-hosted fonts), site header with Industries mega menu, footer, animated hero stages, schema (Organization, SoftwareApplication, FAQ, breadcrumbs, industry hub), automatic image ALT text, automatic live-page links, Rank Math helpers, SEO Health screen with one-click SEO fill, llms.txt and redirects. Replaces the two WPCode snippets "UpTrendPos Design System" and "UpTrendPos SEO Snippet". Page designs are pasted as HTML into Elementor HTML widgets.
 * Version:           1.5.1
 * Requires at least: 6.3
 * Requires PHP:      7.4
 * Author:            UpTrendPos
 * Author URI:        https://uptrendpos.com/
 * License:           GPL-2.0-or-later
 * Text Domain:       uptrendpos-site-kit
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'UTPK_VERSION', '1.5.1' );
define( 'UTPK_FILE', __FILE__ );
define( 'UTPK_DIR', plugin_dir_path( __FILE__ ) );
define( 'UTPK_URL', plugin_dir_url( __FILE__ ) );

require_once UTPK_DIR . 'inc/config.php';
require_once UTPK_DIR . 'inc/front.php';
require_once UTPK_DIR . 'inc/schema.php';
require_once UTPK_DIR . 'inc/seo.php';
require_once UTPK_DIR . 'inc/auto.php';
require_once UTPK_DIR . 'inc/pages.php';
require_once UTPK_DIR . 'inc/api.php';

if ( is_admin() ) {
	require_once UTPK_DIR . 'inc/admin.php';
}

register_activation_hook( __FILE__, function () {
	delete_transient( 'utpk_live' );
	if ( false === get_option( 'utpk', false ) ) {
		add_option( 'utpk', utpk_defaults() );
	}
} );

add_filter( 'plugin_action_links_' . plugin_basename( __FILE__ ), function ( $links ) {
	array_unshift(
		$links,
		'<a href="' . esc_url( admin_url( 'admin.php?page=utpk-seo' ) ) . '">SEO Health</a>',
		'<a href="' . esc_url( admin_url( 'admin.php?page=utpk-settings' ) ) . '">Settings</a>'
	);
	return $links;
} );
