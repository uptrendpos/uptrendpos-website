"""Shared render loop for daily-automation image generators (same house style as gen_electrical_baby.py)."""
import asyncio, sys
from playwright.async_api import async_playwright
from PIL import Image
from gen_ind import B, OUT, frame


async def _run(scenes, only):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1200, 'height': 900})
        for name, (label, tint, body, chips) in scenes.items():
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


def run(scenes):
    asyncio.run(_run(scenes, sys.argv[1:]))
