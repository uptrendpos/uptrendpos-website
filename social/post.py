"""UpTrendPos daily social post renderer (light theme of the 30 Oct 2026 feature posts).

One post = one JSON spec -> 2160x2700 PNG master (4:5, 4K) + 1640x2048 Meta/LinkedIn/Instagram upload copy.

usage:
  python3 social/post.py setup                 # npm install icons + Poppins into social/.work (once per fresh workspace)
  python3 social/post.py next                  # prints today's calendar entry (JSON) from calendar.json + log.json
  python3 social/post.py render <spec.json>    # renders; exit 2 when a layout gate fails (overlap / cut / outside safe box)
  python3 social/post.py mark <key> <date>     # appends the published entry to log.json
  python3 social/post.py demo                  # renders social/examples/*.json (regression check)

Design px = 1080x1350, rendered x2. Hero canvas (".in") = 952 x 700 design px; blocks are placed inside it.
"""
import json, re, subprocess, sys, datetime, pathlib

S = pathlib.Path(__file__).resolve().parent
WORK = S / '.work'; NM = WORK / 'node_modules'
OUT = S / 'out'; HT = WORK / 'html'
PHONE = '+92 319 2223292'
NAVY = '#10224A'; YEL = '#FAE814'; MINT = '#6FE0A6'; GRN = '#1E8A43'; BLUE = '#0A5BC4'; RED = '#D64545'; AMB = '#B7791F'

# gradient pairs used in the 30 Oct posts (name -> (from, to))
GRAD = {
    'green': ('#1E9E5A', '#47C683'), 'mint': ('#1E8A43', '#47C683'), 'blue': ('#0A5BC4', '#2F9BFF'),
    'sky': ('#0884F6', '#5CC8FF'), 'teal': ('#0A7FD0', '#3FD0C9'), 'red': ('#D64545', '#F07070'),
    'orange': ('#E8663C', '#F7B731'), 'pink': ('#E0457B', '#FF9A62'), 'navy': ('#10224A', '#0A5BC4'),
    'lime': ('#2E8B3E', '#A6D84A'), 'yellow': ('#F59E0B', '#FAE814'), 'deep': ('#024691', '#2F9BFF'),
    'purple': ('#6D3FD1', '#A77BFF'), 'grey': ('#E3E9F2', '#E3E9F2'),
}
TONE = {'ok': ('#E7F7EE', GRN), 'warn': ('#FFF4D6', AMB), 'bad': ('#FDECEC', RED), 'info': ('#E6F0FF', BLUE)}


def grad(c):
    a, b = GRAD.get(c, (c, c)) if not (isinstance(c, (list, tuple))) else c
    return f'linear-gradient(135deg,{a},{b})'


def rgba(h, a):
    h = h.lstrip('#'); return f'rgba({int(h[0:2],16)},{int(h[2:4],16)},{int(h[4:6],16)},{a})'


def icon(name, size=24, color='currentColor', sw=1.8):
    p = NM / '@tabler/icons/icons/outline' / f'{name}.svg'
    if not p.exists():
        raise SystemExit(f'ICON MISSING: {name} (pick a Tabler outline icon name that exists in {p.parent})')
    s = p.read_text()
    body = s[s.index('>', s.index('<svg')) + 1: s.rindex('</svg>')]
    body = re.sub(r'<path stroke="none" d="M0 0h24v24H0z" fill="none"\s*/>', '', body)
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{body}</svg>')


FONT_CSS = ''.join(
    f"@font-face{{font-family:'Poppins';font-weight:{w};src:url('file://{NM}/@fontsource/poppins/files/poppins-latin-{w}-normal.woff2') format('woff2')}}"
    for w in (400, 500, 600, 700, 800, 900))
LOGO = f'file://{S}/assets/Logo-Horizontal-Color.svg'

BASE = '''
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}
body{font-family:Poppins,sans-serif;position:relative;-webkit-font-smoothing:antialiased;background:var(--bg);color:var(--fg)}
.safe{position:absolute;inset:64px;display:flex;flex-direction:column}
.top{display:flex;justify-content:space-between;align-items:center;height:80px}
.logo{background:#fff;border-radius:22px;padding:14px 22px;box-shadow:0 12px 30px rgba(0,8,40,.22)}
.logo img{display:block;height:48px}
.badge{display:flex;align-items:center;gap:12px;padding:13px 24px;border-radius:99px;font-weight:700;font-size:20px;letter-spacing:2px;white-space:nowrap}
.badge i{width:12px;height:12px;border-radius:50%;background:var(--c2);box-shadow:0 0 0 5px var(--c2a)}
.h{margin-top:40px;font-weight:800;font-size:82px;line-height:1.02;letter-spacing:-1.6px;white-space:nowrap;text-align:center}
.h em{font-style:normal;color:var(--hl)}
.s{margin-top:16px;font-weight:500;font-size:30px;white-space:nowrap;text-align:center;color:var(--sub)}
.s b{font-weight:700;color:var(--hl2)}
.vis{position:relative;flex:1;margin-top:28px}
.vis>.in{position:absolute;left:0;right:0;top:50%;height:700px;transform:translateY(-50%);transform-origin:50% 50%}
.tiles{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:22px}
.tile{display:flex;align-items:center;gap:14px;border-radius:22px;padding:16px 18px;background:var(--tile);border:1.5px solid var(--tileb)}
.tile b{width:52px;height:52px;border-radius:15px;display:flex;align-items:center;justify-content:center;flex:none}
.tile span{font-weight:600;font-size:21px;line-height:1.2;white-space:nowrap}
.foot{margin-top:22px;height:78px;display:flex;justify-content:center}
.fp{display:flex;align-items:center;gap:18px;border-radius:99px;padding:0 32px 0 12px;font-weight:700;font-size:28px;white-space:nowrap}
.fp .wa{width:56px;height:56px;border-radius:50%;background:linear-gradient(135deg,#1E8A43,#47C683);display:flex;align-items:center;justify-content:center}
.fp small{font-weight:500;font-size:21px;opacity:.75}
.fp i{width:2px;height:32px;background:currentColor;opacity:.2}
.ph{position:absolute;background:#0f172a;border-radius:48px;padding:12px;border:2px solid #3b465a;box-shadow:0 34px 80px rgba(0,8,30,.35)}
.scr{position:relative;width:100%;height:100%;border-radius:37px;background:#F3F6FB;overflow:hidden;color:#10224A}
.pt{color:#fff;padding:18px 22px 20px}
.pt .st{display:flex;justify-content:space-between;font-size:13px;font-weight:600;opacity:.9}
.pt h4{font-size:25px;font-weight:700;margin-top:12px;line-height:1.1}
.pt p{font-size:14px;opacity:.85}
.it{display:flex;align-items:center;gap:12px;background:#fff;border:1px solid #E3E9F2;border-radius:16px;padding:11px 14px;margin:0 14px 10px}
.it .sw{width:40px;height:40px;border-radius:12px;flex:none;display:flex;align-items:center;justify-content:center}
.it b{display:block;font-size:16px;line-height:1.2}.it small{font-size:13px;color:#64748b}
.it em{margin-left:auto;font-style:normal;font-weight:800;font-size:16px;white-space:nowrap}
.btn{border-radius:16px;text-align:center;font-weight:800;padding:15px 0;font-size:19px;margin:6px 14px 0}
.card{position:absolute;background:#fff;color:#10224A;border-radius:26px;padding:22px 24px;box-shadow:0 20px 50px rgba(10,43,108,.15)}
.ct{display:flex;align-items:center;gap:12px;font-weight:800;font-size:22px}
.ct .ci{width:44px;height:44px;border-radius:13px;display:flex;align-items:center;justify-content:center;flex:none}
.cs{font-size:14px;color:#5C687C;margin:4px 0 6px}
.kv{display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid #EEF2F8;font-size:17px;gap:12px}
.kv:last-child{border-bottom:0}
.kv b{font-weight:700;white-space:nowrap}
.pill{font-size:14px;font-weight:700;padding:5px 12px;border-radius:99px;white-space:nowrap}
.stat{position:absolute;border-radius:24px;padding:18px 22px;box-shadow:0 22px 50px rgba(10,43,108,.22);color:#10224A}
.stat b{display:block;font-weight:800;font-size:44px;line-height:1}
.stat span{display:block;font-weight:600;font-size:17px;margin-top:6px}
.chip{position:absolute;display:flex;align-items:center;gap:12px;background:#fff;color:#10224A;border-radius:99px;padding:10px 22px 10px 10px;font-weight:700;font-size:21px;white-space:nowrap;box-shadow:0 16px 40px rgba(10,43,108,.18)}
.chip b{width:42px;height:42px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex:none}
.tg{display:flex;flex-wrap:wrap;gap:10px;margin-top:12px}
.tg span{display:flex;align-items:center;gap:8px;font-size:16px;font-weight:600;padding:9px 14px;border-radius:14px;background:#F3F6FB;border:1px solid #E3E9F2;white-space:nowrap}
'''

CHECK_JS = """<script>
function fitAll(){document.querySelectorAll('.fit').forEach(el=>{
  const max=parseFloat(el.dataset.max||el.parentElement.clientWidth);let fs=parseFloat(getComputedStyle(el).fontSize);
  const tw=()=>{const r=document.createRange();r.selectNodeContents(el);return r.getBoundingClientRect().width;};
  while(tw()>max&&fs>10){fs-=1;el.style.fontSize=fs+'px';}
  el.dataset.final=fs;});}
function fitVis(){const v=document.querySelector('.vis'),i=v&&v.querySelector('.in');if(!i)return;
 const sc=Math.min(1,(v.clientHeight-8)/700);i.style.transform='translateY(-50%) scale('+sc+')';i.dataset.scale=sc;}
window.__check=function(){
 const bad=[];const safe=document.querySelector('.safe').getBoundingClientRect();
 document.querySelectorAll('.safe *').forEach(e=>{const r=e.getBoundingClientRect();
  if(r.width&&r.height&&(r.left<safe.left-1||r.right>safe.right+1||r.top<safe.top-1||r.bottom>safe.bottom+1))bad.push('OUTSIDE SAFE BOX: '+(e.className||e.tagName));});
 const q=s=>document.querySelector(s);const seq=['.top','.h','.s','.vis>.in','.tiles','.foot'].map(q).filter(Boolean);
 for(let k=1;k<seq.length;k++){if(seq[k].getBoundingClientRect().top<seq[k-1].getBoundingClientRect().bottom-1)bad.push('OVERLAP '+seq[k-1].className+' / '+seq[k].className);}
 const blk=[...document.querySelectorAll('.in>[data-b]')];
 for(let a=0;a<blk.length;a++)for(let b=a+1;b<blk.length;b++){
  if(blk[a].dataset.ov==='1'||blk[b].dataset.ov==='1')continue;
  const r1=blk[a].getBoundingClientRect(),r2=blk[b].getBoundingClientRect();
  const ix=Math.min(r1.right,r2.right)-Math.max(r1.left,r2.left),iy=Math.min(r1.bottom,r2.bottom)-Math.max(r1.top,r2.top);
  if(ix>2&&iy>2)bad.push('BLOCKS OVERLAP: '+blk[a].dataset.b+' / '+blk[b].dataset.b+' (set "overlap":true on a block only if the overlap is intended)');}
 const inr=q('.vis>.in').getBoundingClientRect();
 blk.forEach(e=>{const r=e.getBoundingClientRect();if(r.left<inr.left-2||r.right>inr.right+2||r.top<inr.top-2||r.bottom>inr.bottom+2)bad.push('BLOCK OUTSIDE HERO (952x700): '+e.dataset.b);});
 document.querySelectorAll('.scr').forEach(s=>{if(s.scrollHeight>s.clientHeight+1)bad.push('PHONE CONTENT CUT: remove a row or shorten the phone');});
 document.querySelectorAll('.card,.stat,.chip,.tile span').forEach(e=>{if(e.scrollWidth>e.clientWidth+1)bad.push('TEXT TOO WIDE in '+e.className+': '+e.textContent.trim().slice(0,40));});
 const h=q('.h'),s=q('.s');
 if(h&&parseFloat(h.dataset.final)<58)bad.push('HEADLINE TOO LONG: shrank to '+h.dataset.final+'px (min 58). Shorten it.');
 if(s&&parseFloat(s.dataset.final)<24)bad.push('SUB-LINE TOO LONG: shrank to '+s.dataset.final+'px (min 24). Shorten it.');
 const sc=parseFloat(q('.vis>.in').dataset.scale||1);if(sc<0.86)bad.push('HERO SQUEEZED to '+sc.toFixed(2)+' (min 0.86)');
 return bad;};
fitAll();fitVis();document.fonts.ready.then(()=>{fitAll();fitVis();});
</script>"""


# ---------------------------------------------------------------- blocks
def _pos(b, extra=''):
    st = ''
    for k in ('left', 'right', 'top', 'bottom'):
        if k in b: st += f'{k}:{b[k]}px;'
    if 'x' in b: st += f'left:{b["x"]}px;'
    if 'y' in b: st += f'top:{b["y"]}px;'
    if 'w' in b: st += f'width:{b["w"]}px;'
    if 'h' in b: st += f'height:{b["h"]}px;'
    if b.get('center'): st += 'left:50%;transform:translateX(-50%);'
    if b.get('rotate'): st += f'transform:rotate({b["rotate"]}deg);'
    return st + extra


def _attrs(b, i):
    return f'data-b="{b["type"]}#{i}"' + (' data-ov="1"' if b.get('overlap') else '')


def _kv(rows):
    out = ''
    for r in rows:
        a, v = r[0], r[1]
        t = r[2] if len(r) > 2 else None
        if t:
            bg, fg = TONE[t]
            out += f'<div class="kv"><span>{a}</span><span class="pill" style="background:{bg};color:{fg}">{v}</span></div>'
        else:
            out += f'<div class="kv"><span>{a}</span><b>{v}</b></div>'
    return out


def b_phone(b, i, c1):
    rows = ''
    for r in b.get('rows', []):
        col = r.get('color', 'green')
        bg = '#E3E9F2' if col == 'grey' else (grad(col) if col in GRAD else col)
        ic = icon(r['icon'], 22, '#fff', 2.2) if r.get('icon') and col != 'grey' else ''
        end = r.get('end')
        ec = TONE[r['tone']][1] if r.get('tone') in TONE else ('#94A3B8' if col == 'grey' else NAVY)
        rows += (f'<div class="it"><span class="sw" style="background:{bg}">{ic}</span><div><b>{r["title"]}</b><small>{r.get("sub", "")}</small></div>'
                 + (f'<em style="color:{ec}">{end}</em>' if end else '') + '</div>')
    top = ''
    if b.get('search'):
        top += (f'<div style="margin:14px 14px 0;display:flex;align-items:center;gap:10px;background:#fff;border:1px solid #E3E9F2;'
                f'border-radius:14px;padding:12px 14px;font-size:16px">{icon("search", 20, "#64748b", 2)}<b>{b["search"]}</b></div>')
    if b.get('banner'):
        bn = b['banner']; bg, fg = TONE[bn.get('tone', 'warn')]
        top += (f'<div style="margin:14px 14px 0;display:flex;align-items:center;gap:10px;background:{bg};border-radius:14px;padding:12px 14px;'
                f'font-size:15px;font-weight:700;color:{fg}">{icon(bn.get("icon", "info-circle"), 22, fg, 2.2)}{bn["text"]}</div>')
    btn = f'<div class="btn" style="background:{YEL};color:{NAVY}">{b["button"]}</div>' if b.get('button') else ''
    hb = grad(b.get('color', c1)) if b.get('color', c1) in GRAD else grad((b.get('color', c1), b.get('color2', BLUE)))
    b.setdefault('w', 380); b.setdefault('h', 700)
    return (f'<div class="ph" {_attrs(b, i)} style="{_pos(b)}"><div class="scr">'
            f'<div class="pt" style="background:{hb}"><div class="st"><span>9:41</span><span>UpTrendPos</span></div><h4>{b["title"]}</h4><p>{b.get("subtitle", "")}</p></div>'
            f'{top}<div style="padding-top:14px">{rows}</div>{btn}</div></div>')


def b_card(b, i, c1):
    body = _kv(b.get('rows', [])) + b.get('html', '')
    if b.get('balance'):
        lab, val, t = (b['balance'] + ['bad'])[:3]
        bg, fg = TONE[t]
        body = (f'<div style="margin:6px 0 10px;background:{bg};border-radius:16px;padding:14px 18px"><div style="font-size:14px;color:#5C687C">{lab}</div>'
                f'<b style="font-size:36px;color:{fg}">{val}</b></div>') + body
    if b.get('tags'):
        body += '<div class="tg">' + ''.join(f'<span>{icon(t[0], 18, NAVY, 2)}{t[1]}</span>' for t in b['tags']) + '</div>'
    sub = f'<div class="cs">{b["sub"]}</div>' if b.get('sub') else '<div style="height:8px"></div>'
    return (f'<div class="card" {_attrs(b, i)} style="{_pos(b)}"><div class="ct"><span class="ci" style="background:{grad(b.get("color", "blue"))}">'
            f'{icon(b.get("icon", "check"), 24, "#fff", 2.2)}</span>{b["title"]}</div>{sub}{body}</div>')


def b_table(b, i, c1):
    cols = b.get('cols', '1fr 150px 250px')
    tr = ''
    for r in b['rows']:
        t = TONE[r[3]] if len(r) > 3 and r[3] else TONE['info']
        tr += (f'<div style="display:grid;grid-template-columns:{cols};align-items:center;padding:{b.get("pad", 22)}px 0;border-bottom:1px solid #EEF2F8">'
               f'<b style="font-size:22px">{r[0]}</b><span style="font-size:17px;color:#5C687C">{r[1]}</span>'
               f'<span style="justify-self:end;font-size:18px;font-weight:700;padding:8px 16px;border-radius:99px;background:{t[0]};color:{t[1]}">{r[2]}</span></div>')
    b.setdefault('x', 20); b.setdefault('w', 912)
    return (f'<div class="card" {_attrs(b, i)} style="{_pos(b, "padding:26px 32px")}"><div class="ct"><span class="ci" style="background:{grad(b.get("color", "blue"))}">'
            f'{icon(b.get("icon", "list"), 24, "#fff", 2.2)}</span>{b["title"]}</div>{tr}</div>')


def b_stat(b, i, c1):
    bg = grad(b.get('color', 'yellow')) if b.get('color', 'yellow') != 'yellow' else grad(('#FAE814', '#FFD43B'))
    fg = '#fff' if b.get('color', 'yellow') not in ('yellow',) else NAVY
    return f'<div class="stat" {_attrs(b, i)} style="{_pos(b)}background:{bg};color:{fg}"><b>{b["num"]}</b><span>{b["label"]}</span></div>'


def b_chip(b, i, c1):
    bg, fg = TONE[b.get('tone', 'ok')]
    return f'<div class="chip" {_attrs(b, i)} style="{_pos(b)}"><b style="background:{bg}">{icon(b.get("icon", "check"), 24, fg, 2.2)}</b>{b["text"]}</div>'


def b_html(b, i, c1):
    return f'<div {_attrs(b, i)} style="position:absolute;{_pos(b)}">{b["html"]}</div>'


def b_image(b, i, c1):
    src = b['src'] if b['src'].startswith(('file:', 'http')) else f'file://{S}/assets/{b["src"]}'
    return f'<img {_attrs(b, i)} src="{src}" style="position:absolute;{_pos(b)}">'


BLOCKS = {'phone': b_phone, 'card': b_card, 'table': b_table, 'stat': b_stat, 'chip': b_chip, 'html': b_html, 'image': b_image}


def page(spec):
    c1 = spec['c1']; c2 = spec.get('c2', c1)
    bg = (f'radial-gradient(760px 600px at 92% 2%,{rgba(c2,.22)},transparent 60%),'
          f'radial-gradient(760px 640px at 0% 100%,{rgba(c1,.16)},transparent 60%),'
          f'linear-gradient(170deg,#FFFFFF 0%,#F2F7FF 55%,#E8F0FD 100%)')
    v = (f'--bg:{bg};--fg:{NAVY};--sub:#4A5873;--hl:{c1};--hl2:{c1};--tile:#FFFFFF;--tileb:#E2E9F4;--c2:{c1};--c2a:{rgba(c1,.18)}')
    deco = (f'<div style="position:absolute;inset:0;background-image:radial-gradient({rgba(c1,.10)} 1.4px,transparent 1.6px);background-size:28px 28px;'
            f'-webkit-mask-image:radial-gradient(700px 600px at 50% 40%,#000,transparent 80%)"></div>'
            f'<div style="position:absolute;width:640px;height:640px;right:-300px;top:-260px;border-radius:50%;background:{rgba(YEL,.35)}"></div>'
            f'<div style="position:absolute;width:560px;height:560px;left:-300px;bottom:-280px;border-radius:50%;background:{rgba(c1,.10)}"></div>')
    css = BASE + (f'.badge{{background:#fff;border:1.5px solid {rgba(c1,.3)};color:{NAVY};box-shadow:0 8px 24px rgba(10,43,108,.08)}}'
                  f'.fp{{background:{NAVY};color:#fff;box-shadow:0 14px 34px rgba(10,43,108,.25)}}') + spec.get('css', '')
    vis = ''.join(BLOCKS[b['type']](b, i, c1) for i, b in enumerate(spec['blocks']))
    tl = ''
    for t in spec['tiles']:
        ic, lab = t[0], t[1]; col = t[2] if len(t) > 2 else 'blue'
        fg = NAVY if col == 'yellow' else '#fff'
        tl += f'<div class="tile"><b style="background:{grad(col)}">{icon(ic, 28, fg, 2)}</b><span>{lab}</span></div>'
    body = f'''<div class="safe">
  <div class="top"><div class="logo"><img src="{LOGO}"></div><div class="badge"><i></i>{spec["badge"]}</div></div>
  <div class="h fit" data-max="952">{spec["head"]}</div>
  <div class="s fit" data-max="952">{spec["sub"]}</div>
  <div class="vis"><div class="in">{vis}</div></div>
  <div class="tiles">{tl}</div>
  <div class="foot"><div class="fp"><span class="wa">{icon("brand-whatsapp", 32, "#fff", 2)}</span><span><small>Free demo </small>{PHONE}</span><i></i><span>uptrendpos.com</span></div></div>
</div>'''
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{FONT_CSS}:root{{{v}}}{css}</style></head>'
            f'<body>{deco}{body}{CHECK_JS}</body></html>')


# ---------------------------------------------------------------- spec gate (content rules)
BANNED = [r'\bRs\.?\s?\d[\d,]*\s*(/|per)\s*(month|mo|year)', r'\bPKR\b', r'%\s*off', r'\bdiscount offer', r'free plan', r'free forever',
          r'certified', r'FBR approved', r'pakistan.?s (first|no\.? ?1)', r'\bAGR\b', r'ready-?made', r'\bone pos\b', r'\bsmart\b',
          r'\biOS\b', r'\biPhone app\b', r'installation (fee|charge)', r'setup (fee|charge)', r'\bswipe\b', r'unlimited offline']


def gate_spec(spec):
    errs = []
    txt = json.dumps(spec, ensure_ascii=False)
    for p in BANNED:
        if re.search(p, txt, re.I): errs.append(f'BANNED WORDING matches /{p}/')
    if len(spec.get('tiles', [])) != 3: errs.append('need exactly 3 tiles')
    plain = re.sub('<[^>]+>', '', spec['head'])
    if len(plain) > 36: errs.append(f'headline {len(plain)} chars (max 36, one line)')
    if len(re.sub('<[^>]+>', '', spec['sub'])) > 62: errs.append('sub-line over 62 chars')
    if len(spec['badge']) > 30: errs.append('badge over 30 chars')
    return errs


def meta_copy(src, dst_png, dst_jpg):
    from PIL import Image
    im = Image.open(src).convert('RGB')
    r = im.resize((1638, 2048), Image.LANCZOS)
    out = Image.new('RGB', (1640, 2048))
    out.paste(r, (1, 0))
    out.paste(r.crop((0, 0, 1, 2048)), (0, 0)); out.paste(r.crop((1637, 0, 1638, 2048)), (1639, 0))
    out.save(dst_png, optimize=True); out.save(dst_jpg, quality=92, optimize=True, progressive=True)


def render(spec_path):
    spec = json.loads(pathlib.Path(spec_path).read_text())
    errs = gate_spec(spec)
    date = spec.get('date') or datetime.date.today().isoformat()
    name = f'UpTrendPos-Post-{date}-{spec["slug"]}-EN'
    od = OUT / date; od.mkdir(parents=True, exist_ok=True); HT.mkdir(parents=True, exist_ok=True)
    hp = HT / f'{name}.html'; hp.write_text(page(spec))
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
        pg.goto('file://' + str(hp)); pg.wait_for_load_state('networkidle'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(400)
        master = od / f'{name}-4K.png'
        pg.screenshot(path=str(master), full_page=False)
        errs += pg.evaluate('window.__check()')
        br.close()
    meta_copy(master, od / f'{name}-1640x2048.png', od / f'{name}-1640x2048.jpg')
    print(json.dumps({'master': str(master), 'upload_png': str(od / f'{name}-1640x2048.png'),
                      'upload_jpg': str(od / f'{name}-1640x2048.jpg'), 'errors': errs}, indent=1))
    return 2 if errs else 0


# ---------------------------------------------------------------- calendar
def _load(n, d):
    p = S / n
    return json.loads(p.read_text()) if p.exists() else d


def nxt():
    cal = _load('calendar.json', {})['posts']; log = _load('log.json', [])
    last = log[-1]['key'] if log else None
    keys = [c['key'] for c in cal]
    i = (keys.index(last) + 1) % len(cal) if last in keys else 0
    e = dict(cal[i]); e['index'] = i + 1; e['of'] = len(cal); e['recent'] = [l['key'] for l in log[-7:]]
    print(json.dumps(e, indent=1, ensure_ascii=False))


def mark(key, date, extra=''):
    log = _load('log.json', [])
    log.append({'key': key, 'date': date, 'note': extra})
    (S / 'log.json').write_text(json.dumps(log, indent=1, ensure_ascii=False) + '\n')
    print('marked', key, date)


def setup():
    WORK.mkdir(exist_ok=True)
    if not (NM / '@tabler/icons').exists() or not (NM / '@fontsource/poppins').exists():
        (WORK / 'package.json').write_text('{"name":"utp-social-work","private":true}')
        subprocess.run(['npm', 'i', '@tabler/icons@3.35.0', '@fontsource/poppins@5.2.7'], cwd=WORK, check=True)
    print('setup ok')


if __name__ == '__main__':
    a = sys.argv[1:]
    cmd = a[0] if a else 'help'
    if cmd == 'setup': setup()
    elif cmd == 'next': nxt()
    elif cmd == 'render': sys.exit(render(a[1]))
    elif cmd == 'mark': mark(a[1], a[2], ' '.join(a[3:]))
    elif cmd == 'demo':
        rc = 0
        for f in sorted((S / 'examples').glob('*.json')): rc |= render(f)
        sys.exit(rc)
    else: print(__doc__)
