import pathlib, re, asyncio, sys
from playwright.async_api import async_playwright
P=pathlib.Path('/home/claude/site')
ds=(P/'pages/UpTrendPos_Design_System.html').read_text()
ds=re.sub(r'<link[^>]+fonts[^>]*>','',ds)
foot=(P/'src/website_footer_v1.html').read_text()
def page(name):
    body=(P/f'pages/{name}.html').read_text().replace('https://uptrendpos.com/wp-content/uploads/','file:///home/claude/site/hw/img/').replace(' loading="lazy"','')
    return f'''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{ds}
<style>body{{margin:0;font-family:Poppins}} .site-header{{position:absolute;top:0;left:0;right:0;height:96px;display:flex;align-items:center;padding:0 40px;z-index:9;font:600 15px Poppins;color:#10224A}}</style></head>
<body><header class="site-header">UpTrendPos header (overlay)</header><main><div class="page-header"><h1 class="entry-title">POS Software For Grocery Store</h1></div><div class="elementor-widget-html">{body}</div></main>{foot}</body></html>'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for name in sys.argv[1:]:
            f=P/f'preview/{name}.html'; f.write_text(page(name))
            for w,tag in [(1366,'d'),(390,'m')]:
                pg=await b.new_page(viewport={'width':w,'height':900})
                await pg.goto('file://'+str(f)); await pg.wait_for_timeout(600)
                await pg.evaluate('async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,60));}window.scrollTo(0,0);}'); await pg.wait_for_timeout(800)
                print('wide:', await pg.evaluate('(()=>{const W=innerWidth;return [...document.querySelectorAll(".utp *")].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.right>W+1&&!e.closest(".utp-marquee")&&!e.closest(".utp-cmp-box")&&!e.closest(".utp-doc-table")}).slice(0,5).map(e=>e.className+" "+Math.round(e.getBoundingClientRect().right))})()'), 'title visible:', await pg.evaluate('getComputedStyle(document.querySelector(".page-header")).display'))
                sw=await pg.evaluate('document.documentElement.scrollWidth')
                print(name,tag,'scrollWidth',sw)
                await pg.screenshot(path=str(P/f'preview/{name}-{tag}.png'),full_page=True)
                await pg.close()
        await b.close()
asyncio.run(main())
