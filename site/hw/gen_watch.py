"""Watch Shop page images. No brand names. Generic model names only.
Bill adds up: Steel Classic Black 8,500 + Slim Leather Brown 4,200 + Leather Strap 20 mm 650 -> 13,350; cash 13,500, change 150.
Variants: 4 models x 3 dial colours = 12 items.
Run: python3 gen_watch.py [name ...]"""
from gen_ind import g
from gen_fashion_beauty import tablet, mini_ui, ui_report, five_steps, hardware_scene
from gen_shoes_vehicle import variant_tablet, phone_list, counter_monitor, printer_with, t, NAVY, MUTED
from _daily_common import run

BLUE = '#024691'


def wt_catalog():
    b = ['<rect x="44" y="94" width="692" height="38" rx="12" fill="#fff" stroke="#dfe6f1"/>', t(64, 118, 'steel', 13, 600, NAVY), t(716, 118, '18 results', 11, 500, MUTED, 'end')]
    rows = [('Steel Classic Gents Watch', 'Gents · Steel chain', 'Gents', True), ('Steel Slim Ladies Watch', 'Ladies · Steel chain', 'Ladies', True),
            ('Steel Sport Chrono Watch', 'Gents · Chronograph', 'Gents', False), ('Steel Mesh Strap 20 mm', 'Strap · Replacement', 'Strap', True),
            ('Steel Link Strap 22 mm', 'Strap · Replacement', 'Strap', False)]
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
    return tablet('cpWtCat', 'Watch Catalog', '150+ products', ''.join(b))


def wt_variants():
    return variant_tablet('cpWtV', 'Variant Generator', '4 x 3 = 12 items', 'Gents Watch Range', 'Pick models and dial colours, get every item in one go',
                          'Model', ['Steel Classic', 'Sport Chrono', 'Slim Leather', 'Smart Band'], 'Dial', ['Black', 'Silver', 'Blue'],
                          [('Steel Classic Black', 'STC-BLK', '6', 'Rs 8,500'), ('Steel Classic Silver', 'STC-SLV', '4', 'Rs 8,500'),
                           ('Steel Classic Blue', 'STC-BLU', '3', 'Rs 8,900'), ('Sport Chrono Black', 'SPC-BLK', '5', 'Rs 11,500')],
                          'Each item has its own stock and price', 'Create 12 items')


def wt_moves_phone():
    return phone_list('cpWtM', 'Inventory movements', 'This week · Main counter', [
        ('Sport Chrono Blue', 'Glass broken in box', 'Damage', '#fef2f2', '#b91c1c'), ('Slim Leather Brown', 'Display piece for showcase', 'Sample', '#fffbeb', '#92400e'),
        ('Steel Classic Silver', 'Count corrected', 'Adjustment', '#eaf1ff', '#024691'), ('Showcase B stock audit', '48 pieces counted', 'Matched', '#ecfdf3', '#15803d')], 'Open report')


def wt_monitor():
    return counter_monitor('cpMonWt', 'Watch Counter', 'Scan a barcode or search a watch',
                           [(46, 'Item', 'start'), (250, 'Qty', 'start'), (400, 'Rate', 'middle'), (488, 'Amount', 'end')],
                           [('Steel Classic Black', '1 pc', '8,500', '8,500'), ('Slim Leather Brown', '1 pc', '4,200', '4,200'),
                            ('Leather Strap 20 mm', '1 pc', '650', '650')],
                           ('Barcode brings the fixed price', 'Warranty note on the sale', 'Stock drops for each colour'),
                           'Usman Javed · 0300 5522119', ['Cash', 'Bank', 'Udhaar'], 0, ('Cash received Rs 13,500', 'Change Rs 150'), 'Rs 13,350')


def scene_wt_process():
    return five_steps([
        ('Pick products', mini_ui('Catalog · 150+', [('Searched', 'steel'), ('Ticked', '3 items'), ('Your price', 'Set')], 'Added to shop'), 'Search, tick, add'),
        ('Receive stock', mini_ui('GRN-0274 · Supplier', [('Steel Classic', '12 pcs'), ('Slim Leather', '8 pcs'), ('Straps', '24 pcs')], 'Stock and cost updated'), 'Stock and cost'),
        ('Bill the sale', mini_ui('INV-2316', [('Steel Classic', '8,500'), ('Slim Leather', '4,200'), ('Strap 20 mm', '650')], 'Total Rs 13,350', '#eaf1ff', BLUE), 'Scan the barcode'),
        ('Note the warranty', mini_ui('Sale note', [('Bill', 'INV-2316'), ('Machine', '1 year'), ('Battery', '6 months')], 'Note saved on sale', '#fffbeb', '#92400e'), 'On record'),
        ('Close the day', ui_report("Today's sales", 'Rs 96,400', '21 bills · 1 damage entry · drawer matched'), 'Cash and profit'),
    ])


SCENES = {
    'uptrendpos-watch-shop-product-catalog': ('150+ Products Ready', 'green', lambda: g(wt_catalog(), 210, 150, 1.0),
        [(60, 770, 'Search, tick, add', '#2F7BD9'), (330, 770, 'Your own price', '#2FA455')]),
    'uptrendpos-watch-shop-model-dial-variants': ('Model x Dial Colour', 'blue', lambda: g(wt_variants(), 210, 150, 1.0),
        [(60, 770, 'Every colour counted', '#2F7BD9'), (350, 770, 'Own stock and price', '#2FA455')]),
    'uptrendpos-watch-shop-pos-hardware': ('Watch Shop Hardware', 'teal',
        lambda: hardware_scene(wt_monitor, lambda: printer_with('CITY TIME WATCH HOUSE', [('Steel Classic', '8,500'), ('Slim Leather', '4,200'), ('Strap 20 mm', '650')], 'Rs 13,350'),
                               wt_moves_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-watch-shop-pos-process': ('Watch Shop Day, Step by Step', 'yellow', scene_wt_process, [(60, 470, 'All connected', '#2FA455')]),
}

if __name__ == '__main__':
    run(SCENES)
