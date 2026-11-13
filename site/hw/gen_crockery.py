"""Crockery & Household page images. No brand names. Generic item names only.
Bill adds up: Dinner Set 72 pcs 1 set 18,500 + Water Glass set of 6 x 2 = 1,800 + Tea Cup piece x 2 = 300 + Steel Jug 1 pc 1,250 -> 21,850; cash 22,000, change 150.
Units: carton / set / piece from one stock (stock in pieces).
Run: python3 gen_crockery.py [name ...]"""
from gen_ind import g
from gen_fashion_beauty import tablet, mini_ui, ui_report, five_steps, hardware_scene
from gen_shoes_vehicle import phone_list, counter_monitor, printer_with, t, NAVY, MUTED
from gen_electrical_baby import unit_tablet
from _daily_common import run

BLUE = '#024691'


def cr_catalog():
    b = ['<rect x="44" y="94" width="692" height="38" rx="12" fill="#fff" stroke="#dfe6f1"/>', t(64, 118, 'dinner set', 13, 600, NAVY), t(716, 118, '36 results', 11, 500, MUTED, 'end')]
    rows = [('Dinner Set 72 Pieces White', 'Crockery · Dinner sets', 'Set', True), ('Dinner Set 48 Pieces Floral', 'Crockery · Dinner sets', 'Set', True),
            ('Dinner Set 32 Pieces Gold Line', 'Crockery · Dinner sets', 'Set', False), ('Dinner Plate 10 inch White', 'Crockery · Plates', 'Piece', True),
            ('Serving Bowl Set of 3', 'Crockery · Bowls', 'Set', False)]
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
    return tablet('cpCrCat', 'Crockery Catalog', '2,000+ products', ''.join(b))


def cr_units():
    return unit_tablet('cpCrU', 'Units and Packing', 'Carton · Set · Piece', 'One stock, sold the way you sell it', 'Buy by the carton, sell by the set or the single piece',
                       [('Water Glass 300 ml', 'Carton of 48', 'Set of 6 or piece', '264 pcs', 'Rs 900 /set'), ('Tea Cup White', 'Carton of 36', 'Set of 6 or piece', '180 pcs', 'Rs 150'),
                        ('Dinner Plate 10 inch', 'Carton of 24', 'Piece or set', '96 pcs', 'Rs 450'), ('Coffee Mug Plain', 'Box of 12', 'Piece or box', '60 pcs', 'Rs 350'),
                        ('Dinner Set 72 Pieces', 'Box of 1', 'Set', '8 sets', 'Rs 18,500'), ('Steel Jug 2 Litre', 'Carton of 10', 'Piece', '22 pcs', 'Rs 1,250')],
                       'A set of 6 drops 6 pieces from the same stock', 'Sell 2 sets of glasses')


def cr_moves_phone():
    return phone_list('cpCrM', 'Inventory movements', 'This week · Main counter', [
        ('Water Glass 300 ml', '3 broken while packing', 'Damage', '#fef2f2', '#b91c1c'), ('Tea Cup White', '2 cracked in carton', 'Damage', '#fef2f2', '#b91c1c'),
        ('Dinner Set 48 Floral', 'Opened for display', 'Sample', '#fffbeb', '#92400e'), ('Shelf stock audit', '1,240 pieces counted', 'Matched', '#ecfdf3', '#15803d')], 'Open report')


def cr_monitor():
    return counter_monitor('cpMonCr', 'Crockery Counter', 'Scan a barcode or search an item',
                           [(46, 'Item', 'start'), (250, 'Qty / unit', 'start'), (400, 'Rate', 'middle'), (488, 'Amount', 'end')],
                           [('Dinner Set 72 Pieces', '1 set', '18,500', '18,500'), ('Water Glass 300 ml', '2 set of 6', '900', '1,800'),
                            ('Tea Cup White', '2 piece', '150', '300'), ('Steel Jug 2 Litre', '1 piece', '1,250', '1,250')],
                           ('Water Glass: 252 pcs left', 'Bought as cartons · sold by set or piece', 'Breakage recorded as damage'),
                           'Nadia Saleem · 0301 7735210', ['Cash', 'Bank', 'Udhaar'], 0, ('Cash received Rs 22,000', 'Change Rs 150'), 'Rs 21,850')


def scene_cr_process():
    return five_steps([
        ('Pick products', mini_ui('Catalog · 2,000+', [('Searched', 'dinner set'), ('Ticked', '3 items'), ('Your price', 'Set')], 'Added to shop'), 'Search, tick, add'),
        ('Receive cartons', mini_ui('GRN-0427 · Supplier', [('Water Glass', '6 cartons'), ('Tea Cup', '4 cartons'), ('Dinner Set', '8 sets')], 'Stock and cost updated'), 'Stock and cost'),
        ('Bill the sale', mini_ui('INV-5208', [('Dinner Set', '18,500'), ('Glass x 2 sets', '1,800'), ('Cup + Jug', '1,550')], 'Total Rs 21,850', '#eaf1ff', BLUE), 'Set or piece'),
        ('Record breakage', mini_ui('Damage', [('Water Glass', '3 pcs'), ('Tea Cup', '2 pcs'), ('Loss at cost', 'Rs 620')], 'Stock corrected', '#fef2f2', '#b91c1c'), 'Damage on record'),
        ('Close the day', ui_report("Today's sales", 'Rs 96,400', '31 bills · 5 pieces damaged · drawer matched'), 'Cash and profit'),
    ])


SCENES = {
    'uptrendpos-crockery-shop-product-catalog': ('2,000+ Products Ready', 'green', lambda: g(cr_catalog(), 210, 150, 1.0),
        [(60, 770, 'Search, tick, add', '#2F7BD9'), (330, 770, 'Your own price', '#2FA455')]),
    'uptrendpos-crockery-shop-carton-set-piece': ('Carton, Set and Piece', 'blue', lambda: g(cr_units(), 210, 150, 1.0),
        [(60, 770, 'One stock, any unit', '#2F7BD9'), (350, 770, 'Right count every sale', '#2FA455')]),
    'uptrendpos-crockery-shop-pos-hardware': ('Crockery Shop Hardware', 'teal',
        lambda: hardware_scene(cr_monitor, lambda: printer_with('NOOR CROCKERY HOUSE', [('Dinner Set 72 pcs', '18,500'), ('Glass x 2 sets', '1,800'), ('Cups + Jug', '1,550')], 'Rs 21,850'),
                               cr_moves_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-crockery-shop-pos-process': ('Crockery Shop Day, Step by Step', 'yellow', scene_cr_process, [(60, 470, 'All connected', '#2FA455')]),
}

if __name__ == '__main__':
    run(SCENES)
