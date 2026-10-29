import asyncio, sys, pathlib
from playwright.async_api import async_playwright
S=pathlib.Path('/home/claude/preview_site/p'); O=pathlib.Path('/tmp/claude-0/-home-claude/87102ad8-da2a-5171-940b-4b06fbb8ca5a/scratchpad/shots')
names=sys.argv[1].split(',') if len(sys.argv)>1 and sys.argv[1] else [f.name for f in sorted(S.glob('*.html'))]
mode=sys.argv[2] if len(sys.argv)>2 else 'hero'
wait=int(sys.argv[3]) if len(sys.argv)>3 else 3500
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for vw,vh,tag in [(1440,900,'d'),(390,844,'m')]:
            pg=await b.new_page(viewport={'width':vw,'height':vh})
            for n in names:
                await pg.goto('file://'+str(S/n)); await pg.wait_for_timeout(wait)
                ov=await pg.evaluate('''()=>{const W=document.documentElement.clientWidth;const bad=[];document.querySelectorAll('body *').forEach(e=>{const r=e.getBoundingClientRect();if(r.width>0&&r.right>W+2&&!e.closest('.utp-marquee')&&!e.closest('.utp-jump')&&!e.closest('.utn-mega')&&!e.closest('.utn-drawer')&&!e.closest('.st-canvas'))bad.push(e.tagName+'.'+(e.className||'').toString().slice(0,40)+' '+Math.round(r.right))});return [document.documentElement.scrollWidth,W,bad.slice(0,5)]}''')
                if ov[0]>ov[1] or ov[2]: print(tag,n,'OVERFLOW',ov)
                await pg.screenshot(path=str(O/f'{n[:-5]}-{tag}.png'),full_page=(mode=='full'))
            await pg.close()
        await b.close()
asyncio.run(main())
