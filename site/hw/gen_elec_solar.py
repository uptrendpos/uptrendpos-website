"""Solar shop + Electronics/Appliances/CCTV page images (house style + watermark from gen_ind.py).
Run: python3 gen_elec_solar.py [name ...]"""
import asyncio, sys
from playwright.async_api import async_playwright
from PIL import Image
from gen_ind import B, OUT, t, shadow, phone_shell, status_bar, frame, g, pcard, arrow, circle_badge, printer80, scanner_small, mini_printer_usb
from gen_tailor_mobile import NAVY, BLUE, MUTED, INK, screen_open, monitor_stand, screen_close


# ----------------------------------------------------------------- generic builders
def monitor_sale(clip, title, sub, rows, cust, adv, plan_txt, total, note=None):
    """rows = (item, qty, serial, amount)."""
    W, H = 780, 486
    g_ = monitor_stand(W, H) + screen_open(W, H, clip, title, sub)
    g_ += ['<rect x="32" y="76" width="470" height="34" rx="10" fill="#fff" stroke="#dfe6f1"/>', t(48, 98, 'Search item or scan serial number', 11.5, 500, '#94a3b8'),
           '<rect x="32" y="122" width="470" height="30" fill="#e9effa"/>']
    for x, c, a in [(46, 'Item', 'start'), (236, 'Qty', 'start'), (284, 'Serial no.', 'start'), (488, 'Amount', 'end')]:
        g_.append(t(x, 142, c, 11, 700, NAVY, a))
    y = 172
    for i, (n, q, s, a) in enumerate(rows):
        if i % 2:
            g_.append(f'<rect x="32" y="{y-19}" width="470" height="32" fill="#f7f9fd"/>')
        g_ += [t(46, y, n, 11, 600, INK), t(236, y, q, 10.5, 600, '#475569'), t(284, y, s, 10, 600, BLUE if s != '—' else '#94a3b8'), t(488, y, a, 11.5, 700, NAVY, 'end')]
        y += 32
    if note:
        g_ += [f'<rect x="32" y="{y+8}" width="470" height="96" rx="12" fill="#fff" stroke="#e1e7f0"/>', t(48, y + 34, note[0], 12, 700, BLUE),
               t(48, y + 56, note[1], 11, 500, MUTED), t(48, y + 80, note[2], 11, 600, '#15803d')]
    g_ += ['<rect x="520" y="76" width="228" height="344" rx="14" fill="#fff" stroke="#e1e7f0"/>',
           t(538, 104, 'Customer', 11, 600, MUTED), t(538, 124, cust, 12.5, 700, NAVY), t(538, 156, 'Pay by', 11, 600, MUTED)]
    x = 538
    for i, lab in enumerate(['Cash', 'Bank', 'Qist']):
        g_ += [f'<rect x="{x}" y="166" width="58" height="28" rx="14" fill="{"#024691" if i == 2 else "#fff"}" stroke="#c7d7ff"/>', t(x + 29, 185, lab, 11, 700, '#fff' if i == 2 else BLUE, 'middle')]
        x += 64
    g_ += ['<rect x="532" y="206" width="204" height="44" rx="12" fill="#f3f7ff"/>', t(546, 224, adv, 10.5, 700, NAVY), t(546, 241, plan_txt, 10, 500, MUTED),
           '<rect x="532" y="258" width="204" height="44" rx="14" fill="#eaf1ff"/>', t(546, 285, 'Total', 12, 600, '#475569'), t(724, 287, total, 18, 800, BLUE, 'end'),
           '<rect x="532" y="312" width="98" height="38" rx="12" fill="#fff" stroke="#c7d7ff"/>', t(581, 336, 'Hold', 12, 700, BLUE, 'middle'),
           '<rect x="638" y="312" width="98" height="38" rx="12" fill="#1E8A43"/>', t(687, 336, 'WhatsApp', 11.5, 700, '#fff', 'middle'),
           '<rect x="532" y="360" width="204" height="40" rx="12" fill="#FAE814"/>', t(634, 385, 'Save &amp; Print', 13, 800, NAVY, 'middle')]
    return ''.join(g_ + screen_close(W, H))


def phone_warranty_g(clip, serial, until, left, rows):
    g_ = ['<rect x="14" y="14" width="272" height="104" fill="url(#gBlue)"/>', status_bar(), t(32, 84, 'Warranty lookup', 15, 700, '#fff'),
          t(32, 104, serial, 10.5, 500, '#cfe0ff'),
          '<rect x="26" y="136" width="248" height="64" rx="16" fill="#ecfdf3" stroke="#bfe6cc"/>', t(42, 162, 'In warranty', 15, 800, '#15803d'),
          t(42, 184, f'Until {until} · {left}', 10.5, 600, '#15803d')]
    y = 230
    for a, b in rows:
        g_ += [t(36, y, a, 11, 500, MUTED), t(264, y, b, 11, 700, NAVY, 'end'), f'<line x1="36" y1="{y+12}" x2="264" y2="{y+12}" stroke="#e6ebf3"/>']
        y += 34
    g_ += [f'<rect x="26" y="{y+8}" width="248" height="40" rx="14" fill="#FAE814"/>', t(150, y + 34, 'Open the bill', 12, 800, NAVY, 'middle')]
    return phone_shell(''.join(g_), clip)


def phone_qist_g(clip, who, left, of, months):
    g_ = ['<rect x="14" y="14" width="272" height="150" fill="url(#gBlue)"/>', status_bar(),
          t(32, 80, 'Installment plan · ' + who, 12, 500, '#cfe0ff'), t(32, 114, left, 28, 800, '#fff'), t(32, 140, of, 11, 500, '#cfe0ff')]
    y = 182
    for m, a, st in months:
        bg, fg = {'Paid': ('#ecfdf3', '#15803d'), 'Upcoming': ('#eef1f6', '#475569')}.get(st, ('#fffbeb', '#92400e'))
        g_ += [f'<rect x="26" y="{y}" width="248" height="58" rx="14" fill="#fff" stroke="#e6ebf3"/>', t(40, y + 24, m, 12, 700, NAVY), t(40, y + 42, a, 10.5, 600, MUTED),
               f'<rect x="186" y="{y+18}" width="78" height="22" rx="11" fill="{bg}"/>', t(225, y + 33, st, 9.5, 800, fg, 'middle')]
        y += 66
    g_ += [f'<rect x="26" y="{y+6}" width="248" height="44" rx="14" fill="#FAE814"/>', t(150, y + 34, 'Receive payment', 12, 800, NAVY, 'middle')]
    return phone_shell(''.join(g_), clip)


def tablet_catalog_g(clip, title, badge, query, results, rows, btn):
    W, H = 780, 500
    g_ = [shadow(390, 600, 380, 30), '<polygon points="430,300 490,300 590,590 548,596" fill="#2a313d"/>', '<rect x="530" y="588" width="70" height="10" rx="5" fill="#1b212b"/>',
          f'<rect x="0" y="0" width="{W}" height="{H}" rx="40" fill="#111827"/>', '<rect x="22" y="26" width="736" height="452" rx="16" fill="#f3f6fb"/>',
          f'<clipPath id="{clip}"><rect x="22" y="26" width="736" height="452" rx="16"/></clipPath><g clip-path="url(#{clip})">',
          '<rect x="22" y="26" width="736" height="52" fill="url(#gGreen)"/>', t(44, 58, title, 16, 700, '#fff'),
          '<rect x="560" y="38" width="180" height="28" rx="14" fill="#fff" fill-opacity=".22"/>', t(650, 57, badge, 12, 700, '#fff', 'middle'),
          '<rect x="44" y="94" width="692" height="38" rx="12" fill="#fff" stroke="#dfe6f1"/>', t(64, 118, query, 13, 600, NAVY), t(716, 118, results, 11, 500, MUTED, 'end')]
    y = 146
    for n, sub, cls, on in rows:
        g_ += [f'<rect x="44" y="{y}" width="692" height="44" rx="12" fill="{"#eefaf2" if on else "#fff"}" stroke="{"#bfe6cc" if on else "#e3e9f2"}"/>',
               f'<rect x="58" y="{y+12}" width="20" height="20" rx="6" fill="{"#2FA455" if on else "#fff"}" stroke="#bcd0c4"/>',
               (f'<path d="M62,{y+22} l4,4 7,-8" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>' if on else ''),
               t(94, y + 20, n, 12.5, 700, NAVY), t(94, y + 36, sub, 10.5, 500, MUTED),
               f'<rect x="612" y="{y+12}" width="106" height="20" rx="10" fill="#eaf1ff"/>', t(665, y + 26, cls, 10, 600, BLUE, 'middle')]
        y += 50
    g_ += ['<rect x="500" y="424" width="236" height="44" rx="14" fill="#FAE814"/>', t(618, 452, btn, 13, 800, NAVY, 'middle'),
           t(64, 452, 'Not in the list? Add your own product.', 11.5, 600, BLUE), '</g>', '<rect x="22" y="26" width="736" height="452" rx="16" fill="url(#gGlass)"/>']
    return ''.join(g_)


def printer_g(shop, l1, l2, l3, a1, a2, a3, total):
    out = printer80()
    for a, b in [('CITY KIRYANA STORE', shop), ('>Chakki Atta 10 kg<', f'>{l1}<'), ('>Sugar 2.5 kg<', f'>{l2}<'), ('>Cooking Oil 1 L x2<', f'>{l3}<'),
                 ('>1,200<', f'>{a1}<'), ('>400<', f'>{a2}<'), ('>1,180<', f'>{a3}<'), ('>Rs 4,200<', f'>{total}<')]:
        out = out.replace(a, b)
    return out


def ui_box(title, rows, foot=None, foot_c=('#ecfdf3', '#15803d'), head=True):
    g_ = ['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>']
    if head:
        g_ += ['<rect width="260" height="38" rx="16" fill="url(#gNavy)"/><rect y="22" width="260" height="16" fill="#1a3a74"/>', t(14, 25, title, 12, 700, '#fff')]
        y = 62
    else:
        g_ += [t(14, 26, title, 12, 700, NAVY)]
        y = 54
    for a, b in rows:
        g_ += [t(14, y, a, 10.5, 600, MUTED), t(246, y, b, 11, 700, NAVY, 'end')]
        y += 25
    if foot:
        g_ += [f'<rect x="14" y="150" width="232" height="30" rx="9" fill="{foot_c[0]}"/>', t(26, 170, foot, 10.5, 700, foot_c[1])]
    return ''.join(g_)


def ui_serials(title, item, serials):
    g_ = ['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>', '<rect width="260" height="38" rx="16" fill="url(#gNavy)"/><rect y="22" width="260" height="16" fill="#1a3a74"/>',
          t(14, 25, title, 12, 700, '#fff'), t(14, 60, item, 11, 700, NAVY)]
    y = 84
    for s in serials:
        g_ += [f'<rect x="14" y="{y-15}" width="232" height="22" rx="7" fill="#fff"/>', t(24, y, s, 10.5, 600, BLUE if '+' not in s else MUTED)]
        y += 26
    return ''.join(g_)


def ui_report_g(title, big, sub):
    g_ = ['<rect width="260" height="190" rx="16" fill="url(#gBlue)"/>', t(14, 28, title, 11, 500, '#cfe0ff'), t(14, 56, big, 22, 800, '#fff'),
          t(14, 76, sub, 9.5, 500, '#cfe0ff'), '<rect x="14" y="88" width="232" height="90" rx="12" fill="#fff"/>']
    for i, h in enumerate([38, 50, 34, 62, 44, 66, 54]):
        g_.append(f'<rect x="{30+i*31}" y="{168-h}" width="18" height="{h}" rx="4" fill="url(#gBar)"/>')
    return ''.join(g_)


def process(cards):
    y1, y2 = 120, 520
    pos = [(60, y1), (450, y1), (840, y1), (645, y2), (255, y2)]
    return ''.join([pcard(x, y, i + 1, h, ui, f) for i, ((x, y), (h, ui, f)) in enumerate(zip(pos, cards))] + [
        arrow('M368,280 L436,280', 'M424,268 L438,280 L424,292'), arrow('M758,280 L826,280', 'M814,268 L828,280 L814,292'),
        arrow('M990,446 C990,500 960,560 952,600', 'M942,588 L951,604 L965,592'), arrow('M640,680 L566,680', 'M578,668 L564,680 L578,692')])


def hardware(mon, prn, ph, labels, last=None):
    body = ['<circle cx="600" cy="300" r="232" fill="#dcebff" opacity=".75"/>',
            '<circle cx="600" cy="300" r="232" fill="none" stroke="#bfd6f5" stroke-width="2" stroke-dasharray="6 9"/>',
            g(prn, 372, 300, .34), g(mon, 446, 150, .4), g(scanner_small(), 740, 352, .3, -22, 180, 180), g(ph, 770, 196, .26)]
    xs = [150, 375, 600, 825, 1050]
    body.append('<path d="M600,532 L600,580" stroke="#2F7BD9" stroke-width="3" fill="none"/>')
    body.append(f'<path d="M{xs[0]},630 L{xs[0]},600 Q{xs[0]},580 {xs[0]+20},580 L{xs[-1]-20},580 Q{xs[-1]},580 {xs[-1]},600 L{xs[-1]},630" stroke="#2F7BD9" stroke-width="3" fill="none"/>')
    for x in xs[1:-1]:
        body.append(f'<path d="M{x},580 L{x},630" stroke="#2F7BD9" stroke-width="3" fill="none"/>')
    cy, r = 712, 82
    inners = [g(mon, xs[0] - 59, cy - 46, .15, flt=False), g(scanner_small(), xs[1] - 45, cy - 48, .26, -22, 180, 180, flt=False),
              g(prn, xs[2] - 51, cy - 54, .22, flt=False), g(ph, xs[3] - 26, cy - 53, .17, flt=False),
              last or g(mini_printer_usb(), xs[4] - 45, cy - 48, .3, flt=False)]
    for x, inner, lab in zip(xs, inners, labels):
        body.append(circle_badge(x, cy, r, inner, lab))
    return ''.join(body)


# ----------------------------------------------------------------- SOLAR
def mon_solar():
    return monitor_sale('cpMonS', 'New Sale', 'Solar Shop Counter',
                        [('Solar Panel 585W Mono', '10', '10 serials', '2,80,000'), ('Hybrid Inverter 6kW', '1', 'SN HI6K-23A1187', '1,75,000'),
                         ('Lithium Battery 5kWh', '1', 'SN LB5-77K0412', '1,45,000'), ('DC Cable 6mm', '30 m', '—', '10,500'), ('Mounting Structure', '1 set', '—', '29,500')],
                        'Imran Ali · 0333 5566778', 'Advance Rs 2,40,000', '12 months · Rs 36,000 a month', 'Rs 6,40,000')


def ph_war_solar():
    return phone_warranty_g('cpWarS', 'Serial SN HI6K-23A1187', 'Jul 2031', 'about 5 years left',
                            [('Item', 'Hybrid Inverter 6kW'), ('Sold on', '12 Jul 2026'), ('Invoice', 'INV-1842'), ('Customer', 'Imran Ali'), ('Bought from', 'Sun Power Traders'), ('Purchase', 'GRN-305 · 2 Jul')])


def ph_qist_solar():
    return phone_qist_g('cpQistS', 'Imran Ali', 'Rs 3,96,000', 'left of Rs 4,32,000 · 1 of 12 paid',
                        [('Aug 2026', 'Rs 36,000', 'Paid'), ('Sep 2026', 'Rs 36,000', 'Due 12 Sep'), ('Oct 2026', 'Rs 36,000', 'Upcoming'), ('Nov 2026', 'Rs 36,000', 'Upcoming')])


def cat_solar():
    return tablet_catalog_g('cpCatS', 'Solar, Electronics &amp; CCTV Catalog', '1,100+ products', 'solar', '64 results',
                            [('Solar Panel 585W Mono', 'Panel · Serial no.', 'Panel', True), ('Hybrid Solar Inverter 6kW', 'Inverter · Serial no.', 'Inverter', True),
                             ('Lithium Battery 5kWh 51.2V', 'Battery · Serial no.', 'Battery', True), ('Solar DC Cable 6mm', 'Wire · sold by meter', 'Wire', False),
                             ('Solar Panel Mounting Structure', 'Structure · set', 'Structure', False)], 'Add 3 to my shop')


def prn_solar():
    return printer_g('SUN POWER SOLAR', 'Panel 585W x10', 'Hybrid Inverter 6kW', 'Lithium Battery 5kWh', '2,80,000', '1,75,000', '1,45,000', 'Rs 6,40,000')


def quote_ui():
    return ui_box('Quotation QT-0218 · 6kW system', [('Panels 585W x10', '2,80,000'), ('Inverter 6kW', '1,75,000'), ('Battery 5kWh', '1,45,000'), ('Wire + structure', '40,000')],
                  'Convert to sale in one tap', ('#eaf1ff', BLUE))


def scene_solar_process():
    return process([('Make a quote', quote_ui(), 'A4 quotation for the customer'),
                    ('Receive stock', ui_serials('GRN · Sun Power Traders', 'Hybrid Inverter 6kW · 4 pcs', ['SN HI6K-23A1187', 'SN HI6K-23A1188', 'SN HI6K-23A1189', '+ 1 more scanned']), 'Serial of every unit saved'),
                    ('Cash or qist', ui_box('Qist plan · 12 months', [('Bill', 'Rs 6,40,000'), ('Advance', 'Rs 2,40,000'), ('Markup', 'Rs 32,000'), ('Monthly', 'Rs 36,000')], 'Next due: 12 Sep', ('#fffbeb', '#92400e'), head=False), 'Advance and monthly plan'),
                    ('Warranty check', ui_box('Serial SN HI6K-23A1187', [('Sold', '12 Jul 2026'), ('Invoice', 'INV-1842'), ('Customer', 'Imran Ali'), ('Warranty till', 'Jul 2031')], 'In warranty', head=False), 'Find any sold unit'),
                    ('See profit', ui_report_g('This month', 'Rs 48,60,000', '7 systems · 214 items · qist due Rs 6,12,000'), 'Sales, qist and stock')])


# ----------------------------------------------------------------- ELECTRONICS / APPLIANCES / CCTV
def mon_elec():
    return monitor_sale('cpMonE', 'New Sale', 'Electronics &amp; Appliances',
                        [('Inverter AC 1.5 Ton', '1', 'SN AC15-90H2231', '1,45,000'), ('Smart LED TV 32"', '1', 'SN TV32-55Q0917', '36,500'),
                         ('Voltage Stabilizer', '1', '—', '3,500')],
                        'Usman Tariq · 0300 9988776', 'Advance Rs 45,000', '6 months · Rs 25,000 a month', 'Rs 1,85,000',
                        ('Serial SN AC15-90H2231', 'In stock since GRN-412 · Metro Appliances', 'Inverter AC 1.5 Ton · 5 more left in stock'))


def ph_war_elec():
    return phone_warranty_g('cpWarE', 'Serial SN AC15-90H2231', 'Jun 2027', '8 months left',
                            [('Item', 'Inverter AC 1.5 Ton'), ('Sold on', '20 Jun 2026'), ('Invoice', 'INV-5520'), ('Customer', 'Usman Tariq'), ('Bought from', 'Metro Appliances'), ('Purchase', 'GRN-412 · 11 Jun')])


def ph_qist_elec():
    return phone_qist_g('cpQistE', 'Usman Tariq', 'Rs 1,25,000', 'left of Rs 1,50,000 · 1 of 6 paid',
                        [('Jul 2026', 'Rs 25,000', 'Paid'), ('Aug 2026', 'Rs 25,000', 'Due 20 Aug'), ('Sep 2026', 'Rs 25,000', 'Upcoming'), ('Oct 2026', 'Rs 25,000', 'Upcoming')])


def cat_elec():
    return tablet_catalog_g('cpCatE', 'Electronics, Solar &amp; CCTV Catalog', '1,100+ products', 'smart', '42 results',
                            [('Smart LED TV 43"', 'TV · Serial no.', 'TV', True), ('Inverter AC 1.5 Ton Smart', 'AC · Serial no.', 'AC', True),
                             ('Smart Wi-Fi Camera 4MP', 'CCTV · Serial no.', 'CCTV', True), ('Smart LED TV 55" 4K', 'TV · Serial no.', 'TV', False),
                             ('Smart Plug 16A', 'Accessory', 'Accessory', False)], 'Add 3 to my shop')


def prn_elec():
    return printer_g('METRO ELECTRONICS', 'Inverter AC 1.5 Ton', 'Smart LED TV 32"', 'Voltage Stabilizer', '1,45,000', '36,500', '3,500', 'Rs 1,85,000')


def scene_elec_process():
    return process([('Receive stock', ui_serials('GRN · Metro Appliances', 'Inverter AC 1.5 Ton · 6 pcs', ['SN AC15-90H2231', 'SN AC15-90H2232', 'SN AC15-90H2233', '+ 3 more scanned']), 'Serial of every unit saved'),
                    ('Sell fast', ui_box('Scanned SN AC15-90H2231', [('Inverter AC 1.5 Ton', '1,45,000'), ('Smart LED TV 32"', '36,500'), ('Voltage Stabilizer', '3,500')], 'Serials saved on this sale', head=False), 'Scan the serial, add items'),
                    ('Cash or qist', ui_box('Qist plan · 6 months', [('Bill', 'Rs 1,85,000'), ('Advance', 'Rs 45,000'), ('Markup', 'Rs 10,000'), ('Monthly', 'Rs 25,000')], 'Next due: 20 Aug', ('#fffbeb', '#92400e'), head=False), 'Advance and monthly plan'),
                    ('Warranty check', ui_box('Serial SN AC15-90H2231', [('Sold', '20 Jun 2026'), ('Invoice', 'INV-5520'), ('Customer', 'Usman Tariq'), ('Warranty till', 'Jun 2027')], 'In warranty', head=False), 'Find any sold unit'),
                    ('See profit', ui_report_g("Today's sales", 'Rs 7,85,400', '6 ACs · 4 TVs · 2 CCTV kits · qist due Rs 1,40,000'), 'Sales, qist and stock')])


def ph_war_cctv():
    return phone_warranty_g('cpWarC', 'Serial SN DVR8-31C0045', 'Mar 2027', '5 months left',
                            [('Item', 'DVR 8-channel'), ('Sold on', '18 Mar 2026'), ('Invoice', 'INV-4471'), ('Customer', 'Al-Madina Plaza'), ('Bought from', 'Secure Vision Traders'), ('Purchase', 'GRN-377 · 9 Mar')])


def cctv_quote():
    return ui_box('Quotation QT-0331 · 8 camera kit', [('Camera 2MP x8', '52,000'), ('DVR 8-channel', '18,500'), ('Hard disk 1TB', '11,000'), ('Cable, power, BNC', '15,500')],
                  'Total Rs 97,000 · convert to sale', ('#eaf1ff', BLUE))


SCENES = {
    'uptrendpos-solar-shop-pos-software': ('Solar Shop Counter', 'yellow',
        lambda: g(mon_solar(), 40, 140, .9) + g(prn_solar(), 830, 548, .5) + g(scanner_small(), 660, 660, .4, -24, 180, 180) + g(ph_qist_solar(), 905, 112, .66),
        [(60, 780, 'Serial on every unit', '#2F7BD9'), (300, 780, 'Solar on qist', '#F59E0B')]),
    'uptrendpos-solar-shop-product-catalog': ('1,100+ Products Ready', 'green', lambda: g(cat_solar(), 210, 150, 1.0),
        [(60, 770, 'Search and tick', '#2FA455'), (300, 770, 'Panels, inverters, batteries', '#F59E0B')]),
    'uptrendpos-solar-shop-serial-warranty-installments': ('Serial, Warranty and Qist', 'teal', lambda: g(ph_war_solar(), 230, 140, 1.0) + g(ph_qist_solar(), 680, 140, 1.0),
        [(60, 780, 'Warranty lookup by serial', '#2FA455'), (450, 780, '12-month solar qist', '#F59E0B')]),
    'uptrendpos-solar-shop-pos-hardware': ('Solar Shop Hardware', 'yellow',
        lambda: hardware(mon_solar(), prn_solar(), ph_war_solar(), ['Windows PC', 'Serial scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']), [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-solar-shop-pos-process': ('Solar Sale, Step by Step', 'yellow', scene_solar_process, [(60, 470, 'All connected', '#2FA455')]),
    'uptrendpos-solar-shop-quotation': ('Solar Quote to Sale', 'green',
        lambda: g(ui_box('Quotation QT-0218 · 6kW system', [('Panels 585W x10', '2,80,000'), ('Hybrid inverter 6kW', '1,75,000'), ('Lithium battery 5kWh', '1,45,000'), ('Wire and structure', '40,000')],
                         'Total Rs 6,40,000 · convert to sale', ('#eaf1ff', BLUE)), 140, 170, 2.0) + g(ph_war_solar(), 780, 140, 1.0),
        [(60, 780, 'A4 quotation for a full system', '#2FA455'), (450, 780, 'Serial and warranty', '#2F7BD9')]),
    'uptrendpos-electronics-store-pos-software': ('Electronics Shop Counter', 'blue',
        lambda: g(mon_elec(), 40, 140, .9) + g(prn_elec(), 830, 548, .5) + g(scanner_small(), 660, 660, .4, -24, 180, 180) + g(ph_qist_elec(), 905, 112, .66),
        [(60, 780, 'Serial on every unit', '#2F7BD9'), (300, 780, 'Appliances on qist', '#F59E0B')]),
    'uptrendpos-electronics-store-product-catalog': ('1,100+ Products Ready', 'navy', lambda: g(cat_elec(), 210, 150, 1.0),
        [(60, 770, 'Search and tick', '#2FA455'), (300, 770, 'TVs, ACs, CCTV and more', '#2F7BD9')]),
    'uptrendpos-electronics-store-serial-warranty-installments': ('Serial, Warranty and Qist', 'teal', lambda: g(ph_war_elec(), 230, 140, 1.0) + g(ph_qist_elec(), 680, 140, 1.0),
        [(60, 780, 'Warranty lookup by serial', '#2FA455'), (450, 780, 'Monthly qist plan', '#F59E0B')]),
    'uptrendpos-electronics-store-pos-hardware': ('Electronics Shop Hardware', 'blue',
        lambda: hardware(mon_elec(), prn_elec(), ph_war_elec(), ['Windows PC', 'Serial scanner', 'Receipt printer', 'Owner phone', 'Type-C printer']), [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-electronics-store-pos-process': ('Electronics Sale, Step by Step', 'navy', scene_elec_process, [(60, 470, 'All connected', '#2FA455')]),
    'uptrendpos-cctv-shop-quotation': ('CCTV Quote to Sale', 'green',
        lambda: g(cctv_quote(), 140, 170, 2.0) + g(ph_war_cctv(), 780, 140, 1.0),
        [(60, 780, 'A4 quotation for CCTV kits', '#2FA455'), (430, 780, 'Serial and warranty', '#2F7BD9')]),
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
