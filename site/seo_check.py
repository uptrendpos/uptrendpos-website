import re,sys,html
def text(s):
    s=re.sub(r'<svg.*?</svg>','',s,flags=re.S)
    s=re.sub(r'<[^>]+>',' ',s); s=html.unescape(s)
    return re.sub(r'\s+',' ',s).strip()
for f,kw in [(a.split('::')[0],a.split('::')[1]) for a in sys.argv[1:]]:
    s=open(f).read(); t=text(s); w=len(t.split())
    n=len(re.findall(re.escape(kw),t,flags=re.I)); kwn=len(kw.split())
    print(f, 'words',w,'kw',n,'density %.2f%%'%(100*n*kwn/w))
    print(' H1:',re.findall(r'<h1[^>]*>(.*?)</h1>',s,re.S))
    print(' H2 with kw:',sum(1 for h in re.findall(r'<h2[^>]*>(.*?)</h2>',s,re.S) if kw.lower() in text(h).lower()))
    print(' alt with kw:',sum(1 for a in re.findall(r'alt="([^"]*)"',s) if kw.lower() in a.lower()))
    print(' first p:', kw.lower() in text(re.findall(r'class="utp-lead">(.*?)</p>',s,re.S)[0]).lower())
    print(' comments:', '<!--' in s, ' style/script:', '<style' in s or '<script' in s, ' section sign:', '§' in s)
    faqs=re.findall(r'<details[^>]*>\s*<summary>(.*?)</summary>\s*<p>(.*?)</p>',s,re.S)
    for q,a in faqs: print('  faq',len(text(a).split()),'|',q)
    links=re.findall(r'href="(https://uptrendpos[^"#]*)',s); 
    from collections import Counter; print(' internal:',Counter(links).most_common())
