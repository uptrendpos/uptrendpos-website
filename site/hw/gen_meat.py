"""Poultry, Meat & Seafood page images. No brand names, no weighing-scale cable visuals (weight is typed in), no freshness or health claims.
Bill adds up: Chicken 1.25 kg x 640 = 800 + Boneless 0.75 kg x 1,100 = 825 + Mutton 1 kg x 2,400 = 2,400 -> 4,025; paid 2,000, 2,025 udhaar.
Ledger: 6,400 - 5,000 + 2,025 = 3,425. Cash session: 5,000 + 48,600 + 5,000 = 58,600.
Run: python3 gen_meat.py [name ...]"""
from gen_ind import g
from gen_fashion_beauty import mini_ui, ui_report, five_steps, hardware_scene
from gen_shoes_vehicle import phone_list, phone_kv, counter_monitor, printer_with
from gen_electrical_baby import unit_tablet
from _daily_common import run

BLUE = '#024691'


def mt_units():
    return unit_tablet('cpMtU', 'Units and Rates', 'Kg · Gram · Pack', 'Sold by weight, stock in kg', 'Type the weight from your scale, the bill does the rest',
                       [('Chicken Whole', 'Kg', 'Kg or gram', '86.5 kg', 'Rs 640 /kg'), ('Chicken Boneless', 'Kg', 'Kg or gram', '24.25 kg', 'Rs 1,100 /kg'),
                        ('Mutton', 'Kg', 'Kg or gram', '38 kg', 'Rs 2,400 /kg'), ('Beef Mince', 'Kg', 'Kg or gram', '19.5 kg', 'Rs 1,250 /kg'),
                        ('Fish Rahu', 'Kg', 'Kg or gram', '22 kg', 'Rs 900 /kg'), ('Frozen Nuggets 1 kg', 'Carton of 12', 'Pack', '30 packs', 'Rs 1,450')],
                       'Stock drops by the exact weight on every sale', 'Sell 750 g boneless')


def mt_ledger_phone():
    return phone_list('cpMtL', 'Customer ledger', 'Al Noor Hotel · 0300 4455667', [
        ('Bill INV-2214', '30 Oct · udhaar', 'Rs 6,400', '#fffbeb', '#92400e'), ('Payment', '31 Oct · cash', 'Rs 5,000', '#ecfdf3', '#15803d'),
        ('Bill INV-2291', '1 Nov · part udhaar', 'Rs 2,025', '#fffbeb', '#92400e'), ('Balance due', 'Statement on WhatsApp', 'Rs 3,425', '#eaf1ff', BLUE)], 'Send statement')


def mt_session_phone():
    return phone_kv('cpMtS', 'Cash session', 'Morning shift · Counter 1 · Imran', 'Session closed', '8:00 am to 4:00 pm',
                    [('Opening cash', 'Rs 5,000'), ('Cash sales', 'Rs 48,600'), ('Udhaar received', 'Rs 5,000'), ('Expected in drawer', 'Rs 58,600'), ('Counted', 'Rs 58,600 · matched')],
                    'Send day report')


def mt_monitor():
    return counter_monitor('cpMonMt', 'Meat Counter', 'Search chicken, mutton, beef or fish',
                           [(46, 'Item', 'start'), (250, 'Weight', 'start'), (400, 'Rate /kg', 'middle'), (488, 'Amount', 'end')],
                           [('Chicken Whole', '1.25 kg', '640', '800'), ('Chicken Boneless', '750 g', '1,100', '825'),
                            ('Mutton', '1 kg', '2,400', '2,400')],
                           ('Weight typed from the scale', 'Amount = weight x rate per kg', 'Udhaar for regular hotels'),
                           'Al Noor Hotel · 0300 4455667', ['Cash', 'Bank', 'Udhaar'], 2, ('Paid now Rs 2,000', 'Rs 2,025 on the ledger'), 'Rs 4,025')


def scene_mt_process():
    return five_steps([
        ('Open the shift', mini_ui('Cash session', [('Shift', 'Morning'), ('Cashier', 'Imran'), ('Opening', 'Rs 5,000')], 'Session open'), 'Drawer counted'),
        ('Receive stock', mini_ui('GRN-0742 · Supplier', [('Chicken Whole', '120 kg'), ('Mutton', '40 kg'), ('Nuggets 1 kg', '2 ctn')], 'Stock and cost updated'), 'Stock in kg'),
        ('Bill by weight', mini_ui('INV-2291', [('Chicken 1.25 kg', '800'), ('Boneless 750 g', '825'), ('Mutton 1 kg', '2,400')], 'Total Rs 4,025', '#eaf1ff', BLUE), 'Weight x rate'),
        ('Udhaar, damage', mini_ui('Al Noor Hotel', [('Bill', '4,025'), ('Paid now', '2,000'), ('On ledger', '2,025')], 'Damage: 3.5 kg spoiled', '#fffbeb', '#92400e'), 'On record'),
        ('Close the day', ui_report("Today's sales", 'Rs 96,800', '142 bills · 2 udhaar payments · 1 damage entry'), 'Cash and profit'),
    ])


SCENES = {
    'uptrendpos-meat-shop-kg-gram-units': ('Kg, Gram and Rate per Kg', 'blue', lambda: g(mt_units(), 210, 150, 1.0),
        [(60, 770, 'Bill by weight', '#2F7BD9'), (330, 770, 'Stock in kg', '#2FA455')]),
    'uptrendpos-meat-shop-udhaar-cash': ('Udhaar and Cash Sessions', 'yellow', lambda: g(mt_ledger_phone(), 230, 140, 1.0) + g(mt_session_phone(), 680, 140, 1.0),
        [(60, 780, 'Udhaar for hotels', '#2F7BD9'), (440, 780, 'Cash checked per shift', '#2FA455')]),
    'uptrendpos-meat-shop-pos-hardware': ('Meat Shop Hardware', 'teal',
        lambda: hardware_scene(mt_monitor, lambda: printer_with('MADINA CHICKEN AND MEAT', [('Chicken 1.25 kg', '800'), ('Boneless 750 g', '825'), ('Mutton 1 kg', '2,400')], 'Rs 4,025'),
                               mt_session_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-meat-shop-pos-process': ('Meat Shop Day, Step by Step', 'navy', scene_mt_process, [(60, 470, 'All connected', '#2FA455')]),
}

if __name__ == '__main__':
    run(SCENES)
