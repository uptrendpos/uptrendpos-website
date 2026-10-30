"""Tailor shop + Mobile shop page images (same house style and watermark as gen_ind.py).
Run: python3 gen_tailor_mobile.py [name ...]"""
import asyncio, sys
from playwright.async_api import async_playwright
from PIL import Image
from gen_ind import (B, OUT, t, shadow, qr, receipt, phone_shell, status_bar, frame, g, pcard, arrow, circle_badge,
                     printer80, scanner_small, mini_printer_usb)

NAVY, BLUE, MUTED, INK = '#10224A', '#024691', '#64748b', '#1e293b'


def screen_open(W, H, clip, title, sub, pill='Online'):
    return [f'<rect x="0" y="0" width="{W}" height="{H}" rx="20" fill="#0f172a"/>', f'<circle cx="{W/2}" cy="{H-18}" r="3" fill="#3b82f6"/>',
            f'<rect x="16" y="16" width="{W-32}" height="{H-66}" rx="6" fill="#f3f6fb"/>',
            f'<clipPath id="{clip}"><rect x="16" y="16" width="{W-32}" height="{H-66}" rx="6"/></clipPath><g clip-path="url(#{clip})">',
            f'<rect x="16" y="16" width="{W-32}" height="46" fill="url(#gNavy)"/>', t(34, 45, 'UpTrendPos', 15, 700, '#fff'),
            t(150, 45, f'{title}  ·  {sub}', 12, 500, '#c9dbf2'),
            f'<rect x="{W-140}" y="27" width="108" height="24" rx="12" fill="#2FA455"/>', t(W - 86, 43, pill, 11, 700, '#fff', 'middle')]


def monitor_stand(W, H):
    return [f'<rect x="{W/2-38}" y="{H-8}" width="76" height="118" fill="url(#gSilver)"/>',
            f'<rect x="{W/2-140}" y="{H+104}" width="280" height="22" rx="11" fill="url(#gSilver)"/>']


def screen_close(W, H):
    return ['</g>', f'<rect x="16" y="16" width="{W-32}" height="{H-66}" rx="6" fill="url(#gGlass)"/>']


def slip(x, y, w, title, lines, foot):
    """Thermal paper slip with zigzag bottom. lines = [(label, value) or ('--', '')]."""
    h = 70 + len(lines) * 21 + 60
    zz = ''.join(f' l-{w/24:.2f},9 -{w/24:.2f},-9' for _ in range(12))
    out = [f'<g filter="url(#fDrop)"><path d="M{x},{y} L{x+w},{y} L{x+w},{y+h}{zz} Z" fill="#fff"/></g>',
           t(x + w / 2, y + 34, title, 15, 800, '#111', 'middle'),
           f'<line x1="{x+16}" y1="{y+48}" x2="{x+w-16}" y2="{y+48}" stroke="#999" stroke-dasharray="4 3"/>']
    yy = y + 72
    for a, b in lines:
        if a == '--':
            out.append(f'<line x1="{x+16}" y1="{yy-10}" x2="{x+w-16}" y2="{yy-10}" stroke="#bbb" stroke-dasharray="4 3"/>')
            yy += 8
            continue
        out += [t(x + 18, yy, a, 11.5, 500, '#333'), t(x + w - 18, yy, b, 12, 700, '#111', 'end')]
        yy += 21
    out.append(t(x + w / 2, yy + 18, foot, 10.5, 600, '#555', 'middle'))
    return ''.join(out)


# ================================================================= TAILOR
MEAS_K = [('Length', '40'), ('Chest', '42'), ('Waist', '38'), ('Shoulder', '18.5'), ('Sleeve', '24'), ('Collar', '15.5'), ('Daman', '23')]
MEAS_S = [('Length', '39'), ('Pancha', '8.5'), ('Waist', 'Elastic')]


def monitor_tailor():
    W, H = 780, 486
    g_ = monitor_stand(W, H) + screen_open(W, H, 'cpMonT', 'New Stitching Order', 'Al-Noor Tailors')
    g_ += ['<rect x="32" y="76" width="470" height="62" rx="12" fill="#fff" stroke="#dfe6f1"/>',
           '<circle cx="62" cy="107" r="18" fill="#eaf1ff"/>', t(62, 112, 'AR', 12, 800, BLUE, 'middle'),
           t(92, 102, 'Ahmed Raza', 14, 700, NAVY), t(92, 122, 'Customer #1283  ·  0300 1234567', 11, 500, MUTED),
           '<rect x="380" y="94" width="108" height="26" rx="13" fill="#ecfdf3"/>', t(434, 111, '7 past orders', 10.5, 700, '#15803d', 'middle')]
    # tabs
    x = 32
    for i, tab in enumerate(['Kameez', 'Shalwar', 'Coat', 'Waistcoat']):
        wch = len(tab) * 8 + 26
        g_ += [f'<rect x="{x}" y="150" width="{wch}" height="28" rx="14" fill="{"#024691" if i == 0 else "#fff"}" stroke="#d6e0ee"/>',
               t(x + wch / 2, 169, tab, 11.5, 700, '#fff' if i == 0 else BLUE, 'middle')]
        x += wch + 8
    # measurement grid
    for i, (a, b) in enumerate(MEAS_K):
        cx, cy = 32 + (i % 4) * 118, 192 + (i // 4) * 66
        g_ += [f'<rect x="{cx}" y="{cy}" width="110" height="56" rx="12" fill="#fff" stroke="#e1e7f0"/>',
               t(cx + 12, cy + 22, a, 10.5, 600, MUTED), t(cx + 12, cy + 44, b + '"', 16, 800, NAVY)]
    g_ += ['<rect x="386" y="258" width="110" height="56" rx="12" fill="#eaf1ff" stroke="#c7d7ff"/>', t(398, 280, 'Shalwar', 10.5, 600, BLUE),
           t(398, 302, '39" / 8.5"', 15, 800, NAVY),
           '<rect x="32" y="330" width="470" height="78" rx="12" fill="#fff" stroke="#e1e7f0"/>', t(48, 354, 'Workshop', 11, 700, NAVY)]
    for i, (role, name) in enumerate([('Cutting master', 'Rashid'), ('Stitching master', 'Naveed')]):
        g_ += [t(48 + i * 230, 378, role, 10.5, 500, MUTED), t(48 + i * 230, 398, name, 13, 700, NAVY)]
    g_ += ['<rect x="520" y="76" width="228" height="344" rx="14" fill="#fff" stroke="#e1e7f0"/>',
           t(538, 104, 'Order ORD-1044', 12, 700, NAVY), t(538, 124, '2 suits  ·  shalwar kameez', 11, 500, MUTED)]
    y = 154
    for a, b in [('Stitching', 'Rs 3,000'), ('Delivery', 'Thu 22 Oct'), ('Advance', 'Rs 1,000')]:
        g_ += [t(538, y, a, 11.5, 500, MUTED), t(732, y, b, 11.5, 700, NAVY, 'end')]
        y += 24
    g_ += ['<rect x="532" y="222" width="204" height="58" rx="14" fill="#eaf1ff"/>', t(546, 244, 'Balance at delivery', 11, 600, '#475569'),
           t(724, 270, 'Rs 2,000', 20, 800, BLUE, 'end'),
           '<rect x="532" y="292" width="98" height="38" rx="12" fill="#fff" stroke="#c7d7ff"/>', t(581, 316, 'Size slip', 12, 700, BLUE, 'middle'),
           '<rect x="638" y="292" width="98" height="38" rx="12" fill="#1E8A43"/>', t(687, 316, 'WhatsApp', 11.5, 700, '#fff', 'middle'),
           '<rect x="532" y="342" width="204" height="40" rx="12" fill="#FAE814"/>', t(634, 367, 'Save Order', 13, 800, NAVY, 'middle')]
    return ''.join(g_ + screen_close(W, H))


STATUS = [('Booked', '#eef1f6', '#475569'), ('Cutting', '#fffbeb', '#92400e'), ('Stitching', '#eaf1ff', BLUE), ('Ready', '#ecfdf3', '#15803d')]


def phone_orders():
    g_ = ['<rect x="14" y="14" width="272" height="150" fill="url(#gBlue)"/>', status_bar(),
          t(32, 80, 'Deliveries this week', 12, 500, '#cfe0ff'), t(32, 114, '18 orders', 28, 800, '#fff'), t(32, 140, '5 ready  ·  Rs 26,500 balance', 11, 500, '#cfe0ff')]
    y = 182
    for o, n, d, si in [('ORD-1041', 'Bilal Ahmed', 'Today', 3), ('ORD-1044', 'Ahmed Raza', 'Thu 22 Oct', 2), ('ORD-1046', 'Usman Ali', 'Sat 24 Oct', 1), ('ORD-1049', 'Hamid Khan', 'Mon 26 Oct', 0)]:
        lab, bg, fg = STATUS[si]
        g_ += [f'<rect x="26" y="{y}" width="248" height="58" rx="14" fill="#fff" stroke="#e6ebf3"/>', t(40, y + 24, f'{o} · {n}', 11.5, 700, NAVY),
               t(40, y + 42, 'Delivery ' + d, 10, 500, MUTED), f'<rect x="196" y="{y+30}" width="68" height="20" rx="10" fill="{bg}"/>', t(230, y + 44, lab, 9.5, 800, fg, 'middle')]
        y += 66
    g_ += [f'<rect x="26" y="{y+6}" width="248" height="44" rx="14" fill="#FAE814"/>', t(150, y + 34, 'Collect balance at delivery', 11.5, 800, NAVY, 'middle')]
    return phone_shell(''.join(g_), 'cpOrd')


def phone_measure():
    g_ = ['<rect x="14" y="14" width="272" height="122" fill="url(#gBlue)"/>', status_bar(), t(32, 84, 'Ahmed Raza', 16, 700, '#fff'),
          t(32, 106, 'Customer #1283 · Kameez size', 10.5, 500, '#cfe0ff'),
          '<rect x="202" y="70" width="70" height="24" rx="12" fill="#fff" fill-opacity=".2"/>', t(237, 87, 'Edit', 11, 700, '#fff', 'middle')]
    y = 152
    for a, b in MEAS_K:
        g_ += [f'<rect x="26" y="{y}" width="248" height="44" rx="12" fill="#fff" stroke="#e6ebf3"/>', t(42, y + 27, a, 12, 600, '#475569'),
               t(258, y + 28, b + '"', 15, 800, NAVY, 'end')]
        y += 50
    g_ += [t(150, y + 16, 'Updated for this order · 14 Oct', 10.5, 600, MUTED, 'middle'),
           f'<rect x="26" y="{y+28}" width="248" height="40" rx="14" fill="#FAE814"/>', t(150, y + 54, 'Save new size', 12, 800, NAVY, 'middle')]
    return phone_shell(''.join(g_), 'cpMeas')


def phone_customer():
    g_ = ['<rect x="14" y="14" width="272" height="104" fill="url(#gBlue)"/>', status_bar(), t(32, 84, 'Search: 1283', 15, 700, '#fff'),
          t(32, 104, 'By ID, name or phone', 10.5, 500, '#cfe0ff'),
          '<rect x="26" y="136" width="248" height="188" rx="16" fill="#fff" stroke="#e6ebf3"/>',
          '<circle cx="62" cy="174" r="22" fill="#eaf1ff"/>', t(62, 180, 'AR', 13, 800, BLUE, 'middle'),
          t(96, 170, 'Ahmed Raza', 14, 700, NAVY), t(96, 190, '0300 1234567', 11, 500, MUTED)]
    y = 226
    for a, b in [('Customer ID', '#1283 (old register)'), ('Referred by', 'Bilal Ahmed'), ('Orders', '7'), ('Balance due', 'Rs 2,000')]:
        g_ += [t(42, y, a, 11, 500, MUTED), t(258, y, b, 11, 700, '#b42318' if 'Rs' in b else NAVY, 'end')]
        y += 24
    y = 344
    for lab, c in [('Kameez size', '#eaf1ff'), ('Shalwar size', '#eaf1ff'), ('Coat size', '#eaf1ff')]:
        g_ += [f'<rect x="26" y="{y}" width="248" height="40" rx="12" fill="{c}"/>', t(42, y + 25, lab, 12, 700, BLUE), t(258, y + 25, 'Saved', 11, 700, '#15803d', 'end')]
        y += 48
    g_ += [f'<rect x="26" y="{y+4}" width="248" height="40" rx="14" fill="#FAE814"/>', t(150, y + 30, 'New stitching order', 12, 800, NAVY, 'middle')]
    return phone_shell(''.join(g_), 'cpCust')


def board_tailor():
    W, H = 760, 470
    g_ = [shadow(380, 520, 360, 26), f'<rect x="0" y="0" width="{W}" height="{H}" rx="34" fill="#111827"/>', '<rect x="20" y="22" width="720" height="426" rx="16" fill="#f3f6fb"/>',
          '<clipPath id="cpBoard"><rect x="20" y="22" width="720" height="426" rx="16"/></clipPath><g clip-path="url(#cpBoard)">',
          '<rect x="20" y="22" width="720" height="50" fill="url(#gNavy)"/>', t(42, 53, 'Stitching Orders', 16, 700, '#fff'),
          '<rect x="560" y="34" width="160" height="26" rx="13" fill="#fff" fill-opacity=".18"/>', t(640, 52, 'This week · 18', 11.5, 700, '#fff', 'middle')]
    cols = [[('ORD-1049', 'Hamid Khan', '—', 'Mon 26')], [('ORD-1046', 'Usman Ali', 'Rashid', 'Sat 24'), ('ORD-1047', 'Saad Malik', 'Rashid', 'Sat 24')],
            [('ORD-1044', 'Ahmed Raza', 'Naveed', 'Thu 22'), ('ORD-1045', 'Zain Iqbal', 'Imran', 'Fri 23')], [('ORD-1041', 'Bilal Ahmed', 'Naveed', 'Today')]]
    for ci, ((lab, bg, fg), cards) in enumerate(zip(STATUS, cols)):
        x = 34 + ci * 176
        g_ += [f'<rect x="{x}" y="86" width="166" height="348" rx="14" fill="#fff" stroke="#e3e9f2"/>', f'<rect x="{x+10}" y="96" width="146" height="28" rx="10" fill="{bg}"/>',
               t(x + 83, 115, lab, 12, 800, fg, 'middle')]
        y = 136
        for o, n, m, d in cards:
            g_ += [f'<rect x="{x+10}" y="{y}" width="146" height="88" rx="12" fill="#f8fafd" stroke="#e6ebf3"/>', t(x + 22, y + 22, o, 11, 800, NAVY),
                   t(x + 22, y + 40, n, 10.5, 600, '#334155'), t(x + 22, y + 58, 'Master: ' + m, 10, 500, MUTED),
                   f'<rect x="{x+22}" y="{y+66}" width="72" height="16" rx="8" fill="#fff4d6"/>', t(x + 58, y + 78, d, 9, 800, '#92400e', 'middle')]
            y += 98
    g_ += ['</g>', '<rect x="20" y="22" width="720" height="426" rx="16" fill="url(#gGlass)"/>']
    return ''.join(g_)


def size_slip():
    return slip(0, 0, 250, 'SIZE SLIP · ORD-1044',
                [('Customer', '#1283'), ('Suits', '2'), ('--', ''), ('Length', '40"'), ('Chest', '42"'), ('Waist', '38"'), ('Shoulder', '18.5"'), ('Sleeve', '24"'),
                 ('Collar', '15.5"'), ('Shalwar', '39" / 8.5"'), ('--', ''), ('Cutting', 'Rashid'), ('Delivery', '22-10-2026')], 'For workshop · no prices')


def printer_tailor():
    out = printer80()
    for a, b in [('CITY KIRYANA STORE', 'AL-NOOR TAILORS'), ('>Chakki Atta 10 kg<', '>Stitching x2 suits<'), ('>Sugar 2.5 kg<', '>Advance paid<'),
                 ('>Cooking Oil 1 L x2<', '>Balance due<'), ('>1,200<', '>3,000<'), ('>400<', '>1,000<'), ('>1,180<', '>2,000<'), ('>Rs 4,200<', '>Rs 3,000<')]:
        out = out.replace(a, b)
    return out


def tape():
    marks = ''.join(f'<rect x="{150+i*14}" y="104" width="2" height="{12 if i % 5 == 0 else 7}" fill="#10224A"/>' for i in range(14))
    nums = ''.join(t(152 + i * 70, 136, str(10 + i), 11, 700, NAVY) for i in range(3))
    return ''.join([shadow(150, 214, 140, 16), '<circle cx="100" cy="120" r="88" fill="#FAE814" stroke="#e0cc00" stroke-width="4"/>',
                    '<circle cx="100" cy="120" r="30" fill="#fff8b8" stroke="#e0cc00" stroke-width="3"/>', '<circle cx="100" cy="120" r="8" fill="#10224A"/>',
                    '<rect x="140" y="100" width="210" height="44" rx="4" fill="#fff6a6" stroke="#e0cc00" stroke-width="2"/>', marks, nums])


def ui_measure():
    g_ = ['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>', t(14, 26, 'Customer #1283 · Kameez', 12, 700, NAVY)]
    for i, (a, b) in enumerate(MEAS_K[:6]):
        cx, cy = 14 + (i % 3) * 79, 40 + (i // 3) * 64
        g_ += [f'<rect x="{cx}" y="{cy}" width="73" height="54" rx="10" fill="#fff" stroke="#e1e7f0"/>', t(cx + 9, cy + 20, a, 9.5, 600, MUTED), t(cx + 9, cy + 42, b + '"', 15, 800, NAVY)]
    g_.append(t(14, 182, 'Saved for every next order', 10, 600, '#15803d'))
    return ''.join(g_)


def ui_book():
    g_ = ['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>', '<rect width="260" height="38" rx="16" fill="url(#gNavy)"/><rect y="22" width="260" height="16" fill="#1a3a74"/>',
          t(14, 25, 'Order ORD-1044 · 2 suits', 12, 700, '#fff')]
    y = 62
    for a, b in [('Stitching', 'Rs 3,000'), ('Advance', 'Rs 1,000'), ('Balance', 'Rs 2,000'), ('Delivery', 'Thu 22 Oct'), ('Referred by', 'Bilal Ahmed')]:
        g_ += [t(14, y, a, 10.5, 600, MUTED), t(246, y, b, 11, 700, NAVY, 'end')]
        y += 25
    return ''.join(g_)


def ui_workshop():
    g_ = ['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>']
    y = 14
    for a, b, (lab, bg, fg) in [('Cutting master', 'Rashid', STATUS[1]), ('Stitching master', 'Naveed', STATUS[2])]:
        g_ += [f'<rect x="14" y="{y}" width="232" height="54" rx="12" fill="#fff" stroke="#e3e9f2"/>', t(26, y + 22, a, 10.5, 600, MUTED), t(26, y + 42, b, 13, 700, NAVY),
               f'<rect x="166" y="{y+17}" width="70" height="20" rx="10" fill="{bg}"/>', t(201, y + 31, lab, 9.5, 800, fg, 'middle')]
        y += 62
    g_ += ['<rect x="14" y="140" width="232" height="38" rx="10" fill="#eaf1ff"/>', t(26, 164, 'Size slip printed for workshop', 10.5, 700, BLUE)]
    return ''.join(g_)


def ui_ready():
    g_ = ['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>', '<rect x="14" y="14" width="232" height="44" rx="12" fill="#ecfdf3"/>',
          t(28, 42, 'ORD-1044 is ready', 12, 800, '#15803d')]
    y = 82
    for a, b in [('Balance received', 'Rs 2,000'), ('Paid by', 'Cash'), ('Status', 'Delivered')]:
        g_ += [t(14, y, a, 11, 600, MUTED), t(246, y, b, 11.5, 700, NAVY, 'end')]
        y += 26
    g_ += ['<rect x="14" y="150" width="232" height="30" rx="10" fill="#1E8A43"/>', t(130, 170, 'Send receipt on WhatsApp', 11, 700, '#fff', 'middle')]
    return ''.join(g_)


def ui_report_t():
    g_ = ['<rect width="260" height="190" rx="16" fill="url(#gBlue)"/>', t(14, 28, 'This month', 11, 500, '#cfe0ff'), t(14, 56, '146 suits', 22, 800, '#fff'),
          t(14, 76, 'Rs 2.1 lakh billed · Rs 38,000 to collect', 10, 500, '#cfe0ff'), '<rect x="14" y="88" width="232" height="90" rx="12" fill="#fff"/>']
    for i, h in enumerate([30, 44, 38, 56, 48, 62, 52]):
        g_.append(f'<rect x="{30+i*31}" y="{168-h}" width="18" height="{h}" rx="4" fill="url(#gBar)"/>')
    return ''.join(g_)


def scene_tailor_process():
    y1, y2 = 120, 520
    return ''.join([
        pcard(60, y1, 1, 'Take the size', ui_measure(), 'Saved on the customer, by ID'),
        pcard(450, y1, 2, 'Book the order', ui_book(), 'Delivery date and advance'),
        pcard(840, y1, 3, 'Cut and stitch', ui_workshop(), 'Masters assigned, size slip out'),
        pcard(645, y2, 4, 'Ready, deliver', ui_ready(), 'Collect the balance'),
        pcard(255, y2, 5, 'See your month', ui_report_t(), 'Orders, income, dues'),
        arrow('M368,280 L436,280', 'M424,268 L438,280 L424,292'),
        arrow('M758,280 L826,280', 'M814,268 L828,280 L814,292'),
        arrow('M990,446 C990,500 960,560 952,600', 'M942,588 L951,604 L965,592'),
        arrow('M640,680 L566,680', 'M578,668 L564,680 L578,692'),
    ])


def scene_tailor_hardware():
    body = ['<circle cx="600" cy="300" r="232" fill="#dcebff" opacity=".75"/>',
            '<circle cx="600" cy="300" r="232" fill="none" stroke="#bfd6f5" stroke-width="2" stroke-dasharray="6 9"/>',
            g(printer_tailor(), 372, 300, .34), g(monitor_tailor(), 446, 150, .4),
            g(tape(), 700, 380, .42), g(phone_orders(), 770, 196, .26)]
    xs = [150, 375, 600, 825, 1050]
    body.append('<path d="M600,532 L600,580" stroke="#2F7BD9" stroke-width="3" fill="none"/>')
    body.append(f'<path d="M{xs[0]},630 L{xs[0]},600 Q{xs[0]},580 {xs[0]+20},580 L{xs[-1]-20},580 Q{xs[-1]},580 {xs[-1]},600 L{xs[-1]},630" stroke="#2F7BD9" stroke-width="3" fill="none"/>')
    for x in xs[1:-1]:
        body.append(f'<path d="M{x},580 L{x},630" stroke="#2F7BD9" stroke-width="3" fill="none"/>')
    cy, r = 712, 82
    inners = [g(monitor_tailor(), xs[0] - 59, cy - 46, .15, flt=False),
              g(printer_tailor(), xs[1] - 51, cy - 54, .22, flt=False),
              g(mini_printer_usb(), xs[2] - 45, cy - 48, .3, flt=False),
              g(phone_orders(), xs[3] - 26, cy - 53, .17, flt=False),
              g(tape(), xs[4] - 52, cy - 34, .3, flt=False)]
    for x, inner, lab in zip(xs, inners, ['Windows PC', 'Slip printer', 'Type-C printer', 'Owner phone', 'Measuring tape']):
        body.append(circle_badge(x, cy, r, inner, lab))
    return ''.join(body)


# ================================================================= MOBILE SHOP
def monitor_mobile():
    W, H = 780, 486
    g_ = monitor_stand(W, H) + screen_open(W, H, 'cpMonM', 'New Sale', 'Mobile Counter')
    g_ += ['<rect x="32" y="76" width="470" height="34" rx="10" fill="#fff" stroke="#dfe6f1"/>', t(48, 98, 'Search item or scan IMEI / serial', 11.5, 500, '#94a3b8'),
           '<rect x="32" y="122" width="470" height="30" fill="#e9effa"/>']
    for x, c, a in [(46, 'Item', 'start'), (200, 'IMEI / Serial', 'start'), (338, 'Warranty', 'start'), (488, 'Amount', 'end')]:
        g_.append(t(x, 142, c, 11, 700, NAVY, a))
    rows = [('Phone X1 8/256GB', '3567 8910 4523 118', '12 months', '84,000'), ('Fast Charger 25W', '—', '6 months', '2,200'),
            ('Back Cover', '—', '—', '650'), ('Glass Protector', '—', '—', '450')]
    y = 172
    for i, (n, s, w, a) in enumerate(rows):
        if i % 2:
            g_.append(f'<rect x="32" y="{y-19}" width="470" height="32" fill="#f7f9fd"/>')
        g_ += [t(46, y, n, 11, 600, INK), t(200, y, s, 10, 600, BLUE if s != '—' else '#94a3b8'), t(338, y, w, 10, 500, MUTED), t(488, y, a, 11.5, 700, NAVY, 'end')]
        y += 32
    g_ += ['<rect x="32" y="312" width="470" height="96" rx="12" fill="#fff" stroke="#e1e7f0"/>', t(48, 338, 'IMEI 3567 8910 4523 118', 12, 700, BLUE),
           t(48, 360, 'In stock since GRN-221 · City Mobile Traders', 11, 500, MUTED), t(48, 384, 'Phone X1 8/256GB · 4 more left in stock', 11, 600, '#15803d')]
    g_ += ['<rect x="520" y="76" width="228" height="344" rx="14" fill="#fff" stroke="#e1e7f0"/>',
           t(538, 104, 'Customer', 11, 600, MUTED), t(538, 124, 'Ali Hassan · 0321 7654321', 12.5, 700, NAVY),
           t(538, 156, 'Pay by', 11, 600, MUTED)]
    x = 538
    for i, lab in enumerate(['Cash', 'Bank', 'Qist']):
        g_ += [f'<rect x="{x}" y="166" width="58" height="28" rx="14" fill="{"#024691" if i == 2 else "#fff"}" stroke="#c7d7ff"/>', t(x + 29, 185, lab, 11, 700, '#fff' if i == 2 else BLUE, 'middle')]
        x += 64
    g_ += ['<rect x="532" y="206" width="204" height="44" rx="12" fill="#f3f7ff"/>', t(546, 224, 'Advance Rs 27,300', 10.5, 700, NAVY),
           t(546, 241, '6 months · Rs 10,500 a month', 10, 500, MUTED),
           '<rect x="532" y="258" width="204" height="44" rx="14" fill="#eaf1ff"/>', t(546, 285, 'Total', 12, 600, '#475569'), t(724, 287, 'Rs 87,300', 18, 800, BLUE, 'end'),
           '<rect x="532" y="312" width="98" height="38" rx="12" fill="#fff" stroke="#c7d7ff"/>', t(581, 336, 'Hold', 12, 700, BLUE, 'middle'),
           '<rect x="638" y="312" width="98" height="38" rx="12" fill="#1E8A43"/>', t(687, 336, 'WhatsApp', 11.5, 700, '#fff', 'middle'),
           '<rect x="532" y="360" width="204" height="40" rx="12" fill="#FAE814"/>', t(634, 385, 'Save &amp; Print', 13, 800, NAVY, 'middle')]
    return ''.join(g_ + screen_close(W, H))


def phone_warranty():
    g_ = ['<rect x="14" y="14" width="272" height="104" fill="url(#gBlue)"/>', status_bar(), t(32, 84, 'Warranty lookup', 15, 700, '#fff'),
          t(32, 104, 'IMEI 3567 8910 4523 118', 10.5, 500, '#cfe0ff'),
          '<rect x="26" y="136" width="248" height="64" rx="16" fill="#ecfdf3" stroke="#bfe6cc"/>', t(42, 162, 'In warranty', 15, 800, '#15803d'),
          t(42, 184, 'Until 02 Sep 2027 · 10 months left', 10.5, 600, '#15803d')]
    y = 230
    for a, b in [('Item', 'Phone X1 8/256GB'), ('Sold on', '02 Sep 2026'), ('Invoice', 'INV-3311'), ('Customer', 'Ali Hassan'), ('Bought from', 'City Mobile Traders'),
                 ('Purchase', 'GRN-221 · 20 Aug')]:
        g_ += [t(36, y, a, 11, 500, MUTED), t(264, y, b, 11, 700, NAVY, 'end'), f'<line x1="36" y1="{y+12}" x2="264" y2="{y+12}" stroke="#e6ebf3"/>']
        y += 34
    g_ += [f'<rect x="26" y="{y+8}" width="248" height="40" rx="14" fill="#FAE814"/>', t(150, y + 34, 'Open the bill', 12, 800, NAVY, 'middle')]
    return phone_shell(''.join(g_), 'cpWar')


def phone_qist():
    g_ = ['<rect x="14" y="14" width="272" height="150" fill="url(#gBlue)"/>', status_bar(),
          t(32, 80, 'Installment plan · Ali Hassan', 12, 500, '#cfe0ff'), t(32, 114, 'Rs 52,500', 28, 800, '#fff'), t(32, 140, 'left of Rs 63,000 · 1 of 6 paid', 11, 500, '#cfe0ff')]
    y = 182
    for m, a, st, bg, fg in [('Oct 2026', 'Rs 10,500', 'Paid', '#ecfdf3', '#15803d'), ('Nov 2026', 'Rs 10,500', 'Due 02 Nov', '#fffbeb', '#92400e'),
                             ('Dec 2026', 'Rs 10,500', 'Upcoming', '#eef1f6', '#475569'), ('Jan 2027', 'Rs 10,500', 'Upcoming', '#eef1f6', '#475569')]:
        g_ += [f'<rect x="26" y="{y}" width="248" height="58" rx="14" fill="#fff" stroke="#e6ebf3"/>', t(40, y + 24, m, 12, 700, NAVY), t(40, y + 42, a, 10.5, 600, MUTED),
               f'<rect x="186" y="{y+18}" width="78" height="22" rx="11" fill="{bg}"/>', t(225, y + 33, st, 9.5, 800, fg, 'middle')]
        y += 66
    g_ += [f'<rect x="26" y="{y+6}" width="248" height="44" rx="14" fill="#FAE814"/>', t(150, y + 34, 'Receive payment', 12, 800, NAVY, 'middle')]
    return phone_shell(''.join(g_), 'cpQist')


def tablet_mobile_catalog():
    W, H = 780, 500
    g_ = [shadow(390, 600, 380, 30), '<polygon points="430,300 490,300 590,590 548,596" fill="#2a313d"/>', '<rect x="530" y="588" width="70" height="10" rx="5" fill="#1b212b"/>',
          f'<rect x="0" y="0" width="{W}" height="{H}" rx="40" fill="#111827"/>', '<rect x="22" y="26" width="736" height="452" rx="16" fill="#f3f6fb"/>',
          '<clipPath id="cpMCat"><rect x="22" y="26" width="736" height="452" rx="16"/></clipPath><g clip-path="url(#cpMCat)">',
          '<rect x="22" y="26" width="736" height="52" fill="url(#gNavy)"/>', t(44, 58, 'Mobile &amp; Computer Catalog', 16, 700, '#fff'),
          '<rect x="560" y="38" width="180" height="28" rx="14" fill="#fff" fill-opacity=".2"/>', t(650, 57, '700+ products', 12, 700, '#fff', 'middle'),
          '<rect x="44" y="94" width="692" height="38" rx="12" fill="#fff" stroke="#dfe6f1"/>', t(64, 118, '128gb', 13, 600, NAVY),
          t(716, 118, '31 results', 11, 500, MUTED, 'end')]
    rows = [('Phone A15 6/128GB', 'Smartphone · IMEI', 'Mobile', True), ('Phone N12 8/128GB', 'Smartphone · IMEI', 'Mobile', True),
            ('Tab T8 4/128GB', 'Tablet · IMEI', 'Tablet', False), ('Laptop 14" 8GB / 128GB SSD', 'Laptop · Serial no.', 'Computer', True),
            ('MicroSD Card 128GB', 'Storage', 'Accessory', False)]
    y = 146
    for n, sub, cls, on in rows:
        g_ += [f'<rect x="44" y="{y}" width="692" height="44" rx="12" fill="{"#eef5ff" if on else "#fff"}" stroke="{"#c7d7ff" if on else "#e3e9f2"}"/>',
               f'<rect x="58" y="{y+12}" width="20" height="20" rx="6" fill="{"#024691" if on else "#fff"}" stroke="#bcc9dc"/>',
               (f'<path d="M62,{y+22} l4,4 7,-8" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>' if on else ''),
               t(94, y + 20, n, 12.5, 700, NAVY), t(94, y + 36, sub, 10.5, 500, MUTED),
               f'<rect x="612" y="{y+12}" width="106" height="20" rx="10" fill="#eaf1ff"/>', t(665, y + 26, cls, 10, 600, BLUE, 'middle')]
        y += 50
    g_ += ['<rect x="500" y="424" width="236" height="44" rx="14" fill="#FAE814"/>', t(618, 452, 'Add 3 to my shop', 13, 800, NAVY, 'middle'),
           t(64, 452, 'Not in the list? Add your own product.', 11.5, 600, BLUE), '</g>', '<rect x="22" y="26" width="736" height="452" rx="16" fill="url(#gGlass)"/>']
    return ''.join(g_)


def printer_mobile():
    out = printer80()
    for a, b in [('CITY KIRYANA STORE', 'CITY MOBILE ZONE'), ('>Chakki Atta 10 kg<', '>Phone X1 8/256GB<'), ('>Sugar 2.5 kg<', '>IMEI ...4523118<'),
                 ('>Cooking Oil 1 L x2<', '>Back Cover<'), ('>1,200<', '>84,000<'), ('>400<', '><'), ('>1,180<', '>650<'), ('>Rs 4,200<', '>Rs 84,650<')]:
        out = out.replace(a, b)
    return out


def ui_grn_m():
    g_ = ['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>', '<rect width="260" height="38" rx="16" fill="url(#gNavy)"/><rect y="22" width="260" height="16" fill="#1a3a74"/>',
          t(14, 25, 'GRN · City Mobile Traders', 12, 700, '#fff'), t(14, 60, 'Phone X1 8/256GB  ·  5 pcs', 11, 700, NAVY)]
    y = 84
    for imei in ['3567 8910 4523 118', '3567 8910 4523 126', '3567 8910 4523 134', '+ 2 more scanned']:
        g_ += [f'<rect x="14" y="{y-15}" width="232" height="22" rx="7" fill="#fff"/>', t(24, y, imei, 10.5, 600, BLUE if '+' not in imei else MUTED)]
        y += 26
    return ''.join(g_)


def ui_sell_m():
    g_ = ['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>', '<rect x="14" y="12" width="232" height="30" rx="9" fill="#fff" stroke="#dfe6f1"/>',
          t(26, 32, 'Scanned IMEI ...4523118', 10.5, 600, BLUE)]
    y = 66
    for a, b in [('Phone X1 8/256GB', '84,000'), ('Back Cover', '650'), ('Glass Protector', '450')]:
        g_ += [t(14, y, a, 11, 600, NAVY), t(246, y, b, 11, 700, NAVY, 'end')]
        y += 26
    g_ += ['<rect x="14" y="140" width="232" height="38" rx="10" fill="#ecfdf3"/>', t(26, 164, 'IMEI saved on this sale', 10.5, 700, '#15803d')]
    return ''.join(g_)


def ui_qist_m():
    g_ = ['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>', t(14, 26, 'Qist plan · 6 months', 12, 700, NAVY)]
    y = 54
    for a, b in [('Bill', 'Rs 87,300'), ('Advance', 'Rs 27,300'), ('Markup', 'Rs 3,000'), ('Monthly', 'Rs 10,500')]:
        g_ += [t(14, y, a, 10.5, 600, MUTED), t(246, y, b, 11, 700, NAVY, 'end')]
        y += 25
    g_ += ['<rect x="14" y="152" width="232" height="28" rx="9" fill="#fffbeb"/>', t(26, 171, 'Next due: 02 Nov', 10.5, 700, '#92400e')]
    return ''.join(g_)


def ui_warranty_m():
    g_ = ['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>', '<rect x="14" y="12" width="232" height="30" rx="9" fill="#fff" stroke="#dfe6f1"/>',
          t(26, 32, 'IMEI 3567 8910 4523 118', 10.5, 600, BLUE),
          '<rect x="14" y="54" width="232" height="44" rx="12" fill="#ecfdf3"/>', t(28, 82, 'In warranty till Sep 2027', 11.5, 800, '#15803d')]
    y = 122
    for a, b in [('Sold', '02 Sep 2026'), ('Invoice', 'INV-3311'), ('Customer', 'Ali Hassan')]:
        g_ += [t(14, y, a, 10.5, 600, MUTED), t(246, y, b, 11, 700, NAVY, 'end')]
        y += 24
    return ''.join(g_)


def ui_report_m():
    g_ = ['<rect width="260" height="190" rx="16" fill="url(#gBlue)"/>', t(14, 28, "Today's sales", 11, 500, '#cfe0ff'), t(14, 56, 'Rs 6,42,800', 22, 800, '#fff'),
          t(14, 76, '9 phones · 38 accessories · qist due Rs 74,500', 9.5, 500, '#cfe0ff'), '<rect x="14" y="88" width="232" height="90" rx="12" fill="#fff"/>']
    for i, h in enumerate([40, 52, 36, 60, 46, 66, 56]):
        g_.append(f'<rect x="{30+i*31}" y="{168-h}" width="18" height="{h}" rx="4" fill="url(#gBar)"/>')
    return ''.join(g_)


def scene_mobile_process():
    y1, y2 = 120, 520
    return ''.join([
        pcard(60, y1, 1, 'Receive stock', ui_grn_m(), 'IMEI of every phone saved'),
        pcard(450, y1, 2, 'Sell fast', ui_sell_m(), 'Scan IMEI, add accessories'),
        pcard(840, y1, 3, 'Cash or qist', ui_qist_m(), 'Advance and monthly plan'),
        pcard(645, y2, 4, 'Warranty check', ui_warranty_m(), 'Find any sold phone'),
        pcard(255, y2, 5, 'See profit', ui_report_m(), 'Sales, qist and stock'),
        arrow('M368,280 L436,280', 'M424,268 L438,280 L424,292'),
        arrow('M758,280 L826,280', 'M814,268 L828,280 L814,292'),
        arrow('M990,446 C990,500 960,560 952,600', 'M942,588 L951,604 L965,592'),
        arrow('M640,680 L566,680', 'M578,668 L564,680 L578,692'),
    ])


def scene_mobile_hardware():
    body = ['<circle cx="600" cy="300" r="232" fill="#dcebff" opacity=".75"/>',
            '<circle cx="600" cy="300" r="232" fill="none" stroke="#bfd6f5" stroke-width="2" stroke-dasharray="6 9"/>',
            g(printer_mobile(), 372, 300, .34), g(monitor_mobile(), 446, 150, .4),
            g(scanner_small(), 740, 352, .3, -22, 180, 180), g(phone_qist(), 770, 196, .26)]
    xs = [150, 375, 600, 825, 1050]
    body.append('<path d="M600,532 L600,580" stroke="#2F7BD9" stroke-width="3" fill="none"/>')
    body.append(f'<path d="M{xs[0]},630 L{xs[0]},600 Q{xs[0]},580 {xs[0]+20},580 L{xs[-1]-20},580 Q{xs[-1]},580 {xs[-1]},600 L{xs[-1]},630" stroke="#2F7BD9" stroke-width="3" fill="none"/>')
    for x in xs[1:-1]:
        body.append(f'<path d="M{x},580 L{x},630" stroke="#2F7BD9" stroke-width="3" fill="none"/>')
    cy, r = 712, 82
    inners = [g(monitor_mobile(), xs[0] - 59, cy - 46, .15, flt=False),
              g(scanner_small(), xs[1] - 45, cy - 48, .26, -22, 180, 180, flt=False),
              g(printer_mobile(), xs[2] - 51, cy - 54, .22, flt=False),
              g(phone_warranty(), xs[3] - 26, cy - 53, .17, flt=False),
              g(mini_printer_usb(), xs[4] - 45, cy - 48, .3, flt=False)]
    for x, inner, lab in zip(xs, inners, ['Windows PC', 'IMEI scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']):
        body.append(circle_badge(x, cy, r, inner, lab))
    return ''.join(body)


SCENES = {
    'uptrendpos-tailor-shop-pos-software': ('Tailor Shop Counter', 'yellow',
        lambda: g(monitor_tailor(), 40, 140, .9) + g(slip(0, 0, 250, 'SIZE SLIP · ORD-1044', [('Length', '40"'), ('Chest', '42"'), ('Waist', '38"'), ('Shoulder', '18.5"'), ('Delivery', '22-10')], 'For workshop'), 760, 560, .8)
        + g(tape(), 540, 712, .5) + g(phone_orders(), 905, 112, .66),
        [(60, 780, 'Sizes saved by ID', '#2F7BD9'), (300, 780, 'Advance and balance', '#2FA455')]),
    'uptrendpos-tailor-customer-measurements': ('Every Size, Saved', 'blue', lambda: g(phone_customer(), 230, 140, 1.0) + g(phone_measure(), 680, 140, 1.0),
        [(60, 780, 'Old register number kept', '#2F7BD9'), (420, 780, 'Update size any time', '#2FA455')]),
    'uptrendpos-tailor-order-tracking': ('Order to Delivery', 'green', lambda: g(board_tailor(), 60, 150, 1.0) + g(size_slip(), 860, 170, .95),
        [(60, 780, 'Cutting and stitching masters', '#F59E0B'), (450, 780, 'Size slip for the workshop', '#2FA455')]),
    'uptrendpos-tailor-shop-pos-hardware': ('Tailor Shop Hardware', 'teal', scene_tailor_hardware, [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-tailor-shop-pos-process': ('Tailor Order, Step by Step', 'yellow', scene_tailor_process, [(60, 470, 'All connected', '#2FA455')]),
    'uptrendpos-mobile-shop-pos-software': ('Mobile Shop Counter', 'blue',
        lambda: g(monitor_mobile(), 40, 140, .9) + g(printer_mobile(), 830, 548, .5) + g(scanner_small(), 660, 660, .4, -24, 180, 180) + g(phone_qist(), 905, 112, .66),
        [(60, 780, 'IMEI on every phone', '#2F7BD9'), (300, 780, 'Qist plans', '#F59E0B')]),
    'uptrendpos-mobile-shop-product-catalog': ('700+ Products Ready', 'navy', lambda: g(tablet_mobile_catalog(), 210, 150, 1.0),
        [(60, 770, 'Search and tick', '#2FA455'), (300, 770, 'Mobiles and computers', '#2F7BD9')]),
    'uptrendpos-mobile-shop-imei-warranty-installments': ('IMEI, Warranty and Qist', 'teal', lambda: g(phone_warranty(), 230, 140, 1.0) + g(phone_qist(), 680, 140, 1.0),
        [(60, 780, 'Warranty lookup by IMEI', '#2FA455'), (440, 780, 'Monthly qist plan', '#F59E0B')]),
    'uptrendpos-mobile-shop-pos-hardware': ('Mobile Shop Hardware', 'blue', scene_mobile_hardware, [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-mobile-shop-pos-process': ('Mobile Shop Day, Step by Step', 'navy', scene_mobile_process, [(60, 470, 'All connected', '#2FA455')]),
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
