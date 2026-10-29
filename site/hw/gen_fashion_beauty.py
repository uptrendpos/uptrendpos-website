"""Clothing & Garments + Cosmetics & Beauty page images (same house style and watermark as gen_ind.py).
Run: python3 gen_fashion_beauty.py [name ...]"""
import asyncio, sys
from playwright.async_api import async_playwright
from PIL import Image
from gen_ind import (B, OUT, t, shadow, phone_shell, status_bar, frame, g, pcard, arrow, circle_badge,
                     printer80, scanner_small, mini_printer_usb)
from gen_tailor_mobile import screen_open, monitor_stand, screen_close

NAVY, BLUE, MUTED, INK = '#10224A', '#024691', '#64748b', '#1e293b'


def tablet(clip, title, pill, body):
    """Tablet on a stand with a navy app bar (same frame as the catalog tablets)."""
    W, H = 780, 500
    return ''.join([shadow(390, 600, 380, 30), '<polygon points="430,300 490,300 590,590 548,596" fill="#2a313d"/>',
                    '<rect x="530" y="588" width="70" height="10" rx="5" fill="#1b212b"/>',
                    f'<rect x="0" y="0" width="{W}" height="{H}" rx="40" fill="#111827"/>', '<rect x="22" y="26" width="736" height="452" rx="16" fill="#f3f6fb"/>',
                    f'<clipPath id="{clip}"><rect x="22" y="26" width="736" height="452" rx="16"/></clipPath><g clip-path="url(#{clip})">',
                    '<rect x="22" y="26" width="736" height="52" fill="url(#gNavy)"/>', t(44, 58, title, 16, 700, '#fff'),
                    '<rect x="540" y="38" width="200" height="28" rx="14" fill="#fff" fill-opacity=".2"/>', t(640, 57, pill, 12, 700, '#fff', 'middle'),
                    body, '</g>', '<rect x="22" y="26" width="736" height="452" rx="16" fill="url(#gGlass)"/>'])


def chip(x, y, w, label, on=True, fill_on='#024691'):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="14" fill="{fill_on if on else "#fff"}" stroke="#c7d7ff"/>'
            + t(x + w / 2, y + 19, label, 11, 700, '#fff' if on else BLUE, 'middle'))


# ================================================================= CLOTHING
def tablet_variants():
    b = [t(44, 106, 'Article LP-2207 · Lawn 3-Piece', 14, 800, NAVY), t(44, 126, 'Sale price Rs 4,950 · Cost Rs 3,100', 11, 600, MUTED),
         t(44, 160, 'Colours', 11, 700, MUTED)]
    x = 110
    for c, sw in [('Maroon', '#7f1d1d'), ('Teal', '#0f766e'), ('Black', '#111827')]:
        b += [chip(x, 142, 96, c), f'<circle cx="{x+14}" cy="156" r="6" fill="{sw}" stroke="#fff"/>']
        x += 104
    b += [t(44, 198, 'Sizes', 11, 700, MUTED)]
    x = 110
    for s in ['S', 'M', 'L', 'XL']:
        b.append(chip(x, 180, 58, s))
        x += 66
    b += ['<rect x="44" y="222" width="692" height="30" fill="#e9effa"/>']
    for xx, c, a in [(58, 'Item made', 'start'), (360, 'Barcode', 'start'), (560, 'Stock', 'end'), (716, 'Price', 'end')]:
        b.append(t(xx, 242, c, 11, 700, NAVY, a))
    y = 274
    for i, (n, bc, st) in enumerate([('LP-2207 Maroon / S', '2207-MR-S', '6'), ('LP-2207 Maroon / M', '2207-MR-M', '9'),
                                     ('LP-2207 Teal / L', '2207-TL-L', '7'), ('LP-2207 Black / XL', '2207-BK-XL', '4')]):
        if i % 2:
            b.append(f'<rect x="44" y="{y-19}" width="692" height="32" fill="#f7f9fd"/>')
        b += [t(58, y, n, 11.5, 600, INK), t(360, y, bc, 10.5, 600, BLUE), t(560, y, st, 11.5, 700, NAVY, 'end'), t(716, y, 'Rs 4,950', 11.5, 700, NAVY, 'end')]
        y += 32
    b += ['<rect x="44" y="410" width="400" height="44" rx="12" fill="#ecfdf3"/>', t(60, 437, '3 colours x 4 sizes = 12 items, each with its own stock', 11, 700, '#15803d'),
          '<rect x="500" y="410" width="236" height="44" rx="14" fill="#FAE814"/>', t(618, 438, 'Create 12 items', 13, 800, NAVY, 'middle')]
    return tablet('cpVar', 'Variant Generator', 'Colour x Size', ''.join(b))


def tag_sheet():
    """A strip of 4 price tags with barcode, size and colour."""
    out = [f'<rect x="0" y="0" width="300" height="430" rx="18" fill="#fff" filter="url(#fDrop)"/>', t(150, 34, 'Barcode labels', 14, 800, NAVY, 'middle')]
    y = 56
    for n, s in [('Maroon', 'S'), ('Maroon', 'M'), ('Teal', 'L'), ('Black', 'XL')]:
        out += [f'<rect x="20" y="{y}" width="260" height="84" rx="10" fill="#fafbfe" stroke="#dbe3ef" stroke-dasharray="4 3"/>',
                t(34, y + 22, 'LP-2207 Lawn 3-Piece', 11, 700, INK), t(34, y + 40, f'{n} · Size {s}', 10.5, 600, MUTED),
                t(266, y + 22, 'Rs 4,950', 12, 800, NAVY, 'end')]
        bx = 34
        for k in range(34):
            w = 1.6 if (k * 7) % 5 else 3
            out.append(f'<rect x="{bx}" y="{y+50}" width="{w}" height="24" fill="#111"/>')
            bx += w + 1.8
        y += 92
    return ''.join(out)


def phone_exchange():
    g_ = ['<rect x="14" y="14" width="272" height="104" fill="url(#gBlue)"/>', status_bar(), t(32, 84, 'Edit bill INV-5120', 15, 700, '#fff'),
          t(32, 104, 'Same bill number after the change', 10.5, 500, '#cfe0ff')]
    y = 140
    for a, b, c in [('Kurta LK-118 Navy / M', 'Returned', '#b91c1c'), ('Kurta LK-118 Navy / L', 'Added', '#15803d')]:
        g_ += [f'<rect x="26" y="{y}" width="248" height="58" rx="14" fill="#fff" stroke="#e6ebf3"/>', t(40, y + 24, a, 11.5, 700, NAVY),
               t(40, y + 43, 'Rs 2,450', 10.5, 600, MUTED), f'<rect x="188" y="{y+16}" width="76" height="24" rx="12" fill="#f8fafc" stroke="#e2e8f0"/>',
               t(226, y + 32, b, 10, 800, c, 'middle')]
        y += 68
    g_ += [f'<rect x="26" y="{y+4}" width="248" height="56" rx="14" fill="#ecfdf3" stroke="#bfe6cc"/>', t(42, y + 28, 'Balance Rs 0', 14, 800, '#15803d'),
           t(42, y + 48, 'Stock: M back on the shelf, L out', 10.5, 600, '#15803d'),
           f'<rect x="26" y="{y+74}" width="248" height="42" rx="14" fill="#FAE814"/>', t(150, y + 101, 'Save and print', 12, 800, NAVY, 'middle')]
    return phone_shell(''.join(g_), 'cpExch')


def monitor_clothing():
    W, H = 780, 486
    g_ = monitor_stand(W, H) + screen_open(W, H, 'cpMonC', 'New Sale', 'Garments Counter')
    g_ += ['<rect x="32" y="76" width="470" height="34" rx="10" fill="#fff" stroke="#dfe6f1"/>', t(48, 98, 'Scan the tag or search article, colour, size', 11.5, 500, '#94a3b8'),
           '<rect x="32" y="122" width="470" height="30" fill="#e9effa"/>']
    for x, c, a in [(46, 'Item', 'start'), (250, 'Colour / Size', 'start'), (400, 'Qty', 'middle'), (488, 'Amount', 'end')]:
        g_.append(t(x, 142, c, 11, 700, NAVY, a))
    rows = [('Lawn 3-Piece LP-2207', 'Teal / L', '1', '4,950'), ('Kurta LK-118', 'Navy / M', '2', '4,900'),
            ('Dupatta Chiffon DP-31', 'Black / Free', '1', '1,350'), ('Kids Frock KF-09', 'Pink / 4-5Y', '1', '1,800')]
    y = 172
    for i, (n, s, q, a) in enumerate(rows):
        if i % 2:
            g_.append(f'<rect x="32" y="{y-19}" width="470" height="32" fill="#f7f9fd"/>')
        g_ += [t(46, y, n, 11, 600, INK), t(250, y, s, 10.5, 600, BLUE), t(400, y, q, 11, 600, INK, 'middle'), t(488, y, a, 11.5, 700, NAVY, 'end')]
        y += 32
    g_ += ['<rect x="32" y="312" width="470" height="96" rx="12" fill="#fff" stroke="#e1e7f0"/>', t(48, 338, 'Teal / L: 6 left in this branch', 12, 700, BLUE),
           t(48, 360, 'Maroon / L sold out · Teal / M 3 left', 11, 500, MUTED), t(48, 384, 'Sold by Usman · his own staff login', 11, 600, '#15803d')]
    g_ += ['<rect x="520" y="76" width="228" height="344" rx="14" fill="#fff" stroke="#e1e7f0"/>',
           t(538, 104, 'Customer', 11, 600, MUTED), t(538, 124, 'Sana Tariq · 0300 1234567', 12.5, 700, NAVY), t(538, 156, 'Pay by', 11, 600, MUTED)]
    x = 538
    for i, lab in enumerate(['Cash', 'Bank', 'Udhaar']):
        g_ += [f'<rect x="{x}" y="166" width="62" height="28" rx="14" fill="{"#024691" if i == 0 else "#fff"}" stroke="#c7d7ff"/>', t(x + 31, 185, lab, 11, 700, '#fff' if i == 0 else BLUE, 'middle')]
        x += 68
    g_ += ['<rect x="532" y="206" width="204" height="44" rx="12" fill="#f3f7ff"/>', t(546, 224, 'Discount Rs 500', 10.5, 700, NAVY), t(546, 241, 'On this bill', 10, 500, MUTED),
           '<rect x="532" y="258" width="204" height="44" rx="14" fill="#eaf1ff"/>', t(546, 285, 'Total', 12, 600, '#475569'), t(724, 287, 'Rs 12,500', 18, 800, BLUE, 'end'),
           '<rect x="532" y="312" width="98" height="38" rx="12" fill="#fff" stroke="#c7d7ff"/>', t(581, 336, 'Hold', 12, 700, BLUE, 'middle'),
           '<rect x="638" y="312" width="98" height="38" rx="12" fill="#1E8A43"/>', t(687, 336, 'WhatsApp', 11.5, 700, '#fff', 'middle'),
           '<rect x="532" y="360" width="204" height="40" rx="12" fill="#FAE814"/>', t(634, 385, 'Save &amp; Print', 13, 800, NAVY, 'middle')]
    return ''.join(g_ + screen_close(W, H))


def printer_cloth():
    out = printer80()
    for a, b in [('CITY KIRYANA STORE', 'CITY FASHION HOUSE'), ('>Chakki Atta 10 kg<', '>Lawn 3-Pc Teal/L<'), ('>Sugar 2.5 kg<', '>Kurta Navy/M x2<'),
                 ('>Cooking Oil 1 L x2<', '>Dupatta Black<'), ('>1,200<', '>4,950<'), ('>400<', '>4,900<'), ('>1,180<', '>1,350<'), ('>Rs 4,200<', '>Rs 12,500<')]:
        out = out.replace(a, b)
    return out


def mini_ui(title, rows, foot=None, foot_bg='#ecfdf3', foot_fg='#15803d'):
    g_ = ['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>', '<rect width="260" height="38" rx="16" fill="url(#gNavy)"/><rect y="22" width="260" height="16" fill="#1a3a74"/>',
          t(14, 25, title, 12, 700, '#fff')]
    y = 62
    for a, b in rows:
        g_ += [t(14, y, a, 10.5, 600, MUTED if b else NAVY), t(246, y, b, 11, 700, NAVY, 'end')]
        y += 24
    if foot:
        g_ += [f'<rect x="14" y="150" width="232" height="30" rx="9" fill="{foot_bg}"/>', t(26, 170, foot, 10.5, 700, foot_fg)]
    return ''.join(g_)


def ui_report(top, big, sub):
    g_ = ['<rect width="260" height="190" rx="16" fill="url(#gBlue)"/>', t(14, 28, top, 11, 500, '#cfe0ff'), t(14, 56, big, 22, 800, '#fff'),
          t(14, 76, sub, 9.5, 500, '#cfe0ff'), '<rect x="14" y="88" width="232" height="90" rx="12" fill="#fff"/>']
    for i, h in enumerate([40, 52, 36, 60, 46, 66, 56]):
        g_.append(f'<rect x="{30+i*31}" y="{168-h}" width="18" height="{h}" rx="4" fill="url(#gBar)"/>')
    return ''.join(g_)


def five_steps(cards):
    y1, y2 = 120, 520
    (a, b, c, d, e) = cards
    return ''.join([pcard(60, y1, 1, *a), pcard(450, y1, 2, *b), pcard(840, y1, 3, *c), pcard(645, y2, 4, *d), pcard(255, y2, 5, *e),
                    arrow('M368,280 L436,280', 'M424,268 L438,280 L424,292'), arrow('M758,280 L826,280', 'M814,268 L828,280 L814,292'),
                    arrow('M990,446 C990,500 960,560 952,600', 'M942,588 L951,604 L965,592'), arrow('M640,680 L566,680', 'M578,668 L564,680 L578,692')])


def scene_clothing_process():
    return five_steps([
        ('Make items', mini_ui('Variant Generator', [('Article', 'LP-2207'), ('Colours', '3'), ('Sizes', 'S M L XL')], '12 items created'), 'Colour x size in one go'),
        ('Receive stock', mini_ui('GRN · Lahore Textiles', [('Teal / L', '8 pcs'), ('Maroon / M', '10 pcs'), ('Black / XL', '6 pcs')], 'Cost Rs 3,100 each'), 'Stock per size and colour'),
        ('Print tags', mini_ui('Barcode labels', [('LP-2207 Teal / L', 'x8'), ('LP-2207 Maroon / M', 'x10'), ('Price on tag', 'Rs 4,950')], '24 tags ready', '#eaf1ff', BLUE), 'Barcode, size, price'),
        ('Exchange a size', mini_ui('Edit bill INV-5120', [('Navy / M', 'Returned'), ('Navy / L', 'Added'), ('Balance', 'Rs 0')], 'Same bill number'), 'No new bill, no mess'),
        ('See profit', ui_report("Today's sales", 'Rs 1,86,400', '64 pieces · 3 exchanges · 2 salesmen'), 'Sales, stock and profit'),
    ])


def hardware_scene(monitor, printer, phone, labels, scan_label='Barcode scanner'):
    body = ['<circle cx="600" cy="300" r="232" fill="#dcebff" opacity=".75"/>',
            '<circle cx="600" cy="300" r="232" fill="none" stroke="#bfd6f5" stroke-width="2" stroke-dasharray="6 9"/>',
            g(printer(), 372, 300, .34), g(monitor(), 446, 150, .4), g(scanner_small(), 740, 352, .3, -22, 180, 180), g(phone(), 770, 196, .26)]
    xs = [150, 375, 600, 825, 1050]
    body.append('<path d="M600,532 L600,580" stroke="#2F7BD9" stroke-width="3" fill="none"/>')
    body.append(f'<path d="M{xs[0]},630 L{xs[0]},600 Q{xs[0]},580 {xs[0]+20},580 L{xs[-1]-20},580 Q{xs[-1]},580 {xs[-1]},600 L{xs[-1]},630" stroke="#2F7BD9" stroke-width="3" fill="none"/>')
    for x in xs[1:-1]:
        body.append(f'<path d="M{x},580 L{x},630" stroke="#2F7BD9" stroke-width="3" fill="none"/>')
    cy, r = 712, 82
    inners = [g(monitor(), xs[0] - 59, cy - 46, .15, flt=False), g(scanner_small(), xs[1] - 45, cy - 48, .26, -22, 180, 180, flt=False),
              g(printer(), xs[2] - 51, cy - 54, .22, flt=False), g(phone(), xs[3] - 26, cy - 53, .17, flt=False),
              g(mini_printer_usb(), xs[4] - 45, cy - 48, .3, flt=False)]
    for x, inner, lab in zip(xs, inners, labels):
        body.append(circle_badge(x, cy, r, inner, lab))
    return ''.join(body)


# ================================================================= COSMETICS
def tablet_beauty_catalog():
    b = ['<rect x="44" y="94" width="692" height="38" rx="12" fill="#fff" stroke="#dfe6f1"/>', t(64, 118, 'lipstick', 13, 600, NAVY), t(716, 118, '86 results', 11, 500, MUTED, 'end')]
    rows = [('Matte Lipstick Shade 04 Rose', 'Makeup · Shade', 'Lips', True), ('Matte Lipstick Shade 11 Brick', 'Makeup · Shade', 'Lips', True),
            ('Lip Gloss Clear 6ml', 'Makeup', 'Lips', False), ('Lipstick Remover Wipes x25', 'Skin care', 'Care', False),
            ('Liquid Lipstick Shade 07 Nude', 'Makeup · Shade', 'Lips', True)]
    y = 146
    for n, sub, cls, on in rows:
        b += [f'<rect x="44" y="{y}" width="692" height="44" rx="12" fill="{"#eef5ff" if on else "#fff"}" stroke="{"#c7d7ff" if on else "#e3e9f2"}"/>',
              f'<rect x="58" y="{y+12}" width="20" height="20" rx="6" fill="{"#024691" if on else "#fff"}" stroke="#bcc9dc"/>',
              (f'<path d="M62,{y+22} l4,4 7,-8" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>' if on else ''),
              t(94, y + 20, n, 12.5, 700, NAVY), t(94, y + 36, sub, 10.5, 500, MUTED),
              f'<rect x="612" y="{y+12}" width="106" height="20" rx="10" fill="#fdf2f8"/>', t(665, y + 26, cls, 10, 600, '#9d174d', 'middle')]
        y += 50
    b += ['<rect x="500" y="424" width="236" height="44" rx="14" fill="#FAE814"/>', t(618, 452, 'Add 3 to my shop', 13, 800, NAVY, 'middle'),
          t(64, 452, 'Not in the list? Add your own product.', 11.5, 600, BLUE)]
    return tablet('cpBCat', 'Beauty &amp; Cosmetics Catalog', '5,000+ products', ''.join(b))


def phone_shades():
    g_ = ['<rect x="14" y="14" width="272" height="104" fill="url(#gBlue)"/>', status_bar(), t(32, 84, 'Matte Lipstick', 15, 700, '#fff'),
          t(32, 104, 'Shades in stock · Rs 1,250 each', 10.5, 500, '#cfe0ff')]
    y = 134
    for n, sw, st, low in [('Shade 01 Red', '#b91c1c', '14', False), ('Shade 04 Rose', '#e11d48', '9', False), ('Shade 07 Nude', '#c2856b', '2', True),
                           ('Shade 11 Brick', '#9a3412', '11', False), ('Shade 15 Plum', '#6b21a8', '0', True)]:
        g_ += [f'<rect x="26" y="{y}" width="248" height="46" rx="14" fill="#fff" stroke="#e6ebf3"/>', f'<circle cx="50" cy="{y+23}" r="11" fill="{sw}"/>',
               t(70, y + 28, n, 11.5, 700, NAVY), f'<rect x="200" y="{y+12}" width="64" height="22" rx="11" fill="{"#fffbeb" if low else "#ecfdf3"}"/>',
               t(232, y + 27, (st + ' left') if st != '0' else 'Out', 9.5, 800, '#92400e' if low else '#15803d', 'middle')]
        y += 52
    g_ += [f'<rect x="26" y="{y+6}" width="248" height="40" rx="14" fill="#FAE814"/>', t(150, y + 32, 'Add to demand list', 12, 800, NAVY, 'middle')]
    return phone_shell(''.join(g_), 'cpShade')


def phone_expiry():
    g_ = ['<rect x="14" y="14" width="272" height="150" fill="url(#gBlue)"/>', status_bar(), t(32, 80, 'Expiry alerts', 12, 500, '#cfe0ff'),
          t(32, 114, '6 batches', 28, 800, '#fff'), t(32, 140, 'expire in the next 30 days', 11, 500, '#cfe0ff')]
    y = 182
    for n, bt, d, bg, fg in [('Sunblock SPF 50 · 60ml', 'Batch SB-224', '12 days', '#fffbeb', '#92400e'), ('Face Wash Neem 100ml', 'Batch FW-19', '21 days', '#fffbeb', '#92400e'),
                             ('Night Cream 50g', 'Batch NC-07', 'Expired', '#fef2f2', '#b91c1c'), ('Hair Serum 100ml', 'Batch HS-33', '28 days', '#fffbeb', '#92400e')]:
        g_ += [f'<rect x="26" y="{y}" width="248" height="58" rx="14" fill="#fff" stroke="#e6ebf3"/>', t(40, y + 24, n, 11.5, 700, NAVY), t(40, y + 42, bt, 10.5, 600, MUTED),
               f'<rect x="188" y="{y+18}" width="76" height="22" rx="11" fill="{bg}"/>', t(226, y + 33, d, 9.5, 800, fg, 'middle')]
        y += 66
    g_ += [f'<rect x="26" y="{y+6}" width="248" height="44" rx="14" fill="#FAE814"/>', t(150, y + 34, 'Sell first or return', 12, 800, NAVY, 'middle')]
    return phone_shell(''.join(g_), 'cpExp')


def monitor_beauty():
    W, H = 780, 486
    g_ = monitor_stand(W, H) + screen_open(W, H, 'cpMonB', 'New Sale', 'Beauty Counter')
    g_ += ['<rect x="32" y="76" width="470" height="34" rx="10" fill="#fff" stroke="#dfe6f1"/>', t(48, 98, 'Scan barcode or search product, shade, brand', 11.5, 500, '#94a3b8'),
           '<rect x="32" y="122" width="470" height="30" fill="#e9effa"/>']
    for x, c, a in [(46, 'Item', 'start'), (270, 'Shade / Batch', 'start'), (400, 'Qty', 'middle'), (488, 'Amount', 'end')]:
        g_.append(t(x, 142, c, 11, 700, NAVY, a))
    rows = [('Matte Lipstick', 'Shade 04 Rose', '1', '1,250'), ('Liquid Foundation 30ml', 'Shade 220 Beige', '1', '2,800'),
            ('Face Wash Neem 100ml', 'Batch FW-21', '2', '1,300'), ('Kohl Pencil Black', 'Batch KP-08', '1', '450')]
    y = 172
    for i, (n, s, q, a) in enumerate(rows):
        if i % 2:
            g_.append(f'<rect x="32" y="{y-19}" width="470" height="32" fill="#f7f9fd"/>')
        g_ += [t(46, y, n, 11, 600, INK), t(270, y, s, 10.5, 600, BLUE), t(400, y, q, 11, 600, INK, 'middle'), t(488, y, a, 11.5, 700, NAVY, 'end')]
        y += 32
    g_ += ['<rect x="32" y="312" width="470" height="96" rx="12" fill="#fff" stroke="#e1e7f0"/>', t(48, 338, 'Batch and expiry kept with the stock', 12, 700, BLUE),
           t(48, 360, 'Face Wash Neem · Batch FW-21 · expires Mar 2027', 11, 500, MUTED), t(48, 384, 'Shade 04 Rose · 8 left after this sale', 11, 600, '#15803d')]
    g_ += ['<rect x="520" y="76" width="228" height="344" rx="14" fill="#fff" stroke="#e1e7f0"/>',
           t(538, 104, 'Customer', 11, 600, MUTED), t(538, 124, 'Ayesha Khan · 0333 7654321', 12.5, 700, NAVY), t(538, 156, 'Pay by', 11, 600, MUTED)]
    x = 538
    for i, lab in enumerate(['Cash', 'Bank', 'Udhaar']):
        g_ += [f'<rect x="{x}" y="166" width="62" height="28" rx="14" fill="{"#024691" if i == 1 else "#fff"}" stroke="#c7d7ff"/>', t(x + 31, 185, lab, 11, 700, '#fff' if i == 1 else BLUE, 'middle')]
        x += 68
    g_ += ['<rect x="532" y="206" width="204" height="44" rx="12" fill="#f3f7ff"/>', t(546, 224, 'Discount Rs 300', 10.5, 700, NAVY), t(546, 241, 'Regular customer', 10, 500, MUTED),
           '<rect x="532" y="258" width="204" height="44" rx="14" fill="#eaf1ff"/>', t(546, 285, 'Total', 12, 600, '#475569'), t(724, 287, 'Rs 5,500', 18, 800, BLUE, 'end'),
           '<rect x="532" y="312" width="98" height="38" rx="12" fill="#fff" stroke="#c7d7ff"/>', t(581, 336, 'Hold', 12, 700, BLUE, 'middle'),
           '<rect x="638" y="312" width="98" height="38" rx="12" fill="#1E8A43"/>', t(687, 336, 'WhatsApp', 11.5, 700, '#fff', 'middle'),
           '<rect x="532" y="360" width="204" height="40" rx="12" fill="#FAE814"/>', t(634, 385, 'Save &amp; Print', 13, 800, NAVY, 'middle')]
    return ''.join(g_ + screen_close(W, H))


def printer_beauty():
    out = printer80()
    for a, b in [('CITY KIRYANA STORE', 'GLOW BEAUTY STORE'), ('>Chakki Atta 10 kg<', '>Matte Lipstick 04<'), ('>Sugar 2.5 kg<', '>Foundation 220<'),
                 ('>Cooking Oil 1 L x2<', '>Face Wash x2<'), ('>1,200<', '>1,250<'), ('>400<', '>2,800<'), ('>1,180<', '>1,300<'), ('>Rs 4,200<', '>Rs 5,500<')]:
        out = out.replace(a, b)
    return out


def scene_beauty_process():
    return five_steps([
        ('Pick products', mini_ui('Beauty catalog', [('Matte Lipstick 04', 'Ticked'), ('Foundation 220', 'Ticked'), ('Face Wash Neem', 'Ticked')], '3 added to my shop'), 'From 5,000+ items'),
        ('Receive stock', mini_ui('GRN · Karachi Cosmetics', [('Face Wash Neem', 'FW-21'), ('Expiry', 'Mar 2027'), ('Qty', '24 pcs')], 'Batch and expiry saved'), 'Batch and expiry on GRN'),
        ('Scan and sell', mini_ui('New sale', [('Matte Lipstick 04', '1,250'), ('Foundation 220', '2,800'), ('Face Wash x2', '1,300')], 'Bill on WhatsApp', '#eaf1ff', BLUE), 'Scan the barcode, bill fast'),
        ('Check expiry', mini_ui('Expiry alerts', [('Sunblock SPF 50', '12 days'), ('Night Cream', 'Expired'), ('Testers used', '2 pcs')], 'Sell first or return', '#fffbeb', '#92400e'), 'Before it is a loss'),
        ('See profit', ui_report("Today's sales", 'Rs 96,300', '142 items · 18 shades sold · 0 expired'), 'Sales, stock and profit'),
    ])


SCENES = {
    'uptrendpos-clothing-store-size-colour-variants': ('Every Size and Colour', 'blue', lambda: g(tablet_variants(), 210, 150, 1.0),
        [(60, 770, 'Colour x size in one go', '#2F7BD9'), (330, 770, 'Own stock for each size', '#2FA455')]),
    'uptrendpos-clothing-store-barcode-tags-exchange': ('Tags and Easy Exchange', 'green', lambda: g(tag_sheet(), 220, 150, 1.25) + g(phone_exchange(), 680, 140, 1.0),
        [(60, 780, 'Barcode tags with size and price', '#2F7BD9'), (500, 780, 'Exchange on the same bill', '#2FA455')]),
    'uptrendpos-clothing-store-pos-hardware': ('Garment Shop Hardware', 'yellow',
        lambda: hardware_scene(monitor_clothing, printer_cloth, phone_exchange, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-clothing-store-pos-process': ('Garment Sale, Step by Step', 'navy', scene_clothing_process, [(60, 470, 'All connected', '#2FA455')]),
    'uptrendpos-cosmetics-store-product-catalog': ('5,000+ Products Ready', 'green', lambda: g(tablet_beauty_catalog(), 210, 150, 1.0),
        [(60, 770, 'Search and tick', '#2FA455'), (300, 770, 'Makeup, skin and hair care', '#F59E0B')]),
    'uptrendpos-cosmetics-store-shades-expiry': ('Shades and Expiry', 'teal', lambda: g(phone_shades(), 230, 140, 1.0) + g(phone_expiry(), 680, 140, 1.0),
        [(60, 780, 'Stock for every shade', '#2F7BD9'), (440, 780, 'Batch expiry alerts', '#F59E0B')]),
    'uptrendpos-cosmetics-store-pos-hardware': ('Beauty Store Hardware', 'blue',
        lambda: hardware_scene(monitor_beauty, printer_beauty, phone_expiry, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']),
        [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-cosmetics-store-pos-process': ('Beauty Sale, Step by Step', 'yellow', scene_beauty_process, [(60, 470, 'All connected', '#2FA455')]),
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
