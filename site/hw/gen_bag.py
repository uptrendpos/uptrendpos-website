"""Bags & Luggage page images. No brand names. Generic model names only.
Bill adds up: City Backpack Black 3,200 + Laptop Bag Navy 4,800 + Travel Duffel Grey 2,950 -> 10,950; cash 11,000, change 50.
Variants: 4 models x 3 colours = 12 items.
Run: python3 gen_bag.py [name ...]"""
from gen_ind import g
from gen_fashion_beauty import tablet, mini_ui, ui_report, five_steps, hardware_scene
from gen_shoes_vehicle import variant_tablet, phone_list, counter_monitor, printer_with, t, NAVY, MUTED
from _daily_common import run

BLUE = '#024691'


def bg_catalog():
    b = ['<rect x="44" y="94" width="692" height="38" rx="12" fill="#fff" stroke="#dfe6f1"/>', t(64, 118, 'trolley', 13, 600, NAVY), t(716, 118, '24 results', 11, 500, MUTED, 'end')]
    rows = [('Hard Shell Trolley 20 inch', 'Luggage · Cabin size', 'Trolley', True), ('Hard Shell Trolley 24 inch', 'Luggage · Medium', 'Trolley', True),
            ('Hard Shell Trolley 28 inch', 'Luggage · Large', 'Trolley', False), ('Soft Fabric Trolley 24 inch', 'Luggage · Medium', 'Trolley', True),
            ('Trolley Cover 24 inch', 'Travel accessory', 'Accessory', False)]
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
    return tablet('cpBgCat', 'Bag Catalog', '680+ products', ''.join(b))


def bg_variants():
    return variant_tablet('cpBgV', 'Variant Generator', '4 x 3 = 12 items', 'Daily Bags Range', 'Pick models and colours, get every item in one go',
                          'Model', ['City Backpack', 'Laptop Bag', 'Travel Duffel', 'Ladies Tote'], 'Colour', ['Black', 'Navy', 'Grey'],
                          [('City Backpack Black', 'CBP-BLK', '9', 'Rs 3,200'), ('City Backpack Navy', 'CBP-NVY', '6', 'Rs 3,200'),
                           ('City Backpack Grey', 'CBP-GRY', '4', 'Rs 3,200'), ('Laptop Bag Black', 'LPB-BLK', '7', 'Rs 4,800')],
                          'Each item has its own stock and price', 'Create 12 items')


def bg_moves_phone():
    return phone_list('cpBgM', 'Inventory movements', 'This week · Main counter', [
        ('Laptop Bag Grey', 'Zip broken in carton', 'Damage', '#fef2f2', '#b91c1c'), ('Ladies Tote Navy', 'Hung as display piece', 'Sample', '#fffbeb', '#92400e'),
        ('City Backpack Black', 'Count corrected', 'Adjustment', '#eaf1ff', '#024691'), ('Store room stock audit', '112 pieces counted', 'Matched', '#ecfdf3', '#15803d')], 'Open report')


def bg_monitor():
    return counter_monitor('cpMonBg', 'Bag Counter', 'Scan a barcode or search a bag',
                           [(46, 'Item', 'start'), (250, 'Qty', 'start'), (400, 'Rate', 'middle'), (488, 'Amount', 'end')],
                           [('City Backpack Black', '1 pc', '3,200', '3,200'), ('Laptop Bag Navy', '1 pc', '4,800', '4,800'),
                            ('Travel Duffel Grey', '1 pc', '2,950', '2,950')],
                           ('Barcode brings the fixed price', 'Exchange on the same bill', 'Stock drops for each colour'),
                           'Hassan Raza · 0300 6614420', ['Cash', 'Bank', 'Udhaar'], 0, ('Cash received Rs 11,000', 'Change Rs 50'), 'Rs 10,950')


def scene_bg_process():
    return five_steps([
        ('Pick products', mini_ui('Catalog · 680+', [('Searched', 'trolley'), ('Ticked', '3 items'), ('Your price', 'Set')], 'Added to shop'), 'Search, tick, add'),
        ('Receive stock', mini_ui('GRN-0318 · Supplier', [('City Backpack', '24 pcs'), ('Laptop Bag', '12 pcs'), ('Trolley 24 in', '6 pcs')], 'Stock and cost updated'), 'Stock and cost'),
        ('Bill the sale', mini_ui('INV-3142', [('City Backpack', '3,200'), ('Laptop Bag', '4,800'), ('Travel Duffel', '2,950')], 'Total Rs 10,950', '#eaf1ff', BLUE), 'Scan the barcode'),
        ('Exchange', mini_ui('INV-3142', [('Back', 'Backpack Black'), ('Given', 'Backpack Navy'), ('Difference', 'Rs 0')], 'Same invoice number', '#fffbeb', '#92400e'), 'Same bill'),
        ('Close the day', ui_report("Today's sales", 'Rs 84,750', '26 bills · 2 exchanges · drawer matched'), 'Cash and profit'),
    ])


SCENES = {
    'uptrendpos-bag-shop-product-catalog': ('680+ Products Ready', 'green', lambda: g(bg_catalog(), 210, 150, 1.0),
        [(60, 770, 'Search, tick, add', '#2F7BD9'), (330, 770, 'Your own price', '#2FA455')]),
    'uptrendpos-bag-shop-model-colour-variants': ('Model x Colour', 'blue', lambda: g(bg_variants(), 210, 150, 1.0),
        [(60, 770, 'Every colour counted', '#2F7BD9'), (350, 770, 'Own stock and price', '#2FA455')]),
    'uptrendpos-bag-shop-pos-hardware': ('Bag Shop Hardware', 'teal',
        lambda: hardware_scene(bg_monitor, lambda: printer_with('CITY TRAVEL BAG HOUSE', [('City Backpack', '3,200'), ('Laptop Bag', '4,800'), ('Travel Duffel', '2,950')], 'Rs 10,950'),
                               bg_moves_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-bag-shop-pos-process': ('Bag Shop Day, Step by Step', 'yellow', scene_bg_process, [(60, 470, 'All connected', '#2FA455')]),
}

if __name__ == '__main__':
    run(SCENES)
