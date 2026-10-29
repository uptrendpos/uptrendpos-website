/*
 * WPCode snippet name: UpTrendPos SEO Snippet  (Code type: PHP Snippet, Insert: Auto Insert, Location: Run Everywhere)
 * Version: 2026-10-13d (shortcodes such as [fluentform id="1"] now work inside page HTML widgets). Always update THIS one snippet - never add a second PHP SEO snippet.
 * One snippet for every page: schema + automatic image ALT text + shortcodes inside Elementor HTML widgets.
 * Adds to Rank Math's own schema (same @ids), so nothing is duplicated.
 * - Organization: fixed brand data on every page
 * - SoftwareApplication: UpTrendPos product on every page
 * - FAQPage: built automatically from the FAQ list on any page (only the questions shown on that page)
 * - Industry pages: WebPage gets the business type as its audience
 * If Rank Math is ever switched off, the same schema is printed by this snippet instead.
 */

if ( ! function_exists( 'utp_schema_config' ) ) {

	/* ===== EDIT HERE ONLY ===== */
	function utp_schema_config() {
		return array(
			'name'        => 'UpTrendPos',
			'alt_name'    => 'UpTrend POS',
			'logo'        => 'https://uptrendpos.com/wp-content/uploads/uptrend-POS-Logo.png',
			'logo_w'      => 512,
			'logo_h'      => 512,
			'email'       => 'sales@uptrendpos.com',
			'phone'       => '+92-319-2223292',
			'street'      => 'House No 193/A, Umer Block, Shadab Town', // official address - always use this
			'city'        => 'Sahiwal',
			'region'      => 'Punjab',
			'postcode'    => '57000',
			'country'     => 'PK',
			'same_as'     => array(
				'https://www.facebook.com/uptrendpos',
				'https://www.instagram.com/uptrendpos/',
				'https://www.youtube.com/@UpTrendPos',
				'https://www.linkedin.com/company/uptrendpos',
			),
			'price_low'   => '2000',
			'price_high'  => '6000',
			'offer_count' => '3',
			'pricing_url' => 'https://uptrendpos.com/pos-software-pricing/',
		);
	}
	/* ========================== */

	function utp_schema_home() {
		return trailingslashit( home_url( '/' ) );
	}

	function utp_schema_org( $c ) {
		$address = array(
			'@type'           => 'PostalAddress',
			'addressLocality' => $c['city'],
			'addressRegion'   => $c['region'],
			'postalCode'      => $c['postcode'],
			'addressCountry'  => $c['country'],
		);
		if ( '' !== $c['street'] ) {
			$address = array_merge( array( '@type' => 'PostalAddress', 'streetAddress' => $c['street'] ), $address );
		}
		return array(
			'@type'              => 'Organization',
			'@id'                => utp_schema_home() . '#organization',
			'name'               => $c['name'],
			'alternateName'      => $c['alt_name'],
			'url'                => utp_schema_home(),
			'logo'               => array(
				'@type'  => 'ImageObject',
				'@id'    => utp_schema_home() . '#logo',
				'url'    => $c['logo'],
				'width'  => $c['logo_w'],
				'height' => $c['logo_h'],
			),
			'image'              => array( '@id' => utp_schema_home() . '#logo' ),
			'email'              => $c['email'],
			'telephone'          => $c['phone'],
			'address'            => $address,
			'areaServed'         => $c['country'],
			'contactPoint'       => array(
				array(
					'@type'             => 'ContactPoint',
					'telephone'         => $c['phone'],
					'contactType'       => 'sales',
					'email'             => $c['email'],
					'availableLanguage' => array( 'en', 'ur' ),
					'areaServed'        => $c['country'],
				),
			),
			'sameAs'             => $c['same_as'],
		);
	}

	function utp_schema_software( $c ) {
		return array(
			'@type'                  => 'SoftwareApplication',
			'@id'                    => utp_schema_home() . '#software',
			'name'                   => $c['name'],
			'applicationCategory'    => 'BusinessApplication',
			'applicationSubCategory' => 'Point of Sale',
			'operatingSystem'        => 'Windows, Android, Web browser',
			'description'            => 'POS and accounting software for Pakistani businesses with offline billing, inventory, udhaar khata, installments, multi-branch control and FBR-ready invoices.',
			'image'                  => $c['logo'],
			'url'                    => utp_schema_home(),
			'publisher'              => array( '@id' => utp_schema_home() . '#organization' ),
			'offers'                 => array(
				'@type'         => 'AggregateOffer',
				'priceCurrency' => 'PKR',
				'lowPrice'      => $c['price_low'],
				'highPrice'     => $c['price_high'],
				'offerCount'    => $c['offer_count'],
				'url'           => $c['pricing_url'],
			),
		);
	}

	/* Reads the FAQ list from the page's Elementor HTML widget (details/summary) */
	function utp_schema_faq_items( $post_id ) {
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
		if ( false === strpos( $html, 'utp-faq-list' ) ) {
			return array();
		}
		$html  = substr( $html, strpos( $html, 'utp-faq-list' ) );
		$items = array();
		if ( preg_match_all( '#<details[^>]*>\s*<summary[^>]*>(.*?)</summary>(.*?)</details>#is', $html, $m, PREG_SET_ORDER ) ) {
			foreach ( $m as $row ) {
				$q = trim( html_entity_decode( wp_strip_all_tags( $row[1] ), ENT_QUOTES, 'UTF-8' ) );
				$a = trim( preg_replace( '/\s+/', ' ', html_entity_decode( wp_strip_all_tags( $row[2] ), ENT_QUOTES, 'UTF-8' ) ) );
				if ( '' !== $q && '' !== $a ) {
					$items[] = array(
						'@type'          => 'Question',
						'name'           => $q,
						'acceptedAnswer' => array( '@type' => 'Answer', 'text' => $a ),
					);
				}
			}
		}
		return $items;
	}

	/* Business type for pages under /industries/ (from the page title) */
	function utp_schema_industry( $post_id ) {
		$parent = (int) wp_get_post_parent_id( $post_id );
		if ( ! $parent || 'industries' !== get_post_field( 'post_name', $parent ) ) {
			return '';
		}
		$title = wp_strip_all_tags( get_the_title( $post_id ) );
		$title = preg_replace( '/^POS Software for\s+/i', '', $title );
		return trim( $title );
	}

	/* Extra nodes for the current page */
	function utp_schema_extra( $c ) {
		$out = array( 'UtpSoftware' => utp_schema_software( $c ) );
		if ( is_singular() ) {
			$id    = get_queried_object_id();
			$url   = get_permalink( $id );
			$items = utp_schema_faq_items( $id );
			if ( $url && count( $items ) > 0 ) {
				$out['UtpFAQ'] = array(
					'@type'      => 'FAQPage',
					'@id'        => $url . '#faq',
					'isPartOf'   => array( '@id' => $url . '#webpage' ),
					'mainEntity' => $items,
				);
			}
		}
		return $out;
	}

	function utp_schema_has_type( $node, $type ) {
		if ( ! is_array( $node ) || ! isset( $node['@type'] ) ) {
			return false;
		}
		$t = $node['@type'];
		return is_array( $t ) ? in_array( $type, $t, true ) : ( $type === $t );
	}

	/* Rank Math active: merge into its graph */
	add_filter(
		'rank_math/json_ld',
		function ( $data, $jsonld ) {
			if ( ! is_array( $data ) ) {
				return $data;
			}
			$c        = utp_schema_config();
			$industry = is_singular() ? utp_schema_industry( get_queried_object_id() ) : '';
			foreach ( $data as $key => $node ) {
				if ( utp_schema_has_type( $node, 'Organization' ) ) {
					$data[ $key ] = array_merge( $node, utp_schema_org( $c ) );
				}
				if ( is_array( $node ) && isset( $node['@id'] ) && is_string( $node['@id'] ) && '#webpage' === substr( $node['@id'], -8 ) ) {
					$data[ $key ]['about'] = array( '@id' => utp_schema_home() . '#software' );
					if ( '' !== $industry ) {
						$data[ $key ]['audience'] = array( '@type' => 'BusinessAudience', 'audienceType' => $industry );
					}
				}
			}
			foreach ( utp_schema_extra( $c ) as $k => $node ) {
				$data[ $k ] = $node;
			}
			return $data;
		},
		99,
		2
	);

	/* Rank Math not active: print the same schema ourselves */
	add_action(
		'wp_head',
		function () {
			if ( defined( 'RANK_MATH_VERSION' ) ) {
				return;
			}
			$c     = utp_schema_config();
			$graph = array(
				utp_schema_org( $c ),
				array(
					'@type'      => 'WebSite',
					'@id'        => utp_schema_home() . '#website',
					'url'        => utp_schema_home(),
					'name'       => $c['name'],
					'inLanguage' => 'en-PK',
					'publisher'  => array( '@id' => utp_schema_home() . '#organization' ),
				),
			);
			foreach ( utp_schema_extra( $c ) as $node ) {
				$graph[] = $node;
			}
			echo '<script type="application/ld+json">' . wp_json_encode( array( '@context' => 'https://schema.org', '@graph' => $graph ), JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) . '</script>' . "\n";
		},
		20
	);
}

/*
 * UpTrendPos automatic image ALT text (every page, every image).
 * 1) When an image is uploaded, its ALT is filled from the file name (if the ALT is empty).
 * 2) When a page is shown, any image with no ALT (or an empty ALT) gets one:
 *    a clear file name is used; if the file name means nothing (pos10, img-123, logo),
 *    the first such image uses the page's Rank Math focus keyword, the rest use the page title.
 * Images marked aria-hidden="true" or role="presentation" are left as decoration.
 */
if ( ! function_exists( 'utp_alt_from_file' ) ) {

	function utp_alt_from_file( $src ) {
		$path = (string) wp_parse_url( $src, PHP_URL_PATH );
		$name = pathinfo( $path, PATHINFO_FILENAME );
		$name = preg_replace( '/-(scaled|rotated|e\d+|\d+x\d+)$/i', '', $name );
		$name = preg_replace( '/-(scaled|\d+x\d+)$/i', '', $name );
		$name = preg_replace( '/[-_.+]+/', ' ', $name );
		$name = preg_replace( '/\s*\d+$/', '', $name );
		$name = trim( preg_replace( '/\s+/', ' ', $name ) );
		$letters = preg_replace( '/[^a-z]/i', '', $name );
		if ( strlen( $letters ) < 4 || preg_match( '/^(img|image|photo|pic|picture|screenshot|screen shot|dsc|whatsapp image|pos|untitled|logo|banner|icon|design|frame|group|copy|new|final)( .*)?$/i', $name ) && str_word_count( $name ) < 3 ) {
			return '';
		}
		$name = ucwords( strtolower( $name ) );
		$name = preg_replace( '/\bUptrendpos\b/i', 'UpTrendPos', $name );
		$name = preg_replace( '/\bUptrend Pos\b/i', 'UpTrendPos', $name );
		return $name;
	}

	add_action(
		'add_attachment',
		function ( $post_id ) {
			if ( ! wp_attachment_is_image( $post_id ) ) {
				return;
			}
			$alt = get_post_meta( $post_id, '_wp_attachment_image_alt', true );
			if ( '' !== trim( (string) $alt ) ) {
				return;
			}
			$new = utp_alt_from_file( wp_get_attachment_url( $post_id ) );
			if ( '' !== $new ) {
				update_post_meta( $post_id, '_wp_attachment_image_alt', sanitize_text_field( $new ) );
			}
		}
	);

	function utp_alt_fill_html( $html ) {
		if ( false === stripos( $html, '<img' ) ) {
			return $html;
		}
		$id      = is_singular() ? get_queried_object_id() : 0;
		$keyword = '';
		$title   = 'UpTrendPos';
		if ( $id ) {
			$kw      = (string) get_post_meta( $id, 'rank_math_focus_keyword', true );
			$keyword = trim( strtok( $kw, ',' ) );
			$t       = trim( wp_strip_all_tags( get_the_title( $id ) ) );
			if ( '' !== $t && ! is_front_page() ) {
				$title = $t . ' - UpTrendPos';
			}
		}
		$state = array( 'used_kw' => false, 'n' => 0 );
		return preg_replace_callback(
			'#<img\b[^>]*>#i',
			function ( $m ) use ( $keyword, $title, &$state ) {
				$tag = $m[0];
				if ( preg_match( '/\saria-hidden\s*=\s*["\']true["\']|\srole\s*=\s*["\']presentation["\']/i', $tag ) ) {
					return $tag;
				}
				$has_alt = preg_match( '/\salt\s*=\s*(["\'])(.*?)\1/is', $tag, $a );
				if ( $has_alt && '' !== trim( $a[2] ) ) {
					return $tag;
				}
				$src = '';
				if ( preg_match( '/\ssrc\s*=\s*(["\'])(.*?)\1/is', $tag, $s ) && 0 !== strpos( $s[2], 'data:' ) ) {
					$src = $s[2];
				}
				$alt = $src ? utp_alt_from_file( $src ) : '';
				if ( '' === $alt ) {
					if ( '' !== $keyword && ! $state['used_kw'] ) {
						$alt              = ( false !== stripos( $keyword, 'uptrendpos' ) ) ? $keyword : $keyword . ' - UpTrendPos';
						$state['used_kw'] = true;
					} else {
						$state['n']++;
						$alt = $title . ( $state['n'] > 1 ? ' ' . $state['n'] : '' );
					}
				}
				$alt = esc_attr( $alt );
				if ( $has_alt ) {
					return preg_replace( '/\salt\s*=\s*(["\'])(.*?)\1/is', ' alt="' . $alt . '"', $tag, 1 );
				}
				return preg_replace( '#\s*/?>$#', ' alt="' . $alt . '"$0', $tag, 1 );
			},
			$html
		);
	}

	add_action(
		'template_redirect',
		function () {
			if ( is_admin() || is_feed() || wp_doing_ajax() || ( defined( 'REST_REQUEST' ) && REST_REQUEST ) || isset( $_GET['elementor-preview'] ) ) {
				return;
			}
			ob_start( 'utp_alt_fill_html' );
		},
		0
	);
}

/*
 * Shortcodes inside Elementor HTML widgets.
 * Elementor's HTML widget prints text as it is, so [fluentform id="1"] would show as plain text.
 * This runs the Fluent Forms shortcode inside our page code (only [fluentform ...], nothing else).
 */
add_filter(
	'elementor/widget/render_content',
	function ( $content, $widget ) {
		if ( is_object( $widget ) && method_exists( $widget, 'get_name' ) && 'html' === $widget->get_name() && false !== strpos( $content, '[fluentform' ) ) {
			$content = preg_replace_callback(
				'/\[fluentform\b[^\]]*\]/',
				function ( $m ) {
					return do_shortcode( $m[0] );
				},
				$content
			);
		}
		return $content;
	},
	10,
	2
);

