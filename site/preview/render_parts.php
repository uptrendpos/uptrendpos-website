<?php
/* Preview helper: renders the plugin's real header, footer and sprite outside WordPress.
   Usage: php render_parts.php <plugin dir> <current slug> <page html file> <asset url> <live,slugs> */
define( 'ABSPATH', '/' );
define( 'DAY_IN_SECONDS', 86400 );
$GLOBALS['utpk_prev'] = array( 'dir' => rtrim( $argv[1], '/' ) . '/', 'slug' => $argv[2], 'html' => file_get_contents( $argv[3] ), 'url' => rtrim( $argv[4], '/' ) . '/', 'live' => array_filter( explode( ',', $argv[5] ) ) );
function plugin_dir_path( $f ) { return $GLOBALS['utpk_prev']['dir']; }
function plugin_dir_url( $f ) { return $GLOBALS['utpk_prev']['url']; }
function plugin_basename( $f ) { return 'uptrendpos-site-kit/uptrendpos-site-kit.php'; }
function add_action() {} function add_filter() {} function register_activation_hook() {}
function home_url( $p = '/' ) { return 'https://uptrendpos.com' . $p; }
function esc_url( $u ) { return htmlspecialchars( $u, ENT_QUOTES ); }
function esc_url_raw( $u ) { return $u; }
function esc_attr( $s ) { return htmlspecialchars( $s, ENT_QUOTES ); }
function esc_html( $s ) { return htmlspecialchars( $s, ENT_QUOTES ); }
function get_option( $k, $d = false ) { return $d; }
function wp_parse_args( $a, $d ) { return array_merge( $d, (array) $a ); }
function get_transient( $k ) { return $GLOBALS['utpk_prev']['live']; }
function set_transient() {} function delete_transient() {}
function sanitize_title( $s ) { return strtolower( preg_replace( '/[^a-z0-9-]+/i', '-', $s ) ); }
function is_singular() { return true; }
function get_queried_object_id() { return 1; }
function get_post_meta() { return ''; }
function get_post_field( $f, $id ) { return 'post_name' === $f ? $GLOBALS['utpk_prev']['slug'] : $GLOBALS['utpk_prev']['html']; }
function is_admin() { return false; } function is_feed() { return false; } function wp_doing_ajax() { return false; }
define( 'UTPK_DIR', $GLOBALS['utpk_prev']['dir'] ); define( 'UTPK_URL', $GLOBALS['utpk_prev']['url'] ); define( 'UTPK_VERSION', '1.0.0' ); define( 'UTPK_FILE', UTPK_DIR . 'uptrendpos-site-kit.php' );
require $GLOBALS['utpk_prev']['dir'] . 'inc/config.php';
require $GLOBALS['utpk_prev']['dir'] . 'inc/front.php';
echo json_encode( array( 'sprite' => utpk_sprite(), 'header' => utpk_header_html(), 'footer' => utpk_footer_html(), 'gated' => utpk_gate_html( $GLOBALS['utpk_prev']['html'] ), 'cfg' => utpk_js_config() ) );
