/*
 * WPCode snippet name: UpTrendPos SEO Snippet  (Code type: PHP Snippet, Insert: Auto Insert, Location: Run Everywhere)
 * Version: 2026-10-14c (solar + electronics/appliances/CCTV page images and names. 14b: tailor + mobile shop page images. 14a: FBR POS integration page breadcrumb + page image; pharmacy page image. Earlier: legal + support breadcrumbs, support hours, industry hub CollectionPage + live list, breadcrumbs, page image, audience map).
 * Always update THIS one snippet - never add a second PHP SEO snippet.
 * One snippet for every page: schema + automatic image ALT text + shortcodes inside Elementor HTML widgets.
 * Adds to Rank Math's own schema (same @ids), so nothing is duplicated.
 * - Organization: fixed brand data on every page
 * - SoftwareApplication: UpTrendPos product on every page (with feature list)
 * - FAQPage: built automatically from the FAQ list on any page (only the questions shown on that page)
 * - Industries hub (/industries/): CollectionPage + ItemList of the business-type pages that are LIVE
 *   (published and not set to noindex in Rank Math) - it grows on its own as pages go live
 * - Industry pages (/industries/<slug>/): BusinessAudience from the map below, page image, breadcrumb
 * - Privacy Policy, Terms and Conditions, Support: Home > page breadcrumb
 * - Organization: sales contact + customer support contact with support hours (Mon-Sat 10:00-19:00)
 * - BreadcrumbList: added only when Rank Math does not print its own
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
			'uploads'     => 'https://uptrendpos.com/wp-content/uploads/',
			// Support hours (Pakistan time) - shown on the Organization as the customer support contact
			'support_days'  => array( 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' ),
			'support_open'  => '10:00',
			'support_close' => '19:00',
			'support_url'   => 'https://uptrendpos.com/support/',
			// Simple pages that get a Home > Page breadcrumb: slug => name
			'simple_pages'  => array(
				'privacy-policy'       => 'Privacy Policy',
				'terms-and-conditions' => 'Terms and Conditions',
				'support'              => 'Support',
				'fbr-pos-integration'  => 'FBR POS Integration',
			),
			// Page image for top-level pages: slug => file name in uploads
			'page_images'   => array(
				'fbr-pos-integration' => 'uptrendpos-fbr-pos-invoice-qr.webp',
			),
			// Industries hub: slug + its page image (file name in uploads)
			'hub_slug'    => 'industries',
			'hub_image'   => 'uptrendpos-industry-specific-pos-software.webp',
			// Industry pages under /industries/: slug => array( card name, audience, page image file name or '' )
			// A new page needs NO change here unless it gets its own image. Hub list only shows LIVE pages (published, not noindex).
			'industry_pages' => array(
				'grocery-store-pos-software' => array( 'Grocery & Kiryana Store', 'Grocery and kiryana store owners', 'uptrendpos-grocery-store-pos-software.webp' ),
				'pharmacy-pos-software' => array( 'Pharmacy & Medical Store', 'Pharmacy and medical store owners', 'uptrendpos-pharmacy-pos-software.webp' ),
				'clothing-store-pos-software' => array( 'Clothing & Garments', 'Clothing and garment shop owners', '' ),
				'shoe-store-pos-software' => array( 'Shoes & Footwear', 'Shoe and footwear shop owners', '' ),
				'tailor-shop-pos-software' => array( 'Tailoring & Boutique', 'Tailors and boutique owners', 'uptrendpos-tailor-shop-pos-software.webp' ),
				'cosmetics-store-pos-software' => array( 'Cosmetics & Beauty Store', 'Cosmetics and beauty store owners', '' ),
				'baby-store-pos-software' => array( 'Baby & Diaper Store', 'Baby and diaper store owners', '' ),
				'undergarments-shop-pos-software' => array( 'Undergarments & Hosiery', 'Undergarments and hosiery shop owners', '' ),
				'electronics-store-pos-software' => array( 'Electronics, Appliances & CCTV', 'Electronics, home appliance and CCTV shop owners', 'uptrendpos-electronics-store-pos-software.webp' ),
				'solar-shop-pos-software' => array( 'Solar Shop', 'Solar shop and solar business owners', 'uptrendpos-solar-shop-pos-software.webp' ),
				'electrical-store-pos-software' => array( 'Electrical & LED Lighting', 'Electrical and LED lighting shop owners', '' ),
				'mobile-shop-pos-software' => array( 'Mobile & Computer Shop', 'Mobile and computer shop owners', 'uptrendpos-mobile-shop-pos-software.webp' ),
				'battery-shop-pos-software' => array( 'Battery Shop', 'Battery shop owners', '' ),
				'hardware-store-pos-software' => array( 'Hardware, Sanitary & Building Material', 'Hardware, sanitary and building material store owners', '' ),
				'paint-store-pos-software' => array( 'Paint Store', 'Paint store owners', '' ),
				'glass-shop-pos-software' => array( 'Glass & Aluminium Shop', 'Glass and aluminium shop owners', '' ),
				'auto-parts-pos-software' => array( 'Auto Spare Parts', 'Auto spare parts shop owners', '' ),
				'tyre-shop-pos-software' => array( 'Tyre Shop', 'Tyre shop owners', '' ),
				'jewellery-shop-pos-software' => array( 'Jewellery & Gold Shop', 'Jewellery and gold shop owners', '' ),
				'artificial-jewellery-shop-pos-software' => array( 'Artificial Jewellery Shop', 'Artificial jewellery shop owners', '' ),
				'watch-shop-pos-software' => array( 'Watch Shop', 'Watch shop owners', '' ),
				'perfume-shop-pos-software' => array( 'Perfume & Attar Shop', 'Perfume and attar shop owners', '' ),
				'bag-shop-pos-software' => array( 'Bags & Luggage', 'Bag and luggage shop owners', '' ),
				'toy-shop-pos-software' => array( 'Toys & Gift Shop', 'Toy and gift shop owners', '' ),
				'sports-shop-pos-software' => array( 'Sports Goods', 'Sports goods shop owners', '' ),
				'stationery-shop-pos-software' => array( 'Stationery & Book Shop', 'Stationery and book shop owners', '' ),
				'crockery-shop-pos-software' => array( 'Crockery & Household Shop', 'Crockery and household shop owners', '' ),
				'furniture-shop-pos-software' => array( 'Furniture Shop', 'Furniture shop owners', '' ),
				'meat-shop-pos-software' => array( 'Poultry, Meat & Seafood', 'Poultry, meat and seafood shop owners', '' ),
				'fertilizer-shop-pos-software' => array( 'Agri Inputs (Seed, Fertilizer & Pesticides)', 'Seed, fertilizer and pesticide dealers', '' ),
				'veterinary-store-pos-software' => array( 'Veterinary Store', 'Veterinary store owners', '' ),
				'vape-shop-pos-software' => array( 'Vape & Pan Shop', 'Vape and pan shop owners', '' ),
			),
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
				array(
					'@type'             => 'ContactPoint',
					'telephone'         => $c['phone'],
					'contactType'       => 'customer support',
					'email'             => $c['email'],
					'url'               => $c['support_url'],
					'availableLanguage' => array( 'en', 'ur' ),
					'areaServed'        => $c['country'],
					'hoursAvailable'    => array(
						'@type'     => 'OpeningHoursSpecification',
						'dayOfWeek' => $c['support_days'],
						'opens'     => $c['support_open'],
						'closes'    => $c['support_close'],
					),
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
			'featureList'            => array( 'Offline billing with auto sync', 'Barcode billing', 'Sell by carton, pack, piece or kg', 'Udhaar khata (customer ledger)', 'Stock, low stock and expiry alerts', 'Purchase orders, GRN and supplier ledger', 'Bills on WhatsApp as picture or PDF', 'Thermal printing from Android phone by USB Type-C', 'Double-entry accounts and profit reports', 'Multi-branch stock and prices', 'FBR invoice number and QR code' ),
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

	/* Is this page the industries hub? */
	function utp_schema_is_hub( $post_id, $c ) {
		return $post_id && 'page' === get_post_type( $post_id ) && $c['hub_slug'] === get_post_field( 'post_name', $post_id ) && ! wp_get_post_parent_id( $post_id );
	}

	/* Slug of an industry page (child of the hub), or '' */
	function utp_schema_industry_slug( $post_id, $c ) {
		$parent = (int) wp_get_post_parent_id( $post_id );
		if ( ! $parent || $c['hub_slug'] !== get_post_field( 'post_name', $parent ) ) {
			return '';
		}
		return (string) get_post_field( 'post_name', $post_id );
	}

	/* Business type audience for pages under /industries/ (map first, then the page title) */
	function utp_schema_industry( $post_id ) {
		$c    = utp_schema_config();
		$slug = utp_schema_industry_slug( $post_id, $c );
		if ( '' === $slug ) {
			return '';
		}
		if ( isset( $c['industry_pages'][ $slug ] ) ) {
			return $c['industry_pages'][ $slug ][1];
		}
		$title = wp_strip_all_tags( get_the_title( $post_id ) );
		$title = preg_replace( '/^POS Software for\s+/i', '', $title );
		return trim( $title );
	}

	/* Page image (hub, industry page or top-level page) from the config, or '' */
	function utp_schema_page_image( $post_id, $c ) {
		$file = '';
		if ( utp_schema_is_hub( $post_id, $c ) ) {
			$file = $c['hub_image'];
		} else {
			$slug = utp_schema_industry_slug( $post_id, $c );
			if ( '' !== $slug && isset( $c['industry_pages'][ $slug ] ) ) {
				$file = $c['industry_pages'][ $slug ][2];
			} elseif ( ! wp_get_post_parent_id( $post_id ) ) {
				$name = (string) get_post_field( 'post_name', $post_id );
				if ( isset( $c['page_images'][ $name ] ) ) {
					$file = $c['page_images'][ $name ];
				}
			}
		}
		return '' === $file ? '' : $c['uploads'] . $file;
	}

	/* Live industry pages: published children of the hub that are not noindex in Rank Math */
	function utp_schema_live_industries( $hub_id, $c ) {
		$kids = get_pages(
			array(
				'parent'      => $hub_id,
				'post_status' => 'publish',
				'sort_column' => 'menu_order,post_title',
			)
		);
		$list = array();
		foreach ( (array) $kids as $p ) {
			$robots = get_post_meta( $p->ID, 'rank_math_robots', true );
			if ( is_array( $robots ) && in_array( 'noindex', $robots, true ) ) {
				continue;
			}
			$name   = isset( $c['industry_pages'][ $p->post_name ] ) ? $c['industry_pages'][ $p->post_name ][0] : wp_strip_all_tags( get_the_title( $p->ID ) );
			$list[] = array( 'name' => $name, 'url' => get_permalink( $p->ID ) );
		}
		return $list;
	}

	/* Breadcrumb trail for the hub and industry pages, or empty array */
	function utp_schema_breadcrumb( $post_id, $c ) {
		$url = get_permalink( $post_id );
		if ( ! $url ) {
			return array();
		}
		$trail = array( array( 'Home', utp_schema_home() ) );
		if ( utp_schema_is_hub( $post_id, $c ) ) {
			$trail[] = array( 'Industries', $url );
		} elseif ( '' !== utp_schema_industry_slug( $post_id, $c ) ) {
			$slug    = utp_schema_industry_slug( $post_id, $c );
			$name    = isset( $c['industry_pages'][ $slug ] ) ? $c['industry_pages'][ $slug ][0] : wp_strip_all_tags( get_the_title( $post_id ) );
			$trail[] = array( 'Industries', get_permalink( wp_get_post_parent_id( $post_id ) ) );
			$trail[] = array( $name, $url );
		} elseif ( ! wp_get_post_parent_id( $post_id ) && isset( $c['simple_pages'][ (string) get_post_field( 'post_name', $post_id ) ] ) ) {
			$trail[] = array( $c['simple_pages'][ (string) get_post_field( 'post_name', $post_id ) ], $url );
		} else {
			return array();
		}
		$items = array();
		foreach ( $trail as $i => $t ) {
			$items[] = array( '@type' => 'ListItem', 'position' => $i + 1, 'name' => $t[0], 'item' => $t[1] );
		}
		return array( '@type' => 'BreadcrumbList', '@id' => $url . '#breadcrumb', 'itemListElement' => $items );
	}

	/* Hub: ItemList of live business-type pages, or empty array */
	function utp_schema_hub_list( $post_id, $c ) {
		if ( ! utp_schema_is_hub( $post_id, $c ) ) {
			return array();
		}
		$live = utp_schema_live_industries( $post_id, $c );
		if ( ! $live ) {
			return array();
		}
		$items = array();
		foreach ( $live as $i => $p ) {
			$items[] = array( '@type' => 'ListItem', 'position' => $i + 1, 'name' => $p['name'], 'url' => $p['url'] );
		}
		return array(
			'@type'           => 'ItemList',
			'@id'             => get_permalink( $post_id ) . '#business-types',
			'name'            => 'POS software by business type',
			'numberOfItems'   => count( $items ),
			'itemListElement' => $items,
		);
	}

	/* Extra nodes for the current page */
	function utp_schema_extra( $c ) {
		$out = array( 'UtpSoftware' => utp_schema_software( $c ) );
		if ( is_singular() ) {
			$id    = get_queried_object_id();
			$url   = get_permalink( $id );
			$items = utp_schema_faq_items( $id );
			$list  = utp_schema_hub_list( $id, $c );
			if ( $list ) {
				$out['UtpBusinessTypes'] = $list;
			}
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
			$industry    = is_singular() ? utp_schema_industry( get_queried_object_id() ) : '';
			$webpage_key = null;
			$has_crumb   = false;
			foreach ( $data as $key => $node ) {
				if ( utp_schema_has_type( $node, 'Organization' ) ) {
					$data[ $key ] = array_merge( $node, utp_schema_org( $c ) );
				}
				if ( is_array( $node ) && isset( $node['@id'] ) && is_string( $node['@id'] ) && '#webpage' === substr( $node['@id'], -8 ) ) {
					$data[ $key ]['about'] = array( '@id' => utp_schema_home() . '#software' );
					if ( '' !== $industry ) {
						$data[ $key ]['audience'] = array( '@type' => 'BusinessAudience', 'audienceType' => $industry );
					}
					$webpage_key = $key;
				}
				if ( utp_schema_has_type( $node, 'BreadcrumbList' ) ) {
					$has_crumb = true;
				}
			}
			if ( is_singular() && null !== $webpage_key ) {
				$pid = get_queried_object_id();
				$url = get_permalink( $pid );
				if ( utp_schema_is_hub( $pid, $c ) ) {
					$data[ $webpage_key ]['@type'] = 'CollectionPage';
					if ( utp_schema_hub_list( $pid, $c ) ) {
						$data[ $webpage_key ]['mainEntity'] = array( '@id' => $url . '#business-types' );
					}
				}
				$img = utp_schema_page_image( $pid, $c );
				if ( '' !== $img && empty( $data[ $webpage_key ]['primaryImageOfPage'] ) ) {
					$data['UtpPageImage']                         = array( '@type' => 'ImageObject', '@id' => $url . '#pageimage', 'url' => $img, 'contentUrl' => $img, 'width' => 1200, 'height' => 900 );
					$data[ $webpage_key ]['primaryImageOfPage'] = array( '@id' => $url . '#pageimage' );
				}
				if ( ! $has_crumb ) {
					$crumb = utp_schema_breadcrumb( $pid, $c );
					if ( $crumb ) {
						$data['UtpBreadcrumb']                = $crumb;
						$data[ $webpage_key ]['breadcrumb'] = array( '@id' => $crumb['@id'] );
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
			if ( is_singular() ) {
				$crumb = utp_schema_breadcrumb( get_queried_object_id(), $c );
				if ( $crumb ) {
					$graph[] = $crumb;
				}
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

