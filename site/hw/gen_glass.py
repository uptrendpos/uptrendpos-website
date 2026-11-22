"""Glass & Aluminium Shop page images. No brand names, no size calculator or cutting-plan visuals (square feet typed on the bill).
Bills add up: counter = glass 24 sq ft x 180 = 4,320 + aluminium 60 ft x 220 = 13,200 + handles 6 x 350 = 2,100 + rubber 40 ft x 25 = 1,000 = 20,620.
Quote QT-0418 = 72 sq ft x 220 = 15,840 + 180 ft x 220 = 39,600 + 12 x 350 = 4,200 = 59,640; advance 20,000; balance 39,640.
Run: python3 gen_glass.py [name ...]"""
from gen_ind import g
from gen_fashion_beauty import mini_ui, ui_report, five_steps, hardware_scene
from gen_shoes_vehicle import phone_list, counter_monitor, printer_with
from gen_electrical_baby import unit_tablet
from _daily_common import run

BLUE = '#024691'


def gl_units():
    return unit_tablet('cpGlU', 'Units and Packing', 'Sq ft · Foot · Piece', 'One item, sold the way you sell it', 'Buy by the sheet, length or box, sell by sq ft, foot or piece',
                       [('Clear Glass 5 mm', 'Sheet 48 sq ft', 'Sq ft', '1,152 sq ft', 'Rs 180'), ('Tinted Glass 5 mm', 'Sheet 48 sq ft', 'Sq ft', '624 sq ft', 'Rs 220'),
                        ('Mirror 4 mm', 'Sheet 24 sq ft', 'Sq ft', '288 sq ft', 'Rs 260'), ('Aluminium Section 2"', 'Length 16 ft', 'Foot', '1,920 ft', 'Rs 220'),
                        ('Window Handle', 'Box of 20', 'Piece', '140 pcs', 'Rs 350'), ('Rubber Beading', 'Roll 100 ft', 'Foot', '850 ft', 'Rs 25')],
                       'Stock drops in sq ft, feet or pieces on every sale', 'Sell 24 sq ft glass')


def gl_quote_phone():
    return phone_list('cpGlQ', 'Quotation QT-0418', '6 windows · Nadeem Ahmed', [
        ('Tinted Glass 72 sq ft', 'Rs 220 per sq ft', 'Rs 15,840', '#eaf1ff', BLUE), ('Aluminium 2" x 180 ft', 'Rs 220 per foot', 'Rs 39,600', '#eaf1ff', BLUE),
        ('Handle and lock x 12', 'Rs 350 each', 'Rs 4,200', '#eaf1ff', BLUE), ('Total', 'Sent on WhatsApp', 'Rs 59,640', '#ecfdf3', '#15803d')], 'Convert to sale')


def gl_advance_phone():
    return phone_list('cpGlA', 'Customer ledger', 'Nadeem Ahmed · 0321 5566778', [
        ('Quotation QT-0418', '8 Nov · agreed', 'Rs 59,640', '#eaf1ff', BLUE), ('Advance received', '10 Nov · cash', 'Rs 20,000', '#ecfdf3', '#15803d'),
        ('Final bill INV-2381', '18 Nov · from quote', 'Rs 59,640', '#eaf1ff', BLUE), ('Balance due', 'Statement on WhatsApp', 'Rs 39,640', '#fffbeb', '#92400e')], 'Receive payment')


def gl_monitor():
    return counter_monitor('cpMonGl', 'Glass Counter', 'Search glass, section or scan barcode',
                           [(46, 'Item', 'start'), (250, 'Qty / unit', 'start'), (400, 'Rate', 'middle'), (488, 'Amount', 'end')],
                           [('Clear Glass 5 mm', '24 sq ft', '180', '4,320'), ('Aluminium Section 2"', '60 foot', '220', '13,200'),
                            ('Window Handle', '6 piece', '350', '2,100'), ('Rubber Beading', '40 foot', '25', '1,000')],
                           ('Sq ft, foot and piece on one bill', 'Stock drops in the unit you sell', 'Udhaar for regular contractors'),
                           'Bilal Builders · 0300 7788990', ['Cash', 'Bank', 'Udhaar'], 2, ('Udhaar balance Rs 48,300', 'Regular contractor'), 'Rs 20,620')


def scene_gl_process():
    return five_steps([
        ('Receive stock', mini_ui('GRN-0391 · Supplier', [('Clear Glass 5 mm', '1,152 sq ft'), ('Aluminium 2"', '1,920 ft'), ('Handles', '7 box')], 'Stock and cost updated'), 'Sheets into sq ft'),
        ('Send the quote', mini_ui('QT-0418', [('Glass 72 sq ft', '15,840'), ('Aluminium 180 ft', '39,600'), ('Handles x 12', '4,200')], 'Sent on WhatsApp', '#eaf1ff', BLUE), 'A4 quotation'),
        ('Take the advance', mini_ui('Nadeem Ahmed', [('Quote', '59,640'), ('Advance', '20,000'), ('Paid by', 'Cash')], 'On the customer ledger', '#fffbeb', '#92400e'), 'Advance on record'),
        ('Final bill', mini_ui('INV-2381', [('From quote', 'QT-0418'), ('Bill', '59,640'), ('Balance due', '39,640')], 'Made in one tap'), 'Quote to sale'),
        ('See profit', ui_report("Today's sales", 'Rs 1,86,500', '23 bills · 3 quotes · 2 advances'), 'Sales, stock and profit'),
    ])


SCENES = {
    'uptrendpos-glass-shop-units-sqft': ('Sq ft, Foot, Piece', 'blue', lambda: g(gl_units(), 210, 150, 1.0),
        [(60, 770, 'Glass by the sq ft', '#2F7BD9'), (330, 770, 'Aluminium by the foot', '#2FA455')]),
    'uptrendpos-glass-shop-quotation-advance': ('Quotation and Advance', 'yellow', lambda: g(gl_quote_phone(), 230, 140, 1.0) + g(gl_advance_phone(), 680, 140, 1.0),
        [(60, 780, 'A4 quote, then the sale', '#2F7BD9'), (440, 780, 'Advance on the ledger', '#2FA455')]),
    'uptrendpos-glass-shop-pos-hardware': ('Glass Shop Hardware', 'teal',
        lambda: hardware_scene(gl_monitor, lambda: printer_with('CITY GLASS HOUSE', [('Clear Glass 24 sq ft', '4,320'), ('Alum. 2" 60 ft', '13,200'), ('Handle x6', '2,100')], 'Rs 19,620'),
                               gl_advance_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-glass-shop-pos-process': ('Glass Job, Step by Step', 'navy', scene_gl_process, [(60, 470, 'All connected', '#2FA455')]),
}

if __name__ == '__main__':
    run(SCENES)
