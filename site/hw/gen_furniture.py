"""Furniture Shop page images. No delivery scheduling or carpenter job order visuals (coming soon). Run: python3 gen_furniture.py [name ...]"""
from gen_ind import g
from gen_fashion_beauty import mini_ui, ui_report, five_steps, hardware_scene
from gen_shoes_vehicle import phone_list, counter_monitor, printer_with, variant_tablet
from _daily_common import run

BLUE = '#024691'


def fn_variants():
    return variant_tablet('cpFnV', 'Variant Generator', 'Finish x Colour', 'Sofa Set SF-501 · 5 Seater', 'Group: Sofa sets · Sale price Rs 1,45,000',
                          'Finishes', ['Walnut', 'Teak', 'White'], 'Fabric', ['Grey', 'Beige'],
                          [('SF-501 Walnut / Grey', '501-WN-GR', '2', 'Rs 1,45,000'), ('SF-501 Walnut / Beige', '501-WN-BG', '1', 'Rs 1,45,000'),
                           ('SF-501 Teak / Grey', '501-TK-GR', '3', 'Rs 1,45,000'), ('SF-501 White / Beige', '501-WH-BG', '0', 'Rs 1,45,000')],
                          '3 finishes x 2 colours = 6 items, each with its own stock', 'Create 6 items')


def fn_quote_phone():
    return phone_list('cpFnQ', 'Quotation QT-0244', 'Bedroom set · Sana Ahmed', [
        ('Bed King BK-210', 'Walnut · 1 piece', 'Rs 1,10,000', '#eaf1ff', BLUE), ('Side Table ST-12 x 2', 'Rs 18,000 each', 'Rs 36,000', '#eaf1ff', BLUE),
        ('Dressing DT-30', 'Walnut · 1 piece', 'Rs 42,000', '#eaf1ff', BLUE), ('Total', 'Valid till 10 Nov', 'Rs 1,88,000', '#ecfdf3', '#15803d')], 'Convert to sale')


def fn_ledger_phone():
    return phone_list('cpFnL', 'Customer ledger', 'Sana Ahmed · bedroom set', [
        ('Advance · 12 Oct', 'Cash · receipt RC-118', '-Rs 50,000', '#ecfdf3', '#15803d'), ('Sale INV-3310', '26 Oct · from QT-0244', 'Rs 1,88,000', '#eaf1ff', BLUE),
        ('Payment · 26 Oct', 'Bank transfer', '-Rs 1,00,000', '#ecfdf3', '#15803d'), ('Balance due', 'Send statement', 'Rs 38,000', '#fffbeb', '#92400e')], 'Receive payment')


def fn_qist_phone():
    return phone_list('cpFnK', 'Qist plan', 'Sofa SF-501 · Rizwan Ali', [
        ('Advance', '20 Oct', 'Rs 45,000', '#ecfdf3', '#15803d'), ('Qist 1 of 5', '20 Nov · paid', 'Rs 20,000', '#ecfdf3', '#15803d'),
        ('Qist 2 of 5', 'Due 20 Dec', 'Rs 20,000', '#fffbeb', '#92400e'), ('Left to pay', 'Guarantor saved', 'Rs 80,000', '#eaf1ff', BLUE)], 'Receive qist')


def fn_monitor():
    return counter_monitor('cpMonFn', 'Furniture Counter', 'Search model name or code, or scan barcode',
                           [(46, 'Item', 'start'), (250, 'Finish / qty', 'start'), (400, 'Rate', 'middle'), (488, 'Amount', 'end')],
                           [('Bed King BK-210', 'Walnut · 1', '1,10,000', '1,10,000'), ('Side Table ST-12', 'Walnut · 2', '18,000', '36,000'),
                            ('Dressing DT-30', 'Walnut · 1', '42,000', '42,000')],
                           ('Converted from quote QT-0244', 'Advance Rs 50,000 already on the ledger', 'Balance shows what is left to pay'),
                           'Sana Ahmed · 0333 7788990', ['Cash', 'Bank', 'Udhaar'], 1, ('Advance paid Rs 50,000', 'On customer ledger'), 'Rs 1,88,000')


def scene_fn_process():
    return five_steps([
        ('Make models', mini_ui('Variant Generator', [('Model', 'SF-501'), ('Finishes', '3'), ('Colours', '2')], '6 items created'), 'Model x finish'),
        ('Quote the customer', mini_ui('Quotation QT-0244', [('Bed King', '1,10,000'), ('Side Tables x 2', '36,000'), ('Dressing', '42,000')], 'Sent on WhatsApp', '#eaf1ff', BLUE), 'A4 quote on WhatsApp'),
        ('Take an advance', mini_ui('Receipt RC-118', [('Sana Ahmed', ''), ('Advance', 'Rs 50,000'), ('Paid by', 'Cash')], 'On customer ledger'), 'On the ledger'),
        ('Convert to sale', mini_ui('INV-3310', [('From', 'QT-0244'), ('Bill', 'Rs 1,88,000'), ('Paid so far', 'Rs 1,50,000')], 'Balance Rs 38,000', '#fffbeb', '#92400e'), 'One tap, balance clear'),
        ('See profit', ui_report("Today's sales", 'Rs 4,85,000', '7 bills · 3 advances · 2 qist payments'), 'Sales, stock and profit'),
    ])


SCENES = {
    'uptrendpos-furniture-shop-models-finishes': ('Model x Finish', 'blue', lambda: g(fn_variants(), 210, 150, 1.0),
        [(60, 770, 'Every finish in one go', '#2F7BD9'), (330, 770, 'Own stock for each', '#2FA455')]),
    'uptrendpos-furniture-shop-quotation-advance': ('Quotes and Advances', 'yellow', lambda: g(fn_quote_phone(), 230, 140, 1.0) + g(fn_ledger_phone(), 680, 140, 1.0),
        [(60, 780, 'A4 quote, then sale', '#2F7BD9'), (440, 780, 'Advance on the ledger', '#2FA455')]),
    'uptrendpos-furniture-shop-pos-hardware': ('Furniture Shop Hardware', 'teal',
        lambda: hardware_scene(fn_monitor, lambda: printer_with('CITY FURNITURE HOUSE', [('Receipt RC-118', ''), ('Sana Ahmed', ''), ('Advance paid', '50,000')], 'Rs 50,000'),
                               fn_qist_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-furniture-shop-pos-process': ('Furniture Sale, Step by Step', 'navy', scene_fn_process, [(60, 470, 'All connected', '#2FA455')]),
}

if __name__ == '__main__':
    run(SCENES)
