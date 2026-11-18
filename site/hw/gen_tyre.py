"""Tyre Shop page images. No brand names, no serial / warranty-lookup visuals (only a warranty NOTE on the sale), trade-in not shown.
Bills add up: CT 185/65 R15 4 x 14,500 = 58,000 + valves 4 x 150 = 600 + polish 350 = 58,950; paid 30,000, ledger 28,950.
Qist: 6 truck tyres x 62,000 = 3,72,000; advance 1,20,000; 6 x 42,000 = 2,52,000; after qist 1 left 2,10,000.
Run: python3 gen_tyre.py [name ...]"""
from gen_ind import g
from gen_fashion_beauty import mini_ui, ui_report, five_steps, hardware_scene
from gen_shoes_vehicle import phone_list, phone_kv, counter_monitor, printer_with, variant_tablet
from _daily_common import run

BLUE = '#024691'


def ty_variants():
    return variant_tablet('cpTyV', 'Variant Generator', 'Size x Rim', 'Car Tyre CT · Radial tubeless', 'Group: Car tyres · Sold by the piece',
                          'Size', ['175/70', '185/65', '195/65'], 'Rim', ['R14', 'R15'],
                          [('CT 175/70 R14', 'CT-17570-14', '12', 'Rs 12,800'), ('CT 185/65 R14', 'CT-18565-14', '0', 'Rs 13,900'),
                           ('CT 185/65 R15', 'CT-18565-15', '16', 'Rs 14,500'), ('CT 195/65 R15', 'CT-19565-15', '8', 'Rs 16,200')],
                          '3 sizes x 2 rims = 6 items, each with its own stock', 'Create 6 items')


def ty_warranty_phone():
    return phone_kv('cpTyW', 'Sale INV-4127', 'Usman Ali · 0333 4455667', 'Warranty note on bill', 'Written at the sale',
                    [('Item', 'CT 185/65 R15 x 4'), ('Amount', 'Rs 58,950'), ('Paid', 'Cash · 18 Nov'), ('Bill', 'Sent on WhatsApp'), ('Sold by', 'Counter 1 · Kashif')],
                    'Send bill again')


def ty_qist_phone():
    return phone_list('cpTyK', 'Qist plan', 'Truck tyre TT-1020 x 6 · Raza Goods', [
        ('Advance', '1 Oct', 'Rs 1,20,000', '#ecfdf3', '#15803d'), ('Qist 1 of 6', '1 Nov · paid', 'Rs 42,000', '#ecfdf3', '#15803d'),
        ('Qist 2 of 6', 'Due 1 Dec', 'Rs 42,000', '#fffbeb', '#92400e'), ('Left to pay', 'Guarantor saved', 'Rs 2,10,000', '#eaf1ff', BLUE)], 'Receive qist')


def ty_monitor():
    return counter_monitor('cpMonTy', 'Tyre Counter', 'Search size, rim or scan barcode',
                           [(46, 'Item', 'start'), (250, 'Qty / unit', 'start'), (400, 'Rate', 'middle'), (488, 'Amount', 'end')],
                           [('CT 185/65 R15', '4 piece', '14,500', '58,000'), ('Tubeless Valve', '4 piece', '150', '600'),
                            ('Tyre Polish', '1 bottle', '350', '350')],
                           ('Warranty note on the sale', 'Printed on the bill and on WhatsApp', 'Udhaar for regular transporters'),
                           'Raza Goods · 0300 6677889', ['Cash', 'Bank', 'Udhaar'], 2, ('Paid now Rs 30,000', 'Rs 28,950 on the ledger'), 'Rs 58,950')


def scene_ty_process():
    return five_steps([
        ('Make items', mini_ui('Variant Generator', [('Tyre', 'CT Radial'), ('Size', '175 185 195'), ('Rim', 'R14 R15')], '6 items created'), 'Size x rim'),
        ('Receive stock', mini_ui('GRN-0742 · Distributor', [('CT 185/65 R15', '16 pcs'), ('TT-1020 Truck', '12 pcs'), ('Valves', '2 box')], 'Stock and cost updated'), 'Stock in the record'),
        ('Make the bill', mini_ui('INV-4127', [('Tyres 4 x 14,500', '58,000'), ('Valves 4 x 150', '600'), ('Polish', '350')], 'Warranty note on the sale', '#eaf1ff', BLUE), 'Warranty note'),
        ('Udhaar or qist', mini_ui('Raza Goods', [('Bill', '58,950'), ('Paid now', '30,000'), ('On ledger', '28,950')], 'Statement on WhatsApp', '#fffbeb', '#92400e'), 'On the ledger'),
        ('See profit', ui_report("Today's sales", 'Rs 2,64,300', '19 bills · 4 udhaar payments · 1 qist'), 'Sales, stock and profit'),
    ])


SCENES = {
    'uptrendpos-tyre-shop-size-rim': ('Size x Rim', 'blue', lambda: g(ty_variants(), 210, 150, 1.0),
        [(60, 770, 'Every size in one go', '#2F7BD9'), (330, 770, 'Own stock and price', '#2FA455')]),
    'uptrendpos-tyre-shop-warranty-qist': ('Warranty Note and Qist', 'yellow', lambda: g(ty_warranty_phone(), 230, 140, 1.0) + g(ty_qist_phone(), 680, 140, 1.0),
        [(60, 780, 'Warranty on the bill', '#2F7BD9'), (440, 780, 'Qist with guarantor', '#2FA455')]),
    'uptrendpos-tyre-shop-pos-hardware': ('Tyre Shop Hardware', 'teal',
        lambda: hardware_scene(ty_monitor, lambda: printer_with('CITY TYRE HOUSE', [('CT 185/65 R15 x4', '58,000'), ('Tubeless Valve x4', '600'), ('Tyre Polish', '350')], 'Rs 58,950'),
                               ty_qist_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-tyre-shop-pos-process': ('Tyre Sale, Step by Step', 'navy', scene_ty_process, [(60, 470, 'All connected', '#2FA455')]),
}

if __name__ == '__main__':
    run(SCENES)
