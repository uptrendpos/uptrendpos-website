"""Artificial Jewellery Shop page images. No brand names, no gold rate (that is the gold jewellery page). Generic item names only.
Bill adds up: Jhumka JE-205 Peacock / Gold tone = 1,250 + Kundan Necklace Set KN-48 Red = 4,800 + Bangles BG-12 Maroon set of 6 = 1,450 -> 7,500.
Udhaar: INV-3118 Rs 12,500 - paid 8,000 - payment 2,500 = 2,000 due.
Variants: 3 designs x 3 colours = 9 items. Barcode labels = Enterprise+ (shown as a feature, tagged on the page).
Run: python3 gen_artificial.py [name ...]"""
from gen_ind import g
from gen_fashion_beauty import mini_ui, ui_report, five_steps, hardware_scene
from gen_shoes_vehicle import variant_tablet, phone_list, counter_monitor, printer_with, t, NAVY, MUTED

BLUE = '#024691'
INK = '#1e293b'
from _daily_common import run


def aj_variants():
    return variant_tablet('cpAjV', 'Variant Generator', '3 x 3 = 9 items', 'Jhumka Earrings JE-205', 'Pick designs and colours, get every item in one go',
                          'Design', ['Peacock', 'Bell', 'Chand'], 'Colour', ['Gold tone', 'Silver tone', 'Red stone'],
                          [('JE-205 Peacock / Gold tone', '205-PK-GT', '24', 'Rs 1,250'), ('JE-205 Peacock / Red stone', '205-PK-RS', '12', 'Rs 1,350'),
                           ('JE-205 Bell / Silver tone', '205-BL-ST', '18', 'Rs 1,150'), ('JE-205 Chand / Gold tone', '205-CH-GT', '9', 'Rs 1,250')],
                          'Each item has its own stock and price', 'Create 9 items')


def aj_tags():
    """A strip of 4 small jewellery tags with barcode, design, colour and price."""
    out = ['<rect x="0" y="0" width="300" height="430" rx="18" fill="#fff" filter="url(#fDrop)"/>', t(150, 34, 'Barcode labels', 14, 800, NAVY, 'middle')]
    y = 56
    for n, c, p in [('JE-205 Jhumka', 'Peacock · Gold tone', 'Rs 1,250'), ('JE-205 Jhumka', 'Bell · Silver tone', 'Rs 1,150'),
                    ('KN-48 Necklace Set', 'Kundan · Red', 'Rs 4,800'), ('BG-12 Bangles', 'Maroon · Set of 6', 'Rs 1,450')]:
        out += [f'<rect x="20" y="{y}" width="260" height="84" rx="10" fill="#fafbfe" stroke="#dbe3ef" stroke-dasharray="4 3"/>',
                t(34, y + 22, n, 11, 700, INK), t(34, y + 40, c, 10.5, 600, MUTED), t(266, y + 22, p, 12, 800, NAVY, 'end')]
        bx = 34
        for k in range(34):
            w = 1.6 if (k * 7) % 5 else 3
            out.append(f'<rect x="{bx}" y="{y+50}" width="{w}" height="24" fill="#111"/>')
            bx += w + 1.8
        y += 92
    return ''.join(out)


def aj_ledger_phone():
    return phone_list('cpAjL', 'Customer ledger', 'Sana Tariq · udhaar khata', [
        ('Sale INV-3118', 'Bridal set and bangles', 'Rs 12,500', '#eaf1ff', BLUE), ('Paid at counter', 'Cash · 2 Nov', '-Rs 8,000', '#ecfdf3', '#15803d'),
        ('Payment · 12 Nov', 'Bank transfer', '-Rs 2,500', '#ecfdf3', '#15803d'), ('Balance due', 'Send statement', 'Rs 2,000', '#fffbeb', '#92400e')], 'Receive payment')


def aj_monitor():
    return counter_monitor('cpMonAj', 'Jewellery Counter', 'Scan tag or search design, colour or code',
                           [(46, 'Item', 'start'), (250, 'Design / colour', 'start'), (400, 'Qty', 'middle'), (488, 'Amount', 'end')],
                           [('Jhumka JE-205', 'Peacock · Gold tone', '1', '1,250'), ('Necklace Set KN-48', 'Kundan · Red', '1', '4,800'),
                            ('Bangles BG-12', 'Maroon · set of 6', '1', '1,450')],
                           ('Scan the small tag, the item comes on the bill', 'Every design and colour has its own stock', 'Bill on WhatsApp as a picture or PDF'),
                           'Walk-in customer', ['Cash', 'Bank', 'Udhaar'], 0, ('Cash Rs 8,000', 'Change Rs 500'), 'Rs 7,500')


def scene_aj_process():
    return five_steps([
        ('Make designs', mini_ui('Variant Generator', [('Item', 'JE-205'), ('Designs', '3'), ('Colours', '3')], '9 items created'), 'Design x colour'),
        ('Receive stock', mini_ui('GRN-0638 · Supplier', [('JE-205 Peacock / GT', '24 pcs'), ('KN-48 Kundan / Red', '6 sets'), ('BG-12 Maroon', '10 sets')], 'Stock and cost updated'), 'Stock in the record'),
        ('Print tags', mini_ui('Barcode labels', [('JE-205 Peacock / GT', 'x24'), ('KN-48 Kundan / Red', 'x6'), ('Price on tag', 'Rs 1,250')], '40 tags ready', '#eaf1ff', BLUE), 'Code, design, price'),
        ('Fast bill', mini_ui('INV-3124', [('Jhumka', '1,250'), ('Necklace set', '4,800'), ('Bangles', '1,450')], 'Total Rs 7,500', '#fffbeb', '#92400e'), 'Scan and save'),
        ('See profit', ui_report("Today's sales", 'Rs 64,300', '38 bills · 2 udhaar payments'), 'Sales, stock and profit'),
    ])


SCENES = {
    'uptrendpos-artificial-jewellery-designs-colours': ('Every Design and Colour', 'blue', lambda: g(aj_variants(), 210, 150, 1.0),
        [(60, 770, 'Design x colour in one go', '#2F7BD9'), (360, 770, 'Own stock for each', '#2FA455')]),
    'uptrendpos-artificial-jewellery-tags-udhaar': ('Small Tags and Udhaar', 'green', lambda: g(aj_tags(), 220, 150, 1.25) + g(aj_ledger_phone(), 680, 140, 1.0),
        [(60, 780, 'Barcode tags with design and price', '#2F7BD9'), (520, 780, 'Udhaar on the ledger', '#2FA455')]),
    'uptrendpos-artificial-jewellery-pos-hardware': ('Jewellery Counter Hardware', 'yellow',
        lambda: hardware_scene(aj_monitor, lambda: printer_with('STYLE JEWELLERS', [('Jhumka JE-205', '1,250'), ('Necklace Set KN-48', '4,800'), ('Bangles BG-12 x6', '1,450')], 'Rs 7,500'),
                               aj_ledger_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-artificial-jewellery-pos-process': ('Jewellery Sale, Step by Step', 'navy', scene_aj_process, [(60, 470, 'All connected', '#2FA455')]),
}

if __name__ == '__main__':
    run(SCENES)
