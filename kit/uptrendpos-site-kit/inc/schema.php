<?php
/**
 * Schema. Merged into Rank Math's own graph (same @ids, nothing duplicated):
 * - Organization (brand facts, address, contact points with support hours, map, knowsAbout)
 * - SoftwareApplication #software (features, platforms, 3 plan offers, download links)
 * - WebPage: about #software, publisher, reviewedBy (EEAT), lastReviewed, page image, audience for business-type pages
 * - FAQPage built from the FAQ list on the page (only the questions shown)
 * - Industries hub: CollectionPage + ItemList of LIVE business-type pages (grows on its own)
 * - BreadcrumbList for every page when Rank Math does not print one
 * - Generic "Article" node removed on pages
 * If Rank Math is switched off, the same graph is printed by this plugin.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function utpk_home() {
	return trailingslashit( home_url( '/' ) );
}

function utpk_schema_org() {
	$b = utpk_brand();
	return array(
		'@type'         => 'Organization',
		'@id'           => utpk_home() . '#organization',
		'name'          => $b['name'],
		'alternateName' => $b['alt_name'],
		'url'           => utpk_home(),
		'logo'          => array(
			'@type'  => 'ImageObject',
			'@id'    => utpk_home() . '#logo',
			'url'    => home_url( '/wp-content/uploads/uptrend-POS-Logo.png' ),
			'width'  => 512,
			'height' => 512,
		),
		'image'         => array( '@id' => utpk_home() . '#logo' ),
		'description'   => 'UpTrendPos makes POS and accounting software for Pakistani shops: offline billing, stock, udhaar khata, purchases, accounts and FBR invoices on Windows, Android and the web.',
		'slogan'        => 'Simple POS software for every Pakistani shop',
		'email'         => $b['email'],
		'telephone'     => $b['phone'],
		'address'       => array(
			'@type'           => 'PostalAddress',
			'streetAddress'   => $b['street'],
			'addressLocality' => $b['city'],
			'addressRegion'   => $b['region'],
			'postalCode'      => $b['postcode'],
			'addressCountry'  => $b['country'],
		),
		'location'      => array(
			'@type'  => 'Place',
			'name'   => 'UpTrendPos office, Sahiwal',
			'hasMap' => $b['map'],
			'geo'    => array( '@type' => 'GeoCoordinates', 'latitude' => $b['lat'], 'longitude' => $b['lng'] ),
		),
		'areaServed'    => array( '@type' => 'Country', 'name' => 'Pakistan' ),
		'knowsAbout'    => array( 'POS software', 'Point of sale', 'Inventory management', 'Udhaar khata (customer credit ledger)', 'Installment sales', 'Double-entry accounting', 'FBR POS integration', 'Offline-first billing', 'Thermal receipt printing' ),
		'contactPoint'  => array(
			array(
				'@type'             => 'ContactPoint',
				'telephone'         => $b['phone'],
				'contactType'       => 'sales',
				'email'             => $b['email'],
				'availableLanguage' => array( 'en', 'ur' ),
				'areaServed'        => $b['country'],
			),
			array(
				'@type'             => 'ContactPoint',
				'telephone'         => $b['phone'],
				'contactType'       => 'customer support',
				'email'             => $b['email'],
				'url'               => home_url( '/support/' ),
				'availableLanguage' => array( 'en', 'ur' ),
				'areaServed'        => $b['country'],
				'hoursAvailable'    => array(
					'@type'     => 'OpeningHoursSpecification',
					'dayOfWeek' => $b['support_days'],
					'opens'     => $b['support_open'],
					'closes'    => $b['support_close'],
				),
			),
		),
		'sameAs'        => $b['same_as'],
	);
}

function utpk_schema_software() {
	$b      = utpk_brand();
	$offers = array();
	foreach ( $b['plans'] as $name => $price ) {
		$offers[] = array(
			'@type'              => 'Offer',
			'name'               => $name . ' plan',
			'price'              => (string) $price,
			'priceCurrency'      => 'PKR',
			'url'                => home_url( '/pos-software-pricing/' ),
			'availability'       => 'https://schema.org/InStock',
			'priceSpecification' => array(
				'@type'            => 'UnitPriceSpecification',
				'price'            => (string) $price,
				'priceCurrency'    => 'PKR',
				'billingDuration'  => 'P1M',
				'unitText'         => 'month',
			),
		);
	}
	$node = array(
		'@type'                  => 'SoftwareApplication',
		'@id'                    => utpk_home() . '#software',
		'name'                   => $b['name'],
		'applicationCategory'    => 'BusinessApplication',
		'applicationSubCategory' => 'Point of Sale',
		'operatingSystem'        => 'Windows 10, Windows 11, Android, Web browser',
		'description'            => 'POS and accounting software for Pakistani businesses with offline billing, inventory, udhaar khata, installments, multi-branch control and FBR-ready invoices.',
		'image'                  => home_url( '/wp-content/uploads/uptrend-POS-Logo.png' ),
		'url'                    => utpk_home(),
		'installUrl'             => $b['app'],
		'inLanguage'             => 'en-PK',
		'publisher'              => array( '@id' => utpk_home() . '#organization' ),
		'featureList'            => array( 'Offline billing with auto sync', 'Barcode billing', 'Sell by carton, pack, piece or kg', 'Udhaar khata (customer ledger)', 'Stock, low stock and expiry alerts', 'Purchase orders, GRN and supplier ledger', 'Bills and reports on WhatsApp as picture or PDF', 'Thermal printing from an Android phone by USB Type-C', 'Quotations with convert to sale', 'Double-entry accounts and profit reports', 'Multi-branch stock and prices', 'FBR invoice number and QR code' ),
		'offers'                 => $offers,
	);
	$dl = array_values( array_filter( array( (string) utpk_opt( 'exe' ), (string) utpk_opt( 'apk' ) ) ) );
	if ( $dl ) {
		$node['downloadUrl'] = count( $dl ) > 1 ? $dl : $dl[0];
	}
	return $node;
}

function utpk_schema_faq_items( $post_id ) {
	$html = utpk_page_html( $post_id );
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
				$items[] = array( '@type' => 'Question', 'name' => $q, 'acceptedAnswer' => array( '@type' => 'Answer', 'text' => $a ) );
			}
		}
	}
	return $items;
}

function utpk_is_hub( $post_id ) {
	return $post_id && 'page' === get_post_type( $post_id ) && utpk_brand()['hub_slug'] === get_post_field( 'post_name', $post_id ) && ! wp_get_post_parent_id( $post_id );
}

function utpk_industry_slug_of( $post_id ) {
	$parent = (int) wp_get_post_parent_id( $post_id );
	if ( ! $parent || utpk_brand()['hub_slug'] !== get_post_field( 'post_name', $parent ) ) {
		return '';
	}
	return (string) get_post_field( 'post_name', $post_id );
}

function utpk_short_name( $post_id ) {
	$slug = utpk_industry_slug_of( $post_id );
	if ( '' !== $slug ) {
		$t = utpk_industry( $slug );
		if ( $t ) {
			return $t['name'];
		}
	}
	$names = array(
		'industries'            => 'Industries',
		'privacy-policy'        => 'Privacy Policy',
		'terms-and-conditions'  => 'Terms and Conditions',
		'support'               => 'Support',
		'fbr-pos-integration'   => 'FBR POS Integration',
		'pos-software-pricing'  => 'Pricing',
		'download-pos-software' => 'Download',
		'about-uptrendpos'      => 'About UpTrendPos',
		'contact-us'            => 'Contact Us',
	);
	$name = (string) get_post_field( 'post_name', $post_id );
	return isset( $names[ $name ] ) ? $names[ $name ] : trim( wp_strip_all_tags( get_the_title( $post_id ) ) );
}

function utpk_schema_breadcrumb( $post_id ) {
	$url = get_permalink( $post_id );
	if ( ! $url || (int) get_option( 'page_on_front' ) === (int) $post_id ) {
		return array();
	}
	$trail = array( array( 'Home', utpk_home() ) );
	foreach ( array_reverse( get_post_ancestors( $post_id ) ) as $anc ) {
		$trail[] = array( utpk_short_name( $anc ), get_permalink( $anc ) );
	}
	$trail[] = array( utpk_short_name( $post_id ), $url );
	$items   = array();
	foreach ( $trail as $i => $t ) {
		$items[] = array( '@type' => 'ListItem', 'position' => $i + 1, 'name' => $t[0], 'item' => $t[1] );
	}
	return array( '@type' => 'BreadcrumbList', '@id' => $url . '#breadcrumb', 'itemListElement' => $items );
}

function utpk_schema_hub_list( $post_id ) {
	if ( ! utpk_is_hub( $post_id ) ) {
		return array();
	}
	$kids  = get_pages( array( 'parent' => $post_id, 'post_status' => 'publish', 'sort_column' => 'menu_order,post_title' ) );
	$items = array();
	foreach ( (array) $kids as $p ) {
		if ( ! utpk_is_live( $p->post_name ) ) {
			continue;
		}
		$t       = utpk_industry( $p->post_name );
		$items[] = array( '@type' => 'ListItem', 'position' => count( $items ) + 1, 'name' => $t ? $t['name'] : wp_strip_all_tags( get_the_title( $p->ID ) ), 'url' => get_permalink( $p->ID ) );
	}
	if ( ! $items ) {
		return array();
	}
	return array( '@type' => 'ItemList', '@id' => get_permalink( $post_id ) . '#business-types', 'name' => 'POS software by business type', 'numberOfItems' => count( $items ), 'itemListElement' => $items );
}

function utpk_schema_reviewer() {
	$name = trim( (string) utpk_opt( 'reviewer_name' ) );
	if ( '' === $name ) {
		return array( '@id' => utpk_home() . '#organization' );
	}
	$p = array( '@type' => 'Person', '@id' => utpk_home() . '#reviewer', 'name' => $name, 'worksFor' => array( '@id' => utpk_home() . '#organization' ) );
	if ( '' !== trim( (string) utpk_opt( 'reviewer_title' ) ) ) {
		$p['jobTitle'] = trim( (string) utpk_opt( 'reviewer_title' ) );
	}
	if ( '' !== trim( (string) utpk_opt( 'reviewer_url' ) ) ) {
		$p['sameAs'] = esc_url_raw( trim( (string) utpk_opt( 'reviewer_url' ) ) );
	}
	return $p;
}

function utpk_has_type( $node, $type ) {
	if ( ! is_array( $node ) || ! isset( $node['@type'] ) ) {
		return false;
	}
	$t = $node['@type'];
	return is_array( $t ) ? in_array( $type, $t, true ) : ( $type === $t );
}

/* Extra nodes + WebPage enrichment for the current page, applied to a graph array */
function utpk_schema_apply( $data ) {
	$webpage_key = null;
	$has_crumb   = false;
	foreach ( $data as $key => $node ) {
		if ( utpk_has_type( $node, 'Organization' ) || ( is_array( $node ) && isset( $node['@id'] ) && utpk_home() . '#organization' === $node['@id'] ) ) {
			$data[ $key ] = array_merge( $node, utpk_schema_org() );
		}
		if ( is_array( $node ) && isset( $node['@id'] ) && is_string( $node['@id'] ) && '#webpage' === substr( $node['@id'], -8 ) ) {
			$webpage_key = $key;
		}
		if ( utpk_has_type( $node, 'BreadcrumbList' ) ) {
			$has_crumb = true;
		}
		if ( is_page() && ( utpk_has_type( $node, 'Article' ) || utpk_has_type( $node, 'BlogPosting' ) ) ) {
			unset( $data[ $key ] );
		}
		if ( is_page() && utpk_has_type( $node, 'Person' ) && isset( $node['@id'] ) && false !== strpos( (string) $node['@id'], '/author/' ) ) {
			unset( $data[ $key ] );
		}
	}
	$data['UtpSoftware'] = utpk_schema_software();

	if ( is_singular() ) {
		$pid = get_queried_object_id();
		$url = get_permalink( $pid );

		if ( null !== $webpage_key ) {
			$wp                = $data[ $webpage_key ];
			$wp['about']       = array( '@id' => utpk_home() . '#software' );
			$wp['publisher']   = array( '@id' => utpk_home() . '#organization' );
			$wp['inLanguage']  = 'en-PK';
			$reviewer          = utpk_schema_reviewer();
			if ( isset( $reviewer['@type'] ) ) {
				$data['UtpReviewer'] = $reviewer;
				$wp['reviewedBy']    = array( '@id' => $reviewer['@id'] );
			} else {
				$wp['reviewedBy'] = $reviewer;
			}
			$wp['lastReviewed'] = get_the_modified_date( 'Y-m-d', $pid );
			$slug               = utpk_industry_slug_of( $pid );
			if ( '' !== $slug ) {
				$t                = utpk_industry( $slug );
				$wp['audience']   = array( '@type' => 'BusinessAudience', 'audienceType' => $t ? $t['audience'] : utpk_short_name( $pid ) );
			}
			if ( utpk_is_hub( $pid ) ) {
				$wp['@type'] = 'CollectionPage';
				$list        = utpk_schema_hub_list( $pid );
				if ( $list ) {
					$data['UtpBusinessTypes'] = $list;
					$wp['mainEntity']         = array( '@id' => $list['@id'] );
				}
			}
			$img = utpk_page_image( $pid );
			if ( '' !== $img && empty( $wp['primaryImageOfPage'] ) ) {
				$data['UtpPageImage']     = array( '@type' => 'ImageObject', '@id' => $url . '#pageimage', 'url' => $img, 'contentUrl' => $img, 'width' => 1200, 'height' => 900 );
				$wp['primaryImageOfPage'] = array( '@id' => $url . '#pageimage' );
			}
			if ( ! $has_crumb ) {
				$crumb = utpk_schema_breadcrumb( $pid );
				if ( $crumb ) {
					$data['UtpBreadcrumb'] = $crumb;
					$wp['breadcrumb']      = array( '@id' => $crumb['@id'] );
				}
			}
			$data[ $webpage_key ] = $wp;
		}

		$faq = utpk_schema_faq_items( $pid );
		if ( $url && $faq ) {
			$data['UtpFAQ'] = array( '@type' => 'FAQPage', '@id' => $url . '#faq', 'isPartOf' => array( '@id' => $url . '#webpage' ), 'mainEntity' => $faq );
		}
	}
	return $data;
}

/* Rank Math active: merge into its graph */
add_filter( 'rank_math/json_ld', function ( $data, $jsonld ) {
	if ( ! utpk_opt( 'schema' ) || ! is_array( $data ) || function_exists( 'utp_schema_config' ) ) {
		return $data; // old WPCode snippet still active: let it run alone until it is switched off
	}
	return utpk_schema_apply( $data );
}, 99, 2 );

/* Rank Math not active: print the same graph */
add_action( 'wp_head', function () {
	if ( defined( 'RANK_MATH_VERSION' ) || ! utpk_opt( 'schema' ) || function_exists( 'utp_schema_config' ) || ! utpk_front_ok() ) {
		return;
	}
	$graph = array(
		'org'     => utpk_schema_org(),
		'website' => array( '@type' => 'WebSite', '@id' => utpk_home() . '#website', 'url' => utpk_home(), 'name' => 'UpTrendPos', 'inLanguage' => 'en-PK', 'publisher' => array( '@id' => utpk_home() . '#organization' ) ),
	);
	if ( is_singular() ) {
		$pid              = get_queried_object_id();
		$graph['webpage'] = array( '@type' => 'WebPage', '@id' => get_permalink( $pid ) . '#webpage', 'url' => get_permalink( $pid ), 'name' => wp_get_document_title(), 'isPartOf' => array( '@id' => utpk_home() . '#website' ) );
	}
	$graph = utpk_schema_apply( $graph );
	echo '<script type="application/ld+json">' . wp_json_encode( array( '@context' => 'https://schema.org', '@graph' => array_values( $graph ) ), JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) . '</script>' . "\n"; // phpcs:ignore WordPress.Security.EscapeOutput
}, 20 );
