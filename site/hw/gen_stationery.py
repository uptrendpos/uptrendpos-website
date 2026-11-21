"""Stationery & Book Shop page images. No brand names. Generic item names only.
Bill adds up: Register A4 200 Pages 2 pc x 350 = 700 + Ball Pen Blue 1 box (10) 250 + Pencil HB 6 pc x 25 = 150 + Geometry Box 1 pc 450 -> 1,550; cash 2,000, change 450.
Units: carton / box / dozen / ream / piece from one stock (stock in the selling unit).
School quote: 300 notebooks x 120 = 36,000 + 50 registers x 350 = 17,500 -> 53,500.
Run: python3 gen_stationery.py [name ...]"""
from gen_ind import g
from gen_fashion_beauty import tablet, mini_ui, ui_report, five_steps, hardware_scene
from gen_shoes_vehicle import phone_list, counter_monitor, printer_with, t, NAVY, MUTED
from gen_electrical_baby import unit_tablet
from _daily_common import run

BLUE = '#024691'


def st_catalog():
    b = ['<rect x="44" y="94" width="692" height="38" rx="12" fill="#fff" stroke="#dfe6f1"/>', t(64, 118, 'notebook', 13, 600, NAVY), t(716, 118, '22 results', 11, 500, MUTED, 'end')]
    rows = [('Notebook 80 Pages Single Line', 'School · Notebooks', 'Piece', True), ('Notebook 120 Pages Four Line', 'School · Notebooks', 'Piece', True),
            ('Register A4 200 Pages', 'Office · Registers', 'Piece', True), ('Drawing Copy Large', 'School · Art', 'Piece', False),
            ('Spiral Notebook A5', 'Office · Notebooks', 'Piece', False)]
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
    return tablet('cpStCat', 'Stationery Catalog', '200+ products', ''.join(b))


def st_units():
    return unit_tablet('cpStU', 'Units and Packing', 'Box · Dozen · Piece', 'Sell a full box or one piece', 'Buy by the carton or box, sell by the box, dozen or piece',
                       [('Ball Pen Blue', 'Box of 10', 'Box or piece', '840 pcs', 'Rs 25'), ('Pencil HB', 'Box of 12', 'Dozen or piece', '600 pcs', 'Rs 25'),
                        ('Notebook 80 Pages', 'Bundle of 12', 'Dozen or piece', '420 pcs', 'Rs 120'), ('Eraser White', 'Box of 30', 'Piece', '270 pcs', 'Rs 15'),
                        ('A4 Paper 80 gsm', 'Carton of 5 reams', 'Ream', '38 reams', 'Rs 1,850'), ('Glue Stick 21g', 'Box of 24', 'Piece', '96 pcs', 'Rs 90')],
                       'Open a box and sell pieces, stock stays right', 'Sell 3 pens')


def st_moves_phone():
    return phone_list('cpStM', 'Inventory movements', 'This week · Main counter', [
        ('Notebook 120 Pages', 'Cover torn in bundle', 'Damage', '#fef2f2', '#b91c1c'), ('Geometry Box', 'Open piece for display', 'Sample', '#fffbeb', '#92400e'),
        ('Ball Pen Blue', 'Count corrected', 'Adjustment', '#eaf1ff', '#024691'), ('Shelf stock audit', '2,180 pieces counted', 'Matched', '#ecfdf3', '#15803d')], 'Open report')


def st_monitor():
    return counter_monitor('cpMonSt', 'Stationery Counter', 'Scan a barcode or search an item',
                           [(46, 'Item', 'start'), (250, 'Qty / unit', 'start'), (400, 'Rate', 'middle'), (488, 'Amount', 'end')],
                           [('Register A4 200 Pages', '2 pc', '350', '700'), ('Ball Pen Blue', '1 box', '250', '250'),
                            ('Pencil HB', '6 pc', '25', '150'), ('Geometry Box', '1 pc', '450', '450')],
                           ('Ball Pen Blue: 830 pcs left', 'Bought as boxes · sold by box or piece', 'Barcode brings the fixed price'),
                           'Hina Tariq · 0333 4417258', ['Cash', 'Bank', 'Udhaar'], 0, ('Cash received Rs 2,000', 'Change Rs 450'), 'Rs 1,550')


def scene_st_process():
    return five_steps([
        ('Pick products', mini_ui('Catalog · 200+', [('Searched', 'notebook'), ('Ticked', '3 items'), ('Your price', 'Set')], 'Added to shop'), 'Search, tick, add'),
        ('Receive stock', mini_ui('GRN-0712 · Supplier', [('Notebook 80 Pages', '25 bundles'), ('Ball Pen Blue', '40 boxes'), ('A4 Paper', '8 cartons')], 'Stock and cost updated'), 'Stock and cost'),
        ('Quote the school', mini_ui('QT-0219 · Model School', [('Notebook x 300', '36,000'), ('Register x 50', '17,500'), ('Total', '53,500')], 'Sent on WhatsApp', '#eaf1ff', BLUE), 'A4 quotation'),
        ('Bill the order', mini_ui('INV-8104 from QT-0219', [('Notebooks', '300 pcs'), ('Registers', '50 pcs'), ('Paid by', 'Udhaar')], 'On school ledger', '#fffbeb', '#92400e'), 'Sale in one tap'),
        ('Close the day', ui_report("Today's sales", 'Rs 96,800', '214 bills · 1 school order · drawer matched'), 'Cash and profit'),
    ])


SCENES = {
    'uptrendpos-stationery-shop-product-catalog': ('200+ Products Ready', 'green', lambda: g(st_catalog(), 210, 150, 1.0),
        [(60, 770, 'Search, tick, add', '#2F7BD9'), (330, 770, 'Your own price', '#2FA455')]),
    'uptrendpos-stationery-shop-pack-piece-units': ('Box, Dozen and Piece', 'blue', lambda: g(st_units(), 210, 150, 1.0),
        [(60, 770, 'One stock, many units', '#2F7BD9'), (330, 770, 'Stock always right', '#2FA455')]),
    'uptrendpos-stationery-shop-pos-hardware': ('Stationery Shop Hardware', 'teal',
        lambda: hardware_scene(st_monitor, lambda: printer_with('CITY STATIONERS', [('Register A4 x2', '700'), ('Ball Pen box', '250'), ('Pencil + Geo Box', '600')], 'Rs 1,550'),
                               st_moves_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-stationery-shop-pos-process': ('Stationery Shop Day, Step by Step', 'yellow', scene_st_process, [(60, 470, 'All connected', '#2FA455')]),
}

if __name__ == '__main__':
    run(SCENES)
