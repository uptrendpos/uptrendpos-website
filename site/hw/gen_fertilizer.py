"""Agri Inputs (Seed, Fertilizer & Pesticides) page images. No brand names, no crop advice visuals.
Bills add up: counter = Urea 2 bag x 4,600 = 9,200 + DAP 1 bag x 12,800 = 12,800 + Insecticide 2 bottle x 1,450 = 2,900 + Wheat Seed 1 bag x 9,000 = 9,000 = 33,900.
Receipt (first three lines) = 9,200 + 12,800 + 2,900 = 24,900.
Farmer ledger = 18,000 + 34,500 - 15,000 = 37,500.
Run: python3 gen_fertilizer.py [name ...]"""
from gen_ind import g
from gen_fashion_beauty import mini_ui, ui_report, five_steps, hardware_scene
from gen_shoes_vehicle import phone_list, counter_monitor, printer_with
from gen_electrical_baby import unit_tablet
from _daily_common import run

BLUE = '#024691'


def ag_units():
    return unit_tablet('cpAgU', 'Units and Packing', 'Bag · Kg · Bottle · Packet', 'One item, sold the way farmers buy', 'Buy by the truck or carton, sell by the bag, kg, bottle or packet',
                       [('Urea Fertilizer', 'Bag 50 kg', 'Bag or kg', '186 bags', 'Rs 4,600'), ('DAP Fertilizer', 'Bag 50 kg', 'Bag or kg', '74 bags', 'Rs 12,800'),
                        ('Insecticide 500 ml', 'Carton of 20', 'Bottle', '96 bottles', 'Rs 1,450'), ('Herbicide 1 litre', 'Carton of 12', 'Bottle', '40 bottles', 'Rs 2,200'),
                        ('Wheat Seed', 'Bag 50 kg', 'Bag', '62 bags', 'Rs 9,000'), ('Vegetable Seed 100 g', 'Box of 25', 'Packet', '130 pkts', 'Rs 650')],
                       'Sell a full bag or loose kg, stock stays right', 'Sell 10 kg urea')


def ag_expiry_phone():
    return phone_list('cpAgE', 'Expiry alerts', 'Batches that expire in 30 days', [
        ('Insecticide 500 ml', 'Batch IN-27', '12 days', '#fffbeb', '#92400e'), ('Herbicide 1 litre', 'Batch HB-09', '21 days', '#fffbeb', '#92400e'),
        ('Fungicide 250 g', 'Batch FG-14', '28 days', '#fffbeb', '#92400e'), ('Vegetable Seed 100 g', 'Batch VS-05', 'Expired', '#fef2f2', '#b91c1c')], 'Sell first or return')


def ag_udhaar_phone():
    return phone_list('cpAgL', 'Farmer ledger', 'Ghulam Rasool · 0301 4455667', [
        ('Wheat seed · 2 bags', '2 Nov · udhaar', 'Rs 18,000', '#eaf1ff', BLUE), ('Fertilizer bags', '20 Nov · udhaar', 'Rs 34,500', '#eaf1ff', BLUE),
        ('Payment received', '22 Nov · cash', 'Rs 15,000', '#ecfdf3', '#15803d'), ('Balance due', 'Pay after harvest', 'Rs 37,500', '#fffbeb', '#92400e')], 'Send statement')


def ag_monitor():
    return counter_monitor('cpMonAg', 'Agri Counter', 'Scan barcode or search seed, fertilizer, spray',
                           [(46, 'Item', 'start'), (250, 'Qty / unit', 'start'), (400, 'Rate', 'middle'), (488, 'Amount', 'end')],
                           [('Urea Fertilizer', '2 bag', '4,600', '9,200'), ('DAP Fertilizer', '1 bag', '12,800', '12,800'),
                            ('Insecticide 500 ml', '2 bottle', '1,450', '2,900'), ('Wheat Seed', '1 bag', '9,000', '9,000')],
                           ('Bag, kg and bottle on one bill', 'Insecticide Batch IN-27 expires in 12 days', 'Farmer udhaar till harvest'),
                           'Ghulam Rasool · 0301 4455667', ['Cash', 'Bank', 'Udhaar'], 2, ('Udhaar balance Rs 37,500', 'Pays after harvest'), 'Rs 33,900')


def scene_ag_process():
    return five_steps([
        ('Receive stock', mini_ui('GRN-0512 · Supplier', [('Urea 50 kg', '100 bags'), ('Insecticide IN-27', '5 ctn'), ('Seed VS-05', 'exp Dec')], 'Batch and expiry saved'), 'Bags, cartons, expiry'),
        ('Bill the farmer', mini_ui('INV-3307', [('Urea x 2 bags', '9,200'), ('DAP x 1 bag', '12,800'), ('Sprays x 2', '2,900')], 'Sent on WhatsApp', '#eaf1ff', BLUE), 'Fast counter bill'),
        ('Keep the udhaar', mini_ui('Ghulam Rasool', [('Season total', '52,500'), ('Paid', '15,000'), ('Balance', '37,500')], 'On the farmer ledger', '#fffbeb', '#92400e'), 'Till the harvest'),
        ('Check expiry', mini_ui('Expiry alerts', [('Insecticide', '12 days'), ('Herbicide', '21 days'), ('Veg. seed', 'Expired')], 'Sell first or return', '#fffbeb', '#92400e'), 'Before it is a loss'),
        ('See profit', ui_report("Today's sales", 'Rs 2,14,800', '31 bills · 9 udhaar · 2 returns'), 'Sales, stock and profit'),
    ])


SCENES = {
    'uptrendpos-fertilizer-shop-units-bags': ('Bag, Kg, Bottle, Packet', 'blue', lambda: g(ag_units(), 210, 150, 1.0),
        [(60, 770, 'Fertilizer by the bag or kg', '#2F7BD9'), (380, 770, 'Sprays by the bottle', '#2FA455')]),
    'uptrendpos-fertilizer-shop-expiry-udhaar': ('Expiry and Farmer Udhaar', 'yellow', lambda: g(ag_expiry_phone(), 230, 140, 1.0) + g(ag_udhaar_phone(), 680, 140, 1.0),
        [(60, 780, 'Batch expiry alerts', '#F59E0B'), (440, 780, 'Udhaar till the harvest', '#2FA455')]),
    'uptrendpos-fertilizer-shop-pos-hardware': ('Agri Shop Hardware', 'teal',
        lambda: hardware_scene(ag_monitor, lambda: printer_with('KISAN AGRI STORE', [('Urea x2 bag', '9,200'), ('DAP x1 bag', '12,800'), ('Insecticide x2', '2,900')], 'Rs 24,900'),
                               ag_udhaar_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-fertilizer-shop-pos-process': ('Agri Shop, Step by Step', 'navy', scene_ag_process, [(60, 470, 'All connected', '#2FA455')]),
}

if __name__ == '__main__':
    run(SCENES)
