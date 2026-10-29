"""Shoes & Footwear + Vehicle Showroom page images (same house style and watermark as gen_ind.py).
Run: python3 gen_shoes_vehicle.py [name ...]"""
import asyncio, sys
from playwright.async_api import async_playwright
from PIL import Image
from gen_ind import B, OUT, t, phone_shell, status_bar, frame, g, printer80
from gen_tailor_mobile import screen_open, monitor_stand, screen_close
from gen_fashion_beauty import tablet, chip, mini_ui, ui_report, five_steps, hardware_scene

NAVY, BLUE, MUTED, INK = '#10224A', '#024691', '#64748b', '#1e293b'


def variant_tablet(clip, title, pill, article, sub, dim1, dims1, dim2, dims2, rows, note, btn):
    b = [t(44, 106, article, 14, 800, NAVY), t(44, 126, sub, 11, 600, MUTED), t(44, 160, dim1, 11, 700, MUTED)]
    x = 130
    for c in dims1:
        w = 20 + len(c) * 8
        b.append(chip(x, 142, w, c))
        x += w + 8
    b.append(t(44, 198, dim2, 11, 700, MUTED))
    x = 130
    for s in dims2:
        w = 20 + len(s) * 8
        b.append(chip(x, 180, w, s))
        x += w + 8
    b.append('<rect x="44" y="222" width="692" height="30" fill="#e9effa"/>')
    for xx, c, a in [(58, 'Item made', 'start'), (380, 'Code', 'start'), (580, 'Stock', 'end'), (716, 'Price', 'end')]:
        b.append(t(xx, 242, c, 11, 700, NAVY, a))
    y = 274
    for i, (n, code, st, pr) in enumerate(rows):
        if i % 2:
            b.append(f'<rect x="44" y="{y-19}" width="692" height="32" fill="#f7f9fd"/>')
        b += [t(58, y, n, 11.5, 600, INK), t(380, y, code, 10.5, 600, BLUE), t(580, y, st, 11.5, 700, NAVY, 'end'), t(716, y, pr, 11.5, 700, NAVY, 'end')]
        y += 32
    b += ['<rect x="44" y="410" width="420" height="44" rx="12" fill="#ecfdf3"/>', t(60, 437, note, 11, 700, '#15803d'),
          '<rect x="500" y="410" width="236" height="44" rx="14" fill="#FAE814"/>', t(618, 438, btn, 13, 800, NAVY, 'middle')]
    return tablet(clip, title, pill, ''.join(b))


def phone_list(clip, head, sub, rows, btn, tall=True):
    """rows = [(title, line, badge, badge_bg, badge_fg)]"""
    g_ = ['<rect x="14" y="14" width="272" height="104" fill="url(#gBlue)"/>', status_bar(), t(32, 84, head, 15, 700, '#fff'), t(32, 104, sub, 10.5, 500, '#cfe0ff')]
    y = 134
    for a, line, badge, bg, fg in rows:
        g_ += [f'<rect x="26" y="{y}" width="248" height="56" rx="14" fill="#fff" stroke="#e6ebf3"/>', t(40, y + 23, a, 11.5, 700, NAVY), t(40, y + 41, line, 10, 600, MUTED),
               f'<rect x="190" y="{y+17}" width="74" height="22" rx="11" fill="{bg}"/>', t(227, y + 32, badge, 9.5, 800, fg, 'middle')]
        y += 63
    g_ += [f'<rect x="26" y="{y+6}" width="248" height="42" rx="14" fill="#FAE814"/>', t(150, y + 33, btn, 12, 800, NAVY, 'middle')]
    return phone_shell(''.join(g_), clip)


def phone_kv(clip, head, sub, badge, badge_line, rows, btn):
    g_ = ['<rect x="14" y="14" width="272" height="104" fill="url(#gBlue)"/>', status_bar(), t(32, 84, head, 15, 700, '#fff'), t(32, 104, sub, 10.5, 500, '#cfe0ff'),
          '<rect x="26" y="136" width="248" height="64" rx="16" fill="#ecfdf3" stroke="#bfe6cc"/>', t(42, 162, badge, 15, 800, '#15803d'), t(42, 184, badge_line, 10.5, 600, '#15803d')]
    y = 230
    for a, b in rows:
        g_ += [t(36, y, a, 11, 500, MUTED), t(264, y, b, 11, 700, NAVY, 'end'), f'<line x1="36" y1="{y+12}" x2="264" y2="{y+12}" stroke="#e6ebf3"/>']
        y += 34
    g_ += [f'<rect x="26" y="{y+8}" width="248" height="40" rx="14" fill="#FAE814"/>', t(150, y + 34, btn, 12, 800, NAVY, 'middle')]
    return phone_shell(''.join(g_), clip)


def counter_monitor(clip, sub, search, cols, rows, info, cust, pays, active, extra, total):
    W, H = 780, 486
    g_ = monitor_stand(W, H) + screen_open(W, H, clip, 'New Sale', sub)
    g_ += ['<rect x="32" y="76" width="470" height="34" rx="10" fill="#fff" stroke="#dfe6f1"/>', t(48, 98, search, 11.5, 500, '#94a3b8'),
           '<rect x="32" y="122" width="470" height="30" fill="#e9effa"/>']
    for x, c, a in cols:
        g_.append(t(x, 142, c, 11, 700, NAVY, a))
    y = 172
    for i, r in enumerate(rows):
        if i % 2:
            g_.append(f'<rect x="32" y="{y-19}" width="470" height="32" fill="#f7f9fd"/>')
        for (x, _, a), v, k in zip(cols, r, range(4)):
            g_.append(t(x, y, v, 11 if k != 3 else 11.5, 700 if k == 3 else 600, (BLUE if k == 1 and v != '—' else (NAVY if k == 3 else INK)), a))
        y += 32
    g_ += ['<rect x="32" y="312" width="470" height="96" rx="12" fill="#fff" stroke="#e1e7f0"/>', t(48, 338, info[0], 12, 700, BLUE), t(48, 360, info[1], 11, 500, MUTED), t(48, 384, info[2], 11, 600, '#15803d')]
    g_ += ['<rect x="520" y="76" width="228" height="344" rx="14" fill="#fff" stroke="#e1e7f0"/>', t(538, 104, 'Customer', 11, 600, MUTED), t(538, 124, cust, 12.5, 700, NAVY), t(538, 156, 'Pay by', 11, 600, MUTED)]
    x = 538
    for i, lab in enumerate(pays):
        g_ += [f'<rect x="{x}" y="166" width="62" height="28" rx="14" fill="{"#024691" if i == active else "#fff"}" stroke="#c7d7ff"/>', t(x + 31, 185, lab, 11, 700, '#fff' if i == active else BLUE, 'middle')]
        x += 68
    g_ += ['<rect x="532" y="206" width="204" height="44" rx="12" fill="#f3f7ff"/>', t(546, 224, extra[0], 10.5, 700, NAVY), t(546, 241, extra[1], 10, 500, MUTED),
           '<rect x="532" y="258" width="204" height="44" rx="14" fill="#eaf1ff"/>', t(546, 285, 'Total', 12, 600, '#475569'), t(724, 287, total, 18, 800, BLUE, 'end'),
           '<rect x="532" y="312" width="98" height="38" rx="12" fill="#fff" stroke="#c7d7ff"/>', t(581, 336, 'Hold', 12, 700, BLUE, 'middle'),
           '<rect x="638" y="312" width="98" height="38" rx="12" fill="#1E8A43"/>', t(687, 336, 'WhatsApp', 11.5, 700, '#fff', 'middle'),
           '<rect x="532" y="360" width="204" height="40" rx="12" fill="#FAE814"/>', t(634, 385, 'Save &amp; Print', 13, 800, NAVY, 'middle')]
    return ''.join(g_ + screen_close(W, H))


def printer_with(shop, lines, total):
    out = printer80()
    for a, b in [('CITY KIRYANA STORE', shop), ('>Chakki Atta 10 kg<', f'>{lines[0][0]}<'), ('>Sugar 2.5 kg<', f'>{lines[1][0]}<'), ('>Cooking Oil 1 L x2<', f'>{lines[2][0]}<'),
                 ('>1,200<', f'>{lines[0][1]}<'), ('>400<', f'>{lines[1][1]}<'), ('>1,180<', f'>{lines[2][1]}<'), ('>Rs 4,200<', f'>{total}<')]:
        out = out.replace(a, b)
    return out


# ================================================================= SHOES
def shoe_variants():
    return variant_tablet('cpShV', 'Variant Generator', 'Colour x Size', 'Article SH-412 · Men\'s Peshawari Chappal', 'Sale price Rs 3,950 · Cost Rs 2,450',
                          'Colours', ['Brown', 'Black'], 'Sizes', ['39', '40', '41', '42', '43', '44'],
                          [('SH-412 Brown / 40', '412-BR-40', '5', 'Rs 3,950'), ('SH-412 Brown / 42', '412-BR-42', '8', 'Rs 3,950'),
                           ('SH-412 Black / 41', '412-BK-41', '6', 'Rs 3,950'), ('SH-412 Black / 44', '412-BK-44', '2', 'Rs 3,950')],
                          '2 colours x 6 sizes = 12 items, each with its own pairs', 'Create 12 items')


def shoe_size_phone():
    return phone_list('cpShS', 'SH-412 Brown', 'Pairs left in each size', [
        ('Size 40', 'Last sold today', '5 pairs', '#ecfdf3', '#15803d'), ('Size 41', 'Low stock alert', '1 pair', '#fffbeb', '#92400e'),
        ('Size 42', 'Best seller this week', '8 pairs', '#ecfdf3', '#15803d'), ('Size 43', 'Sold out yesterday', 'Out', '#fef2f2', '#b91c1c')], 'Add 41 and 43 to demand list')


def shoe_exchange_phone():
    return phone_list('cpShX', 'Edit bill INV-7731', 'Same bill number after the change', [
        ('Joggers JG-88 White / 41', 'Rs 4,500', 'Returned', '#fef2f2', '#b91c1c'), ('Joggers JG-88 White / 42', 'Rs 4,500', 'Added', '#ecfdf3', '#15803d'),
        ('Balance', 'Size 41 back in stock', 'Rs 0', '#eaf1ff', BLUE)], 'Save and print')


def shoe_monitor():
    return counter_monitor('cpMonSh', 'Shoe Counter', 'Scan the box label or search article, colour, size',
                           [(46, 'Item', 'start'), (250, 'Colour / Size', 'start'), (400, 'Qty', 'middle'), (488, 'Amount', 'end')],
                           [('Peshawari SH-412', 'Brown / 42', '1', '3,950'), ('Joggers JG-88', 'White / 42', '1', '4,500'),
                            ('Kids School Shoe KS-20', 'Black / 2', '2', '4,200'), ('Shoe Polish Black', '—', '1', '350')],
                           ('Brown / 42: 7 pairs left', 'Brown / 41 has 1 pair · 43 is out', 'Sold by Bilal · his own staff login'),
                           'Hamid Raza · 0301 2345678', ['Cash', 'Bank', 'Udhaar'], 0, ('Discount Rs 300', 'On this bill'), 'Rs 12,700')


def scene_shoe_process():
    return five_steps([
        ('Make sizes', mini_ui('Variant Generator', [('Article', 'SH-412'), ('Colours', '2'), ('Sizes', '39 to 44')], '12 items created'), 'Colour x size in one go'),
        ('Receive pairs', mini_ui('GRN · Peshawar Footwear', [('Brown / 42', '8 pairs'), ('Black / 41', '6 pairs'), ('Brown / 44', '4 pairs')], 'Cost Rs 2,450 a pair'), 'Pairs per size'),
        ('Label boxes', mini_ui('Barcode labels', [('SH-412 Brown / 42', 'x8'), ('SH-412 Black / 41', 'x6'), ('Price on label', 'Rs 3,950')], '18 labels ready', '#eaf1ff', BLUE), 'Size and price on box'),
        ('Swap a size', mini_ui('Edit bill INV-7731', [('White / 41', 'Returned'), ('White / 42', 'Added'), ('Balance', 'Rs 0')], 'Same bill number'), 'No new bill needed'),
        ('See profit', ui_report("Today's sales", 'Rs 1,12,600', '31 pairs · 2 size swaps · polish and socks'), 'Pairs, stock and profit'),
    ])


# ================================================================= VEHICLE SHOWROOM
def vehicle_variants():
    return variant_tablet('cpVhV', 'Variant Generator', 'Model year x Colour', 'Motorcycle 125cc Deluxe · Self start', 'Group: Motorcycles · Sale price Rs 2,85,000',
                          'Model year', ['2026', '2027'], 'Colours', ['Red', 'Black', 'Blue'],
                          [('125 Deluxe 2026 / Red', 'MC125-26-RD', '4', 'Rs 2,85,000'), ('125 Deluxe 2026 / Black', 'MC125-26-BK', '6', 'Rs 2,85,000'),
                           ('125 Deluxe 2027 / Red', 'MC125-27-RD', '3', 'Rs 2,95,000'), ('125 Deluxe 2027 / Blue', 'MC125-27-BL', '2', 'Rs 2,95,000')],
                          '2 years x 3 colours = 6 items, each with its own units', 'Create 6 items')


def vehicle_chassis_phone():
    return phone_kv('cpVhC', 'Chassis lookup', 'Chassis no. PK125-DX-4471-88', 'In warranty', 'Until 14 Oct 2027 · 12 months left',
                    [('Unit', '125 Deluxe 2026 / Black'), ('Sold on', '14 Oct 2026'), ('Invoice', 'INV-1208 (A4)'), ('Customer', 'Usman Ali'), ('Bought from', 'Sahiwal Motors Dist.'),
                     ('Purchase', 'GRN-311 · 02 Oct')], 'Open the bill')


def vehicle_qist_phone():
    g_ = ['<rect x="14" y="14" width="272" height="150" fill="url(#gBlue)"/>', status_bar(), t(32, 80, 'Installment plan · Usman Ali', 12, 500, '#cfe0ff'),
          t(32, 114, 'Rs 2,10,100', 28, 800, '#fff'), t(32, 140, 'left · 1 of 12 paid · advance Rs 75,000', 11, 500, '#cfe0ff'),
          '<rect x="26" y="176" width="248" height="46" rx="14" fill="#f3f7ff" stroke="#c7d7ff"/>', t(40, 196, 'Guarantor: Imran Khan', 11, 700, NAVY), t(40, 212, 'CNIC and phone saved', 10, 600, MUTED)]
    y = 232
    for m, a, st, bg, fg in [('Nov 2026', 'Rs 19,100', 'Paid', '#ecfdf3', '#15803d'), ('Dec 2026', 'Rs 19,100', 'Due 14 Dec', '#fffbeb', '#92400e'),
                             ('Jan 2027', 'Rs 19,100', 'Upcoming', '#eef1f6', '#475569')]:
        g_ += [f'<rect x="26" y="{y}" width="248" height="56" rx="14" fill="#fff" stroke="#e6ebf3"/>', t(40, y + 23, m, 12, 700, NAVY), t(40, y + 41, a, 10.5, 600, MUTED),
               f'<rect x="186" y="{y+17}" width="78" height="22" rx="11" fill="{bg}"/>', t(225, y + 32, st, 9.5, 800, fg, 'middle')]
        y += 63
    g_ += [f'<rect x="26" y="{y+6}" width="248" height="42" rx="14" fill="#FAE814"/>', t(150, y + 33, 'Receive payment', 12, 800, NAVY, 'middle')]
    return phone_shell(''.join(g_), 'cpVhQ')


def vehicle_monitor():
    return counter_monitor('cpMonVh', 'Showroom', 'Search model or scan the chassis number',
                           [(46, 'Unit', 'start'), (236, 'Chassis no.', 'start'), (400, 'Year', 'middle'), (488, 'Amount', 'end')],
                           [('125 Deluxe / Black', 'PK125-DX-4471-88', '2026', '2,85,000'), ('Helmet Full Face', '—', '—', '4,500'),
                            ('Engine Oil 1 L', '—', '—', '1,450'), ('Number Plate Frame', '—', '—', '850')],
                           ('Chassis PK125-DX-4471-88', 'In stock since GRN-311 · Sahiwal Motors Dist.', '125 Deluxe 2026 / Black · 5 more in stock'),
                           'Usman Ali · 0345 6789012', ['Cash', 'Bank', 'Qist'], 2, ('Advance Rs 75,000', '12 months · Rs 19,100 a month'), 'Rs 2,91,800')


def scene_vehicle_process():
    return five_steps([
        ('Send a quote', mini_ui('Quotation QT-0431', [('125 Deluxe 2026', '2,85,000'), ('Helmet', '4,500'), ('Valid till', '30 Oct')], 'Sent on WhatsApp', '#eaf1ff', BLUE), 'A4 quote, then sale'),
        ('Receive units', mini_ui('GRN · Sahiwal Motors', [('125 Deluxe / Black', '6 units'), ('PK125-DX-4471-88', 'saved'), ('+ 5 more chassis', '')], 'Chassis of every unit'), 'Chassis on the GRN'),
        ('Cash or qist', mini_ui('Qist plan · 12 months', [('Advance', 'Rs 75,000'), ('Monthly', 'Rs 19,100'), ('Guarantor', 'Imran Khan')], 'Next due 14 Dec', '#fffbeb', '#92400e'), 'Advance and guarantor'),
        ('Warranty check', mini_ui('Chassis lookup', [('Sold', '14 Oct 2026'), ('Invoice', 'INV-1208'), ('Warranty', 'till Oct 2027')], 'In warranty'), 'Find any sold unit'),
        ('See profit', ui_report('This month', 'Rs 38,40,000', '13 units · Rs 4,20,000 qist to collect'), 'Units, qist and profit'),
    ])


SCENES = {
    'uptrendpos-shoe-store-size-variants': ('Every Size and Colour', 'blue', lambda: g(shoe_variants(), 210, 150, 1.0),
        [(60, 770, 'Colour x size in one go', '#2F7BD9'), (330, 770, 'Pairs for each size', '#2FA455')]),
    'uptrendpos-shoe-store-size-stock-exchange': ('Size Stock and Easy Swap', 'green', lambda: g(shoe_size_phone(), 230, 140, 1.0) + g(shoe_exchange_phone(), 680, 140, 1.0),
        [(60, 780, 'Pairs left in each size', '#2F7BD9'), (440, 780, 'Size swap on the same bill', '#2FA455')]),
    'uptrendpos-shoe-store-pos-hardware': ('Shoe Shop Hardware', 'yellow',
        lambda: hardware_scene(shoe_monitor, lambda: printer_with('CITY SHOE HOUSE', [('Peshawari Brown/42', '3,950'), ('Joggers White/42', '4,500'), ('School Shoe x2', '4,200')], 'Rs 12,700'),
                               shoe_size_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-shoe-store-pos-process': ('Shoe Sale, Step by Step', 'navy', scene_shoe_process, [(60, 470, 'All connected', '#2FA455')]),
    'uptrendpos-vehicle-showroom-model-variants': ('Every Model and Colour', 'navy', lambda: g(vehicle_variants(), 210, 150, 1.0),
        [(60, 770, 'Model year x colour', '#2F7BD9'), (300, 770, 'Bikes, EVs, cars, rickshaws', '#F59E0B')]),
    'uptrendpos-vehicle-showroom-chassis-installments': ('Chassis, Warranty and Qist', 'teal', lambda: g(vehicle_chassis_phone(), 230, 140, 1.0) + g(vehicle_qist_phone(), 680, 140, 1.0),
        [(60, 780, 'Warranty lookup by chassis', '#2FA455'), (450, 780, 'Qist with a guarantor', '#F59E0B')]),
    'uptrendpos-vehicle-showroom-pos-hardware': ('Hardware for a Showroom', 'blue',
        lambda: hardware_scene(vehicle_monitor, lambda: printer_with('CITY MOTORS', [('125 Deluxe Black', '2,85,000'), ('Helmet', '4,500'), ('Engine Oil', '1,450')], 'Rs 2,91,800'),
                               vehicle_qist_phone, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'A4 invoice ready', '#2FA455')]),
    'uptrendpos-vehicle-showroom-pos-process': ('Showroom Sale, Step by Step', 'yellow', scene_vehicle_process, [(60, 470, 'All connected', '#2FA455')]),
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
