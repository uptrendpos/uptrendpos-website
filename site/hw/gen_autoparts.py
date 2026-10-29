"""Auto Spare Parts page images. No vehicle-fitment or cross-reference visuals. Run: python3 gen_autoparts.py [name ...]"""
from gen_ind import g
from gen_fashion_beauty import mini_ui, ui_report, five_steps, hardware_scene
from gen_shoes_vehicle import phone_list, counter_monitor, printer_with
from gen_electrical_baby import unit_tablet
from _daily_common import run

BLUE = '#024691'


def ap_units():
    return unit_tablet('cpApU', 'Parts and Units', 'Name · Code · Barcode', 'Every part by name, code or barcode', 'Buy by the carton, box or drum, sell by the piece, can or litre',
                       [('Spark Plug · SP-221', 'Box of 10', 'Piece', '64 pcs', 'Rs 450'), ('Engine Oil 20W-50 4L', 'Carton of 6', 'Can', '22 cans', 'Rs 4,800'),
                        ('Loose Engine Oil', 'Drum 200 L', 'Litre', '146 L', 'Rs 1,150 /L'), ('Air Filter · AF-310', 'Carton of 20', 'Piece', '35 pcs', 'Rs 950'),
                        ('Clutch Plate · CP-125', 'Box of 5', 'Piece', '18 pcs', 'Rs 1,350'), ('Head Bulb 12V · HB-4', 'Box of 10', 'Piece', '40 pcs', 'Rs 380')],
                       'Type a part code and it is on the bill', 'Search CP-125')


def ap_supplier_phone():
    return phone_list('cpApS', 'Supplier ledger', 'Karachi Auto Traders', [
        ('PI-2231 · 12 Oct', 'Purchase invoice', 'Rs 84,500', '#eaf1ff', BLUE), ('Payment · 20 Oct', 'Bank transfer', '-Rs 50,000', '#ecfdf3', '#15803d'),
        ('PI-2290 · 26 Oct', 'Purchase invoice', 'Rs 41,200', '#eaf1ff', BLUE), ('Balance due', 'Pay by 05 Nov', 'Rs 75,700', '#fffbeb', '#92400e')], 'Record payment')


def ap_udhaar_phone():
    return phone_list('cpApM', 'Mechanic udhaar', 'Khata of regular mechanics', [
        ('Bilal Autos', 'Paid 3 days ago', 'Rs 22,350', '#eaf1ff', BLUE), ('Rafiq Motor Works', 'Paid 12 days ago', 'Rs 9,800', '#eaf1ff', BLUE),
        ('Shahid Bike Point', '31 days · follow up', 'Rs 14,600', '#fffbeb', '#92400e'), ('Total to collect', '3 mechanics', 'Rs 46,750', '#ecfdf3', '#15803d')], 'Send statement')


def ap_monitor():
    return counter_monitor('cpMonAp', 'Auto Parts Counter', 'Search part name, part code or scan barcode',
                           [(46, 'Part', 'start'), (250, 'Qty / unit', 'start'), (400, 'Rate', 'middle'), (488, 'Amount', 'end')],
                           [('Engine Oil 20W-50 4L', '1 can', '4,800', '4,800'), ('Spark Plug · SP-221', '4 piece', '450', '1,800'),
                            ('Air Filter · AF-310', '1 piece', '950', '950'), ('Clutch Plate · CP-125', '1 piece', '1,350', '1,350')],
                           ('Spark Plug SP-221: 60 pcs left', 'Found by code · bought by the box of 10', 'Udhaar for regular mechanics'),
                           'Bilal Autos · 0301 5566778', ['Cash', 'Bank', 'Udhaar'], 2, ('Udhaar balance Rs 22,350', 'Regular mechanic'), 'Rs 8,900')


def scene_ap_process():
    return five_steps([
        ('Receive parts', mini_ui('GRN · Karachi Auto Traders', [('Spark Plugs', '5 boxes'), ('Engine Oil 4L', '4 cartons'), ('Clutch Plates', '2 boxes')], 'Average cost updated'), 'GRN and supplier bill'),
        ('Find the part', mini_ui('Search: CP-125', [('Clutch Plate', 'CP-125'), ('In stock', '18 pcs'), ('Price', 'Rs 1,350')], 'Found in seconds', '#eaf1ff', BLUE), 'Name, code or barcode'),
        ('Sell or udhaar', mini_ui('New sale', [('Engine Oil 4L', '4,800'), ('Spark Plug x 4', '1,800'), ('Air Filter', '950')], 'On Bilal Autos khata', '#fffbeb', '#92400e'), 'Cash, bank or khata'),
        ('Reorder', mini_ui('Demand list', [('Air Filter AF-310', '35 left'), ('Head Bulb HB-4', '4 left'), ('Clutch CP-125', '18 left')], 'Make purchase order'), 'Before it runs out'),
        ('See profit', ui_report("Today's sales", 'Rs 1,12,600', '96 bills · 41 to mechanics · 2 GRNs'), 'Sales, stock and profit'),
    ])


SCENES = {
    'uptrendpos-auto-parts-store-search-code-units': ('Name, Code, Barcode', 'blue', lambda: g(ap_units(), 210, 150, 1.0),
        [(60, 770, 'Find parts by code', '#2F7BD9'), (330, 770, 'Box to piece, drum to litre', '#2FA455')]),
    'uptrendpos-auto-parts-store-supplier-mechanic-udhaar': ('Supplier Ledger and Mechanic Udhaar', 'yellow', lambda: g(ap_supplier_phone(), 230, 140, 1.0) + g(ap_udhaar_phone(), 680, 140, 1.0),
        [(60, 780, 'What you owe suppliers', '#2F7BD9'), (440, 780, 'What mechanics owe you', '#2FA455')]),
    'uptrendpos-auto-parts-store-pos-hardware': ('Auto Parts Shop Hardware', 'teal',
        lambda: hardware_scene(ap_monitor, lambda: printer_with('KHAN AUTO PARTS', [('Engine Oil 4L', '4,800'), ('Spark Plug x4', '1,800'), ('Air Filter', '950')], 'Rs 7,550'),
                               ap_udhaar_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-auto-parts-store-pos-process': ('Auto Parts Sale, Step by Step', 'navy', scene_ap_process, [(60, 470, 'All connected', '#2FA455')]),
}

if __name__ == '__main__':
    run(SCENES)
