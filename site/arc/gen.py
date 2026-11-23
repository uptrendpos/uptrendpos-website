import json,sys,html,subprocess
icons=json.load(open('icons.json'))
D=json.load(open('/home/claude/repo/kit/uptrendpos-site-kit/data/industries.json'))
# group palettes: (bg1, bg2, accent1, accent2, glow)
P={
 'daily':      ('#062316','#0e4a2a','#3ddc84','#1E8A43','#7CFFB2'),
 'health':     ('#04212a','#0b4d57','#3fd0d6','#13878f','#9af6ff'),
 'fashion':    ('#140f3d','#33268c','#8f7dff','#5b44e0','#c9bfff'),
 'electronics':('#06163a','#0b3a8a','#4aa3ff','#1d5fd6','#a8d4ff'),
 'hardware':   ('#2a1404','#6b3409','#ffab45','#d9700f','#ffd59a'),
 'gifts':      ('#2b0716','#7a1442','#ff6fa6','#d02a6c','#ffc0d8'),
 'agri':       ('#0f2006','#2f5a10','#a6e04a','#5a9a1a','#e1ff9e'),
}
def chips(line):
    parts=[p.strip() for p in line.split(', ') if p.strip()]
    return [p[0].upper()+p[1:] for p in parts][:2]
OV={'fertilizer-shop-pos-software':['Batch and expiry','Season udhaar'],'electrical-store-pos-software':['Cartons and packs','Single pieces too'],
'vehicle-showroom-software':['Chassis numbers','Warranty and qist'],'crockery-shop-pos-software':['2,000+ products','Sets, cartons, pieces'],
'veterinary-store-pos-software':['Animal medicines','Batch and expiry'],'vape-shop-pos-software':['Flavours and sizes','As variants'],
'jewellery-shop-pos-software':['Gold rate','Making charge'],'battery-shop-pos-software':['Warranty','Qist for big sales'],'glass-shop-pos-software':['Quotations first','Then the bill']}
def card(t):
    g=t['group'];b1,b2,a1,a2,gl=P[g]; ic=icons[t['icon']]
    c=OV.get(t['slug']) or chips(t['line'])
    chip=''.join(f'<div class="chip c{i}"><span class="ck"><svg viewBox="0 0 24 24"><path d="M5 12.5l4.2 4.2L19 7"/></svg></span>{html.escape(x)}</div>' for i,x in enumerate(c))
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:P;src:url(/home/claude/repo/kit/uptrendpos-site-kit/assets/fonts/poppins-latin-600-normal.woff2)}}
*{{margin:0;box-sizing:border-box}}html,body{{width:600px;height:840px;overflow:hidden}}
.c{{position:relative;width:600px;height:840px;overflow:hidden;background:radial-gradient(120% 80% at 20% 0%,{b2} 0%,{b1} 62%);}}
.dots{{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.10) 1.4px,transparent 1.6px);background-size:26px 26px;-webkit-mask-image:radial-gradient(70% 60% at 50% 55%,#000 30%,transparent 80%)}}
.o1{{position:absolute;width:520px;height:520px;left:-120px;top:120px;border-radius:50%;background:{a1};opacity:.30;filter:blur(90px)}}
.o2{{position:absolute;width:420px;height:420px;right:-160px;top:-80px;border-radius:50%;background:{gl};opacity:.22;filter:blur(90px)}}
.beam{{position:absolute;left:-40%;top:-30%;width:180%;height:70%;background:linear-gradient(115deg,transparent 42%,rgba(255,255,255,.07) 50%,transparent 58%);}}
.ring{{position:absolute;left:50%;top:450px;border:2px solid rgba(255,255,255,.14);border-radius:50%;transform:translate(-50%,-50%) rotateX(72deg)}}
.r1{{width:470px;height:470px}}.r2{{width:350px;height:350px;border-color:rgba(255,255,255,.22)}}
.floor{{position:absolute;left:50%;top:560px;width:320px;height:60px;transform:translateX(-50%);border-radius:50%;background:radial-gradient(closest-side,rgba(0,0,0,.55),transparent);filter:blur(6px)}}
.tile{{position:absolute;left:50%;top:320px;width:240px;height:240px;margin-left:-120px;border-radius:64px;
background:linear-gradient(150deg,{a1} 0%,{a2} 70%);box-shadow:0 50px 80px -30px rgba(0,0,0,.65),0 0 0 1px rgba(255,255,255,.18) inset,0 -18px 40px -10px rgba(0,0,0,.25) inset,0 18px 30px -12px rgba(255,255,255,.45) inset;transform:perspective(900px) rotateX(10deg) rotateY(-14deg) rotateZ(-3deg)}}
.tile::before{{content:"";position:absolute;inset:10px;border-radius:56px;background:linear-gradient(180deg,rgba(255,255,255,.35),rgba(255,255,255,0) 45%)}}
.tile svg{{position:absolute;left:50%;top:50%;width:142px;height:142px;transform:translate(-50%,-50%);fill:none;stroke:#fff;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round;filter:drop-shadow(0 6px 10px rgba(0,0,0,.28)) drop-shadow(0 0 18px rgba(255,255,255,.35))}}
.spark{{position:absolute;width:10px;height:10px;border-radius:50%;background:{gl};box-shadow:0 0 18px 4px {gl}}}
.chip{{position:absolute;display:flex;align-items:center;gap:12px;padding:14px 22px 14px 14px;border-radius:999px;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.28);backdrop-filter:blur(10px);color:#fff;font:600 21px/1 P;letter-spacing:.01em;box-shadow:0 16px 30px -14px rgba(0,0,0,.6);white-space:nowrap}}
.ck{{width:34px;height:34px;border-radius:50%;background:#FAE814;display:grid;place-items:center}}.ck svg{{width:22px;height:22px;fill:none;stroke:#10224A;stroke-width:3;stroke-linecap:round;stroke-linejoin:round}}
.c0{{left:30px;top:262px;transform:rotate(-4deg)}}.c1{{right:30px;top:556px;transform:rotate(3deg);max-width:470px}}.chip{{overflow:hidden;text-overflow:ellipsis}}
.fade{{position:absolute;left:0;right:0;bottom:0;height:300px;background:linear-gradient(180deg,transparent,rgba(0,0,0,.72))}}
.top{{position:absolute;left:0;right:0;top:0;height:220px;background:linear-gradient(180deg,rgba(0,0,0,.45),transparent)}}
</style></head><body><div class="c"><div class="o1"></div><div class="o2"></div><div class="beam"></div><div class="dots"></div>
<div class="ring r1"></div><div class="ring r2"></div><div class="floor"></div>
<div class="tile"><svg viewBox="0 0 24 24">{ic}</svg></div>
<span class="spark" style="left:100px;top:430px"></span><span class="spark" style="left:480px;top:360px;width:7px;height:7px"></span><span class="spark" style="left:450px;top:520px;width:6px;height:6px"></span>
{chip}<div class="top"></div><div class="fade"></div></div></body></html>'''
import os
os.makedirs('html',exist_ok=True);os.makedirs('out',exist_ok=True)
only=sys.argv[1:] 
for t in D['types']:
    if only and t['slug'] not in only: continue
    open(f"html/{t['slug']}.html",'w').write(card(t))
print('ok')
