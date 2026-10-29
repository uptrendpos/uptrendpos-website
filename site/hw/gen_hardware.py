"""Hardware, Sanitary & Building Material page images. Run: python3 gen_hardware.py [name ...]"""
from gen_ind import g
from gen_fashion_beauty import mini_ui, ui_report, five_steps, hardware_scene
from gen_shoes_vehicle import phone_list, counter_monitor, printer_with
from gen_electrical_baby import unit_tablet
from _daily_common import run

BLUE = '#024691'


def hw_units():
    return unit_tablet('cpHwU', 'Units and Packing', 'Bag · Foot · Box · Piece', 'One item, sold the way you sell it', 'Buy by the box or bundle, sell by the bag, foot or piece',
                       [('Cement OPC 50 kg', 'Truck load', 'Bag', '310 bags', 'Rs 1,450'), ('PVC Pipe 1"', 'Bundle 200 ft', 'Foot', '640 ft', 'Rs 45 /ft'),
                        ('Steel Bar 12 mm', 'Ton', 'Kg', '1,850 kg', 'Rs 260 /kg'), ('Wood Screw 1.5"', 'Box of 100', 'Piece or box', '820 pcs', 'Rs 6'),
                        ('Floor Tile 2x2', 'Box of 4', 'Box', '96 boxes', 'Rs 1,900'), ('Basin Tap Chrome', 'Carton of 10', 'Piece', '24 pcs', 'Rs 1,250')],
                       'Stock drops in bags, feet or pieces on every sale', 'Sell 40 ft pipe')


def hw_quote_phone():
    return phone_list('cpHwQ', 'Quotation QT-0611', 'Bathroom job · Asif Builders', [
        ('PPR Pipe 3/4" x 120 ft', 'Rs 80 per foot', 'Rs 9,600', '#eaf1ff', BLUE), ('Mixer Tap x 3', 'Rs 4,500 each', 'Rs 13,500', '#eaf1ff', BLUE),
        ('Commode Set x 2', 'Rs 18,500 each', 'Rs 37,000', '#eaf1ff', BLUE), ('Total', 'Valid till 05 Nov', 'Rs 60,100', '#ecfdf3', '#15803d')], 'Convert to sale')


def hw_search_phone():
    return phone_list('cpHwS', 'Search: elbow', '4 of 2,840 items match', [
        ('Elbow PVC 1"', 'Rs 35 · piece', '420 pcs', '#ecfdf3', '#15803d'), ('Elbow PPR 3/4"', 'Rs 60 · piece', '185 pcs', '#ecfdf3', '#15803d'),
        ('Elbow GI 1/2"', 'Rs 90 · piece', '64 pcs', '#ecfdf3', '#15803d'), ('Elbow PVC 2"', 'Low stock alert', '6 pcs', '#fffbeb', '#92400e')], 'Add to bill')


def hw_monitor():
    return counter_monitor('cpMonHw', 'Hardware Counter', 'Search any item by name or scan barcode',
                           [(46, 'Item', 'start'), (250, 'Qty / unit', 'start'), (400, 'Rate', 'middle'), (488, 'Amount', 'end')],
                           [('Cement OPC 50 kg', '10 bag', '1,450', '14,500'), ('PVC Pipe 1"', '40 foot', '45', '1,800'),
                            ('Basin Tap Chrome', '2 piece', '1,250', '2,500'), ('Wood Screw 1.5"', '50 piece', '6', '300')],
                           ('PVC Pipe 1": 600 ft left', 'Bought in 200 ft bundles · sold by the foot', 'Udhaar for regular plumbers'),
                           'Imran Plumber · 0321 4455667', ['Cash', 'Bank', 'Udhaar'], 2, ('Udhaar balance Rs 26,300', 'Regular plumber'), 'Rs 19,100')


def scene_hw_process():
    return five_steps([
        ('Receive stock', mini_ui('GRN · Lahore Pipes', [('PVC Pipe 1"', '3 bundles'), ('Screws 1.5"', '10 boxes'), ('Basin Taps', '2 cartons')], 'Bundles turn into feet'), 'Bags, bundles, boxes'),
        ('Quote a contractor', mini_ui('Quotation QT-0611', [('PPR Pipe 120 ft', '9,600'), ('Mixer Tap x 3', '13,500'), ('Commode Set x 2', '37,000')], 'Sent on WhatsApp', '#eaf1ff', BLUE), 'A4 quote, then sale'),
        ('Find and sell', mini_ui('New sale', [('Cement x 10 bags', '14,500'), ('PVC Pipe 40 ft', '1,800'), ('Basin Tap x 2', '2,500')], 'Found in seconds'), 'Bag, foot or piece'),
        ('Udhaar and damage', mini_ui('Today', [('Imran Plumber', 'Rs 26,300 due'), ('Cracked basin', '1 pc damage'), ('Returns', '2')], 'Stock stays right', '#fffbeb', '#92400e'), 'Plumbers on credit'),
        ('See profit', ui_report("Today's sales", 'Rs 2,36,400', '74 bills · 310 bags cement · 2 contractor quotes'), 'Sales, stock and profit'),
    ])


SCENES = {
    'uptrendpos-hardware-store-units-bag-foot': ('Bag, Foot, Box, Piece', 'blue', lambda: g(hw_units(), 210, 150, 1.0),
        [(60, 770, 'Pipe sold by the foot', '#2F7BD9'), (330, 770, 'Cement sold by the bag', '#2FA455')]),
    'uptrendpos-hardware-store-quotation-search': ('Quick Search and Contractor Quotes', 'yellow', lambda: g(hw_search_phone(), 230, 140, 1.0) + g(hw_quote_phone(), 680, 140, 1.0),
        [(60, 780, 'Find any item in seconds', '#2F7BD9'), (440, 780, 'A4 quote for contractors', '#2FA455')]),
    'uptrendpos-hardware-store-pos-hardware': ('Hardware Shop Hardware', 'teal',
        lambda: hardware_scene(hw_monitor, lambda: printer_with('CITY HARDWARE STORE', [('Cement x10 bags', '14,500'), ('PVC Pipe 40 ft', '1,800'), ('Basin Tap x2', '2,500')], 'Rs 18,800'),
                               hw_search_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-hardware-store-pos-process': ('Hardware Sale, Step by Step', 'navy', scene_hw_process, [(60, 470, 'All connected', '#2FA455')]),
}

if __name__ == '__main__':
    run(SCENES)
