"""Undergarments & Hosiery page images. No brand names. Generic item names only. Adult / family-shop items only.
Bill adds up: Cotton Vest White M pack of 3 = 1,350 + Ankle Socks Black dozen = 2,400 + Ladies Stockings Skin 1 pair = 650 -> 4,400; cash 4,500, change 100.
Variants: 5 sizes x 3 colours = 15 items. Units: piece / pack of 3 / dozen from one stock (stock in pieces).
Run: python3 gen_undergarments.py [name ...]"""
from gen_ind import g
from gen_fashion_beauty import tablet, mini_ui, ui_report, five_steps, hardware_scene
from gen_shoes_vehicle import variant_tablet, phone_list, counter_monitor, printer_with, t, NAVY, MUTED
from _daily_common import run

BLUE = '#024691'


def ug_catalog():
    b = ['<rect x="44" y="94" width="692" height="38" rx="12" fill="#fff" stroke="#dfe6f1"/>', t(64, 118, 'vest', 13, 600, NAVY), t(716, 118, '18 results', 11, 500, MUTED, 'end')]
    rows = [('Cotton Vest Round Neck', 'Innerwear · Vests', 'Vest', True), ('Cotton Vest Sleeveless', 'Innerwear · Vests', 'Vest', True),
            ('Ribbed Vest Sports Cut', 'Innerwear · Vests', 'Vest', False), ('Thermal Vest Full Sleeve', 'Winter wear · Thermal', 'Thermal', True),
            ('Mesh Vest Summer', 'Innerwear · Vests', 'Vest', False)]
    y = 146
    for n, sub, cls, on in rows:
        b += [f'<rect x="44" y="{y}" width="692" height="44" rx="12" fill="{"#eef5ff" if on else "#fff"}" stroke="{"#c7d7ff" if on else "#e3e9f2"}"/>',
              f'<rect x="58" y="{y+12}" width="20" height="20" rx="6" fill="{"#024691" if on else "#fff"}" stroke="#bcc9dc"/>',
              (f'<path d="M62,{y+22} l4,4 7,-8" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>' if on else ''),
              t(94, y + 20, n, 12.5, 700, NAVY), t(94, y + 36, sub, 10.5, 500, MUTED),
              f'<rect x="612" y="{y+12}" width="106" height="20" rx="10" fill="#eef2f8"/>', t(665, y + 26, cls, 10, 600, '#334155', 'middle')]
        y += 50
    b += ['<rect x="500" y="424" width="236" height="44" rx="14" fill="#FAE814"/>', t(618, 452, 'Add 3 to my shop', 13, 800, NAVY, 'middle'),
          t(64, 452, 'Not in the list? Add your own product.', 11.5, 600, BLUE)]
    return tablet('cpUgCat', 'Hosiery Catalog', '400+ products', ''.join(b))


def ug_variants():
    return variant_tablet('cpUgV', 'Variant Generator', '5 x 3 = 15 items', 'Cotton Vest Round Neck', 'Pick sizes and colours, get every item in one go',
                          'Size', ['S', 'M', 'L', 'XL', 'XXL'], 'Colour', ['White', 'Black', 'Grey'],
                          [('Cotton Vest White M', 'CV-WHT-M', '36', 'Rs 450'), ('Cotton Vest White L', 'CV-WHT-L', '30', 'Rs 450'),
                           ('Cotton Vest Black M', 'CV-BLK-M', '18', 'Rs 450'), ('Cotton Vest Grey XL', 'CV-GRY-XL', '12', 'Rs 480')],
                          'Each item has its own stock and price', 'Create 15 items')


def ug_moves_phone():
    return phone_list('cpUgM', 'Inventory movements', 'This week · Main counter', [
        ('Ankle Socks Grey', 'Torn pack in carton', 'Damage', '#fef2f2', '#b91c1c'), ('Thermal Vest Black L', 'Opened for display', 'Sample', '#fffbeb', '#92400e'),
        ('Cotton Vest White M', 'Count corrected', 'Adjustment', '#eaf1ff', '#024691'), ('Shelf stock audit', '864 pieces counted', 'Matched', '#ecfdf3', '#15803d')], 'Open report')


def ug_monitor():
    return counter_monitor('cpMonUg', 'Hosiery Counter', 'Scan a barcode or search an item',
                           [(46, 'Item', 'start'), (250, 'Qty', 'start'), (400, 'Rate', 'middle'), (488, 'Amount', 'end')],
                           [('Cotton Vest White M', '1 pack of 3', '1,350', '1,350'), ('Ankle Socks Black', '1 dozen', '2,400', '2,400'),
                            ('Ladies Stockings Skin', '1 pair', '650', '650')],
                           ('Pack and dozen from one stock', 'Exchange on the same bill', 'Stock drops for each size'),
                           'Bilal Ahmed · 0301 4471852', ['Cash', 'Bank', 'Udhaar'], 0, ('Cash received Rs 4,500', 'Change Rs 100'), 'Rs 4,400')


def scene_ug_process():
    return five_steps([
        ('Pick products', mini_ui('Catalog · 400+', [('Searched', 'vest'), ('Ticked', '3 items'), ('Your price', 'Set')], 'Added to shop'), 'Search, tick, add'),
        ('Receive stock', mini_ui('GRN-0412 · Supplier', [('Ankle Socks', '10 dozen'), ('Cotton Vest M', '6 dozen'), ('In stock', '192 pcs')], 'Stock and cost updated'), 'By the dozen'),
        ('Bill the sale', mini_ui('INV-2276', [('Vest pack of 3', '1,350'), ('Socks dozen', '2,400'), ('Stockings pair', '650')], 'Total Rs 4,400', '#eaf1ff', BLUE), 'Piece, pack, dozen'),
        ('Exchange size', mini_ui('INV-2276', [('Back', 'Vest White M'), ('Given', 'Vest White L'), ('Difference', 'Rs 0')], 'Same invoice number', '#fffbeb', '#92400e'), 'Same bill'),
        ('Close the day', ui_report("Today's sales", 'Rs 38,600', '41 bills · 3 exchanges · drawer matched'), 'Cash and profit'),
    ])


SCENES = {
    'uptrendpos-undergarments-shop-product-catalog': ('400+ Products Ready', 'green', lambda: g(ug_catalog(), 210, 150, 1.0),
        [(60, 770, 'Search, tick, add', '#2F7BD9'), (330, 770, 'Your own price', '#2FA455')]),
    'uptrendpos-undergarments-shop-size-colour-variants': ('Size x Colour', 'blue', lambda: g(ug_variants(), 210, 150, 1.0),
        [(60, 770, 'Every size counted', '#2F7BD9'), (330, 770, 'Own stock and price', '#2FA455')]),
    'uptrendpos-undergarments-shop-pos-hardware': ('Hosiery Shop Hardware', 'teal',
        lambda: hardware_scene(ug_monitor, lambda: printer_with('CITY HOSIERY HOUSE', [('Vest pack of 3', '1,350'), ('Socks dozen', '2,400'), ('Stockings pair', '650')], 'Rs 4,400'),
                               ug_moves_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-undergarments-shop-pos-process': ('Hosiery Shop Day, Step by Step', 'yellow', scene_ug_process, [(60, 470, 'All connected', '#2FA455')]),
}

if __name__ == '__main__':
    run(SCENES)
