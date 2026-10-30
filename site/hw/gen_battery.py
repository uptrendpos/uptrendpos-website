"""Battery Shop page images. No brand names, no serial / warranty-lookup visuals (only a warranty NOTE on the sale), trade-in not shown.
Bills add up: CB-50 Wet 22,000 + water 2 x 150 + terminals 450 = 22,750. Qist: 2 x 48,000 = 96,000; advance 30,000; 6 x 11,000.
Run: python3 gen_battery.py [name ...]"""
from gen_ind import g
from gen_fashion_beauty import mini_ui, ui_report, five_steps, hardware_scene
from gen_shoes_vehicle import phone_list, phone_kv, counter_monitor, printer_with, variant_tablet
from _daily_common import run

BLUE = '#024691'


def bt_variants():
    return variant_tablet('cpBtV', 'Variant Generator', 'Ampere x Type', 'Car Battery CB · 12 volt', 'Group: Car batteries · Sold by the piece',
                          'Ampere', ['35 Ah', '50 Ah', '70 Ah'], 'Types', ['Wet', 'Dry'],
                          [('CB 35 Ah / Wet', 'CB-35-W', '8', 'Rs 16,500'), ('CB 50 Ah / Wet', 'CB-50-W', '10', 'Rs 22,000'),
                           ('CB 50 Ah / Dry', 'CB-50-D', '4', 'Rs 26,500'), ('CB 70 Ah / Dry', 'CB-70-D', '0', 'Rs 34,500')],
                          '3 sizes x 2 types = 6 items, each with its own stock', 'Create 6 items')


def bt_warranty_phone():
    return phone_kv('cpBtW', 'Sale INV-3318', 'Hamza Raza · 0321 5566778', 'Warranty note on bill', '12 months · written at the sale',
                    [('Item', 'CB 50 Ah / Wet'), ('Amount', 'Rs 22,000'), ('Paid', 'Cash · 30 Oct'), ('Bill', 'Sent on WhatsApp'), ('Sold by', 'Counter 1 · Asif')],
                    'Send bill again')


def bt_qist_phone():
    return phone_list('cpBtK', 'Qist plan', 'UPS battery TB-200 x 2 · Sana Tariq', [
        ('Advance', '1 Oct', 'Rs 30,000', '#ecfdf3', '#15803d'), ('Qist 1 of 6', '1 Nov · paid', 'Rs 11,000', '#ecfdf3', '#15803d'),
        ('Qist 2 of 6', 'Due 1 Dec', 'Rs 11,000', '#fffbeb', '#92400e'), ('Left to pay', 'Guarantor saved', 'Rs 55,000', '#eaf1ff', BLUE)], 'Receive qist')


def bt_monitor():
    return counter_monitor('cpMonBt', 'Battery Counter', 'Search ampere, type or scan barcode',
                           [(46, 'Item', 'start'), (250, 'Qty / unit', 'start'), (400, 'Rate', 'middle'), (488, 'Amount', 'end')],
                           [('CB 50 Ah / Wet', '1 piece', '22,000', '22,000'), ('Battery Water 1 L', '2 bottle', '150', '300'),
                            ('Terminal Set', '1 piece', '450', '450')],
                           ('Warranty note: 12 months', 'Written on the sale and on the bill', 'Udhaar for regular workshops'),
                           'Bilal Autos · 0301 7788990', ['Cash', 'Bank', 'Udhaar'], 2, ('Paid now Rs 10,000', 'Rs 12,750 on the ledger'), 'Rs 22,750')


def scene_bt_process():
    return five_steps([
        ('Make items', mini_ui('Variant Generator', [('Battery', 'CB 12V'), ('Ampere', '35 50 70'), ('Types', 'Wet Dry')], '6 items created'), 'Ampere x type'),
        ('Receive stock', mini_ui('GRN-0518 · Distributor', [('CB 50 Ah / Wet', '10 pcs'), ('TB-200 UPS', '6 pcs'), ('Water 1 L', '2 ctn')], 'Stock and cost updated'), 'Stock in the record'),
        ('Make the bill', mini_ui('INV-3318', [('CB 50 Ah / Wet', '22,000'), ('Water 2 x 150', '300'), ('Terminals', '450')], 'Warranty note: 12 months', '#eaf1ff', BLUE), 'Warranty note'),
        ('Udhaar or qist', mini_ui('Bilal Autos', [('Bill', '22,750'), ('Paid now', '10,000'), ('On ledger', '12,750')], 'Statement on WhatsApp', '#fffbeb', '#92400e'), 'On the ledger'),
        ('See profit', ui_report("Today's sales", 'Rs 1,86,400', '14 bills · 3 udhaar payments · 1 qist'), 'Sales, stock and profit'),
    ])


SCENES = {
    'uptrendpos-battery-shop-ampere-types': ('Ampere x Type', 'blue', lambda: g(bt_variants(), 210, 150, 1.0),
        [(60, 770, 'Every size in one go', '#2F7BD9'), (330, 770, 'Own stock and price', '#2FA455')]),
    'uptrendpos-battery-shop-warranty-qist': ('Warranty Note and Qist', 'yellow', lambda: g(bt_warranty_phone(), 230, 140, 1.0) + g(bt_qist_phone(), 680, 140, 1.0),
        [(60, 780, 'Warranty on the bill', '#2F7BD9'), (440, 780, 'Qist with guarantor', '#2FA455')]),
    'uptrendpos-battery-shop-pos-hardware': ('Battery Shop Hardware', 'teal',
        lambda: hardware_scene(bt_monitor, lambda: printer_with('CITY BATTERY HOUSE', [('CB 50 Ah / Wet', '22,000'), ('Battery Water 1 L x2', '300'), ('Terminal Set', '450')], 'Rs 22,750'),
                               bt_qist_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-battery-shop-pos-process': ('Battery Sale, Step by Step', 'navy', scene_bt_process, [(60, 470, 'All connected', '#2FA455')]),
}

if __name__ == '__main__':
    run(SCENES)
