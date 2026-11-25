<?php
/**
 * Admin: UpTrendPos menu with "SEO Health" (checks + one-click fill of Rank Math fields
 * from the page code) and "Settings". Plus setup notices.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_action( 'admin_menu', function () {
	add_menu_page( 'UpTrendPos', 'UpTrendPos', 'edit_pages', 'utpk-seo', 'utpk_seo_screen', 'dashicons-store', 59 );
	add_submenu_page( 'utpk-seo', 'SEO Health', 'SEO Health', 'edit_pages', 'utpk-seo', 'utpk_seo_screen' );
	add_submenu_page( 'utpk-seo', 'UpTrendPos Settings', 'Settings', 'manage_options', 'utpk-settings', 'utpk_settings_screen' );
} );

/* =========================================================================
 * Notices
 * ========================================================================= */

function utpk_old_snippets() {
	$out = array();
	if ( post_type_exists( 'wpcode' ) ) {
		$posts = get_posts( array( 'post_type' => 'wpcode', 'post_status' => 'publish', 'numberposts' => 20, 's' => 'UpTrendPos', 'suppress_filters' => true ) );
		foreach ( (array) $posts as $p ) {
			$out[] = $p->post_title;
		}
	}
	if ( ! $out && function_exists( 'utp_schema_config' ) ) {
		$out[] = 'UpTrendPos SEO Snippet';
	}
	return $out;
}

add_action( 'admin_notices', function () {
	if ( ! current_user_can( 'manage_options' ) ) {
		return;
	}
	$old = utpk_old_snippets();
	if ( $old ) {
		echo '<div class="notice notice-error"><p><strong>UpTrendPos Site Kit:</strong> these old WPCode snippets are still active: <em>' . esc_html( implode( ', ', $old ) ) . '</em>. The plugin now does their job. Go to <a href="' . esc_url( admin_url( 'admin.php?page=wpcode' ) ) . '">Code Snippets</a> and switch them off, then purge the cache. Until then the plugin keeps its schema and ALT pass switched off so nothing runs twice.</p></div>';
	}
	if ( '' === trim( (string) get_option( 'blogname' ) ) ) {
		echo '<div class="notice notice-error"><p><strong>UpTrendPos Site Kit:</strong> the Site Title is empty. Set it to <code>UpTrendPos</code> in <a href="' . esc_url( admin_url( 'options-general.php' ) ) . '">Settings &rarr; General</a>.</p></div>';
	}
	if ( ! defined( 'RANK_MATH_VERSION' ) ) {
		echo '<div class="notice notice-warning"><p><strong>UpTrendPos Site Kit:</strong> Rank Math is not active. Schema is still printed by the plugin, but titles, descriptions and the sitemap need Rank Math.</p></div>';
	}
} );

/* =========================================================================
 * SEO Health
 * ========================================================================= */

function utpk_seo_rows() {
	$pages = get_posts( array( 'post_type' => 'page', 'post_status' => array( 'publish', 'draft', 'private' ), 'numberposts' => -1, 'orderby' => 'title', 'order' => 'ASC', 'suppress_filters' => true ) );
	$rows  = array();
	foreach ( $pages as $p ) {
		$robots   = get_post_meta( $p->ID, 'rank_math_robots', true );
		$noindex  = is_array( $robots ) && in_array( 'noindex', $robots, true );
		$code     = utpk_page_seo( $p->ID );
		$rm       = array(
			'title' => (string) get_post_meta( $p->ID, 'rank_math_title', true ),
			'desc'  => (string) get_post_meta( $p->ID, 'rank_math_description', true ),
			'kw'    => (string) get_post_meta( $p->ID, 'rank_math_focus_keyword', true ),
			'score' => (string) get_post_meta( $p->ID, 'rank_math_seo_score', true ),
		);
		$designed = utpk_page_is_designed( $p->ID );
		$issues   = array();
		if ( 'publish' !== $p->post_status ) {
			$issues[] = array( 'grey', ucfirst( $p->post_status ) );
		}
		if ( $designed && $noindex ) {
			$issues[] = array( 'red', 'Designed but set to noindex' );
		}
		if ( ! $designed && ! $noindex && 'publish' === $p->post_status && (int) get_option( 'page_on_front' ) !== $p->ID ) {
			$issues[] = array( 'grey', 'Old design' );
		}
		if ( ! $noindex ) {
			if ( '' === $rm['kw'] ) {
				$issues[] = array( 'red', 'No focus keyword' );
			}
			if ( '' === $rm['title'] ) {
				$issues[] = array( 'red', 'No SEO title' );
			} elseif ( mb_strlen( $rm['title'] ) > 60 ) {
				$issues[] = array( 'amber', 'Title over 60' );
			}
			if ( '' === $rm['desc'] ) {
				$issues[] = array( 'red', 'No description' );
			} elseif ( mb_strlen( $rm['desc'] ) > 160 || mb_strlen( $rm['desc'] ) < 110 ) {
				$issues[] = array( 'amber', 'Description length' );
			}
			$focus = trim( (string) strtok( $rm['kw'], ',' ) );
			if ( '' !== $focus && '' !== $rm['title'] && false === stripos( $rm['title'], $focus ) ) {
				$issues[] = array( 'amber', 'Keyword not in title' );
			}
		}
		if ( $designed && ! has_post_thumbnail( $p->ID ) ) {
			$issues[] = array( 'amber', 'No featured image' );
		}
		$sync = true;
		if ( $code ) {
			if ( ( isset( $code['title'] ) && $code['title'] !== $rm['title'] ) || ( isset( $code['desc'] ) && $code['desc'] !== $rm['desc'] ) || ( isset( $code['kw'] ) && $code['kw'] !== $rm['kw'] ) || ( isset( $code['robots'] ) && ( 'noindex' === $code['robots'] ) !== $noindex ) ) {
				$sync     = false;
				$issues[] = array( 'blue', 'Page code has new SEO values' );
			}
		}
		$rows[] = compact( 'p', 'noindex', 'code', 'rm', 'designed', 'issues', 'sync' );
	}
	return $rows;
}

function utpk_seo_screen() {
	$rows = utpk_seo_rows();
	$done = isset( $_GET['utpk_done'] ) ? (int) $_GET['utpk_done'] : -1; // phpcs:ignore WordPress.Security.NonceVerification
	?>
	<div class="wrap utpk-admin">
		<h1>UpTrendPos SEO Health</h1>
		<style>
			.utpk-admin .cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin:16px 0 20px}
			.utpk-admin .card{background:#fff;border:1px solid #dcdcde;border-radius:10px;padding:14px 16px;margin:0;max-width:none}
			.utpk-admin .card strong{display:block;font-size:14px;margin-bottom:4px}
			.utpk-admin .pill{display:inline-block;margin:0 4px 4px 0;padding:2px 8px;border-radius:99px;font-size:11.5px;font-weight:600;white-space:nowrap}
			.utpk-admin .pill.red{background:#fde8e8;color:#9b1c1c}.utpk-admin .pill.amber{background:#fef3c7;color:#92400e}.utpk-admin .pill.blue{background:#e0ecff;color:#1e429f}.utpk-admin .pill.grey{background:#eef0f3;color:#4b5563}.utpk-admin .pill.green{background:#def7ec;color:#03543f}
			.utpk-admin td small{color:#646970;display:block;line-height:1.4}
			.utpk-admin .len{color:#646970;font-size:11px}
			.utpk-admin .score{font-weight:700}
		</style>
		<?php if ( isset( $_GET['utpk_made'] ) ) : // phpcs:ignore WordPress.Security.NonceVerification ?>
			<div class="notice notice-success"><p><?php echo (int) $_GET['utpk_made']; // phpcs:ignore ?> draft page(s) created.</p></div>
		<?php endif; ?>
		<?php if ( $done >= 0 ) : ?>
			<div class="notice notice-success"><p><?php echo esc_html( $done ); ?> page(s) updated in Rank Math. Open each one in Elementor once and click <strong>Update</strong> so Rank Math recalculates its score, then purge the cache.</p></div>
		<?php endif; ?>
		<div class="cards">
			<div class="card"><strong>Rank Math</strong><?php echo defined( 'RANK_MATH_VERSION' ) ? '<span class="pill green">Active</span>' : '<span class="pill red">Not active</span>'; ?></div>
			<div class="card"><strong>Old WPCode snippets</strong><?php $old = utpk_old_snippets(); echo $old ? '<span class="pill red">Still on: ' . esc_html( implode( ', ', $old ) ) . '</span>' : '<span class="pill green">Off</span>'; ?></div>
			<div class="card"><strong>Business type links</strong><?php
				$chk = array();
				foreach ( array( (int) get_option( 'page_on_front' ), ( get_page_by_path( utpk_brand()['hub_slug'] ) ? get_page_by_path( utpk_brand()['hub_slug'] )->ID : 0 ) ) as $pid ) {
					if ( $pid ) {
						$miss = utpk_missing_types_in_code( $pid );
						$chk[] = get_the_title( $pid ) . ': ' . ( $miss ? count( $miss ) . ' added by the plugin (' . implode( ', ', $miss ) . ')' : 'all ' . count( utpk_industries()['types'] ) . ' listed' );
					}
				}
				echo '<span class="pill green">Always complete</span><small>' . esc_html( implode( ' | ', $chk ) ) . '</small>';
				?></div>
			<div class="card"><strong>Missing pages</strong><form method="post" action="<?php echo esc_url( admin_url( 'admin-post.php' ) ); ?>"><input type="hidden" name="action" value="utpk_make_pages"><?php wp_nonce_field( 'utpk_make_pages' ); ?><button class="button" type="submit">Create missing pages now</button></form><small>Runs on its own after every plugin update and when a new business type is added.</small></div>
			<div class="card"><strong>Live pages</strong><?php echo (int) count( utpk_live_slugs() ); ?> published and indexed. They show in the menu, footer and hub schema on their own.</div>
			<div class="card"><strong>Files for search engines</strong><a href="<?php echo esc_url( home_url( '/sitemap_index.xml' ) ); ?>" target="_blank">sitemap_index.xml</a> · <a href="<?php echo esc_url( home_url( '/llms.txt' ) ); ?>" target="_blank">llms.txt</a> · <a href="<?php echo esc_url( home_url( '/robots.txt' ) ); ?>" target="_blank">robots.txt</a></div>
		</div>
		<p>Each page code carries its own SEO title, description, keywords and index setting. Since 1.3.1 this happens on its own every time a page is saved; the button below is only for a manual re-run. Rows marked <span class="pill blue">Page code has new SEO values</span> are different from Rank Math right now.</p>
		<form method="post" action="<?php echo esc_url( admin_url( 'admin-post.php' ) ); ?>">
			<input type="hidden" name="action" value="utpk_apply_seo">
			<?php wp_nonce_field( 'utpk_apply_seo' ); ?>
			<p><button class="button button-primary" type="submit">Fill Rank Math from page code (selected pages)</button></p>
			<table class="widefat striped">
				<thead><tr><td class="check-column"><input type="checkbox" onclick="document.querySelectorAll('.utpk-cb').forEach(function(c){c.checked=this.checked}.bind(this))"></td><th>Page</th><th>Index</th><th>Focus keyword</th><th>SEO title</th><th>Description</th><th>Score</th><th>Checks</th></tr></thead>
				<tbody>
				<?php foreach ( $rows as $r ) : $p = $r['p']; ?>
					<tr>
						<th class="check-column"><?php if ( $r['code'] ) : ?><input class="utpk-cb" type="checkbox" name="ids[]" value="<?php echo (int) $p->ID; ?>" <?php checked( ! $r['sync'] ); ?>><?php endif; ?></th>
						<td><strong><a href="<?php echo esc_url( get_edit_post_link( $p->ID ) ); ?>"><?php echo esc_html( $p->post_title ); ?></a></strong><small>/<?php echo esc_html( get_page_uri( $p ) ); ?>/ · <a href="<?php echo esc_url( admin_url( 'post.php?post=' . $p->ID . '&action=elementor' ) ); ?>">Elementor</a> · <a href="<?php echo esc_url( get_permalink( $p ) ); ?>" target="_blank">View</a></small></td>
						<td><?php echo $r['noindex'] ? '<span class="pill grey">noindex</span>' : '<span class="pill green">index</span>'; ?><?php if ( isset( $r['code']['robots'] ) ) { echo '<small>code: ' . esc_html( $r['code']['robots'] ) . '</small>'; } ?></td>
						<td><?php echo esc_html( $r['rm']['kw'] ); ?><?php if ( isset( $r['code']['kw'] ) && $r['code']['kw'] !== $r['rm']['kw'] ) { echo '<small>code: ' . esc_html( $r['code']['kw'] ) . '</small>'; } ?></td>
						<td><?php echo esc_html( $r['rm']['title'] ); ?> <span class="len">(<?php echo (int) mb_strlen( $r['rm']['title'] ); ?>)</span><?php if ( isset( $r['code']['title'] ) && $r['code']['title'] !== $r['rm']['title'] ) { echo '<small>code: ' . esc_html( $r['code']['title'] ) . ' (' . (int) mb_strlen( $r['code']['title'] ) . ')</small>'; } ?></td>
						<td><?php echo esc_html( $r['rm']['desc'] ); ?> <span class="len">(<?php echo (int) mb_strlen( $r['rm']['desc'] ); ?>)</span><?php if ( isset( $r['code']['desc'] ) && $r['code']['desc'] !== $r['rm']['desc'] ) { echo '<small>code: ' . esc_html( $r['code']['desc'] ) . ' (' . (int) mb_strlen( $r['code']['desc'] ) . ')</small>'; } ?></td>
						<td class="score"><?php echo '' !== $r['rm']['score'] ? esc_html( $r['rm']['score'] ) : '–'; ?></td>
						<td><?php if ( ! $r['issues'] ) { echo '<span class="pill green">OK</span>'; } foreach ( $r['issues'] as $i ) { echo '<span class="pill ' . esc_attr( $i[0] ) . '">' . esc_html( $i[1] ) . '</span>'; } ?></td>
					</tr>
				<?php endforeach; ?>
				</tbody>
			</table>
			<p><button class="button button-primary" type="submit">Fill Rank Math from page code (selected pages)</button></p>
		</form>
	</div>
	<?php
}

add_action( 'admin_post_utpk_apply_seo', function () {
	if ( ! current_user_can( 'edit_pages' ) ) {
		wp_die( 'Not allowed.' );
	}
	check_admin_referer( 'utpk_apply_seo' );
	$ids  = isset( $_POST['ids'] ) ? array_map( 'absint', (array) wp_unslash( $_POST['ids'] ) ) : array();
	$done = 0;
	foreach ( $ids as $id ) {
		if ( ! $id || ! current_user_can( 'edit_post', $id ) ) {
			continue;
		}
		if ( ! utpk_page_seo( $id, true ) ) {
			continue;
		}
		utpk_apply_code_meta( $id );
		utpk_auto_thumb( $id );
		clean_post_cache( $id );
		$done++;
	}
	utpk_flush_live();
	wp_safe_redirect( admin_url( 'admin.php?page=utpk-seo&utpk_done=' . $done ) );
	exit;
} );

/* =========================================================================
 * Settings
 * ========================================================================= */

add_action( 'admin_init', function () {
	register_setting( 'utpk', 'utpk', array(
		'type'              => 'array',
		'sanitize_callback' => function ( $in ) {
			$in  = (array) $in;
			$out = array();
			foreach ( utpk_defaults() as $k => $v ) {
				if ( is_int( $v ) ) {
					$out[ $k ] = empty( $in[ $k ] ) ? 0 : 1;
				} elseif ( in_array( $k, array( 'apk', 'exe', 'reviewer_url', 'asset_source' ), true ) ) {
					$out[ $k ] = isset( $in[ $k ] ) ? esc_url_raw( trim( $in[ $k ] ) ) : '';
				} elseif ( 'live_extra' === $k ) {
					$out[ $k ] = isset( $in[ $k ] ) ? sanitize_textarea_field( $in[ $k ] ) : '';
				} else {
					$out[ $k ] = isset( $in[ $k ] ) ? sanitize_text_field( $in[ $k ] ) : '';
				}
			}
			return $out;
		},
		'default'           => utpk_defaults(),
	) );
} );

function utpk_settings_screen() {
	$o      = wp_parse_args( (array) get_option( 'utpk', array() ), utpk_defaults() );
	$checks = array(
		'header'        => 'Show the UpTrendPos header (with the Industries mega menu) on every page',
		'footer'        => 'Show the UpTrendPos footer on every page',
		'hide_theme_hf' => 'Hide the theme / Jeg Kit / Elementor header and footer templates',
		'motion'        => 'Hero animations and soft scroll effects (turned off on its own for visitors who ask for less motion)',
		'schema'        => 'Schema in Rank Math: Organization, software, FAQ, breadcrumbs, industry hub',
		'alt'           => 'Automatic image ALT text',
		'gate'          => 'Links to pages that are not live yet show as plain text',
		'cleanup'       => 'Clean the page head (emoji, generator, RSD, shortlink, oEmbed) and turn off XML-RPC',
		'llms'          => 'Serve /llms.txt for AI search engines',
		'redirects'     => '301-redirect old URLs that now return 404',
		'auto_seo'      => 'Fill Rank Math (SEO title, description, focus + secondary keywords, index) from the page code every time a page is saved',
		'auto_thumb'    => 'Set the featured image from the first picture in the page design (a picture you choose by hand is kept)',
		'auto_lists'    => 'Home page and Industries hub always list every business type from the registry (new types appear on their own)',
		'auto_pages'    => 'Make a draft page (right URL, Elementor HTML widget, title hidden, noindex) for every business type or main page that has no page yet',
	);
	$text = array(
		'apk'            => array( 'Android APK link', 'Full URL. Empty = button shows "Coming soon".' ),
		'apk_version'    => array( 'APK version', 'e.g. 1.0.0' ),
		'apk_size'       => array( 'APK size', 'e.g. 58 MB' ),
		'apk_min'        => array( 'Android needed', 'e.g. Android 8.0 or newer' ),
		'exe'            => array( 'Windows setup link', 'Full URL of the .zip or .exe' ),
		'exe_version'    => array( 'Windows version', 'e.g. 1.0.0' ),
		'exe_size'       => array( 'Windows file size', 'e.g. 120 MB' ),
		'updated'        => array( 'Last update date', 'e.g. 20 Oct 2026' ),
		'reviewer_name'  => array( 'Pages reviewed by (name)', 'A real person who checks the page facts, e.g. the founder. Empty = "UpTrendPos team".' ),
		'reviewer_title' => array( 'Reviewer job title', 'e.g. Founder' ),
		'reviewer_url'   => array( 'Reviewer profile link', 'LinkedIn or About page URL' ),
		'asset_source'   => array( 'Asset source (automation)', 'Public GitHub raw folder the daily automation may download page code and images from, e.g. https://raw.githubusercontent.com/owner/uptrendpos-site-assets/main/. Empty = off.' ),
	);
	?>
	<div class="wrap">
		<h1>UpTrendPos Site Kit settings</h1>
		<form method="post" action="options.php">
			<?php settings_fields( 'utpk' ); ?>
			<h2>Site parts</h2>
			<table class="form-table" role="presentation">
				<?php foreach ( $checks as $k => $label ) : ?>
					<tr><th scope="row"><?php echo esc_html( ucwords( str_replace( '_', ' ', $k ) ) ); ?></th><td><label><input type="checkbox" name="utpk[<?php echo esc_attr( $k ); ?>]" value="1" <?php checked( ! empty( $o[ $k ] ) ); ?>> <?php echo esc_html( $label ); ?></label></td></tr>
				<?php endforeach; ?>
			</table>
			<h2>Downloads and page reviewer</h2>
			<table class="form-table" role="presentation">
				<?php foreach ( $text as $k => $t ) : ?>
					<tr><th scope="row"><label for="utpk-<?php echo esc_attr( $k ); ?>"><?php echo esc_html( $t[0] ); ?></label></th><td><input class="regular-text" id="utpk-<?php echo esc_attr( $k ); ?>" type="text" name="utpk[<?php echo esc_attr( $k ); ?>]" value="<?php echo esc_attr( $o[ $k ] ); ?>"><p class="description"><?php echo esc_html( $t[1] ); ?></p></td></tr>
				<?php endforeach; ?>
				<tr><th scope="row"><label for="utpk-live_extra">Always treat as live</label></th><td><textarea class="large-text" rows="2" id="utpk-live_extra" name="utpk[live_extra]"><?php echo esc_textarea( $o['live_extra'] ); ?></textarea><p class="description">Normally empty. Pages go live on their own when they are published and set to index in Rank Math. Add a slug here only for a page that lives outside WordPress.</p></td></tr>
			</table>
			<?php submit_button(); ?>
			<p>Version <?php echo esc_html( UTPK_VERSION ); ?>. After saving, purge the cache (LiteSpeed / hPanel).</p>
		</form>
	</div>
	<?php
}
