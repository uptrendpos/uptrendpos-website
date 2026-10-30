"""Jewellery & Gold Shop page images. Gold rate shown only as the hub wording (no rate breakdown); no purity, old gold or hallmark visuals.
Amounts use one consistent hidden basis (weight x Rs 32,000 per gram + making) so every bill adds up. Run: python3 gen_jewellery.py [name ...]"""
from gen_ind import g
from gen_fashion_beauty import mini_ui, ui_report, five_steps, hardware_scene
from gen_shoes_vehicle import phone_list, counter_monitor, printer_with, variant_tablet
from _daily_common import run

BLUE = '#024691'


def jw_variants():
    s = variant_tablet('cpJwV', 'Variant Generator', 'Design x Size', 'Gold Ring RG-108 · Ladies ring', 'Group: Rings · Weight in grams',
                       'Designs', ['Leaf', 'Flower', 'Plain'], 'Sizes', ['12', '14', '16'],
                       [('RG-108 Leaf / 14', '108-LF-14', '2', '4.20 g'), ('RG-108 Flower / 12', '108-FL-12', '1', '3.90 g'),
                        ('RG-108 Plain / 16', '108-PL-16', '3', '4.60 g'), ('RG-108 Leaf / 16', '108-LF-16', '0', '4.45 g')],
                       '3 designs x 3 sizes = 9 items, each with its own stock', 'Create 9 items')
    return s.replace('>Price</text>', '>Weight</text>')


def jw_ledger_phone():
    return phone_list('cpJwL', 'Customer ledger', 'Ayesha Khan · udhaar khata', [
        ('Sale INV-2105', 'Ring and earrings', 'Rs 2,39,900', '#eaf1ff', BLUE), ('Paid at counter', 'Cash · 30 Oct', '-Rs 1,50,000', '#ecfdf3', '#15803d'),
        ('Payment · 5 Nov', 'Bank transfer', '-Rs 50,000', '#ecfdf3', '#15803d'), ('Balance due', 'Send statement', 'Rs 39,900', '#fffbeb', '#92400e')], 'Receive payment')


def jw_qist_phone():
    return phone_list('cpJwK', 'Qist plan', 'Bridal set BS-22 · Nadia Iqbal', [
        ('Advance', '1 Oct', 'Rs 2,00,000', '#ecfdf3', '#15803d'), ('Qist 1 of 6', '1 Nov · paid', 'Rs 50,000', '#ecfdf3', '#15803d'),
        ('Qist 2 of 6', 'Due 1 Dec', 'Rs 50,000', '#fffbeb', '#92400e'), ('Left to pay', 'Guarantor saved', 'Rs 2,50,000', '#eaf1ff', BLUE)], 'Receive qist')


def jw_monitor():
    return counter_monitor('cpMonJw', 'Jewellery Counter', 'Search design name or code, or scan tag',
                           [(46, 'Item', 'start'), (250, 'Design / weight', 'start'), (400, 'Making', 'middle'), (488, 'Amount', 'end')],
                           [('Gold Ring RG-108', 'Leaf / 14 · 4.20 g', '3,500', '1,37,900'), ('Earrings ER-31', 'Flower · 3.10 g', '2,800', '1,02,000')],
                           ('Daily gold rate and making charge on the bill', 'Weights in grams on every line', 'Bill on WhatsApp as a picture or PDF'),
                           'Ayesha Khan · 0300 4455667', ['Cash', 'Bank', 'Udhaar'], 0, ('Paid now Rs 1,50,000', 'Rs 89,900 on the ledger'), 'Rs 2,39,900')


def scene_jw_process():
    return five_steps([
        ('Make designs', mini_ui('Variant Generator', [('Piece', 'RG-108'), ('Designs', '3'), ('Sizes', '12 14 16')], '9 items created'), 'Design x size'),
        ('Receive stock', mini_ui('GRN-0412 · Supplier', [('RG-108 Leaf / 14', '2 pcs'), ('ER-31 Flower', '4 pcs'), ('Weights', 'in grams')], 'Stock and cost updated'), 'Stock in the record'),
        ('Make the bill', mini_ui('INV-2105', [('Ring 4.20 g', '1,37,900'), ('Earrings 3.10 g', '1,02,000'), ('Making incl.', '6,300')], 'Sent on WhatsApp', '#eaf1ff', BLUE), 'Gold rate and making'),
        ('Udhaar or qist', mini_ui('Ayesha Khan', [('Bill', '2,39,900'), ('Paid now', '1,50,000'), ('On ledger', '89,900')], 'Balance clear', '#fffbeb', '#92400e'), 'On the ledger'),
        ('See profit', ui_report("Today's sales", 'Rs 6,42,500', '5 bills · 2 udhaar payments · 1 qist'), 'Sales, stock and profit'),
    ])


SCENES = {
    'uptrendpos-jewellery-shop-designs-sizes': ('Design x Size', 'blue', lambda: g(jw_variants(), 210, 150, 1.0),
        [(60, 770, 'Every design in one go', '#2F7BD9'), (330, 770, 'Weights in grams', '#2FA455')]),
    'uptrendpos-jewellery-shop-udhaar-qist': ('Udhaar and Qist', 'yellow', lambda: g(jw_ledger_phone(), 230, 140, 1.0) + g(jw_qist_phone(), 680, 140, 1.0),
        [(60, 780, 'Udhaar on the ledger', '#2F7BD9'), (440, 780, 'Qist with guarantor', '#2FA455')]),
    'uptrendpos-jewellery-shop-pos-hardware': ('Jewellery Shop Hardware', 'teal',
        lambda: hardware_scene(jw_monitor, lambda: printer_with('CITY JEWELLERS', [('Ring RG-108 4.20 g', '1,37,900'), ('Earrings ER-31 3.10 g', '1,02,000'), ('Making incl.', '6,300')], 'Rs 2,39,900'),
                               jw_qist_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-jewellery-shop-pos-process': ('Jewellery Sale, Step by Step', 'navy', scene_jw_process, [(60, 470, 'All connected', '#2FA455')]),
}

if __name__ == '__main__':
    run(SCENES)
