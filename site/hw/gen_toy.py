"""Toys & Gift Shop page images. No brand names. Generic item names only.
Bill adds up: Remote Car Racing Red 3,500 + Building Blocks 250 pcs 2,200 + Doll House Set 4,800 + Colouring Gift Set 950 -> 11,450; cash 12,000, change 550.
Variants: 3 models x 3 colours = 9 items. Age groups are categories. Gift sets are normal items.
Run: python3 gen_toy.py [name ...]"""
from gen_ind import g
from gen_fashion_beauty import tablet, mini_ui, ui_report, five_steps, hardware_scene
from gen_shoes_vehicle import variant_tablet, phone_list, counter_monitor, printer_with, t, NAVY, MUTED
from _daily_common import run

BLUE = '#024691'


def ts_catalog():
    b = ['<rect x="44" y="94" width="692" height="38" rx="12" fill="#fff" stroke="#dfe6f1"/>', t(64, 118, 'remote car', 13, 600, NAVY), t(716, 118, '28 results', 11, 500, MUTED, 'end')]
    rows = [('Remote Car Racing 1:18', 'Toys · Age 6-8 years', 'Remote', True), ('Remote Jeep Off Road 1:16', 'Toys · Age 6-8 years', 'Remote', True),
            ('Remote Truck with Lights', 'Toys · Age 9-12 years', 'Remote', False), ('Mini Pull Back Car Set of 4', 'Toys · Age 3-5 years', 'Car set', True),
            ('Remote Car Battery Pack', 'Toys · Spare parts', 'Spare', False)]
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
    return tablet('cpTsCat', 'Toy Catalog', '1,000+ products', ''.join(b))


def ts_variants():
    return variant_tablet('cpTsV', 'Variant Generator', '3 x 3 = 9 items', 'Remote Car Range RC-310', 'Pick models and colours, get every item in one go',
                          'Model', ['Racing', 'Jeep', 'Truck'], 'Colour', ['Red', 'Blue', 'Yellow'],
                          [('RC-310 Racing / Red', '310-RC-RD', '12', 'Rs 3,500'), ('RC-310 Racing / Blue', '310-RC-BL', '8', 'Rs 3,500'),
                           ('RC-310 Jeep / Yellow', '310-JP-YL', '6', 'Rs 4,200'), ('RC-310 Truck / Red', '310-TR-RD', '5', 'Rs 4,600')],
                          'Each item has its own stock and price', 'Create 9 items')


def ts_moves_phone():
    return phone_list('cpTsM', 'Inventory movements', 'This week · Main counter', [
        ('Doll House Set', 'Box torn, part missing', 'Damage', '#fef2f2', '#b91c1c'), ('Remote Car Racing Red', 'Opened to show buyers', 'Sample', '#fffbeb', '#92400e'),
        ('Building Blocks 250 pcs', 'Count corrected', 'Adjustment', '#eaf1ff', '#024691'), ('Store room stock audit', '418 pieces counted', 'Matched', '#ecfdf3', '#15803d')], 'Open report')


def ts_monitor():
    return counter_monitor('cpMonTs', 'Toy Shop Counter', 'Scan a barcode or search a toy',
                           [(46, 'Item', 'start'), (250, 'Qty', 'start'), (400, 'Rate', 'middle'), (488, 'Amount', 'end')],
                           [('Remote Car Racing Red', '1 pc', '3,500', '3,500'), ('Building Blocks 250', '1 pc', '2,200', '2,200'),
                            ('Doll House Set', '1 pc', '4,800', '4,800'), ('Colouring Gift Set', '1 set', '950', '950')],
                           ('Barcode brings the fixed price', 'Gift set sold as one item', 'Stock drops for each colour'),
                           'Sana Tariq · 0302 4417835', ['Cash', 'Bank', 'Udhaar'], 0, ('Cash received Rs 12,000', 'Change Rs 550'), 'Rs 11,450')


def scene_ts_process():
    return five_steps([
        ('Pick products', mini_ui('Catalog · 1,000+', [('Searched', 'remote car'), ('Ticked', '3 items'), ('Your price', 'Set')], 'Added to shop'), 'Search, tick, add'),
        ('Receive stock', mini_ui('GRN-0512 · Supplier', [('Remote Car', '24 pcs'), ('Blocks 250', '18 pcs'), ('Doll House', '10 pcs')], 'Stock and cost updated'), 'Stock and cost'),
        ('Bill the sale', mini_ui('INV-6271', [('Remote Car', '3,500'), ('Blocks + Doll', '7,000'), ('Gift Set', '950')], 'Total Rs 11,450', '#eaf1ff', BLUE), 'Scan the barcode'),
        ('Exchange', mini_ui('INV-6271', [('Back', 'Car Racing Red'), ('Given', 'Car Racing Blue'), ('Difference', 'Rs 0')], 'Same invoice number', '#fffbeb', '#92400e'), 'Same bill'),
        ('Close the day', ui_report("Today's sales", 'Rs 92,300', '58 bills · 3 exchanges · drawer matched'), 'Cash and profit'),
    ])


SCENES = {
    'uptrendpos-toy-shop-product-catalog': ('1,000+ Products Ready', 'green', lambda: g(ts_catalog(), 210, 150, 1.0),
        [(60, 770, 'Search, tick, add', '#2F7BD9'), (330, 770, 'Your own price', '#2FA455')]),
    'uptrendpos-toy-shop-model-colour-variants': ('Model x Colour', 'blue', lambda: g(ts_variants(), 210, 150, 1.0),
        [(60, 770, 'Every colour counted', '#2F7BD9'), (350, 770, 'Own stock and price', '#2FA455')]),
    'uptrendpos-toy-shop-pos-hardware': ('Toy Shop Hardware', 'teal',
        lambda: hardware_scene(ts_monitor, lambda: printer_with('FUN WORLD TOYS', [('Remote Car', '3,500'), ('Blocks + Doll House', '7,000'), ('Colouring Gift Set', '950')], 'Rs 11,450'),
                               ts_moves_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-toy-shop-pos-process': ('Toy Shop Day, Step by Step', 'yellow', scene_ts_process, [(60, 470, 'All connected', '#2FA455')]),
}

if __name__ == '__main__':
    run(SCENES)
