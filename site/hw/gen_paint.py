"""Paint Store page images. No tinting machine or mixing formula visuals. Run: python3 gen_paint.py [name ...]"""
from gen_ind import g
from gen_fashion_beauty import mini_ui, ui_report, five_steps, hardware_scene
from gen_shoes_vehicle import phone_list, counter_monitor, printer_with, variant_tablet
from _daily_common import run

BLUE = '#024691'


def pt_variants():
    return variant_tablet('cpPtV', 'Variant Generator', 'Shade x Pack size', 'Emulsion EM-20 · Interior Matt', 'Group: Wall paint · Gallon Rs 3,400 · Drum Rs 15,200',
                          'Shades', ['Off White', 'Ivory', 'Sky Blue', 'Grey'], 'Pack sizes', ['Quarter', 'Gallon', 'Drum'],
                          [('EM-20 Off White / Gallon', 'EM20-OW-G', '24', 'Rs 3,400'), ('EM-20 Off White / Drum', 'EM20-OW-D', '6', 'Rs 15,200'),
                           ('EM-20 Sky Blue / Quarter', 'EM20-SB-Q', '30', 'Rs 1,050'), ('EM-20 Grey / Gallon', 'EM20-GR-G', '3', 'Rs 3,400')],
                          '4 shades x 3 pack sizes = 12 items, each with its own stock', 'Create 12 items')


def pt_quote_phone():
    return phone_list('cpPtQ', 'Quotation QT-0418', 'House paint job · Javed Painter', [
        ('Emulsion x 6 drums', 'Rs 15,200 each', 'Rs 91,200', '#eaf1ff', BLUE), ('Enamel x 4 gallons', 'Rs 3,900 each', 'Rs 15,600', '#eaf1ff', BLUE),
        ('Wall Putty x 10 bags', 'Rs 1,100 each', 'Rs 11,000', '#eaf1ff', BLUE), ('Total', 'Valid till 05 Nov', 'Rs 1,17,800', '#ecfdf3', '#15803d')], 'Convert to sale')


def pt_udhaar_phone():
    return phone_list('cpPtU', 'Painter udhaar', 'Khata of painters and contractors', [
        ('Javed Painter', 'Paid 4 days ago', 'Rs 34,500', '#eaf1ff', BLUE), ('Akram Painter', 'Paid 10 days ago', 'Rs 12,800', '#eaf1ff', BLUE),
        ('Raza Contractor', '28 days · follow up', 'Rs 56,200', '#fffbeb', '#92400e'), ('Total to collect', '3 customers', 'Rs 1,03,500', '#ecfdf3', '#15803d')], 'Send statement')


def pt_monitor():
    return counter_monitor('cpMonPt', 'Paint Counter', 'Search paint by name, shade or scan barcode',
                           [(46, 'Item', 'start'), (250, 'Qty / unit', 'start'), (400, 'Rate', 'middle'), (488, 'Amount', 'end')],
                           [('EM-20 Off White', '2 gallon', '3,400', '6,800'), ('Enamel EN-10 White', '1 gallon', '3,900', '3,900'),
                            ('Wall Putty 20 kg', '2 bag', '1,100', '2,200'), ('Paint Brush 4"', '3 piece', '350', '1,050')],
                           ('EM-20 Off White Gallon: 22 left', 'Shade x pack size made with the variant generator', 'Udhaar for regular painters'),
                           'Javed Painter · 0345 2233445', ['Cash', 'Bank', 'Udhaar'], 2, ('Udhaar balance Rs 34,500', 'Regular painter'), 'Rs 13,950')


def scene_pt_process():
    return five_steps([
        ('Make shades', mini_ui('Variant Generator', [('Paint', 'EM-20'), ('Shades', '4'), ('Pack sizes', 'Q · G · D')], '12 items created'), 'Shade x pack size'),
        ('Receive stock', mini_ui('GRN · Lahore Paints', [('EM-20 Off White', '6 drums'), ('EM-20 Grey', '12 gallons'), ('Enamel White', '8 gallons')], 'Average cost updated'), 'Drums, gallons, quarters'),
        ('Quote a painter', mini_ui('Quotation QT-0418', [('Emulsion 6 drums', '91,200'), ('Enamel 4 gallons', '15,600'), ('Putty 10 bags', '11,000')], 'Sent on WhatsApp', '#eaf1ff', BLUE), 'A4 quote, then sale'),
        ('Sell and udhaar', mini_ui('Today', [('Javed Painter', 'Rs 34,500 due'), ('Dented tin', '1 pc damage'), ('Returns', '1')], 'Stock stays right', '#fffbeb', '#92400e'), 'Painters on credit'),
        ('See profit', ui_report("Today's sales", 'Rs 1,64,300', '52 bills · 38 gallons · 9 drums'), 'Sales, stock and profit'),
    ])


SCENES = {
    'uptrendpos-paint-store-shades-pack-sizes': ('Shade x Pack Size', 'blue', lambda: g(pt_variants(), 210, 150, 1.0),
        [(60, 770, 'Every shade in one go', '#2F7BD9'), (330, 770, 'Quarter, gallon, drum', '#2FA455')]),
    'uptrendpos-paint-store-quotation-udhaar': ('Painter Quotes and Udhaar', 'yellow', lambda: g(pt_quote_phone(), 230, 140, 1.0) + g(pt_udhaar_phone(), 680, 140, 1.0),
        [(60, 780, 'A4 quote for painters', '#2F7BD9'), (440, 780, 'Udhaar khata', '#2FA455')]),
    'uptrendpos-paint-store-pos-hardware': ('Paint Shop Hardware', 'teal',
        lambda: hardware_scene(pt_monitor, lambda: printer_with('CITY PAINT HOUSE', [('Emulsion Gallon x2', '6,800'), ('Enamel Gallon', '3,900'), ('Wall Putty x2', '2,200')], 'Rs 12,900'),
                               pt_udhaar_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-paint-store-pos-process': ('Paint Sale, Step by Step', 'navy', scene_pt_process, [(60, 470, 'All connected', '#2FA455')]),
}

if __name__ == '__main__':
    run(SCENES)
