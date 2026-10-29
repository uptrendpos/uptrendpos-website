"""FBR POS Integration + Pharmacy page images (same house style and watermark as gen_ind.py).
Run: python3 gen_fbr_pharm.py [name ...]"""
import asyncio, sys
from playwright.async_api import async_playwright
from PIL import Image
from gen_ind import (B, OUT, t, shadow, qr, receipt, phone_shell, status_bar, frame, g, pcard, arrow, circle_badge,
                     printer80, scanner_small, mini_printer_usb, phone_reports)


# ---------------------------------------------------------------- FBR receipt explained
def fbr_receipt(x, y, w=380):
    s = w / 380
    rows = [('Cooking Oil 1 L x2', '1,000.00'), ('Basmati Rice 5 kg', '1,400.00'), ('Tea Pack 450 g', '950.00'), ('Biscuits x4', '210.00')]
    L, R = x + 26 * s, x + w - 26 * s
    out = [f'<g filter="url(#fDrop)"><path d="M{x},{y+18} Q{x+w/2},{y-6} {x+w},{y+18} L{x+w},{y+742*s} l-14,10 -14,-10 -14,10 -14,-10 -14,10 -14,-10 -14,10 -14,-10 -14,10 -14,-10 -14,10 -14,-10 -14,10 -14,-10 -14,10 -14,-10 -14,10 -14,-10 -14,10 -14,-10 -14,10 -14,-10 -14,10 -14,-10 -14,10 -14,-10 -14,10 Z" fill="#fff"/></g>']
    cy = y + 52 * s
    out += [t(x + w / 2, cy, 'CITY SUPER STORE', 20 * s, 800, '#111', 'middle'),
            t(x + w / 2, cy + 22 * s, 'Main Boulevard, Lahore', 12 * s, 400, '#555', 'middle'),
            t(x + w / 2, cy + 40 * s, 'NTN 1234567-8   STRN 32-77-8761-234-55', 11 * s, 600, '#333', 'middle'),
            f'<line x1="{L}" y1="{cy+54*s}" x2="{R}" y2="{cy+54*s}" stroke="#999" stroke-dasharray="5 4"/>']
    yy = cy + 78 * s
    for a, b in [('Invoice No', 'INV-2087'), ('POS ID', '123456'), ('Date', '14-10-2026  10:35')]:
        out += [t(L, yy, a, 12 * s, 500, '#444'), t(R, yy, b, 12 * s, 700, '#111', 'end')]; yy += 20 * s
    out.append(f'<line x1="{L}" y1="{yy-4*s}" x2="{R}" y2="{yy-4*s}" stroke="#999" stroke-dasharray="5 4"/>')
    yy += 16 * s
    for a, b in rows:
        out += [t(L, yy, a, 12.5 * s, 500, '#222'), t(R, yy, b, 12.5 * s, 600, '#222', 'end')]; yy += 21 * s
    out.append(f'<line x1="{L}" y1="{yy-6*s}" x2="{R}" y2="{yy-6*s}" stroke="#999" stroke-dasharray="5 4"/>')
    yy += 14 * s
    for a, b, wgt in [('Value excl. tax', '3,016.95', 500), ('Sales tax 18%', '543.05', 500), ('FBR POS fee', '1.00', 700)]:
        out += [t(L, yy, a, 12.5 * s, wgt, '#222'), t(R, yy, b, 12.5 * s, wgt, '#222', 'end')]; yy += 21 * s
    out += [f'<rect x="{L-6}" y="{yy-4*s}" width="{R-L+12}" height="{34*s}" rx="6" fill="#f2f4f7"/>',
            t(L, yy + 19 * s, 'TOTAL', 16 * s, 800, '#111'), t(R, yy + 19 * s, 'Rs 3,561.00', 16 * s, 800, '#111', 'end')]
    yy += 58 * s
    out += [t(x + w / 2, yy, 'FBR Invoice No', 11.5 * s, 600, '#555', 'middle'),
            t(x + w / 2, yy + 20 * s, '123456-141026103512-0001', 15 * s, 800, '#111', 'middle'),
            qr(x + w / 2 - 52 * s, yy + 34 * s, 104 * s, seed=11),
            t(x + w / 2, yy + 160 * s, 'Verify this invoice with the Tax Asaan app', 11 * s, 500, '#555', 'middle'),
            t(x + w / 2, yy + 178 * s, 'SAMPLE RECEIPT', 10 * s, 700, '#999', 'middle')]
    anchors = {'inv': (R + 12, cy + 78 * s - 5), 'pos': (L - 12, cy + 98 * s - 5), 'ntn': (x + w / 2 + 120 * s, cy + 36 * s),
               'fee': (R + 12, cy + 78 * s + 60 * s + 21 * s * 4 + 30 * s + 42 * s - 5), 'fbrno': (x + w / 2 + 112 * s, yy + 14 * s),
               'qr': (x + w / 2 + 52 * s, yy + 86 * s)}
    return ''.join(out), anchors


def callout(ax, ay, bx, by, txt, sub, side, dot):
    """Chip at (bx,by) with a leader line to anchor (ax,ay)."""
    wch = 40 + max(len(txt) * 9.4, len(sub) * 7.2)
    cx = bx + (wch if side == 'L' else 0)
    return (f'<path d="M{ax},{ay} L{cx},{by+28}" stroke="{dot}" stroke-width="2.5" stroke-dasharray="4 5" fill="none"/>'
            f'<circle cx="{ax}" cy="{ay}" r="6" fill="{dot}"/>'
            f'<g filter="url(#fSoft)"><rect x="{bx}" y="{by}" width="{wch:.0f}" height="56" rx="16" fill="#fff"/></g>'
            f'<circle cx="{bx+20}" cy="{by+20}" r="6" fill="{dot}"/>' + t(bx + 34, by + 25, txt, 15, 700, '#10224A')
            + t(bx + 34, by + 44, sub, 12, 500, '#64748b'))


def scene_fbr_receipt():
    r, a = fbr_receipt(410, 80, 380)
    c = [callout(*a['ntn'], 830, 120, 'NTN and STRN', 'Your FBR registration', 'R', '#2F7BD9'),
         callout(*a['inv'], 830, 230, 'Your invoice number', 'From your own POS', 'R', '#2FA9B0'),
         callout(*a['pos'], 60, 250, 'POS ID', 'Given by FBR per counter', 'L', '#10224A'),
         callout(*a['fee'], 830, 430, 'Re 1 FBR POS fee', 'Paid by the buyer', 'R', '#F59E0B'),
         callout(*a['fbrno'], 50, 520, 'FBR invoice number', 'Comes back from FBR', 'L', '#2FA455'),
         callout(*a['qr'], 830, 640, 'QR code', 'Buyer scans to verify', 'R', '#2FA455')]
    return r + ''.join(c)


# ---------------------------------------------------------------- FBR steps
def ui_tier1():
    g_ = ['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>', t(14, 26, 'Are you Tier-1?', 13, 700, '#10224A')]
    y = 50
    for txt, on in [('Shop in a mall or plaza', False), ('Card machine on counter', True), ('Part of a chain', False), ('Big electricity bill', True)]:
        fill = '#2FA455' if on else '#fff'
        g_ += [f'<rect x="14" y="{y-13}" width="18" height="18" rx="5" fill="{fill}" stroke="#c7d7ff"/>',
               (f'<path d="M18,{y-4} l4,4 7,-8" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>' if on else ''),
               t(42, y + 1, txt, 11.5, 600, '#10224A')]
        y += 28
    g_ += ['<rect x="14" y="156" width="232" height="26" rx="10" fill="#fff4a3"/>', t(130, 174, 'One tick = Tier-1', 11.5, 800, '#10224A', 'middle')]
    return ''.join(g_)


def ui_iris():
    g_ = ['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>', '<rect width="260" height="38" rx="16" fill="#1a7f4b"/><rect y="22" width="260" height="16" fill="#1a7f4b"/>',
          t(14, 25, 'IRIS - Registration', 12.5, 700, '#fff')]
    y = 62
    for a, b in [('NTN / STRN', 'Done'), ('Outlet address', 'Done'), ('POS counters', '2 added')]:
        g_ += [t(14, y, a, 11.5, 600, '#10224A'), f'<rect x="168" y="{y-14}" width="78" height="20" rx="10" fill="#ecfdf3"/>', t(207, y + 1, b, 10.5, 700, '#15803d', 'middle')]
        y += 34
    g_ += [t(14, 172, 'Register every counter', 10.5, 500, '#64748b')]
    return ''.join(g_)


def ui_keys():
    g_ = ['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>', t(14, 26, 'Your FBR details', 13, 700, '#10224A')]
    y = 52
    for a, b in [('POS Registration No', '123456'), ('POS Terminal ID', 'TID-01'), ('API token', '•••• •••• 9f2a')]:
        g_ += [t(14, y, a, 10.5, 600, '#64748b'), f'<rect x="14" y="{y+6}" width="232" height="22" rx="7" fill="#fff" stroke="#dfe6f1"/>', t(22, y + 21, b, 11, 700, '#10224A')]
        y += 44
    return ''.join(g_)


def ui_mode():
    g_ = ['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>', t(14, 26, 'FBR Fiscalization', 13, 700, '#10224A'),
          '<rect x="196" y="12" width="46" height="24" rx="12" fill="#024691"/><circle cx="230" cy="24" r="9" fill="#fff"/>']
    y = 50
    for txt, sel in [('Practice (no FBR)', False), ('Sandbox (FBR test)', False), ('Production (FBR live)', True)]:
        g_ += [f'<rect x="14" y="{y}" width="232" height="34" rx="10" fill="{"#eaf1ff" if sel else "#fff"}" stroke="{"#024691" if sel else "#dfe6f1"}" stroke-width="{2 if sel else 1}"/>',
               t(28, y + 22, txt, 11.5, 700 if sel else 500, '#10224A')]
        if sel:
            g_.append(f'<circle cx="228" cy="{y+17}" r="8" fill="#2FA455"/><path d="M224,{y+17} l3,3 6,-6" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>')
        y += 42
    return ''.join(g_)


def ui_live():
    return ''.join(['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>',
                    '<rect x="14" y="14" width="120" height="162" rx="8" fill="#fff" stroke="#e3e7ee"/>',
                    t(74, 34, 'CITY SUPER STORE', 8.5, 800, '#111', 'middle'), t(74, 52, 'FBR Invoice No', 7, 600, '#555', 'middle'),
                    t(74, 64, '123456-1410261...', 7.5, 800, '#111', 'middle'), qr(46, 74, 56, seed=5), t(74, 150, 'Re 1 POS fee', 7.5, 700, '#b45309', 'middle'),
                    '<rect x="146" y="30" width="100" height="126" rx="16" fill="#10224A"/>', '<rect x="152" y="38" width="88" height="110" rx="11" fill="#fff"/>',
                    t(196, 64, 'Tax Asaan', 9.5, 800, '#1a7f4b', 'middle'), '<circle cx="196" cy="94" r="16" fill="#2FA455"/>',
                    '<path d="M188,94 l6,6 11,-12" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
                    t(196, 130, 'Invoice verified', 8.5, 700, '#10224A', 'middle')])


def scene_fbr_steps():
    y1, y2 = 120, 520
    return ''.join([
        pcard(60, y1, 1, 'Check Tier-1', ui_tier1(), 'Any one test is enough'),
        pcard(450, y1, 2, 'Register in IRIS', ui_iris(), 'NTN, STRN, outlet and counters'),
        pcard(840, y1, 3, 'Get FBR details', ui_keys(), 'POS ID and token for each counter'),
        pcard(645, y2, 4, 'Add to UpTrendPos', ui_mode(), 'Test in Sandbox, then go live'),
        pcard(255, y2, 5, 'Every bill is live', ui_live(), 'FBR number, QR and Re 1 fee'),
        arrow('M368,280 L436,280', 'M424,268 L438,280 L424,292'),
        arrow('M758,280 L826,280', 'M814,268 L828,280 L814,292'),
        arrow('M990,446 C990,500 960,560 952,600', 'M942,588 L951,604 L965,592'),
        arrow('M640,680 L566,680', 'M578,668 L564,680 L578,692'),
    ])


# ---------------------------------------------------------------- Pharmacy
def printer_ph():
    out = printer80()
    for a, b in [('CITY KIRYANA STORE', 'CITY MEDICAL STORE'), ('>Chakki Atta 10 kg<', '>Paracetamol 500mg<'), ('>Sugar 2.5 kg<', '>ORS Sachet x5<'),
                 ('>Cooking Oil 1 L x2<', '>Cough Syrup 120ml<'), ('>1,200<', '>45<'), ('>400<', '>100<'), ('>1,180<', '>185<'), ('>Rs 4,200<', '>Rs 330<')]:
        out = out.replace(a, b)
    return out


def monitor_pharmacy():
    W, H = 780, 486
    g_ = [f'<rect x="352" y="{H-8}" width="76" height="118" fill="url(#gSilver)"/>',
          f'<rect x="250" y="{H+104}" width="280" height="22" rx="11" fill="url(#gSilver)"/>',
          f'<rect x="0" y="0" width="{W}" height="{H}" rx="20" fill="#0f172a"/>', '<circle cx="390" cy="468" r="3" fill="#3b82f6"/>',
          '<rect x="16" y="16" width="748" height="420" rx="6" fill="#f3f6fb"/>',
          '<clipPath id="cpMonPh"><rect x="16" y="16" width="748" height="420" rx="6"/></clipPath><g clip-path="url(#cpMonPh)">',
          '<rect x="16" y="16" width="748" height="46" fill="url(#gNavy)"/>', t(34, 45, 'UpTrendPos', 15, 700, '#fff'),
          t(150, 45, 'New Sale  ·  Medical Store Counter', 12, 500, '#c9dbf2'),
          '<rect x="640" y="27" width="108" height="24" rx="12" fill="#2FA455"/>', t(694, 43, 'Online', 11, 700, '#fff', 'middle'),
          '<rect x="32" y="76" width="470" height="34" rx="10" fill="#fff" stroke="#dfe6f1"/>', t(48, 98, 'Search by medicine, salt or scan barcode', 11.5, 500, '#94a3b8'),
          '<rect x="32" y="122" width="470" height="30" fill="#e9effa"/>']
    for x, c, a in [(46, 'Medicine', 'start'), (250, 'Pack', 'start'), (322, 'Batch / Exp', 'start'), (488, 'Amount', 'end')]:
        g_.append(t(x, 142, c, 11, 700, '#10224A', a))
    rows = [('Paracetamol 500mg Tab', 'Strip', 'B231 · 08/27', '45', ''), ('Amoxicillin 500mg Cap', 'Strip', 'A118 · 03/27', '320', 'Rx'),
            ('Cough Syrup 120ml', 'Bottle', 'C902 · 11/26', '185', ''), ('ORS Sachet', 'Piece x5', 'R440 · 01/28', '100', ''),
            ('Omeprazole 20mg Cap', 'Box', 'O375 · 06/27', '560', 'Rx'), ('Vitamin D3 Drops', 'Bottle', 'V210 · 12/26', '420', '')]
    y = 172
    for i, (n, p, bt, a, rx) in enumerate(rows):
        if i % 2:
            g_.append(f'<rect x="32" y="{y-19}" width="470" height="32" fill="#f7f9fd"/>')
        g_ += [t(46, y, n, 11, 600, '#1e293b'), t(250, y, p, 10.5, 600, '#024691'), t(322, y, bt, 10, 500, '#64748b'), t(488, y, a, 11.5, 700, '#10224A', 'end')]
        if rx:
            g_ += [f'<rect x="{46+len(n)*6.1}" y="{y-12}" width="22" height="15" rx="4" fill="#fde2e2"/>', t(57 + len(n) * 6.1, y, 'Rx', 9, 800, '#b42318', 'middle')]
        y += 32
    g_ += ['<rect x="520" y="76" width="228" height="344" rx="14" fill="#fff" stroke="#e1e7f0"/>',
           t(538, 104, 'Customer', 11, 600, '#64748b'), t(538, 124, 'Walk-in', 14, 700, '#10224A'),
           '<rect x="538" y="136" width="194" height="40" rx="10" fill="#fef2f2"/>', t(550, 154, 'Rx items on this bill: 2', 11, 700, '#b42318'),
           t(550, 169, 'Red Rx badge on each item', 10, 500, '#b42318'),
           t(538, 204, 'Items', 11.5, 500, '#64748b'), t(732, 204, '6', 11.5, 600, '#10224A', 'end'),
           t(538, 226, 'Discount', 11.5, 500, '#64748b'), t(732, 226, 'Rs 30', 11.5, 600, '#10224A', 'end'),
           '<rect x="532" y="240" width="204" height="58" rx="14" fill="#eaf1ff"/>', t(546, 262, 'Total', 12, 600, '#475569'), t(724, 286, 'Rs 1,600', 22, 800, '#024691', 'end'),
           '<rect x="532" y="310" width="98" height="38" rx="12" fill="#fff" stroke="#c7d7ff"/>', t(581, 334, 'Hold', 12, 700, '#024691', 'middle'),
           '<rect x="638" y="310" width="98" height="38" rx="12" fill="#1E8A43"/>', t(687, 334, 'WhatsApp', 11.5, 700, '#fff', 'middle'),
           '<rect x="532" y="358" width="204" height="40" rx="12" fill="#FAE814"/>', t(634, 383, 'Save &amp; Print', 13, 800, '#10224A', 'middle'),
           '</g>', '<rect x="16" y="16" width="748" height="420" rx="6" fill="url(#gGlass)"/>']
    return ''.join(g_)


def phone_expiry():
    g_ = ['<rect x="14" y="14" width="272" height="150" fill="url(#gBlue)"/>', status_bar(),
          t(32, 80, 'Expiry alerts', 12, 500, '#cfe0ff'), t(32, 114, '9 batches', 28, 800, '#fff'), t(32, 140, 'expire in the next 30 days', 11, 500, '#cfe0ff')]
    y = 182
    for n, b, d, c in [('Cough Syrup 120ml', 'C902 · 4 bottles', '12 days', '#b42318'), ('Insulin Pen', 'I077 · fridge · 3 pcs', '19 days', '#b42318'),
                       ('Vitamin D3 Drops', 'V210 · 6 bottles', '26 days', '#92400e'), ('Eye Drops 10ml', 'E520 · 10 pcs', '29 days', '#92400e')]:
        g_ += [f'<rect x="26" y="{y}" width="248" height="58" rx="14" fill="#fff" stroke="#e6ebf3"/>', t(40, y + 24, n, 12, 700, '#10224A'),
               t(40, y + 42, b, 10, 500, '#64748b'), f'<rect x="196" y="{y+18}" width="66" height="22" rx="11" fill="#fef2f2"/>', t(229, y + 33, d, 10, 700, c, 'middle')]
        y += 66
    g_ += [f'<rect x="26" y="{y+6}" width="248" height="44" rx="14" fill="#FAE814"/>', t(150, y + 34, 'Return to supplier or sell first', 11.5, 800, '#10224A', 'middle')]
    return phone_shell(''.join(g_), 'cpExp')


def tablet_catalog():
    W, H = 780, 500
    g_ = [shadow(390, 600, 380, 30), '<polygon points="430,300 490,300 590,590 548,596" fill="#2a313d"/>', '<rect x="530" y="588" width="70" height="10" rx="5" fill="#1b212b"/>',
          f'<rect x="0" y="0" width="{W}" height="{H}" rx="40" fill="#111827"/>', '<rect x="22" y="26" width="736" height="452" rx="16" fill="#f3f6fb"/>',
          '<clipPath id="cpCat"><rect x="22" y="26" width="736" height="452" rx="16"/></clipPath><g clip-path="url(#cpCat)">',
          '<rect x="22" y="26" width="736" height="52" fill="url(#gGreen)"/>', t(44, 58, 'Medicine Catalog', 16, 700, '#fff'),
          '<rect x="560" y="38" width="180" height="28" rx="14" fill="#fff" fill-opacity=".22"/>', t(650, 57, '17,000+ medicines', 12, 700, '#fff', 'middle'),
          '<rect x="44" y="94" width="692" height="38" rx="12" fill="#fff" stroke="#dfe6f1"/>', t(64, 118, 'paracetamol', 13, 600, '#10224A'),
          t(716, 118, '24 results', 11, 500, '#64748b', 'end')]
    rows = [('Paracetamol 500mg', 'Tablet · Paracetamol', 'Analgesic', True), ('Paracetamol 120mg/5ml', 'Syrup · Paracetamol', 'Analgesic', True),
            ('Paracetamol + Caffeine', 'Tablet · Paracetamol, Caffeine', 'Analgesic', False), ('Paracetamol 250mg Supp.', 'Suppository · Paracetamol', 'Analgesic', True),
            ('Paracetamol IV 1g/100ml', 'Infusion · Paracetamol', 'Analgesic', False), ('Paracetamol Drops 100mg/ml', 'Drops · Paracetamol', 'Analgesic', False)]
    y = 146
    for n, sub, cls, on in rows:
        g_ += [f'<rect x="44" y="{y}" width="692" height="44" rx="12" fill="{"#eefaf2" if on else "#fff"}" stroke="{"#bfe6cc" if on else "#e3e9f2"}"/>',
               f'<rect x="58" y="{y+12}" width="20" height="20" rx="6" fill="{"#2FA455" if on else "#fff"}" stroke="#bcd0c4"/>',
               (f'<path d="M62,{y+22} l4,4 7,-8" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>' if on else ''),
               t(94, y + 20, n, 12.5, 700, '#10224A'), t(94, y + 36, sub, 10.5, 500, '#64748b'),
               f'<rect x="612" y="{y+12}" width="106" height="20" rx="10" fill="#eaf1ff"/>', t(665, y + 26, cls, 10, 600, '#024691', 'middle')]
        y += 50
    g_ += ['<rect x="44" y="448" width="692" height="0" fill="none"/>',
           '<rect x="500" y="424" width="236" height="44" rx="14" fill="#FAE814"/>', t(618, 452, 'Add 3 to my pharmacy', 13, 800, '#10224A', 'middle'),
           t(64, 452, 'Not in the list? Add your own product.', 11.5, 600, '#024691'),
           '</g>', '<rect x="22" y="26" width="736" height="452" rx="16" fill="url(#gGlass)"/>']
    return ''.join(g_)


def phone_salt():
    g_ = ['<rect x="14" y="14" width="272" height="104" fill="url(#gBlue)"/>', status_bar(), t(32, 84, 'Search: omeprazole', 15, 700, '#fff'),
          t(32, 104, 'By salt, brand or barcode', 10.5, 500, '#cfe0ff')]
    y = 134
    for n, chips, stock, rx in [('Brand A 20mg', ['20mg', 'Capsule'], '14 strips', True), ('Brand B 20mg', ['20mg', 'Capsule'], '6 strips', True),
                                ('Brand C 40mg', ['40mg', 'Capsule'], '3 strips', True), ('Brand D 40mg IV', ['40mg', 'Injection'], '2 vials', True)]:
        g_ += [f'<rect x="26" y="{y}" width="248" height="68" rx="14" fill="#fff" stroke="#e6ebf3"/>', t(40, y + 24, n, 12.5, 700, '#10224A')]
        cx = 40
        for c in chips:
            wch = len(c) * 6.6 + 14
            g_ += [f'<rect x="{cx}" y="{y+34}" width="{wch:.0f}" height="20" rx="10" fill="#eaf1ff"/>', t(cx + wch / 2, y + 48, c, 9.5, 700, '#024691', 'middle')]
            cx += wch + 6
        g_ += [t(262, y + 24, stock, 10.5, 700, '#1E8A43', 'end')]
        if rx:
            g_ += [f'<rect x="232" y="{y+36}" width="30" height="18" rx="6" fill="#fde2e2"/>', t(247, y + 49, 'Rx', 10, 800, '#b42318', 'middle')]
        y += 76
    g_ += [t(150, y + 18, 'Same salt, every brand in one list', 10.5, 600, '#64748b', 'middle')]
    return phone_shell(''.join(g_), 'cpSalt')


def ui_pick():
    g_ = ['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>', '<rect x="14" y="12" width="232" height="28" rx="9" fill="#fff" stroke="#dfe6f1"/>', t(26, 31, 'Search 17,000+ medicines', 10.5, 500, '#94a3b8')]
    y = 54
    for n, on in [('Paracetamol 500mg Tab', True), ('Amoxicillin 500mg Cap', True), ('ORS Sachet', True), ('Cough Syrup 120ml', False)]:
        g_ += [f'<rect x="14" y="{y}" width="232" height="26" rx="8" fill="{"#eefaf2" if on else "#fff"}"/>',
               f'<rect x="22" y="{y+6}" width="14" height="14" rx="4" fill="{"#2FA455" if on else "#fff"}" stroke="#bcd0c4"/>', t(44, y + 17, n, 10.5, 600, '#10224A')]
        y += 30
    g_ += ['<rect x="14" y="176" width="0" height="0"/>']
    return ''.join(g_)


def ui_grn_ph():
    g_ = ['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>', '<rect width="260" height="38" rx="16" fill="url(#gNavy)"/><rect y="22" width="260" height="16" fill="#1a3a74"/>',
          t(14, 25, 'GRN · Al-Shifa Distributors', 12, 700, '#fff')]
    y = 60
    for a, b in [('Batch', 'B231'), ('Expiry', '08 / 2027'), ('Packing', '1 box = 10 strips'), ('Rack', 'A-3'), ('Cost / Sale', 'Rs 38 / 45 per strip')]:
        g_ += [t(14, y, a, 10.5, 600, '#64748b'), t(246, y, b, 11, 700, '#10224A', 'end')]
        y += 25
    return ''.join(g_)


def ui_sell_ph():
    g_ = ['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>', t(14, 26, 'Sell by box, strip or tablet', 12, 700, '#10224A')]
    y = 52
    for a, u, b in [('Paracetamol 500mg', '2 strips', '90'), ('Paracetamol 500mg', '4 tablets', '18'), ('Amoxicillin 500mg', '1 box', '3,200')]:
        g_ += [t(14, y, a, 11, 600, '#10224A'), t(150, y, u, 10, 700, '#024691'), t(246, y, b, 11, 700, '#10224A', 'end')]
        y += 26
    g_ += ['<rect x="14" y="134" width="232" height="44" rx="10" fill="#fef2f2"/>', t(26, 152, 'Controlled medicine on bill', 10.5, 700, '#b42318'), t(26, 168, 'Tick prescription checked to save', 10, 500, '#b42318')]
    return ''.join(g_)


def ui_alerts_ph():
    g_ = ['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>']
    y = 14
    for a, b, bg, fg in [('Expiring in 30 days', '9 batches', '#fef2f2', '#b42318'), ('Low stock', '14 items', '#fffbeb', '#92400e'), ('Out of stock', '3 items', '#eef1f6', '#475569'), ('Demand list ready', '17 items', '#ecfdf3', '#15803d')]:
        g_ += [f'<rect x="14" y="{y}" width="232" height="38" rx="10" fill="{bg}"/>', t(26, y + 24, a, 11, 700, fg), t(234, y + 24, b, 11.5, 800, fg, 'end')]
        y += 44
    return ''.join(g_)


def ui_report_ph():
    g_ = ['<rect width="260" height="190" rx="16" fill="url(#gBlue)"/>', t(14, 28, "Today's sales", 11, 500, '#cfe0ff'), t(14, 56, 'Rs 86,400', 22, 800, '#fff'),
          t(14, 76, 'Profit Rs 14,250  ·  211 bills', 10, 500, '#cfe0ff'), '<rect x="14" y="88" width="232" height="90" rx="12" fill="#fff"/>']
    for i, h in enumerate([34, 46, 40, 58, 50, 66, 54]):
        g_.append(f'<rect x="{30+i*31}" y="{168-h}" width="18" height="{h}" rx="4" fill="url(#gBar)"/>')
    return ''.join(g_)


def scene_pharm_process():
    y1, y2 = 120, 520
    return ''.join([
        pcard(60, y1, 1, 'Pick medicines', ui_pick(), 'Tick from 17,000+ in the catalog'),
        pcard(450, y1, 2, 'Receive stock', ui_grn_ph(), 'Batch, expiry, packing and rack'),
        pcard(840, y1, 3, 'Sell fast', ui_sell_ph(), 'Box, strip or tablet, Rx check'),
        pcard(645, y2, 4, 'Get alerts', ui_alerts_ph(), 'Expiry, low stock, demand list'),
        pcard(255, y2, 5, 'See profit', ui_report_ph(), 'Sales, profit and payables'),
        arrow('M368,280 L436,280', 'M424,268 L438,280 L424,292'),
        arrow('M758,280 L826,280', 'M814,268 L828,280 L814,292'),
        arrow('M990,446 C990,500 960,560 952,600', 'M942,588 L951,604 L965,592'),
        arrow('M640,680 L566,680', 'M578,668 L564,680 L578,692'),
    ])


def fridge():
    return ''.join([shadow(80, 250, 90, 14), '<rect x="0" y="0" width="160" height="240" rx="16" fill="url(#gWhiteBody)" stroke="#cfd6e2"/>',
                    '<rect x="12" y="14" width="136" height="150" rx="10" fill="#e8f2ff" stroke="#bfd6f5"/>',
                    '<rect x="22" y="40" width="116" height="6" rx="3" fill="#bfd6f5"/><rect x="22" y="90" width="116" height="6" rx="3" fill="#bfd6f5"/>',
                    '<rect x="30" y="56" width="20" height="30" rx="5" fill="#2FA9B0"/><rect x="58" y="60" width="16" height="26" rx="5" fill="#2F7BD9"/><rect x="82" y="56" width="20" height="30" rx="5" fill="#2FA9B0"/>',
                    '<rect x="30" y="106" width="30" height="20" rx="5" fill="#F59E0B"/><rect x="70" y="106" width="30" height="20" rx="5" fill="#2FA455"/>',
                    t(80, 196, '2-8 °C', 18, 800, '#024691', 'middle'), t(80, 218, 'cold chain', 11, 600, '#64748b', 'middle')])


def scene_pharm_hardware():
    body = ['<circle cx="600" cy="300" r="232" fill="#dcebff" opacity=".75"/>',
            '<circle cx="600" cy="300" r="232" fill="none" stroke="#bfd6f5" stroke-width="2" stroke-dasharray="6 9"/>',
            g(printer_ph(), 372, 300, .34), g(monitor_pharmacy(), 446, 150, .4),
            g(scanner_small(), 740, 352, .3, -22, 180, 180), g(phone_expiry(), 770, 196, .26)]
    xs = [150, 375, 600, 825, 1050]
    body.append('<path d="M600,532 L600,580" stroke="#2F7BD9" stroke-width="3" fill="none"/>')
    body.append(f'<path d="M{xs[0]},630 L{xs[0]},600 Q{xs[0]},580 {xs[0]+20},580 L{xs[-1]-20},580 Q{xs[-1]},580 {xs[-1]},600 L{xs[-1]},630" stroke="#2F7BD9" stroke-width="3" fill="none"/>')
    for x in xs[1:-1]:
        body.append(f'<path d="M{x},580 L{x},630" stroke="#2F7BD9" stroke-width="3" fill="none"/>')
    cy, r = 712, 82
    inners = [g(monitor_pharmacy(), xs[0] - 59, cy - 46, .15, flt=False),
              g(scanner_small(), xs[1] - 45, cy - 48, .26, -22, 180, 180, flt=False),
              g(printer_ph(), xs[2] - 51, cy - 54, .22, flt=False),
              g(phone_expiry(), xs[3] - 26, cy - 53, .17, flt=False),
              g(fridge(), xs[4] - 40, cy - 60, .5, flt=False)]
    for x, inner, lab in zip(xs, inners, ['Windows PC', 'Barcode scanner', 'Receipt printer', 'Owner phone', 'Fridge items']):
        body.append(circle_badge(x, cy, r, inner, lab))
    return ''.join(body)


SCENES = {
    'uptrendpos-fbr-pos-invoice-qr': ('FBR Receipt, Explained', 'green', scene_fbr_receipt, []),
    'uptrendpos-fbr-pos-integration-steps': ('FBR Setup in 5 Steps', 'blue', scene_fbr_steps, [(60, 470, 'We help on WhatsApp', '#2FA455')]),
    'uptrendpos-pharmacy-pos-software': ('Medical Store Counter', 'teal',
        lambda: g(monitor_pharmacy(), 40, 140, .9) + g(printer_ph(), 830, 548, .5) + g(scanner_small(), 660, 660, .4, -24, 180, 180) + g(phone_expiry(), 905, 112, .66),
        [(60, 780, 'Batch and expiry', '#2FA9B0'), (290, 780, 'Rx and controlled checks', '#ef4444')]),
    'uptrendpos-pharmacy-medicine-catalog': ('17,000+ Medicines Ready', 'green', lambda: g(tablet_catalog(), 210, 150, 1.0),
        [(60, 770, 'Search and tick', '#2FA455'), (300, 770, 'No typing needed', '#2F7BD9')]),
    'uptrendpos-pharmacy-salt-search-expiry': ('Salt Search + Expiry', 'blue', lambda: g(phone_salt(), 230, 140, 1.0) + g(phone_expiry(), 680, 140, 1.0),
        [(60, 780, 'Every brand of a salt', '#2F7BD9'), (360, 780, 'Batch-wise expiry', '#ef4444')]),
    'uptrendpos-pharmacy-pos-hardware': ('Pharmacy POS Hardware', 'teal', scene_pharm_hardware, [(880, 110, 'Start with a phone', '#2FA455')]),
    'uptrendpos-pharmacy-pos-process': ('Pharmacy Day, Step by Step', 'green', scene_pharm_process, [(60, 470, 'All connected', '#2FA455')]),
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
