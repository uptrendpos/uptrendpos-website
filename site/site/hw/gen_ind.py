"""UpTrendPos industry-page images (hub + grocery). Same house style as hardware_images_generator.py:
SVG device scenes -> PNG (Playwright) -> WebP, with the soft watermark (diagonal text ~3%, centre logo ~4.5%, corner logo).
Run: python3 gen_ind.py [name ...]"""
import base64, random, pathlib, asyncio, sys
from playwright.async_api import async_playwright
from PIL import Image

B = pathlib.Path('/home/claude/site/hw')
OUT = B / 'img'; OUT.mkdir(parents=True, exist_ok=True)
LOGO_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 240" width="1200" height="240">
<defs><linearGradient id="lg" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#0B8450"/><stop offset="1" stop-color="#48B65E"/></linearGradient>
<linearGradient id="lp" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#022F75"/><stop offset="1" stop-color="#0262B4"/></linearGradient></defs>
<rect x="4" y="13" width="726" height="212" rx="22" fill="url(#lg)"/>
<text x="367" y="172" font-family="Poppins" font-size="150" font-weight="700" fill="#F2F2F2" text-anchor="middle">UpTrend</text>
<text x="980" y="186" font-family="Poppins" font-size="190" font-weight="800" fill="url(#lp)" text-anchor="middle">POS</text>
<rect x="762" y="204" width="112" height="21" rx="10.5" fill="#0884F6"/><rect x="923" y="204" width="112" height="21" rx="10.5" fill="#FAE814"/><rect x="1083" y="204" width="113" height="21" rx="10.5" fill="#47C683"/></svg>'''
LOGO = base64.b64encode(pathlib.Path('/home/claude/site/src/logo.svg').read_bytes()).decode()  # official logo (project doc claude/brand/UpTrendPOS-Logo-Horizontal-Color.svg)
F = 'font-family="Poppins,sans-serif"'


def t(x, y, s, size=12, w=400, fill='#0f172a', anchor='start', extra=''):
    return f'<text x="{x}" y="{y}" {F} font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}" {extra}>{s}</text>'


DEFS = '''
<linearGradient id="gDark" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#323b4b"/><stop offset="1" stop-color="#141922"/></linearGradient>
<linearGradient id="gLid" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4b5567"/><stop offset="1" stop-color="#2a313d"/></linearGradient>
<linearGradient id="gBlue" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2F7BD9"/><stop offset="1" stop-color="#024691"/></linearGradient>
<linearGradient id="gNavy" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#10224A"/><stop offset="1" stop-color="#024691"/></linearGradient>
<linearGradient id="gGreen" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3fbf6a"/><stop offset="1" stop-color="#1E8A43"/></linearGradient>
<linearGradient id="gSilver" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#9aa4b4"/><stop offset=".5" stop-color="#e3e8ef"/><stop offset="1" stop-color="#8b95a6"/></linearGradient>
<linearGradient id="gWhiteBody" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#dfe4ec"/></linearGradient>
<linearGradient id="gGlass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".16"/><stop offset=".45" stop-color="#fff" stop-opacity="0"/></linearGradient>
<linearGradient id="gBar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2FA9B0"/><stop offset="1" stop-color="#024691"/></linearGradient>
<radialGradient id="gShadow"><stop offset="0" stop-color="#0b1a3a" stop-opacity=".30"/><stop offset="1" stop-color="#0b1a3a" stop-opacity="0"/></radialGradient>
<filter id="fDrop" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="18" stdDeviation="18" flood-color="#0b1a3a" flood-opacity=".22"/></filter>
<filter id="fSoft" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#0b1a3a" flood-opacity=".14"/></filter>
<filter id="fGlow"><feGaussianBlur stdDeviation="3"/></filter>
<pattern id="wm" width="380" height="190" patternUnits="userSpaceOnUse" patternTransform="rotate(-24)">
  <text x="10" y="70" font-family="Poppins,sans-serif" font-size="30" font-weight="800" fill="#10224A" fill-opacity=".03">UpTrendPos</text>
  <text x="200" y="165" font-family="Poppins,sans-serif" font-size="30" font-weight="800" fill="#10224A" fill-opacity=".03">UpTrendPos</text>
</pattern>
'''


def shadow(cx, cy, rx, ry):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="url(#gShadow)"/>'


def qr(x, y, s, seed=7):
    r = random.Random(seed); n = 11; c = s / n; out = [f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="#fff"/>']
    for i in range(n):
        for j in range(n):
            corner = (i < 3 and j < 3) or (i < 3 and j > 7) or (i > 7 and j < 3)
            on = (not (i == 1 and j in (1, 9)) and not (i == 9 and j == 1)) if corner else r.random() > .52
            if on:
                out.append(f'<rect x="{x+j*c:.1f}" y="{y+i*c:.1f}" width="{c+.2:.1f}" height="{c+.2:.1f}" fill="#111"/>')
    return ''.join(out)


def receipt(x, y, w, h, shop='CITY KIRYANA STORE', rows=None, total='Rs 4,200', clip=None, sub='Main Bazar, Sahiwal'):
    rows = rows or [('Chakki Atta 10 kg', '1,200'), ('Sugar 2.5 kg', '400'), ('Cooking Oil 1 L x2', '1,180')]
    cx = x + w / 2; s = w / 250
    g = [f'<g {"clip-path=" + chr(34) + clip + chr(34) if clip else ""}>',
         f'<path d="M{x},{y+14} Q{cx},{y-6} {x+w},{y+14} L{x+w},{y+h} L{x},{y+h} Z" fill="#fff" stroke="#e3e7ee"/>',
         t(cx, y + 38*s, shop, 13.5*s, 700, '#111', 'middle'),
         t(cx, y + 53*s, sub, 8.5*s, 400, '#666', 'middle'),
         f'<line x1="{x+16}" y1="{y+63*s}" x2="{x+w-16}" y2="{y+63*s}" stroke="#999" stroke-dasharray="4 3"/>']
    yy = y + 81*s
    for a, b in rows:
        g += [t(x + 18, yy, a, 10*s, 500, '#222'), t(x + w - 18, yy, b, 10*s, 500, '#222', 'end')]; yy += 16*s
    g += [f'<line x1="{x+16}" y1="{yy-6*s}" x2="{x+w-16}" y2="{yy-6*s}" stroke="#999" stroke-dasharray="4 3"/>',
          t(x + 18, yy + 12*s, 'TOTAL', 12.5*s, 700, '#111'), t(x + w - 18, yy + 12*s, total, 12.5*s, 700, '#111', 'end'),
          qr(cx - 15*s, yy + 22*s, 30*s),
          t(cx, yy + 66*s, 'Thank you! Come again', 7.5*s, 500, '#555', 'middle'), '</g>']
    return ''.join(g)


# ---------------------------------------------------------------- devices
def monitor_grocery():
    W, H = 780, 486
    g = [f'<rect x="352" y="{H-8}" width="76" height="118" fill="url(#gSilver)"/>',
         f'<rect x="250" y="{H+104}" width="280" height="22" rx="11" fill="url(#gSilver)"/>',
         f'<rect x="0" y="0" width="{W}" height="{H}" rx="20" fill="#0f172a"/>',
         '<circle cx="390" cy="468" r="3" fill="#3b82f6"/>',
         '<rect x="16" y="16" width="748" height="420" rx="6" fill="#f3f6fb"/>',
         '<clipPath id="cpMonG"><rect x="16" y="16" width="748" height="420" rx="6"/></clipPath><g clip-path="url(#cpMonG)">',
         '<rect x="16" y="16" width="748" height="46" fill="url(#gNavy)"/>',
         t(34, 45, 'UpTrendPos', 15, 700, '#fff'), t(150, 45, 'New Sale  ·  Counter 1', 12, 500, '#c9dbf2'),
         '<rect x="640" y="27" width="108" height="24" rx="12" fill="#2FA455"/>', t(694, 43, 'Online', 11, 700, '#fff', 'middle'),
         '<rect x="32" y="76" width="470" height="34" rx="10" fill="#fff" stroke="#dfe6f1"/>', t(48, 98, 'Scan barcode or type item name', 11.5, 500, '#94a3b8'),
         '<rect x="32" y="122" width="470" height="30" fill="#e9effa"/>']
    for x, c, a in [(46, 'Item', 'start'), (268, 'Unit', 'start'), (374, 'Qty', 'start'), (488, 'Amount', 'end')]:
        g.append(t(x, 142, c, 11, 700, '#10224A', a))
    rows = [('Chakki Atta 10 kg', 'Bag', '1', '1,200'), ('Sugar (loose)', 'Kg', '2.5', '400'), ('Daal Chana', 'Kg', '1', '280'),
            ('Cooking Oil 1 L', 'Pouch', '2', '1,180'), ('Biscuits', 'Carton (24)', '1', '600'), ('Biscuits', 'Piece', '3', '90'),
            ('Chai Patti 190 g', 'Pack', '1', '450')]
    y = 172
    for i, (n, u, q, a) in enumerate(rows):
        if i % 2:
            g.append(f'<rect x="32" y="{y-19}" width="470" height="32" fill="#f7f9fd"/>')
        tag = f'<rect x="262" y="{y-14}" width="{len(u)*6.4+14:.0f}" height="20" rx="10" fill="{"#fff4a3" if u in ("Kg",) else "#eaf1ff"}"/>'
        g += [t(46, y, n, 11.5, 500, '#1e293b'), tag, t(269, y, u, 10.5, 600, '#10224A'), t(374, y, q, 11.5, 500, '#1e293b'), t(488, y, a, 11.5, 600, '#10224A', 'end')]
        y += 32
    g += ['<rect x="520" y="76" width="228" height="344" rx="14" fill="#fff" stroke="#e1e7f0"/>',
          t(538, 104, 'Customer', 11, 600, '#64748b'), t(538, 124, 'Rashid Ahmed', 14, 700, '#10224A'),
          '<rect x="538" y="134" width="194" height="26" rx="8" fill="#fff7ed"/>', t(548, 152, 'Khata balance  Rs 3,450', 11, 600, '#9a3412'),
          '<rect x="538" y="170" width="94" height="30" rx="10" fill="#fff" stroke="#c7d7ff"/>', t(585, 190, 'Cash', 12, 600, '#024691', 'middle'),
          '<rect x="638" y="170" width="94" height="30" rx="10" fill="#024691"/>', t(685, 190, 'Udhaar', 12, 700, '#fff', 'middle'),
          t(538, 226, 'Items', 11.5, 500, '#64748b'), t(732, 226, '7', 11.5, 600, '#10224A', 'end'),
          t(538, 248, 'Discount', 11.5, 500, '#64748b'), t(732, 248, 'Rs 0', 11.5, 600, '#10224A', 'end'),
          '<rect x="532" y="262" width="204" height="56" rx="14" fill="#eaf1ff"/>', t(546, 284, 'Total', 12, 600, '#475569'), t(724, 306, 'Rs 4,200', 22, 800, '#024691', 'end'),
          '<rect x="532" y="328" width="98" height="38" rx="12" fill="#fff" stroke="#c7d7ff"/>', t(581, 352, 'PDF', 12, 700, '#024691', 'middle'),
          '<rect x="638" y="328" width="98" height="38" rx="12" fill="#1E8A43"/>', t(687, 352, 'WhatsApp', 11.5, 700, '#fff', 'middle'),
          '<rect x="532" y="374" width="204" height="38" rx="12" fill="#FAE814"/>', t(634, 398, 'Save &amp; Print', 13, 800, '#10224A', 'middle'),
          '</g>', '<rect x="16" y="16" width="748" height="420" rx="6" fill="url(#gGlass)"/>']
    return ''.join(g)


def monitor_picker():
    """Monitor with the 'choose your business type' step."""
    W, H = 780, 486
    g = [f'<rect x="352" y="{H-8}" width="76" height="118" fill="url(#gSilver)"/>',
         f'<rect x="250" y="{H+104}" width="280" height="22" rx="11" fill="url(#gSilver)"/>',
         f'<rect x="0" y="0" width="{W}" height="{H}" rx="20" fill="#0f172a"/>',
         '<circle cx="390" cy="468" r="3" fill="#3b82f6"/>',
         '<rect x="16" y="16" width="748" height="420" rx="6" fill="#f3f6fb"/>',
         '<clipPath id="cpMonP"><rect x="16" y="16" width="748" height="420" rx="6"/></clipPath><g clip-path="url(#cpMonP)">',
         '<rect x="16" y="16" width="748" height="46" fill="url(#gNavy)"/>',
         t(34, 45, 'UpTrendPos', 15, 700, '#fff'), t(150, 45, 'Create your shop  ·  Step 2 of 3', 12, 500, '#c9dbf2'),
         t(40, 96, 'What do you sell?', 20, 800, '#10224A'), t(40, 118, 'Pick your business type. Your shop opens ready for it.', 11.5, 500, '#64748b'),
         '<rect x="520" y="80" width="226" height="34" rx="10" fill="#fff" stroke="#dfe6f1"/>', t(536, 102, 'Search 30+ business types', 11, 500, '#94a3b8')]
    types = [('Grocery &amp; Kiryana', '#2FA455'), ('Pharmacy', '#2FA9B0'), ('Clothing', '#2F7BD9'), ('Shoes', '#F59E0B'),
             ('Mobile &amp; Computer', '#10224A'), ('Electronics &amp; CCTV', '#024691'), ('Solar Shop', '#eab308'), ('Hardware', '#a16207'),
             ('Tailoring', '#db2777'), ('Cosmetics', '#e11d48'), ('Jewellery', '#ca8a04'), ('Auto Parts', '#475569')]
    for i, (n, col) in enumerate(types):
        r_, c_ = divmod(i, 4); x = 40 + c_ * 178; y = 136 + r_ * 92
        sel = i == 0
        g += [f'<rect x="{x}" y="{y}" width="166" height="80" rx="14" fill="{"#eefaf2" if sel else "#fff"}" stroke="{"#2FA455" if sel else "#e3e9f2"}" stroke-width="{2.5 if sel else 1}"/>',
              f'<rect x="{x+14}" y="{y+14}" width="34" height="34" rx="10" fill="{col}" opacity=".16"/><circle cx="{x+31}" cy="{y+31}" r="9" fill="{col}"/>',
              t(x + 14, y + 66, n, 11.5, 600, '#10224A')]
        if sel:
            g += [f'<circle cx="{x+146}" cy="{y+20}" r="10" fill="#2FA455"/>',
                  f'<path d="M{x+141},{y+20} l4,4 7,-8" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>']
    g += ['<rect x="588" y="392" width="160" height="34" rx="12" fill="#FAE814"/>', t(668, 414, 'Continue', 13, 800, '#10224A', 'middle'),
          '</g>', '<rect x="16" y="16" width="748" height="420" rx="6" fill="url(#gGlass)"/>']
    return ''.join(g)


def phone_shell(inner, clip_id, bg='#f3f6fb'):
    w, h = 300, 612
    return ''.join([shadow(150, 618, 170, 22),
                    f'<rect x="0" y="0" width="{w}" height="{h}" rx="44" fill="#0f172a"/>',
                    f'<rect x="3" y="3" width="{w-6}" height="{h-6}" rx="42" fill="none" stroke="#3b465a" stroke-width="2"/>',
                    '<rect x="-3" y="140" width="4" height="56" rx="2" fill="#1f2937"/><rect x="299" y="120" width="4" height="40" rx="2" fill="#1f2937"/>',
                    f'<rect x="14" y="14" width="272" height="584" rx="32" fill="{bg}"/>',
                    f'<clipPath id="{clip_id}"><rect x="14" y="14" width="272" height="584" rx="32"/></clipPath><g clip-path="url(#{clip_id})">',
                    inner, '</g>', '<rect x="14" y="14" width="272" height="584" rx="32" fill="url(#gGlass)"/>'])


def status_bar(dark=False):
    c = '#10224A' if dark else '#fff'
    return (t(36, 40, '9:41', 11, 600, c) + '<circle cx="150" cy="34" r="7" fill="#0b1222"/>'
            + f'<rect x="236" y="31" width="22" height="10" rx="3" fill="none" stroke="{c}" stroke-width="1.4"/><rect x="238" y="33" width="15" height="6" rx="1.5" fill="{c}"/>')


def phone_ready_setup():
    g = ['<rect x="14" y="14" width="272" height="150" fill="url(#gGreen)"/>', status_bar(),
         t(32, 84, 'Your shop is ready', 18, 700, '#fff'), t(32, 106, 'Grocery &amp; Kiryana setup', 11.5, 500, '#dff7e8'),
         '<rect x="32" y="122" width="132" height="26" rx="13" fill="#fff" fill-opacity=".2"/>', t(98, 140, 'City Kiryana Store', 10.5, 600, '#fff', 'middle')]
    items = [('Units turned on', 'Carton, pack, piece, kg'), ('Expiry alerts', 'On for food items'), ('Udhaar khata', 'Ready for customers'),
             ('Barcode billing', 'Scan and sell'), ('Daily reports', 'Sales, profit, stock'), ('Bills on WhatsApp', 'Picture or PDF')]
    y = 180
    for a, b in items:
        g += [f'<rect x="26" y="{y}" width="248" height="54" rx="14" fill="#fff" stroke="#e6ebf3"/>',
              f'<circle cx="52" cy="{y+27}" r="12" fill="#2FA455"/>',
              f'<path d="M46,{y+27} l4,4 8,-9" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>',
              t(74, y + 23, a, 12, 700, '#10224A'), t(74, y + 41, b, 10.5, 500, '#64748b')]
        y += 62
    g += [f'<rect x="26" y="{y+6}" width="248" height="44" rx="14" fill="#FAE814"/>', t(150, y + 34, 'Start billing', 14, 800, '#10224A', 'middle')]
    return phone_shell(''.join(g), 'cpReady')


def phone_billing_printer():
    g = ['<rect x="14" y="14" width="272" height="112" fill="url(#gBlue)"/>', status_bar(),
         t(32, 86, 'New Sale', 20, 700, '#fff'), t(32, 108, 'Counter 1  ·  Cash', 11, 500, '#cfe0ff'),
         '<rect x="196" y="70" width="76" height="26" rx="13" fill="#FAE814"/>', t(234, 88, 'Bill #208', 10.5, 700, '#10224A', 'middle')]
    items = [('Chakki Atta 10 kg', '1 bag', 'Rs 1,200', '#a16207'), ('Sugar', '2.5 kg', 'Rs 400', '#2FA455'),
             ('Cooking Oil 1 L', '2 pouch', 'Rs 1,180', '#F59E0B'), ('Chai Patti 190 g', '1 pack', 'Rs 450', '#2FA9B0')]
    y = 140
    for n, sub, amt, col in items:
        g += [f'<rect x="28" y="{y}" width="244" height="52" rx="14" fill="#fff" stroke="#e6ebf3"/>',
              f'<rect x="38" y="{y+9}" width="34" height="34" rx="10" fill="{col}" opacity=".18"/><rect x="48" y="{y+19}" width="14" height="14" rx="4" fill="{col}"/>',
              t(82, y + 23, n, 12, 600, '#10224A'), t(82, y + 40, sub, 10.5, 500, '#64748b'), t(262, y + 31, amt, 12, 700, '#10224A', 'end')]
        y += 60
    g += [f'<rect x="28" y="{y+2}" width="244" height="54" rx="14" fill="#eaf1ff"/>',
          t(42, y + 26, 'Total', 12, 600, '#475569'), t(42, y + 45, '4 items', 10, 500, '#64748b'), t(258, y + 40, 'Rs 3,230', 22, 800, '#024691', 'end')]
    y += 68
    g += [f'<rect x="28" y="{y}" width="244" height="34" rx="12" fill="#ecfdf3"/>',
          f'<circle cx="46" cy="{y+17}" r="5" fill="#22c55e"/>', t(58, y + 22, 'Printer connected · USB Type-C', 10.5, 600, '#15803d'),
          f'<rect x="28" y="{y+44}" width="244" height="50" rx="14" fill="#FAE814"/>', t(150, y + 75, 'Print receipt', 15, 800, '#10224A', 'middle')]
    return phone_shell(''.join(g), 'cpBill')


def mini_printer_usb():
    """Compact thermal receipt printer, USB port on the left side. Local ~300x330."""
    return ''.join([
        shadow(150, 330, 160, 20),
        '<clipPath id="cpMiniU"><rect x="0" y="-60" width="300" height="186"/></clipPath>',
        receipt(62, -40, 176, 200, rows=[('Atta 10 kg', '1,200'), ('Sugar 2.5 kg', '400'), ('Oil 1 L x2', '1,180'), ('Chai 190 g', '450')],
                total='Rs 3,230', clip='url(#cpMiniU)'),
        '<rect x="20" y="120" width="260" height="200" rx="40" fill="url(#gWhiteBody)" stroke="#cfd6e2"/>',
        '<rect x="20" y="120" width="260" height="62" rx="34" fill="#2a313d"/>',
        '<rect x="48" y="122" width="204" height="9" rx="4.5" fill="#0b0e13"/>',
        '<rect x="52" y="204" width="196" height="76" rx="18" fill="#eef2f7" stroke="#d6dde8"/>',
        '<circle cx="96" cy="242" r="13" fill="#fff" stroke="#c6cfdc"/><circle cx="146" cy="242" r="5" fill="#22c55e"/><circle cx="146" cy="242" r="9" fill="#22c55e" opacity=".35" filter="url(#fGlow)"/>',
        '<circle cx="176" cy="242" r="5" fill="#2F7BD9"/>',
        '<rect x="8" y="232" width="16" height="22" rx="4" fill="#1f2633"/>',
    ])


def usb_c_cable(x1, y1, x2, y2):
    """Cable from phone bottom (x1,y1) to printer side port (x2,y2) with Type-C plugs."""
    path = f'M{x1},{y1+26} C{x1},{y1+140} {x2-160},{y2} {x2-26},{y2}'
    return ''.join([
        f'<path d="{path}" fill="none" stroke="#1f2633" stroke-width="9" stroke-linecap="round"/>',
        f'<path d="{path}" fill="none" stroke="#4b5567" stroke-width="2.5" stroke-linecap="round" opacity=".6"/>',
        f'<rect x="{x1-11}" y="{y1}" width="22" height="34" rx="6" fill="#2a313d"/><rect x="{x1-6}" y="{y1-8}" width="12" height="10" rx="3" fill="url(#gSilver)"/>',
        f'<rect x="{x2-34}" y="{y2-11}" width="34" height="22" rx="6" fill="#2a313d"/><rect x="{x2-2}" y="{y2-6}" width="10" height="12" rx="3" fill="url(#gSilver)"/>',
    ])


def phone_share():
    g = ['<rect x="14" y="14" width="272" height="250" fill="url(#gGreen)"/>', status_bar(),
         '<circle cx="150" cy="104" r="34" fill="#fff" fill-opacity=".22"/><circle cx="150" cy="104" r="24" fill="#fff"/>',
         '<path d="M139,104 l8,8 15,-16" fill="none" stroke="#1E8A43" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>',
         t(150, 168, 'Sale saved', 20, 800, '#fff', 'middle'), t(150, 192, 'Bill #208  ·  Rs 3,230', 12, 500, '#dff7e8', 'middle'),
         t(150, 226, 'No printer here? Send the bill instead.', 10.5, 500, '#dff7e8', 'middle')]
    y = 286
    for lab, sub, fill, txt, stroke in [('Send on WhatsApp', 'Bill as a picture', '#1E8A43', '#fff', None),
                                        ('Share as PDF', 'For bigger bills', '#fff', '#024691', '#c7d7ff'),
                                        ('Print receipt', 'When a printer is connected', '#fff', '#10224A', '#e3e9f2')]:
        st = f' stroke="{stroke}"' if stroke else ''
        g += [f'<rect x="28" y="{y}" width="244" height="62" rx="16" fill="{fill}"{st}/>',
              t(48, y + 28, lab, 13.5, 700, txt), t(48, y + 47, sub, 10.5, 500, '#dff7e8' if fill == '#1E8A43' else '#64748b')]
        y += 74
    g += [f'<rect x="28" y="{y+6}" width="244" height="72" rx="16" fill="#eaf1ff"/>',
          t(44, y + 32, "Today's report", 12, 700, '#10224A'), t(44, y + 52, 'Sales, cash and udhaar', 10.5, 500, '#64748b'),
          f'<rect x="196" y="{y+24}" width="62" height="34" rx="12" fill="#024691"/>', t(227, y + 46, 'Send', 11.5, 700, '#fff', 'middle')]
    return phone_shell(''.join(g), 'cpShare')


def phone_chat_received():
    g = ['<rect x="14" y="14" width="272" height="104" fill="#1E8A43"/>', status_bar(),
         '<circle cx="50" cy="82" r="20" fill="#fff"/>', t(50, 88, 'RA', 12, 800, '#1E8A43', 'middle'),
         t(80, 80, 'Rashid Ahmed', 15, 700, '#fff'), t(80, 98, 'customer', 11, 500, '#d1f2dc')]
    # image bubble with mini receipt
    g += ['<rect x="112" y="136" width="160" height="214" rx="14" fill="#d9fdd3" filter="url(#fSoft)"/>',
          '<rect x="120" y="144" width="144" height="178" rx="8" fill="#fff"/>',
          receipt(126, 150, 132, 168, rows=[('Atta 10 kg', '1,200'), ('Sugar 2.5 kg', '400'), ('Oil 1 L x2', '1,180')], total='Rs 3,230'),
          t(260, 340, '6:42 pm', 8.5, 500, '#64748b', 'end')]
    # pdf bubble
    g += ['<rect x="96" y="364" width="176" height="64" rx="14" fill="#d9fdd3" filter="url(#fSoft)"/>',
          '<rect x="106" y="374" width="30" height="36" rx="5" fill="#ef4444"/>', t(121, 397, 'PDF', 9, 800, '#fff', 'middle'),
          t(144, 390, 'Khata statement', 11, 700, '#1e293b'), t(144, 406, 'Balance Rs 6,680', 9.5, 500, '#475569'), t(262, 422, '6:42 pm', 8.5, 500, '#64748b', 'end')]
    # reply
    g += ['<rect x="28" y="444" width="178" height="58" rx="14" fill="#fff" filter="url(#fSoft)"/>',
          t(42, 468, 'Shukriya, mil gaya!', 11.5, 500, '#1e293b'), t(42, 486, 'Payment kal karta hoon.', 11.5, 500, '#1e293b'), t(198, 496, '6:44 pm', 8.5, 500, '#64748b', 'end')]
    g += ['<rect x="14" y="540" width="272" height="58" fill="#f6f6f6"/>',
          '<rect x="26" y="551" width="200" height="36" rx="18" fill="#fff"/>', t(42, 574, 'Type a message', 11.5, 500, '#94a3b8'),
          '<circle cx="254" cy="569" r="18" fill="#1E8A43"/><path d="M247,569 l14,-7 -4,7 4,7 z" fill="#fff"/>']
    return phone_shell(''.join(g), 'cpChatR', bg='#efeae2')


def phone_reports():
    g = ['<rect x="14" y="14" width="272" height="156" fill="url(#gBlue)"/>', status_bar(),
         t(32, 80, "Today's sales", 12, 500, '#cfe0ff'), t(32, 114, 'Rs 48,250', 28, 800, '#fff'),
         t(32, 140, 'Profit Rs 6,120  ·  132 bills', 11, 500, '#cfe0ff')]
    # bars
    g += ['<rect x="26" y="184" width="248" height="104" rx="16" fill="#fff" stroke="#e6ebf3"/>', t(42, 206, 'This week', 11, 700, '#10224A')]
    for i, hgt in enumerate([38, 52, 44, 66, 58, 74, 62]):
        x = 46 + i * 31
        g.append(f'<rect x="{x}" y="{276-hgt}" width="18" height="{hgt}" rx="5" fill="url(#gBar)"/>')
    rows = [('Udhaar to collect', 'Rs 86,450', '#fff7ed', '#9a3412'), ('Low stock', '6 items', '#fffbeb', '#92400e'),
            ('Expiring soon', '4 items', '#fef2f2', '#b42318'), ('Cash in drawer', 'Rs 31,900', '#ecfdf3', '#15803d')]
    y = 300
    for a, b, bg, fg in rows:
        g += [f'<rect x="26" y="{y}" width="248" height="46" rx="14" fill="{bg}"/>', t(42, y + 28, a, 11.5, 600, fg), t(260, y + 28, b, 12, 800, fg, 'end')]
        y += 54
    g += [f'<rect x="26" y="{y+4}" width="248" height="44" rx="14" fill="#FAE814"/>', t(150, y + 32, 'Send report on WhatsApp', 12.5, 800, '#10224A', 'middle')]
    return phone_shell(''.join(g), 'cpRep')


def tablet_stock():
    W, H = 780, 500
    g = [shadow(390, 600, 380, 30),
         '<polygon points="430,300 490,300 590,590 548,596" fill="#2a313d"/>', '<rect x="530" y="588" width="70" height="10" rx="5" fill="#1b212b"/>',
         f'<rect x="0" y="0" width="{W}" height="{H}" rx="40" fill="#111827"/>',
         f'<rect x="3" y="3" width="{W-6}" height="{H-6}" rx="38" fill="none" stroke="#374151" stroke-width="2"/>',
         '<rect x="22" y="26" width="736" height="452" rx="16" fill="#f3f6fb"/>',
         '<clipPath id="cpTabS"><rect x="22" y="26" width="736" height="452" rx="16"/></clipPath><g clip-path="url(#cpTabS)">',
         '<rect x="22" y="26" width="736" height="52" fill="url(#gNavy)"/>', t(44, 58, 'Demand List', 16, 700, '#fff'), t(180, 58, 'Items to order this week', 12, 500, '#c9dbf2'),
         '<rect x="44" y="94" width="692" height="30" fill="#e9effa"/>']
    for x, c, a in [(58, 'Item', 'start'), (360, 'In stock', 'start'), (500, 'Alert at', 'start'), (722, 'Status', 'end')]:
        g.append(t(x, 114, c, 11, 700, '#10224A', a))
    rows = [('Chakki Atta 10 kg', '3 bags', '10 bags', 'Low'), ('Sugar', '12 kg', '50 kg', 'Low'),
            ('Cooking Oil 1 L', '8 pouch', '24 pouch', 'Low'), ('Chai Patti 190 g', '5 pack', '20 pack', 'Low'),
            ('Biscuits', '0 carton', '4 carton', 'Out'), ('Daal Chana', '6 kg', '20 kg', 'Low')]
    y = 150
    for i, (n, s_, a_, st) in enumerate(rows):
        if i % 2:
            g.append(f'<rect x="44" y="{y-20}" width="692" height="36" fill="#f7f9fd"/>')
        col = '#b42318' if st == 'Out' else '#92400e'; bgc = '#fef2f2' if st == 'Out' else '#fffbeb'
        g += [t(58, y, n, 12, 600, '#10224A'), t(360, y, s_, 12, 700, '#b42318'), t(500, y, a_, 12, 500, '#475569'),
              f'<rect x="670" y="{y-15}" width="54" height="22" rx="11" fill="{bgc}"/>', t(697, y, st, 10.5, 700, col, 'middle')]
        y += 36
    g += ['<rect x="44" y="384" width="692" height="72" rx="14" fill="#fff" stroke="#e1e7f0"/>',
          t(64, 414, '6 items are below their alert level', 13, 700, '#10224A'), t(64, 436, 'Order them before they run out on the shelf', 11, 500, '#64748b'),
          '</g>', '<rect x="22" y="26" width="736" height="452" rx="16" fill="url(#gGlass)"/>']
    return ''.join(g)


def printer80():
    return ''.join([
        shadow(230, 488, 250, 26),
        '<clipPath id="cpPaper"><rect x="0" y="-40" width="460" height="267"/></clipPath>',
        '<path d="M58,200 Q60,190 74,190 L386,190 Q400,190 402,200 L432,262 L28,262 Z" fill="url(#gLid)"/>',
        receipt(105, 6, 250, 240, clip='url(#cpPaper)'),
        '<rect x="96" y="222" width="268" height="8" rx="4" fill="#0b0e13"/>',
        '<rect x="28" y="262" width="404" height="214" rx="26" fill="url(#gDark)"/>',
        '<rect x="58" y="298" width="344" height="150" rx="16" fill="#202734" stroke="#323c4c"/>',
        '<circle cx="330" cy="330" r="6" fill="#22c55e"/><circle cx="306" cy="330" r="6" fill="#3b4556"/>',
        '<circle cx="370" cy="330" r="14" fill="#353f50" stroke="#4b5668"/>',
    ])


def scanner_small():
    return ''.join([
        '<path d="M34,22 Q34,0 64,0 L292,0 Q330,0 330,40 L330,86 Q330,114 300,120 L270,126 L292,322 Q295,350 266,352 L214,354 Q188,354 186,328 L170,140 L74,126 L44,124 Q32,124 30,104 Z" fill="url(#gDark)"/>',
        '<path d="M206,150 L268,140 L288,322 Q290,342 268,344 L222,346 Q206,346 204,330 Z" fill="url(#gGreen)" opacity=".95"/>',
        '<rect x="14" y="14" width="22" height="104" rx="8" fill="#7f1d1d"/><rect x="18" y="20" width="12" height="92" rx="6" fill="#ef4444" opacity=".85"/>',
        '<circle cx="250" cy="40" r="6" fill="#22c55e"/>',
    ])


def sacks():
    """Simple grocery props: atta bag + oil pouch + tea pack (generic, no brands)."""
    return ''.join([
        shadow(170, 250, 190, 18),
        '<path d="M20,60 Q20,30 40,24 L150,24 Q170,30 170,60 L176,238 Q176,250 160,250 L30,250 Q14,250 14,238 Z" fill="#f5ecd7" stroke="#e2d3ac"/>',
        '<path d="M40,24 Q95,6 150,24" fill="none" stroke="#d6c08a" stroke-width="4"/>',
        '<rect x="34" y="96" width="122" height="64" rx="10" fill="#1E8A43"/>', t(95, 124, 'CHAKKI ATTA', 13, 800, '#fff', 'middle'), t(95, 146, '10 KG', 15, 800, '#FAE814', 'middle'),
        '<path d="M196,110 L276,110 L284,246 L188,246 Z" fill="#fde68a" stroke="#eab308"/>', '<rect x="200" y="150" width="80" height="40" rx="8" fill="#fff"/>',
        t(240, 167, 'COOKING', 10, 800, '#a16207', 'middle'), t(240, 182, 'OIL 1 L', 10, 800, '#a16207', 'middle'),
        '<rect x="296" y="150" width="72" height="96" rx="8" fill="#b91c1c"/>', '<rect x="304" y="168" width="56" height="34" rx="6" fill="#fff"/>',
        t(332, 183, 'CHAI', 10, 800, '#b91c1c', 'middle'), t(332, 197, '190 g', 9, 700, '#b91c1c', 'middle'),
    ])


# ---------------------------------------------------------------- frame
def frame(body, label, chips, tint):
    bg = {'blue': ('#eef5ff', '#f7fbff', 'rgba(47,123,217,.20)', 'rgba(250,232,20,.22)'),
          'green': ('#ecf8f1', '#f8fcfa', 'rgba(47,164,85,.20)', 'rgba(47,123,217,.14)'),
          'yellow': ('#fffbe6', '#fbfcff', 'rgba(250,232,20,.32)', 'rgba(47,123,217,.14)'),
          'teal': ('#eaf7f8', '#f8fbff', 'rgba(47,169,176,.22)', 'rgba(250,232,20,.18)'),
          'navy': ('#edf2fb', '#fafcff', 'rgba(16,34,74,.14)', 'rgba(47,164,85,.16)')}[tint]
    chip_svg = []
    for (x, y, txt, dot) in chips:
        wch = 40 + len(txt.replace('&amp;', '&')) * 9.3
        chip_svg.append(f'<g filter="url(#fSoft)"><rect x="{x}" y="{y}" width="{wch:.0f}" height="40" rx="20" fill="#fff"/>'
                        f'<circle cx="{x+20}" cy="{y+20}" r="6" fill="{dot}"/>' + t(x + 34, y + 26, txt, 15, 600, '#10224A') + '</g>')
    lw = 52 + len(label.replace('&amp;', '&')) * 10.2
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="900" viewBox="0 0 1200 900">
<defs>{DEFS}
<radialGradient id="bgA" cx=".82" cy=".22" r=".6"><stop offset="0" stop-color="{bg[2]}"/><stop offset="1" stop-color="rgba(255,255,255,0)"/></radialGradient>
<radialGradient id="bgB" cx=".1" cy=".95" r=".55"><stop offset="0" stop-color="{bg[3]}"/><stop offset="1" stop-color="rgba(255,255,255,0)"/></radialGradient>
<linearGradient id="bgL" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{bg[0]}"/><stop offset="1" stop-color="{bg[1]}"/></linearGradient>
<pattern id="dots" width="28" height="28" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.4" fill="#10224A" fill-opacity=".07"/></pattern>
</defs>
<rect width="1200" height="900" fill="url(#bgL)"/><rect width="1200" height="900" fill="url(#bgA)"/><rect width="1200" height="900" fill="url(#bgB)"/>
<rect width="1200" height="900" fill="url(#dots)"/>
<circle cx="980" cy="160" r="230" fill="none" stroke="#2F7BD9" stroke-opacity=".10" stroke-width="2" stroke-dasharray="6 10"/>
{body}
{''.join(chip_svg)}
<g filter="url(#fSoft)"><rect x="40" y="38" width="{lw:.0f}" height="48" rx="24" fill="#10224A"/><circle cx="66" cy="62" r="8" fill="#FAE814"/>{t(84, 69, label, 17, 700, '#fff')}</g>
<rect width="1200" height="900" fill="url(#wm)"/>
<g opacity=".045" transform="translate(330 330) scale(.45)"><image href="data:image/svg+xml;base64,{LOGO}" width="1200" height="240"/></g>
<g opacity=".9"><rect x="968" y="842" width="200" height="40" rx="12" fill="#fff" fill-opacity=".85"/><image href="data:image/svg+xml;base64,{LOGO}" x="980" y="848" width="176" height="28"/></g>
</svg>'''


def g(svg, x, y, s=1, rot=0, cx=0, cy=0, flt=True):
    r = f' rotate({rot} {cx} {cy})' if rot else ''
    return f'<g transform="translate({x} {y}) scale({s}){r}"{" filter=" + chr(34) + "url(#fDrop)" + chr(34) if flt else ""}>{svg}</g>'


def scene_type_c():
    # phone left, printer right, cable from phone bottom to printer left port
    ph_x, ph_y, ph_s = 250, 120, 1.0
    pr_x, pr_y, pr_s = 700, 380, 1.15
    phone_bottom = (ph_x + 150 * ph_s, ph_y + 612 * ph_s)
    port = (pr_x + 8 * pr_s, pr_y + 243 * pr_s)
    tag = ('<g filter="url(#fSoft)"><rect x="470" y="770" width="200" height="40" rx="20" fill="#10224A"/>'
           + t(570, 796, 'USB Type-C cable', 14, 700, '#fff', 'middle') + '</g>')
    printed = ('<g filter="url(#fSoft)"><rect x="840" y="250" width="236" height="56" rx="18" fill="#fff"/>'
               '<circle cx="870" cy="278" r="15" fill="#2FA455"/><path d="M862,278 l6,6 11,-12" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
               + t(894, 274, 'Receipt printed', 14, 700, '#10224A') + t(894, 292, 'Straight from your phone', 11.5, 500, '#64748b') + '</g>')
    return (g(phone_billing_printer(), ph_x, ph_y, ph_s) + usb_c_cable(phone_bottom[0], phone_bottom[1] - 2, port[0], port[1])
            + g(mini_printer_usb(), pr_x, pr_y, pr_s) + tag + printed)


def scene_whatsapp():
    arrow = ('<path d="M585,430 C640,400 660,400 712,420" fill="none" stroke="#2FA455" stroke-width="5" stroke-linecap="round" stroke-dasharray="2 12"/>'
             '<path d="M702,404 l20,18 -26,8" fill="none" stroke="#2FA455" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>')
    return g(phone_share(), 250, 140, 1.0) + arrow + g(phone_chat_received(), 740, 120, 1.0)


def scene_grocery_hero():
    return (g(monitor_grocery(), 40, 140, .9) + g(printer80(), 830, 548, .5)
            + g(scanner_small(), 660, 660, .4, -24, 180, 180) + g(phone_reports(), 905, 112, .66))


def scene_hub():
    return g(monitor_picker(), 110, 150, .86) + g(phone_ready_setup(), 840, 170, .9)


def scene_reports():
    return g(tablet_stock(), 70, 250, .78) + g(phone_reports(), 790, 110, 1.0)



def circle_badge(cx, cy, r, inner, label):
    return (f'<g filter="url(#fSoft)"><circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff"/></g>'
            f'<circle cx="{cx}" cy="{cy}" r="{r-8}" fill="#e8f2ff" stroke="#bfd6f5" stroke-width="2"/>'
            + inner + t(cx, cy + r + 34, label, 17, 700, '#10224A', 'middle'))


def scene_hardware():
    body = ['<circle cx="600" cy="300" r="232" fill="#dcebff" opacity=".75"/>',
            '<circle cx="600" cy="300" r="232" fill="none" stroke="#bfd6f5" stroke-width="2" stroke-dasharray="6 9"/>',
            g(printer80(), 372, 300, .34), g(monitor_grocery(), 446, 150, .4),
            g(scanner_small(), 740, 352, .3, -22, 180, 180), g(phone_billing_printer(), 770, 196, .26)]
    xs = [150, 375, 600, 825, 1050]
    body.append('<path d="M600,532 L600,580" stroke="#2F7BD9" stroke-width="3" fill="none"/>')
    body.append(f'<path d="M{xs[0]},630 L{xs[0]},600 Q{xs[0]},580 {xs[0]+20},580 L{xs[-1]-20},580 Q{xs[-1]},580 {xs[-1]},600 L{xs[-1]},630" stroke="#2F7BD9" stroke-width="3" fill="none"/>')
    for x in xs[1:-1]:
        body.append(f'<path d="M{x},580 L{x},630" stroke="#2F7BD9" stroke-width="3" fill="none"/>')
    cy, r = 712, 82
    inners = [g(phone_billing_printer(), xs[0] - 26, cy - 53, .17, flt=False),
              g(mini_printer_usb(), xs[1] - 46, cy - 46, .3, flt=False),
              g(monitor_grocery(), xs[2] - 59, cy - 46, .15, flt=False),
              g(printer80(), xs[3] - 51, cy - 54, .22, flt=False),
              g(scanner_small(), xs[4] - 45, cy - 48, .26, -22, 180, 180, flt=False)]
    labels = ['Android phone', 'Type-C printer', 'Windows PC', '80mm printer', 'Barcode scanner']
    for x, inner, lab in zip(xs, inners, labels):
        body.append(circle_badge(x, cy, r, inner, lab))
    return ''.join(body)


def pcard(x, y, num, title, inner, foot):
    return ''.join([f'<g filter="url(#fDrop)"><rect x="{x}" y="{y}" width="300" height="320" rx="26" fill="#fff"/></g>',
                    f'<circle cx="{x+36}" cy="{y+38}" r="18" fill="#FAE814"/>', t(x + 36, y + 45, str(num), 17, 800, '#10224A', 'middle'),
                    t(x + 66, y + 45, title, 18, 700, '#10224A'),
                    f'<g transform="translate({x+20} {y+74})">{inner}</g>',
                    t(x + 150, y + 300, foot, 12.5, 600, '#64748b', 'middle')])


def ui_grn():
    g_ = ['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>', '<rect width="260" height="40" rx="16" fill="url(#gNavy)"/><rect y="24" width="260" height="16" fill="#1a3a74"/>',
          t(14, 26, 'Goods received (GRN)', 12.5, 700, '#fff')]
    y = 64
    for a, b in [('Chakki Atta 10 kg', '+20 bags'), ('Sugar', '+100 kg'), ('Cooking Oil 1 L', '+48 pouch')]:
        g_ += [t(14, y, a, 11.5, 600, '#10224A'), t(246, y, b, 11.5, 800, '#1E8A43', 'end'), f'<line x1="14" y1="{y+10}" x2="246" y2="{y+10}" stroke="#e3e9f2"/>']
        y += 30
    g_ += [t(14, 160, 'Supplier: Rehman Traders', 10.5, 500, '#64748b'), '<rect x="160" y="146" width="88" height="24" rx="12" fill="#ecfdf3"/>', t(204, 162, 'Stock up', 10.5, 700, '#15803d', 'middle')]
    return ''.join(g_)


def ui_bill():
    g_ = ['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>', t(14, 26, 'New sale', 13, 700, '#10224A'), t(246, 26, 'Counter 1', 10.5, 500, '#64748b', 'end')]
    y = 52
    for a, u, b in [('Chakki Atta 10 kg', 'Bag', '1,200'), ('Sugar (loose)', 'Kg 2.5', '400'), ('Biscuits', 'Carton', '600')]:
        g_ += [t(14, y, a, 11, 600, '#10224A'), t(150, y, u, 10, 600, '#024691'), t(246, y, b, 11, 700, '#10224A', 'end')]
        y += 24
    g_ += ['<rect x="14" y="122" width="232" height="30" rx="10" fill="#eaf1ff"/>', t(26, 142, 'Total', 11.5, 600, '#475569'), t(236, 143, 'Rs 2,200', 15, 800, '#024691', 'end'),
           '<rect x="14" y="158" width="112" height="24" rx="10" fill="#fff" stroke="#c7d7ff"/>', t(70, 175, 'Cash', 11, 700, '#024691', 'middle'),
           '<rect x="134" y="158" width="112" height="24" rx="10" fill="#024691"/>', t(190, 175, 'Udhaar', 11, 700, '#fff', 'middle')]
    return ''.join(g_)


def ui_send():
    return ''.join(['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>',
                    receipt(14, 10, 120, 172, rows=[('Atta 10 kg', '1,200'), ('Sugar 2.5 kg', '400'), ('Biscuits', '600')], total='Rs 2,200'),
                    '<rect x="146" y="46" width="102" height="40" rx="12" fill="#FAE814"/>', t(197, 71, 'Print', 13, 800, '#10224A', 'middle'),
                    t(197, 106, 'or', 11, 600, '#64748b', 'middle'),
                    '<rect x="146" y="118" width="102" height="40" rx="12" fill="#1E8A43"/>', t(197, 143, 'WhatsApp', 12, 800, '#fff', 'middle')])


def ui_khata():
    g_ = ['<rect width="260" height="190" rx="16" fill="#f3f6fb"/>', '<circle cx="32" cy="30" r="16" fill="#eaf1ff"/>', t(32, 35, 'RA', 10.5, 800, '#024691', 'middle'),
          t(56, 27, 'Rashid Ahmed', 12.5, 700, '#10224A'), t(56, 43, 'Udhaar khata', 10, 500, '#64748b')]
    y = 78
    for a, b, c in [('Old balance', 'Rs 6,680', '#10224A'), ('Paid today', '- Rs 3,000', '#1E8A43'), ('New balance', 'Rs 3,680', '#b42318')]:
        g_ += [t(14, y, a, 11.5, 600, '#475569'), t(246, y, b, 12.5, 800, c, 'end'), f'<line x1="14" y1="{y+11}" x2="246" y2="{y+11}" stroke="#e3e9f2"/>']
        y += 32
    g_ += ['<rect x="14" y="156" width="232" height="26" rx="10" fill="#1E8A43"/>', t(130, 174, 'Send statement on WhatsApp', 10.5, 700, '#fff', 'middle')]
    return ''.join(g_)


def ui_profit():
    g_ = ['<rect width="260" height="190" rx="16" fill="url(#gBlue)"/>', t(14, 28, "Today's sales", 11, 500, '#cfe0ff'), t(14, 56, 'Rs 48,250', 22, 800, '#fff'),
          t(14, 76, 'Profit Rs 6,120  ·  Expenses Rs 1,450', 10, 500, '#cfe0ff'), '<rect x="14" y="88" width="232" height="90" rx="12" fill="#fff"/>']
    for i, h in enumerate([30, 42, 36, 54, 46, 62, 50]):
        g_.append(f'<rect x="{30+i*31}" y="{168-h}" width="18" height="{h}" rx="4" fill="url(#gBar)"/>')
    return ''.join(g_)


def arrow(d, head):
    return (f'<path d="{d}" fill="none" stroke="#2FA455" stroke-width="4.5" stroke-linecap="round" stroke-dasharray="2 11"/>'
            f'<path d="{head}" fill="none" stroke="#2FA455" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>')


def scene_process():
    y1, y2 = 120, 520
    return ''.join([
        pcard(60, y1, 1, 'Buy stock', ui_grn(), 'Stock and supplier ledger update'),
        pcard(450, y1, 2, 'Sell at counter', ui_bill(), 'Pick the unit, cash or udhaar'),
        pcard(840, y1, 3, 'Print or send', ui_send(), 'Paper receipt or WhatsApp bill'),
        pcard(645, y2, 4, 'Collect udhaar', ui_khata(), 'Khata updates on its own'),
        pcard(255, y2, 5, 'See profit', ui_profit(), 'Sales, expenses and profit'),
        arrow('M368,280 L436,280', 'M424,268 L438,280 L424,292'),
        arrow('M758,280 L826,280', 'M814,268 L828,280 L814,292'),
        arrow('M990,446 C990,500 960,560 952,600', 'M942,588 L951,604 L965,592'),
        arrow('M640,680 L566,680', 'M578,668 L564,680 L578,692'),
    ])



SCENES = {
    'uptrendpos-industry-specific-pos-software': ('Pick Your Business Type', 'blue', scene_hub,
        [(60, 770, '30+ business types', '#2FA455'), (330, 770, 'Ready fields and reports', '#2F7BD9')]),
    'uptrendpos-grocery-store-pos-software': ('Kiryana Counter', 'green', scene_grocery_hero,
        [(60, 780, 'Pack, piece and kg', '#2FA455'), (300, 780, 'Udhaar on khata', '#F59E0B')]),
    'uptrendpos-mobile-pos-type-c-thermal-printer': ('Phone + Type-C Printer', 'yellow', scene_type_c,
        [(760, 130, 'No computer needed', '#2FA455'), (60, 640, 'Plug in and print', '#2F7BD9')]),
    'uptrendpos-send-bill-on-whatsapp': ('No Printer? Send It', 'green', scene_whatsapp,
        [(60, 300, 'Bill as a picture', '#2FA455'), (60, 360, 'Khata as PDF', '#2F7BD9')]),
    'uptrendpos-grocery-daily-reports': ('Owner Daily Check', 'teal', scene_reports,
        [(80, 160, 'Sales, profit, udhaar', '#2FA9B0'), (80, 760, 'Demand list for orders', '#2FA455')]),
}

SCENES['uptrendpos-grocery-pos-hardware'] = ('POS Hardware for Kiryana', 'blue', scene_hardware,
    [(880, 110, 'Start with just a phone', '#2FA455')])
SCENES['uptrendpos-grocery-pos-process'] = ('Stock-In to Profit', 'green', scene_process,
    [(60, 470, 'All connected', '#2FA455')])


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1200, 'height': 900})
        only = sys.argv[1:]
        for name, (label, tint, body, chips) in SCENES.items():
            if only and name not in only:
                continue
            svg = frame(body(), label, chips, tint)
            (B / f'{name}.svg').write_text(svg)
            await pg.set_content(f'<html><body style="margin:0">{svg}</body></html>')
            await pg.wait_for_timeout(300)
            png = B / f'{name}.png'
            await pg.screenshot(path=str(png), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 900})
            im = Image.open(png).convert('RGB')
            out = OUT / f'{name}.webp'
            im.save(out, 'WEBP', quality=80, method=6)
            print(name, out.stat().st_size // 1024, 'KB')
        await b.close()

if __name__ == "__main__":
    asyncio.run(main())
