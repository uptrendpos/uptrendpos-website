"""Electrical & LED + Baby & Diaper page images (same house style and watermark as gen_ind.py).
Run: python3 gen_electrical_baby.py [name ...]"""
import asyncio, sys
from playwright.async_api import async_playwright
from PIL import Image
from gen_ind import B, OUT, t, frame, g
from gen_fashion_beauty import tablet, chip, mini_ui, ui_report, five_steps, hardware_scene
from gen_shoes_vehicle import phone_list, counter_monitor, printer_with

NAVY, BLUE, MUTED, INK = '#10224A', '#024691', '#64748b', '#1e293b'


def unit_tablet(clip, title, pill, head, sub, rows, note, btn):
    """rows = [(item, buy unit, sell as, in stock, price)]"""
    b = [t(44, 106, head, 14, 800, NAVY), t(44, 126, sub, 11, 600, MUTED), '<rect x="44" y="146" width="692" height="30" fill="#e9effa"/>']
    for xx, c, a in [(58, 'Item', 'start'), (300, 'Bought as', 'start'), (430, 'Sold as', 'start'), (610, 'In stock', 'end'), (716, 'Price', 'end')]:
        b.append(t(xx, 166, c, 11, 700, NAVY, a))
    y = 200
    for i, (n, bu, sa, st, pr) in enumerate(rows):
        if i % 2:
            b.append(f'<rect x="44" y="{y-20}" width="692" height="34" fill="#f7f9fd"/>')
        b += [t(58, y, n, 11.5, 600, INK), t(300, y, bu, 10.5, 600, MUTED), t(430, y, sa, 10.5, 700, BLUE), t(610, y, st, 11, 700, NAVY, 'end'), t(716, y, pr, 11, 700, NAVY, 'end')]
        y += 34
    b += ['<rect x="44" y="410" width="420" height="44" rx="12" fill="#ecfdf3"/>', t(60, 437, note, 11, 700, '#15803d'),
          '<rect x="500" y="410" width="236" height="44" rx="14" fill="#FAE814"/>', t(618, 438, btn, 13, 800, NAVY, 'middle')]
    return tablet(clip, title, pill, ''.join(b))


# ================================================================= ELECTRICAL & LED
def elec_units():
    return unit_tablet('cpElU', 'Units and Packing', 'Coil · Box · Piece', 'One item, sold the way you sell it', 'Buy by coil or box, sell by meter or piece',
                       [('Copper Wire 2.5 mm', 'Coil 90 m', 'Meter', '412 m', 'Rs 95 /m'), ('Copper Wire 7/29', 'Coil 90 m', 'Meter', '186 m', 'Rs 260 /m'),
                        ('Switch 1-Way White', 'Box of 20', 'Piece', '146 pcs', 'Rs 120'), ('LED Bulb 12W Cool', 'Carton of 50', 'Piece or pack', '320 pcs', 'Rs 350'),
                        ('Circuit Breaker 32A', 'Box of 12', 'Piece', '48 pcs', 'Rs 1,150'), ('PVC Pipe 3/4"', 'Bundle of 25', 'Piece', '75 pcs', 'Rs 280')],
                       'Stock drops in meters or pieces on every sale', 'Sell 15 m wire')


def elec_quote_phone():
    return phone_list('cpElQ', 'Quotation QT-0582', 'House wiring · Waqas Electric (contractor)', [
        ('Wire 2.5 mm x 270 m', 'Rs 25,650', 'Wire', '#eaf1ff', BLUE), ('Switch 1-Way x 40', 'Rs 4,800', 'Fittings', '#eaf1ff', BLUE),
        ('Breaker 32A x 6', 'Rs 6,900', 'DB', '#eaf1ff', BLUE), ('Total', 'Valid till 05 Nov', 'Rs 37,350', '#ecfdf3', '#15803d')], 'Convert to sale')


def elec_led_phone():
    return phone_list('cpElL', 'LED Bulb 12W', 'Stock by light colour', [
        ('Cool Daylight', 'Fast seller', '320 pcs', '#ecfdf3', '#15803d'), ('Warm White', 'Low stock alert', '18 pcs', '#fffbeb', '#92400e'),
        ('Natural White', 'Steady', '96 pcs', '#ecfdf3', '#15803d'), ('Fused on arrival', 'Recorded as damage', '4 pcs', '#fef2f2', '#b91c1c')], 'Add Warm White to demand list')


def elec_monitor():
    return counter_monitor('cpMonEl', 'Electrical Counter', 'Search wire, switch, breaker or scan barcode',
                           [(46, 'Item', 'start'), (250, 'Qty / unit', 'start'), (400, 'Rate', 'middle'), (488, 'Amount', 'end')],
                           [('Copper Wire 2.5 mm', '15 meter', '95', '1,425'), ('LED Bulb 12W Cool', '6 piece', '350', '2,100'),
                            ('Switch 1-Way White', '4 piece', '120', '480'), ('Breaker 32A', '1 piece', '1,150', '1,150')],
                           ('Copper Wire 2.5 mm: 397 m left', 'Bought as 90 m coils · sold by the meter', 'Udhaar for regular electricians'),
                           'Waqas Electric · 0306 1122334', ['Cash', 'Bank', 'Udhaar'], 2, ('Udhaar balance Rs 18,400', 'Regular electrician'), 'Rs 5,155')


def scene_elec_process():
    return five_steps([
        ('Receive stock', mini_ui('GRN · Lahore Cables', [('Wire 2.5 mm', '5 coils'), ('Switch 1-Way', '10 boxes'), ('LED 12W', '4 cartons')], 'Coils turn into meters'), 'Coils, boxes, cartons'),
        ('Quote a contractor', mini_ui('Quotation QT-0582', [('Wire 270 m', '25,650'), ('Switches x 40', '4,800'), ('Breakers x 6', '6,900')], 'Sent on WhatsApp', '#eaf1ff', BLUE), 'A4 quote, then sale'),
        ('Sell by meter', mini_ui('New sale', [('Wire 2.5 mm 15 m', '1,425'), ('LED 12W x 6', '2,100'), ('Switch x 4', '480')], 'Stock in meters drops'), 'Meter, piece or pack'),
        ('Udhaar and damage', mini_ui('Today', [('Waqas Electric', 'Rs 18,400 due'), ('Fused bulbs', '4 pcs damage'), ('Returns', '1')], 'Stock stays right', '#fffbeb', '#92400e'), 'Electricians on credit'),
        ('See profit', ui_report("Today's sales", 'Rs 1,48,250', '86 bills · 1,240 m wire · 3 contractor quotes'), 'Sales, stock and profit'),
    ])


# ================================================================= BABY & DIAPER
def baby_units():
    return unit_tablet('cpBbU', 'Units and Packing', 'Carton · Pack · Piece', 'Sell a full pack or loose pieces', 'Diapers, wipes and baby care in the units customers ask for',
                       [('Baby Diapers Size 4 (L)', 'Carton of 4 packs', 'Pack or piece', '9 packs', 'Rs 2,950'), ('Baby Diapers Size 3 (M)', 'Carton of 4 packs', 'Pack or piece', '12 packs', 'Rs 2,850'),
                        ('Baby Wipes 80 pcs', 'Carton of 12', 'Pack', '30 packs', 'Rs 420'), ('Feeding Bottle 250ml', 'Box of 6', 'Piece', '22 pcs', 'Rs 650'),
                        ('Baby Lotion 200ml', 'Carton of 24', 'Piece', '40 pcs', 'Rs 780'), ('Baby Soap 75g', 'Carton of 48', 'Piece', '64 pcs', 'Rs 160')],
                       'Open a pack and sell pieces, stock stays right', 'Sell 5 pieces')


def baby_size_phone():
    return phone_list('cpBbS', 'Baby Diapers', 'Packs left in each size', [
        ('Newborn', 'Up to 5 kg', '6 packs', '#ecfdf3', '#15803d'), ('Size 3 (M)', '6 to 10 kg', '12 packs', '#ecfdf3', '#15803d'),
        ('Size 4 (L)', '9 to 14 kg · best seller', '2 packs', '#fffbeb', '#92400e'), ('Size 5 (XL)', '12 kg and up', 'Out', '#fef2f2', '#b91c1c')], 'Add L and XL to demand list')


def baby_expiry_phone():
    return phone_list('cpBbE', 'Expiry alerts', 'Batches that expire in 30 days', [
        ('Baby Cereal Rice 300g', 'Batch BC-44', '9 days', '#fffbeb', '#92400e'), ('Infant Formula Stage 1', 'Batch IF-12', '24 days', '#fffbeb', '#92400e'),
        ('Baby Wipes 80 pcs', 'Batch BW-30', '27 days', '#fffbeb', '#92400e'), ('Baby Juice 200ml', 'Batch BJ-02', 'Expired', '#fef2f2', '#b91c1c')], 'Sell first or return')


def baby_monitor():
    return counter_monitor('cpMonBb', 'Baby Store Counter', 'Scan barcode or search diapers, wipes, baby care',
                           [(46, 'Item', 'start'), (250, 'Unit', 'start'), (400, 'Qty', 'middle'), (488, 'Amount', 'end')],
                           [('Baby Diapers Size 4 (L)', 'Pack', '1', '2,950'), ('Baby Diapers Size 4 (L)', 'Piece', '5', '375'),
                            ('Baby Wipes 80 pcs', 'Pack', '2', '840'), ('Feeding Bottle 250ml', 'Piece', '1', '650')],
                           ('Size 4 (L): 2 packs + 12 pieces left', 'Wipes Batch BW-30 expires in 27 days', 'Regular mother · udhaar khata'),
                           'Sana Bibi · 0312 3344556', ['Cash', 'Bank', 'Udhaar'], 0, ('Discount Rs 100', 'On this bill'), 'Rs 4,715')


def scene_baby_process():
    return five_steps([
        ('Receive stock', mini_ui('GRN · Karachi Baby Care', [('Diapers L', '3 cartons'), ('Cereal BC-44', 'exp Nov'), ('Wipes BW-30', 'exp Nov')], 'Batch and expiry saved'), 'Cartons, packs, expiry'),
        ('Sell pack or piece', mini_ui('New sale', [('Diapers L pack', '2,950'), ('Diapers L x 5 pcs', '375'), ('Wipes x 2', '840')], 'Stock in pieces drops'), 'Pack or loose pieces'),
        ('Watch sizes', mini_ui('Diaper sizes', [('Size 3 (M)', '12 packs'), ('Size 4 (L)', '2 packs'), ('Size 5 (XL)', 'Out')], 'Demand list ready', '#eaf1ff', BLUE), 'Never run out of L'),
        ('Check expiry', mini_ui('Expiry alerts', [('Baby Cereal', '9 days'), ('Formula Stage 1', '24 days'), ('Baby Juice', 'Expired')], 'Sell first or return', '#fffbeb', '#92400e'), 'Before it is a loss'),
        ('See profit', ui_report("Today's sales", 'Rs 64,900', '58 bills · 41 packs · 120 loose pieces'), 'Sales, stock and profit'),
    ])


SCENES = {
    'uptrendpos-electrical-store-units-meter-coil': ('Coil, Meter, Box, Piece', 'blue', lambda: g(elec_units(), 210, 150, 1.0),
        [(60, 770, 'Wire sold by the meter', '#2F7BD9'), (330, 770, 'Boxes sold by the piece', '#2FA455')]),
    'uptrendpos-electrical-store-quotation-led-stock': ('Contractor Quotes and LED Stock', 'yellow', lambda: g(elec_quote_phone(), 230, 140, 1.0) + g(elec_led_phone(), 680, 140, 1.0),
        [(60, 780, 'A4 quote for contractors', '#2F7BD9'), (440, 780, 'Stock by light colour', '#2FA455')]),
    'uptrendpos-electrical-store-pos-hardware': ('Electrical Shop Hardware', 'teal',
        lambda: hardware_scene(elec_monitor, lambda: printer_with('CITY ELECTRIC STORE', [('Wire 2.5mm 15m', '1,425'), ('LED 12W x6', '2,100'), ('Switch x4', '480')], 'Rs 5,155'),
                               elec_led_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-electrical-store-pos-process': ('Electrical Sale, Step by Step', 'navy', scene_elec_process, [(60, 470, 'All connected', '#2FA455')]),
    'uptrendpos-baby-store-pack-piece-units': ('Pack or Piece', 'green', lambda: g(baby_units(), 210, 150, 1.0),
        [(60, 770, 'Sell a pack or loose pieces', '#2FA455'), (380, 770, 'Stock always right', '#2F7BD9')]),
    'uptrendpos-baby-store-diaper-sizes-expiry': ('Diaper Sizes and Expiry', 'teal', lambda: g(baby_size_phone(), 230, 140, 1.0) + g(baby_expiry_phone(), 680, 140, 1.0),
        [(60, 780, 'Packs left in each size', '#2F7BD9'), (440, 780, 'Batch expiry alerts', '#F59E0B')]),
    'uptrendpos-baby-store-pos-hardware': ('Baby Store Hardware', 'blue',
        lambda: hardware_scene(baby_monitor, lambda: printer_with('LITTLE STARS BABY SHOP', [('Diapers L pack', '2,950'), ('Diapers L x5', '375'), ('Wipes x2', '840')], 'Rs 4,715'),
                               baby_size_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-baby-store-pos-process': ('Baby Store Sale, Step by Step', 'yellow', scene_baby_process, [(60, 470, 'All connected', '#2FA455')]),
}


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1200, 'height': 900})
        only = sys.argv[1:]
        for name, (label, tint, body, chips) in SCENES.items():
            if only and name not in only:
                continue
            svg = frame(body(), label, chips, tint)
            await pg.set_content(f'<html><body style="margin:0">{svg}</body></html>')
            await pg.wait_for_timeout(300)
            png = B / f'{name}.png'
            await pg.screenshot(path=str(png), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 900})
            Image.open(png).convert('RGB').save(OUT / f'{name}.webp', 'WEBP', quality=80, method=6)
            print(name, (OUT / f'{name}.webp').stat().st_size // 1024, 'KB')
        await b.close()

if __name__ == '__main__':
    asyncio.run(main())
