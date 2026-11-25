"""Veterinary Store page images. No brand names, no dose or treatment visuals.
Bills add up: counter = Dewormer Bolus 2 strip x 240 = 480 + Multivitamin Liquid 1 bottle x 1,650 = 1,650 + Calcium Liquid 2 bottle x 850 = 1,700 + Mineral Mix 5 kg x 520 = 2,600 = 6,430.
Receipt (first three lines) = 480 + 1,650 + 1,700 = 3,830.
Farmer ledger = 4,200 + 6,430 - 3,000 = 7,630.
Run: python3 gen_veterinary.py [name ...]"""
from gen_ind import g
from gen_fashion_beauty import mini_ui, ui_report, five_steps, hardware_scene
from gen_shoes_vehicle import phone_list, counter_monitor, printer_with
from gen_electrical_baby import unit_tablet
from _daily_common import run

BLUE = '#024691'


def vt_units():
    return unit_tablet('cpVtU', 'Units and Packing', 'Box · Strip · Piece · Bottle · Kg', 'One item, sold the way farmers buy', 'Buy by the box or carton, sell by the strip, piece, bottle or kg',
                       [('Dewormer Bolus', 'Box of 10 strips', 'Strip or piece', '58 strips', 'Rs 240'), ('Multivitamin Liquid 1 L', 'Carton of 12', 'Bottle', '34 bottles', 'Rs 1,650'),
                        ('Calcium Liquid 500 ml', 'Carton of 24', 'Bottle', '71 bottles', 'Rs 850'), ('Mineral Mix', 'Bag 25 kg', 'Bag or kg', '210 kg', 'Rs 520'),
                        ('Poultry Vitamin Sachet', 'Box of 50', 'Sachet', '140 sachets', 'Rs 95'), ('Liver Tonic 500 ml', 'Carton of 24', 'Bottle', '45 bottles', 'Rs 780')],
                       'Sell a box, strip or piece, stock stays right', 'Sell 2 strips')


def vt_expiry_phone():
    return phone_list('cpVtE', 'Expiry alerts', 'Batches that expire in 30 days', [
        ('Dewormer Bolus', 'Batch DW-31', '9 days', '#fffbeb', '#92400e'), ('Calcium Liquid 500 ml', 'Batch CL-12', '18 days', '#fffbeb', '#92400e'),
        ('Poultry Vitamin Sachet', 'Batch PV-07', '26 days', '#fffbeb', '#92400e'), ('Liver Tonic 500 ml', 'Batch LT-03', 'Expired', '#fef2f2', '#b91c1c')], 'Sell first or return')


def vt_udhaar_phone():
    return phone_list('cpVtL', 'Farmer ledger', 'Muhammad Aslam · 0302 7788991', [
        ('Supplements', '4 Nov · udhaar', 'Rs 4,200', '#eaf1ff', BLUE), ('Medicines', '19 Nov · udhaar', 'Rs 6,430', '#eaf1ff', BLUE),
        ('Payment received', '22 Nov · cash', 'Rs 3,000', '#ecfdf3', '#15803d'), ('Balance due', 'Pays at month end', 'Rs 7,630', '#fffbeb', '#92400e')], 'Send statement')


def vt_monitor():
    return counter_monitor('cpMonVt', 'Vet Counter', 'Scan barcode or search medicine, supplement',
                           [(46, 'Item', 'start'), (250, 'Qty / unit', 'start'), (400, 'Rate', 'middle'), (488, 'Amount', 'end')],
                           [('Dewormer Bolus', '2 strip', '240', '480'), ('Multivitamin Liquid', '1 bottle', '1,650', '1,650'),
                            ('Calcium Liquid 500 ml', '2 bottle', '850', '1,700'), ('Mineral Mix', '5 kg', '520', '2,600')],
                           ('Box, strip and bottle on one bill', 'Dewormer Batch DW-31 expires in 9 days', 'Farmer udhaar on the ledger'),
                           'Muhammad Aslam · 0302 7788991', ['Cash', 'Bank', 'Udhaar'], 2, ('Udhaar balance Rs 7,630', 'Pays at month end'), 'Rs 6,430')


def scene_vt_process():
    return five_steps([
        ('Receive stock', mini_ui('GRN-0284 · Distributor', [('Dewormer DW-31', '10 box'), ('Calcium CL-12', '2 ctn'), ('Mineral Mix', '8 bags')], 'Batch and expiry saved'), 'Boxes, cartons, expiry'),
        ('Bill the farmer', mini_ui('INV-1906', [('Dewormer x 2 strips', '480'), ('Multivitamin x 1', '1,650'), ('Calcium x 2', '1,700')], 'Sent on WhatsApp', '#eaf1ff', BLUE), 'Fast counter bill'),
        ('Keep the udhaar', mini_ui('Muhammad Aslam', [('Month total', '10,630'), ('Paid', '3,000'), ('Balance', '7,630')], 'On the farmer ledger', '#fffbeb', '#92400e'), 'Pays at month end'),
        ('Check expiry', mini_ui('Expiry alerts', [('Dewormer', '9 days'), ('Calcium', '18 days'), ('Liver tonic', 'Expired')], 'Sell first or return', '#fffbeb', '#92400e'), 'Before it is a loss'),
        ('See profit', ui_report("Today's sales", 'Rs 86,450', '47 bills · 12 udhaar · 1 return'), 'Sales, stock and profit'),
    ])


SCENES = {
    'uptrendpos-veterinary-store-units-strips': ('Box, Strip, Piece, Kg', 'blue', lambda: g(vt_units(), 210, 150, 1.0),
        [(60, 770, 'Box, strip or piece', '#2F7BD9'), (380, 770, 'Supplements by the kg', '#2FA455')]),
    'uptrendpos-veterinary-store-expiry-udhaar': ('Expiry and Farmer Udhaar', 'yellow', lambda: g(vt_expiry_phone(), 230, 140, 1.0) + g(vt_udhaar_phone(), 680, 140, 1.0),
        [(60, 780, 'Batch expiry alerts', '#F59E0B'), (440, 780, 'Farmer udhaar ledger', '#2FA455')]),
    'uptrendpos-veterinary-store-pos-hardware': ('Vet Store Hardware', 'teal',
        lambda: hardware_scene(vt_monitor, lambda: printer_with('PASHU VET STORE', [('Dewormer x2 strip', '480'), ('Multivitamin x1', '1,650'), ('Calcium x2', '1,700')], 'Rs 3,830'),
                               vt_udhaar_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-veterinary-store-pos-process': ('Vet Store, Step by Step', 'navy', scene_vt_process, [(60, 470, 'All connected', '#2FA455')]),
}

if __name__ == '__main__':
    run(SCENES)
