"""Perfume & Attar page images. No brand names, no health or skin claims. Generic fragrance names only.
Bill adds up: Oud Perfume 50 ml 3,200 + Rose Attar loose 12 ml x 45 = 540 + Body Spray 200 ml 850 -> 4,590; cash 5,000, change 410.
Variants: 4 fragrances x 3 bottle sizes = 12 items.
Run: python3 gen_perfume.py [name ...]"""
from gen_ind import g
from gen_fashion_beauty import tablet, mini_ui, ui_report, five_steps, hardware_scene
from gen_shoes_vehicle import variant_tablet, phone_list, counter_monitor, printer_with, t, NAVY, MUTED
from _daily_common import run

BLUE = '#024691'


def pf_catalog():
    b = ['<rect x="44" y="94" width="692" height="38" rx="12" fill="#fff" stroke="#dfe6f1"/>', t(64, 118, 'rose', 13, 600, NAVY), t(716, 118, '24 results', 11, 500, MUTED, 'end')]
    rows = [('Rose Attar 6 ml', 'Attar · Roll-on', 'Attar', True), ('Rose Attar 12 ml', 'Attar · Roll-on', 'Attar', True),
            ('Rose Perfume 50 ml', 'Perfume · Spray', 'Perfume', False), ('Rose Oud Perfume 100 ml', 'Perfume · Spray', 'Perfume', True),
            ('Rose Body Spray 200 ml', 'Body spray', 'Spray', False)]
    y = 146
    for n, sub, cls, on in rows:
        b += [f'<rect x="44" y="{y}" width="692" height="44" rx="12" fill="{"#eef5ff" if on else "#fff"}" stroke="{"#c7d7ff" if on else "#e3e9f2"}"/>',
              f'<rect x="58" y="{y+12}" width="20" height="20" rx="6" fill="{"#024691" if on else "#fff"}" stroke="#bcc9dc"/>',
              (f'<path d="M62,{y+22} l4,4 7,-8" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>' if on else ''),
              t(94, y + 20, n, 12.5, 700, NAVY), t(94, y + 36, sub, 10.5, 500, MUTED),
              f'<rect x="612" y="{y+12}" width="106" height="20" rx="10" fill="#fdf2f8"/>', t(665, y + 26, cls, 10, 600, '#9d174d', 'middle')]
        y += 50
    b += ['<rect x="500" y="424" width="236" height="44" rx="14" fill="#FAE814"/>', t(618, 452, 'Add 3 to my shop', 13, 800, NAVY, 'middle'),
          t(64, 452, 'Not in the list? Add your own product.', 11.5, 600, BLUE)]
    return tablet('cpPfCat', 'Perfume &amp; Attar Catalog', '300+ products', ''.join(b))


def pf_variants():
    return variant_tablet('cpPfV', 'Variant Generator', '4 x 3 = 12 items', 'Eau de Parfum Range', 'Pick fragrances and bottle sizes, get every item in one go',
                          'Fragrance', ['Oud', 'Rose', 'Musk', 'Jasmine'], 'Bottle', ['30 ml', '50 ml', '100 ml'],
                          [('Oud 30 ml', 'OUD-30', '18', 'Rs 1,900'), ('Oud 50 ml', 'OUD-50', '24', 'Rs 3,200'),
                           ('Oud 100 ml', 'OUD-100', '9', 'Rs 5,400'), ('Rose 30 ml', 'ROS-30', '22', 'Rs 1,600')],
                          'Each item has its own stock and price', 'Create 12 items')


def pf_moves_phone():
    return phone_list('cpPfM', 'Inventory movements', 'This week · Main counter', [
        ('Oud Perfume 50 ml', 'Tester opened', 'Sample', '#fffbeb', '#92400e'), ('Rose Perfume 100 ml', 'Tester opened', 'Sample', '#fffbeb', '#92400e'),
        ('Musk Attar 12 ml', 'Bottle broken in box', 'Damage', '#fef2f2', '#b91c1c'), ('Shelf A stock audit', '86 items counted', 'Matched', '#ecfdf3', '#15803d')], 'Open report')


def pf_monitor():
    return counter_monitor('cpMonPf', 'Perfume Counter', 'Scan a barcode or search a fragrance',
                           [(46, 'Item', 'start'), (250, 'Qty', 'start'), (400, 'Rate', 'middle'), (488, 'Amount', 'end')],
                           [('Oud Perfume 50 ml', '1 pc', '3,200', '3,200'), ('Rose Attar loose', '12 ml', '45', '540'),
                            ('Body Spray 200 ml', '1 pc', '850', '850')],
                           ('Barcode brings the fixed price', 'Loose attar typed in ml', 'Stock drops for each size'),
                           'Sana Tariq · 0300 7711223', ['Cash', 'Bank', 'Udhaar'], 0, ('Cash received Rs 5,000', 'Change Rs 410'), 'Rs 4,590')


def scene_pf_process():
    return five_steps([
        ('Pick products', mini_ui('Catalog · 300+', [('Searched', 'rose'), ('Ticked', '3 items'), ('Your price', 'Set')], 'Added to shop'), 'Search, tick, add'),
        ('Receive stock', mini_ui('GRN-0318 · Supplier', [('Oud 50 ml', '24 pcs'), ('Rose Attar', '2 litre'), ('Body Spray', '36 pcs')], 'Stock and cost updated'), 'Bottle and ml'),
        ('Record testers', mini_ui('Sample entry', [('Oud 50 ml', '1 tester'), ('Rose 100 ml', '1 tester'), ('Stock', 'Updated')], 'Stock stays true', '#fffbeb', '#92400e'), 'On record'),
        ('Bill the sale', mini_ui('INV-1187', [('Oud 50 ml', '3,200'), ('Rose Attar 12 ml', '540'), ('Body Spray', '850')], 'Total Rs 4,590', '#eaf1ff', BLUE), 'Scan or type ml'),
        ('Close the day', ui_report("Today's sales", 'Rs 84,250', '63 bills · 2 tester entries · 1 damage entry'), 'Cash and profit'),
    ])


SCENES = {
    'uptrendpos-perfume-shop-product-catalog': ('300+ Products Ready', 'green', lambda: g(pf_catalog(), 210, 150, 1.0),
        [(60, 770, 'Search, tick, add', '#2F7BD9'), (330, 770, 'Your own price', '#2FA455')]),
    'uptrendpos-perfume-shop-fragrance-bottle-sizes': ('Fragrance x Bottle Size', 'blue', lambda: g(pf_variants(), 210, 150, 1.0),
        [(60, 770, 'Every size counted', '#2F7BD9'), (350, 770, 'Own stock and price', '#2FA455')]),
    'uptrendpos-perfume-shop-pos-hardware': ('Perfume Shop Hardware', 'teal',
        lambda: hardware_scene(pf_monitor, lambda: printer_with('MADINA ATTAR HOUSE', [('Oud 50 ml', '3,200'), ('Rose Attar 12 ml', '540'), ('Body Spray', '850')], 'Rs 4,590'),
                               pf_moves_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-perfume-shop-pos-process': ('Perfume Shop Day, Step by Step', 'yellow', scene_pf_process, [(60, 470, 'All connected', '#2FA455')]),
}

if __name__ == '__main__':
    run(SCENES)
