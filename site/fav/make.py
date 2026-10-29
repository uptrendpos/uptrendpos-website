import re, asyncio
from playwright.async_api import async_playwright
from PIL import Image
src = open('icon_src.svg').read()
inner = re.search(r'<svg[^>]*>(.*)</svg>', src, re.S).group(1)
defs = re.search(r'<defs>(.*?)</defs>', inner, re.S).group(1)
body = re.sub(r'<defs>.*?</defs>', '', inner, flags=re.S)
white = body.replace('fill="url(#gP)"', 'fill="#ffffff"')

def card(kind):
    # content box of the icon ~ x 25..485, y 143..370 -> centre (255,256); scale so it sits with padding
    s = 0.80
    tr = f'translate({256 - 255*s:.2f} {256 - 256.5*s:.2f}) scale({s})'
    if kind == 'blue':
        bg = ('<linearGradient id="fbg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0567B8"/><stop offset="1" stop-color="#022C74"/></linearGradient>'
              '<radialGradient id="fgl" cx=".25" cy=".15" r=".8"><stop offset="0" stop-color="#ffffff" stop-opacity=".18"/><stop offset="1" stop-color="#ffffff" stop-opacity="0"/></radialGradient>')
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512"><defs>{defs}{bg}</defs>'
                f'<rect width="512" height="512" rx="112" fill="url(#fbg)"/><rect width="512" height="512" rx="112" fill="url(#fgl)"/>'
                f'<g transform="{tr}">{white}</g></svg>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512"><defs>{defs}</defs>'
            f'<rect width="512" height="512" rx="112" fill="#ffffff"/><rect x="4" y="4" width="504" height="504" rx="108" fill="none" stroke="#e3e9f2" stroke-width="8"/>'
            f'<g transform="{tr}">{body}</g></svg>')

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for kind in ['blue', 'white']:
            svg = card(kind)
            open(f'UpTrendPos-Favicon-{kind}.svg', 'w').write(svg)
            pg = await b.new_page(viewport={'width': 4096, 'height': 4096})
            await pg.set_content(f'<html><body style="margin:0;background:transparent">{svg.replace(chr(39)+"512"+chr(39),"x").replace("width=\"512\" height=\"512\"","width=\"4096\" height=\"4096\"",1)}</body></html>')
            await pg.screenshot(path=f'UpTrendPos-Favicon-{kind}-4096.png', omit_background=True, clip={'x':0,'y':0,'width':4096,'height':4096})
            await pg.close()
        await b.close()
asyncio.run(main())

for kind in ['blue', 'white']:
    m = Image.open(f'UpTrendPos-Favicon-{kind}-4096.png').convert('RGBA')
    for sz in [512, 192, 180, 32, 16]:
        m.resize((sz, sz), Image.LANCZOS).save(f'UpTrendPos-Favicon-{kind}-{sz}.png', optimize=True)
    m.resize((256, 256), Image.LANCZOS).save(f'UpTrendPos-Favicon-{kind}.ico', sizes=[(16,16),(32,32),(48,48),(64,64),(128,128),(256,256)])
print('done')
