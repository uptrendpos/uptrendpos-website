"""Sports Goods page images. No brand names. Generic item names only.
Bill adds up: Cricket Bat Hard Ball 6,500 + Hard Ball 2 x 1,100 = 2,200 + Sports Shoes / 9 4,800 + Football Kit / M 1,950 -> 15,450; cash 16,000, change 550.
Variants: 4 sizes x 3 colours = 12 items. School quote: 40 kits x 1,950 = 78,000 + 10 footballs x 2,000 = 20,000 -> 98,000.
Run: python3 gen_sports.py [name ...]"""
from gen_ind import g
from gen_fashion_beauty import tablet, mini_ui, ui_report, five_steps, hardware_scene
from gen_shoes_vehicle import variant_tablet, phone_list, counter_monitor, printer_with, t, NAVY, MUTED
from _daily_common import run

BLUE = '#024691'


def sp_catalog():
    b = ['<rect x="44" y="94" width="692" height="38" rx="12" fill="#fff" stroke="#dfe6f1"/>', t(64, 118, 'cricket bat', 13, 600, NAVY), t(716, 118, '19 results', 11, 500, MUTED, 'end')]
    rows = [('Cricket Bat Hard Ball Full Size', 'Cricket · Bats', 'Hard ball', True), ('Cricket Bat Tape Ball', 'Cricket · Bats', 'Tape ball', True),
            ('Cricket Bat Junior Size 4', 'Cricket · Bats', 'Junior', False), ('Bat Grip Rubber', 'Cricket · Accessories', 'Grip', True),
            ('Bat Cover Padded', 'Cricket · Accessories', 'Cover', False)]
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
    return tablet('cpSpCat', 'Sports Catalog', '250+ products', ''.join(b))


def sp_variants():
    return variant_tablet('cpSpV', 'Variant Generator', '4 x 3 = 12 items', 'Football Kit FK-220', 'Pick sizes and colours, get every item in one go',
                          'Size', ['S', 'M', 'L', 'XL'], 'Colour', ['White', 'Blue', 'Green'],
                          [('FK-220 White / M', '220-WH-M', '14', 'Rs 1,950'), ('FK-220 Blue / L', '220-BL-L', '9', 'Rs 1,950'),
                           ('FK-220 Green / S', '220-GR-S', '6', 'Rs 1,950'), ('FK-220 Blue / XL', '220-BL-XL', '4', 'Rs 2,100')],
                          'Each item has its own stock and price', 'Create 12 items')


def sp_moves_phone():
    return phone_list('cpSpM', 'Inventory movements', 'This week · Main counter', [
        ('Cricket Bat Hard Ball', 'Crack on the edge', 'Damage', '#fef2f2', '#b91c1c'), ('Sports Shoes / 9', 'Display pair', 'Sample', '#fffbeb', '#92400e'),
        ('Hard Ball', 'Count corrected', 'Adjustment', '#eaf1ff', '#024691'), ('Store room stock audit', '612 pieces counted', 'Matched', '#ecfdf3', '#15803d')], 'Open report')


def sp_monitor():
    return counter_monitor('cpMonSp', 'Sports Shop Counter', 'Scan a barcode or search an item',
                           [(46, 'Item', 'start'), (250, 'Qty', 'start'), (400, 'Rate', 'middle'), (488, 'Amount', 'end')],
                           [('Cricket Bat Hard Ball', '1 pc', '6,500', '6,500'), ('Hard Ball', '2 pc', '1,100', '2,200'),
                            ('Sports Shoes / 9', '1 pair', '4,800', '4,800'), ('Football Kit / M', '1 set', '1,950', '1,950')],
                           ('Barcode brings the fixed price', 'Size and colour on every line', 'Stock drops for each size'),
                           'Usman Ghani · 0321 5584102', ['Cash', 'Bank', 'Udhaar'], 0, ('Cash received Rs 16,000', 'Change Rs 550'), 'Rs 15,450')


def scene_sp_process():
    return five_steps([
        ('Pick products', mini_ui('Catalog · 250+', [('Searched', 'cricket bat'), ('Ticked', '3 items'), ('Your price', 'Set')], 'Added to shop'), 'Search, tick, add'),
        ('Receive stock', mini_ui('GRN-0638 · Supplier', [('Football Kit', '48 sets'), ('Football', '24 pcs'), ('Hard Ball', '6 dozen')], 'Stock and cost updated'), 'Stock and cost'),
        ('Quote the school', mini_ui('QT-0148 · City School', [('Kit x 40', '78,000'), ('Football x 10', '20,000'), ('Total', '98,000')], 'Sent on WhatsApp', '#eaf1ff', BLUE), 'A4 quotation'),
        ('Bill the order', mini_ui('INV-7315 from QT-0148', [('Kits', '40 sets'), ('Footballs', '10 pcs'), ('Paid by', 'Udhaar')], 'On school ledger', '#fffbeb', '#92400e'), 'Sale in one tap'),
        ('Close the day', ui_report("Today's sales", 'Rs 186,400', '41 bills · 1 school order · drawer matched'), 'Cash and profit'),
    ])


SCENES = {
    'uptrendpos-sports-shop-product-catalog': ('250+ Products Ready', 'green', lambda: g(sp_catalog(), 210, 150, 1.0),
        [(60, 770, 'Search, tick, add', '#2F7BD9'), (330, 770, 'Your own price', '#2FA455')]),
    'uptrendpos-sports-shop-size-colour-variants': ('Size x Colour', 'blue', lambda: g(sp_variants(), 210, 150, 1.0),
        [(60, 770, 'Every size counted', '#2F7BD9'), (330, 770, 'Own stock and price', '#2FA455')]),
    'uptrendpos-sports-shop-pos-hardware': ('Sports Shop Hardware', 'teal',
        lambda: hardware_scene(sp_monitor, lambda: printer_with('CITY SPORTS', [('Cricket Bat', '6,500'), ('Hard Ball x2', '2,200'), ('Shoes + Kit', '6,750')], 'Rs 15,450'),
                               sp_moves_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-sports-shop-pos-process': ('Sports Shop Day, Step by Step', 'yellow', scene_sp_process, [(60, 470, 'All connected', '#2FA455')]),
}

if __name__ == '__main__':
    run(SCENES)
