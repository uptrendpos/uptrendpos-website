"""Vape & Pan Shop page images. No brand names, no health visuals, nothing aimed at minors.
Bills add up: counter = Pod Cartridge 1 pack x 1,200 = 1,200 + Coil 0.8 ohm 2 piece x 350 = 700 + E-Liquid Mint 30 ml 1 bottle x 1,800 = 1,800 + Sweet Supari 3 piece x 20 = 60 = 3,760.
Receipt (first three lines) = 1,200 + 700 + 1,800 = 3,700.
Cash session = opening 5,000 + cash sales 48,250 - expenses 1,500 = 51,750 expected; counted 51,750.
Run: python3 gen_vape.py [name ...]"""
from gen_ind import g
from gen_fashion_beauty import mini_ui, ui_report, five_steps, hardware_scene
from gen_shoes_vehicle import phone_list, counter_monitor, printer_with, variant_tablet
from gen_electrical_baby import unit_tablet
from _daily_common import run

BLUE = '#024691'


def vp_units():
    return unit_tablet('cpVpU', 'Units and Packing', 'Pack · Piece · Box · Bottle', 'One item, sold the way customers buy', 'Buy by the pack, box or crate, sell by the pack or piece',
                       [('Coil 0.8 ohm', 'Pack of 5', 'Pack or piece', '64 pieces', 'Rs 350'), ('Pod Cartridge', 'Box of 10 packs', 'Pack or piece', '38 packs', 'Rs 1,200'),
                        ('E-Liquid Mint 30 ml', 'Carton of 10', 'Bottle', '22 bottles', 'Rs 1,800'), ('Sweet Supari', 'Box of 24', 'Box or piece', '180 pieces', 'Rs 20'),
                        ('Mouth Freshener', 'Box of 12', 'Box or piece', '96 pieces', 'Rs 30'), ('Cold Drink 500 ml', 'Crate of 24', 'Crate or bottle', '72 bottles', 'Rs 120')],
                       'Sell a pack or a piece, stock stays right', 'Sell 2 coils')


def vp_variants():
    return variant_tablet('cpVpV', 'Variant Generator', '4 x 3 = 12 items', 'E-Liquid Range', 'Pick flavours and bottle sizes, get every item in one go',
                          'Flavour', ['Mint', 'Menthol', 'Coffee', 'Classic'], 'Bottle', ['30 ml', '60 ml', '100 ml'],
                          [('Mint 30 ml', 'MNT-30', '22', 'Rs 1,800'), ('Mint 60 ml', 'MNT-60', '14', 'Rs 3,200'),
                           ('Mint 100 ml', 'MNT-100', '6', 'Rs 4,900'), ('Menthol 30 ml', 'MEN-30', '18', 'Rs 1,800')],
                          'Each item has its own stock and price', 'Create 12 items')


def vp_cash_phone():
    return phone_list('cpVpC', 'Cash session', 'Evening shift · Bilal', [
        ('Opening cash', '6:00 pm', 'Rs 5,000', '#eaf1ff', BLUE), ('Cash sales', '64 bills', 'Rs 48,250', '#ecfdf3', '#15803d'),
        ('Expenses', 'Tea and ice', 'Rs 1,500', '#fffbeb', '#92400e'), ('Expected in drawer', 'Counted Rs 51,750', 'Rs 51,750', '#eaf1ff', BLUE)], 'Close session')


def vp_monitor():
    return counter_monitor('cpMonVp', 'Vape Counter', 'Scan barcode or search item, flavour',
                           [(46, 'Item', 'start'), (250, 'Qty / unit', 'start'), (400, 'Rate', 'middle'), (488, 'Amount', 'end')],
                           [('Pod Cartridge', '1 pack', '1,200', '1,200'), ('Coil 0.8 ohm', '2 piece', '350', '700'),
                            ('E-Liquid Mint 30 ml', '1 bottle', '1,800', '1,800'), ('Sweet Supari', '3 piece', '20', '60')],
                           ('Pack and piece on one bill', 'Mint 100 ml is low: 6 left', 'Cash session: evening shift'),
                           'Walk-in customer', ['Cash', 'Bank', 'Udhaar'], 0, ('Cashier: Bilal', 'Evening shift'), 'Rs 3,760')


def scene_vp_process():
    return five_steps([
        ('Receive stock', mini_ui('GRN-0412 · Supplier', [('Coils 0.8 ohm', '20 packs'), ('E-Liquid Mint', '2 ctn'), ('Sweet Supari', '6 box')], 'Stock and cost updated'), 'Packs, boxes, bottles'),
        ('Open the shift', mini_ui('Cash session', [('Cashier', 'Bilal'), ('Shift', 'Evening'), ('Opening cash', '5,000')], 'Session open', '#eaf1ff', BLUE), 'Drawer per shift'),
        ('Bill the customer', mini_ui('INV-3318', [('Pod Cartridge x 1', '1,200'), ('Coil x 2 pieces', '700'), ('E-Liquid Mint x 1', '1,800')], 'Sent on WhatsApp', '#eaf1ff', BLUE), 'Fast counter bill'),
        ('Close the shift', mini_ui('Close session', [('Expected', '51,750'), ('Counted', '51,750'), ('Difference', '0')], 'Drawer matches', '#ecfdf3', '#15803d'), 'No cash surprise'),
        ('See profit', ui_report("Today's sales", 'Rs 92,640', '118 bills · 2 shifts · 1 return'), 'Sales, stock and profit'),
    ])


SCENES = {
    'uptrendpos-vape-shop-pack-piece-units': ('Pack, Piece, Box, Bottle', 'blue', lambda: g(vp_units(), 210, 150, 1.0),
        [(60, 770, 'Pack or piece', '#2F7BD9'), (380, 770, 'Box or piece', '#2FA455')]),
    'uptrendpos-vape-shop-flavour-variants': ('Flavours and Sizes', 'yellow', lambda: g(vp_variants(), 210, 150, 1.0),
        [(60, 770, 'Flavour x bottle size', '#F59E0B'), (420, 770, 'Own stock and price', '#2FA455')]),
    'uptrendpos-vape-shop-pos-hardware': ('Vape Shop Hardware', 'teal',
        lambda: hardware_scene(vp_monitor, lambda: printer_with('CITY VAPE AND PAN', [('Pod Cartridge x1', '1,200'), ('Coil x2 piece', '700'), ('E-Liquid Mint x1', '1,800')], 'Rs 3,700'),
                               vp_cash_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-vape-shop-pos-process': ('Vape Shop, Step by Step', 'navy', scene_vp_process, [(60, 470, 'All connected', '#2FA455')]),
}

if __name__ == '__main__':
    run(SCENES)
