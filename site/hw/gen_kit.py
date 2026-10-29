"""Site Kit 1.0 images for the legal and support pages (same house style and watermark as gen_ind.py).
Run: python3 gen_kit.py [name ...]"""
import asyncio, sys
from playwright.async_api import async_playwright
from PIL import Image
from gen_ind import B, OUT, t, shadow, qr, phone_shell, status_bar, frame, g


def row(y, title, sub, right, rc='#1E8A43', rb='#ecfdf3'):
    return (f'<rect x="28" y="{y}" width="244" height="58" rx="14" fill="#fff" stroke="#e6ebf3"/>'
            + t(44, y + 25, title, 12, 700, '#10224A') + t(44, y + 43, sub, 9.5, 500, '#64748b')
            + f'<rect x="{258 - len(right) * 6.4 - 12:.0f}" y="{y + 18}" width="{len(right) * 6.4 + 12:.0f}" height="22" rx="11" fill="{rb}"/>'
            + t(258 - len(right) * 3.2 - 6, y + 33, right, 9.5, 700, rc, 'middle'))


def phone_privacy():
    gg = ['<rect x="14" y="14" width="272" height="148" fill="url(#gNavy)"/>', status_bar(),
          t(32, 86, 'Data and privacy', 18, 700, '#fff'), t(32, 108, 'City Medical Store', 11.5, 500, '#c9dbf2'),
          '<rect x="32" y="122" width="150" height="24" rx="12" fill="#fff" fill-opacity=".16"/>', t(107, 138, 'Owner login', 10.5, 600, '#fff', 'middle')]
    y = 178
    for a, b2, c in [('Your shop data', 'Kept apart from every other shop', 'Private'), ('Staff access', 'Each login with its own rights', 'PIN on'),
                     ('Backup', 'Last backup today, 10:42 am', 'Done'), ('Audit trail', 'Deletes and changes logged', 'On')]:
        gg.append(row(y, a, b2, c)); y += 68
    gg += [f'<rect x="28" y="{y+6}" width="244" height="46" rx="14" fill="#024691"/>', t(150, y + 35, 'Export my data (Excel / PDF)', 12, 700, '#fff', 'middle'),
           f'<rect x="28" y="{y+60}" width="244" height="40" rx="14" fill="#fff" stroke="#fecaca"/>', t(150, y + 85, 'Ask to delete my account', 11.5, 700, '#b42318', 'middle')]
    return phone_shell(''.join(gg), 'cpPriv')


def pin_card():
    out = ['<rect x="0" y="0" width="300" height="360" rx="26" fill="#fff"/>',
           '<circle cx="150" cy="62" r="30" fill="#eaf1ff"/>',
           '<rect x="137" y="58" width="26" height="20" rx="4" fill="#024691"/><path d="M141,58 v-7 a9,9 0 0 1 18,0 v7" fill="none" stroke="#024691" stroke-width="4"/>',
           t(150, 118, 'Enter your PIN', 15, 700, '#10224A', 'middle'), t(150, 138, 'Cashier: Bilal', 11, 500, '#64748b', 'middle')]
    for i in range(4):
        out.append(f'<circle cx="{102 + i * 32}" cy="166" r="8" fill="{"#10224A" if i < 3 else "#dbe3ef"}"/>')
    k = 0
    for r_ in range(3):
        for c in range(3):
            k += 1
            x, y = 54 + c * 66, 196 + r_ * 50
            out += [f'<rect x="{x}" y="{y}" width="58" height="40" rx="12" fill="#f3f6fb"/>', t(x + 29, y + 26, str(k), 15, 700, '#10224A', 'middle')]
    return ''.join(out)


def scene_privacy():
    shield = ('<g filter="url(#fSoft)"><circle cx="905" cy="215" r="74" fill="#10224A"/><path d="M905,170 l42,16 v30 c0,26 -18,46 -42,54 c-24,-8 -42,-28 -42,-54 v-30z" fill="#FAE814"/>'
              '<path d="M887,216 l12,12 22,-24" fill="none" stroke="#10224A" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g>')
    return shadow(470, 790, 230, 26) + g(phone_privacy(), 300, 150, 1.0) + g(pin_card(), 700, 340, 1.0) + shield


def a4_doc():
    out = ['<rect x="0" y="0" width="470" height="620" rx="14" fill="#fff"/>', '<rect x="0" y="0" width="470" height="92" rx="14" fill="url(#gNavy)"/>',
           '<rect x="0" y="70" width="470" height="22" fill="url(#gNavy)"/>',
           t(36, 50, 'Terms and Conditions', 22, 800, '#fff'), t(36, 74, 'UpTrendPos · web, Android and Windows apps', 11.5, 500, '#c9dbf2')]
    y = 132
    for i, (a, b2) in enumerate([('Free trial', '14 days, every feature to test'), ('Plans and payments', 'Premium, Enterprise, Custom'), ('Cancel and refunds', 'Clear rules, written simply'),
                                 ('Working offline', 'Bills saved, synced later'), ('FBR integration', 'Your FBR details, your control'), ('Your data', 'Yours to export any time'),
                                 ('Pakistani law', 'Courts and laws of Pakistan')], 1):
        out += [f'<circle cx="52" cy="{y-5}" r="15" fill="#e8f6ee"/>', f'<path d="M45,{y-5} l5,5 10,-11" fill="none" stroke="#1E8A43" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
                t(80, y - 8, f'{i}. {a}', 14, 700, '#10224A'), t(80, y + 10, b2, 11, 500, '#64748b'),
                f'<line x1="36" y1="{y+28}" x2="434" y2="{y+28}" stroke="#eef1f6"/>']
        y += 64
    return ''.join(out)


def phone_plan():
    gg = ['<rect x="14" y="14" width="272" height="160" fill="url(#gGreen)"/>', status_bar(),
          t(32, 86, 'Your plan', 18, 700, '#fff'), t(32, 110, 'Enterprise · Active', 13, 600, '#e9fbe9'),
          '<rect x="32" y="126" width="120" height="26" rx="13" fill="#fff" fill-opacity=".22"/>', t(92, 144, 'Paid monthly', 10.5, 600, '#fff', 'middle')]
    y = 190
    for a, b2, c in [('Branches', '2 of 2 used', '2'), ('Staff logins', '4 of 6 used', '4'), ('Invoices', 'No limit', 'Unlimited'), ('Next bill', '1 November 2026', 'Due')]:
        gg.append(row(y, a, b2, c, '#024691', '#eaf1ff')); y += 68
    gg += [f'<rect x="28" y="{y+8}" width="244" height="46" rx="14" fill="#FAE814"/>', t(150, y + 37, 'Change plan', 12.5, 700, '#10224A', 'middle')]
    return phone_shell(''.join(gg), 'cpPlan')


def scene_terms():
    return shadow(470, 790, 260, 26) + g(a4_doc(), 230, 150, 1.0, -3, 235, 310) + g(phone_plan(), 760, 190, .86)


def phone_support():
    gg = ['<rect x="14" y="14" width="272" height="104" fill="#1E8A43"/>', status_bar(),
          '<circle cx="50" cy="82" r="20" fill="#fff"/>', t(50, 88, 'UP', 12, 800, '#1E8A43', 'middle'),
          t(80, 80, 'UpTrendPos Support', 14.5, 700, '#fff'), t(80, 98, 'online', 11, 500, '#d1f2dc')]
    bubbles = [('me', 136, ['Printer is not printing', 'the bill. Please help.'], '10:12 am'),
               ('them', 214, ['Open Settings, then Printer.', 'Pick 58mm and USB, then', 'tap Test print.'], '10:13 am'),
               ('me', 312, ['Done, it prints now.', 'Shukriya!'], '10:16 am'),
               ('them', 390, ['Happy to help. We are here', 'Mon to Sat, 10 am to 7 pm.'], '10:16 am')]
    for who, y, lines, tm in bubbles:
        h = 26 + len(lines) * 17
        x, w = (106, 166) if who == 'me' else (28, 196)
        gg += [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{"#d9fdd3" if who == "me" else "#fff"}" filter="url(#fSoft)"/>']
        for i, ln in enumerate(lines):
            gg.append(t(x + 12, y + 22 + i * 17, ln, 11, 500, '#1e293b'))
        gg.append(t(x + w - 10, y + h - 6, tm, 8.5, 500, '#64748b', 'end'))
    gg += ['<rect x="14" y="540" width="272" height="58" fill="#f6f6f6"/>', '<rect x="26" y="551" width="200" height="36" rx="18" fill="#fff"/>',
           t(42, 574, 'Type a message', 11.5, 500, '#94a3b8'), '<circle cx="254" cy="569" r="18" fill="#1E8A43"/><path d="M247,569 l14,-7 -4,7 4,7 z" fill="#fff"/>']
    return phone_shell(''.join(gg), 'cpSup', bg='#efeae2')


def hours_card():
    out = ['<rect x="0" y="0" width="330" height="300" rx="26" fill="#fff"/>', t(30, 50, 'Support hours', 18, 800, '#10224A'), t(30, 74, 'Pakistan time', 11.5, 500, '#64748b')]
    y = 108
    for d, h_ in [('Monday to Saturday', '10 am - 7 pm'), ('Sunday', 'Closed')]:
        out += [f'<rect x="30" y="{y-22}" width="270" height="40" rx="12" fill="#f3f6fb"/>', t(44, y + 4, d, 12.5, 600, '#10224A'), t(288, y + 4, h_, 12.5, 700, '#024691', 'end')]
        y += 50
    out += [t(30, y + 14, 'Reach us on', 12, 600, '#64748b')]
    x = 30
    for lab, fill in [('WhatsApp', '#1E8A43'), ('Phone', '#024691'), ('Email', '#10224A')]:
        wch = 22 + len(lab) * 8
        out += [f'<rect x="{x}" y="{y+28}" width="{wch}" height="32" rx="16" fill="{fill}"/>', t(x + wch / 2, y + 49, lab, 11.5, 700, '#fff', 'middle')]
        x += wch + 10
    return ''.join(out)


def scene_support():
    return shadow(470, 800, 220, 24) + g(phone_support(), 330, 140, 1.0) + g(hours_card(), 720, 300, 1.0)


SCENES = {
    'uptrendpos-privacy-policy': ('Your Data, Your Control', 'navy', scene_privacy, [(70, 760, 'Data kept separate', '#2FA455'), (330, 800, 'PIN for every staff login', '#2F7BD9'), (760, 296, 'Export any time', '#FAE814')]),
    'uptrendpos-terms-and-conditions': ('Terms in Plain Words', 'blue', scene_terms, [(60, 790, '14-day free trial', '#2FA455'), (300, 800, 'Pakistani law', '#FAE814'), (900, 120, 'No hidden charges', '#2F7BD9')]),
    'uptrendpos-support-help-center': ('UpTrendPos Support', 'green', scene_support, [(60, 780, 'Urdu or English', '#2FA455'), (320, 806, 'WhatsApp, phone, email', '#2F7BD9'), (760, 650, 'Mon to Sat, 10 to 7', '#FAE814')]),
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
            im = Image.open(png).convert('RGB')
            out = OUT / f'{name}.webp'
            im.save(out, 'WEBP', quality=80, method=6)
            png.unlink()
            print(name, out.stat().st_size // 1024, 'KB')
        await b.close()

if __name__ == '__main__':
    asyncio.run(main())
