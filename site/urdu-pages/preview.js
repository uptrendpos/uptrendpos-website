// Render one Urdu page code like the live site (plugin CSS/JS + fonts) and report layout problems.
// node preview.js PAGE.html OUTPREFIX   -> OUTPREFIX-desktop.png, OUTPREFIX-mobile.png (+ JSON report on stdout)
const fs = require('fs'), path = require('path'), { chromium } = require('playwright');
const [page, out] = process.argv.slice(2);
const KIT = process.env.KIT || path.resolve(__dirname, '../../kit/uptrendpos-site-kit');
const ASSETS = process.env.ASSETS || '/home/claude/assets';
const f = (p) => 'file://' + p;
const faces = [400, 500, 600, 700, 800].map(w => `@font-face{font-family:'Poppins';font-weight:${w};src:url(${f(KIT + '/assets/fonts/poppins-latin-' + w + '-normal.woff2')})}`).join('')
  + `@font-face{font-family:'Jameel Noori Nastaleeq';unicode-range:U+0600-06FF,U+0750-077F,U+200C-200F,U+2066-2069,U+FB50-FDFF,U+FE70-FEFF;src:url(${f(ASSETS + '/fonts/jameel-noori-nastaleeq-ur.woff2')})}`;
const doc = `<!doctype html><html lang="ur-PK" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<style>${faces} body{margin:0;background:#fff}</style><link rel="stylesheet" href="${f(KIT + '/assets/css/utp.css')}">
<script>window.UTPK={live:[],links:{},stage:{}};</script></head><body class="utp-site utp-ur-mode">${fs.readFileSync(page, 'utf8')}
<script src="${f(KIT + '/assets/js/utp.js')}"></script></body></html>`;
const tmp = out + '.preview.html'; fs.writeFileSync(tmp, doc);
(async () => {
  const b = await chromium.launch(); const rep = { errors: [] };
  for (const [name, vp, mob] of [['desktop', { width: 1440, height: 900 }, false], ['mobile', { width: 390, height: 844 }, true]]) {
    const ctx = await b.newContext({ viewport: vp, isMobile: mob, hasTouch: mob }); const p = await ctx.newPage();
    p.on('pageerror', e => rep.errors.push(name + ': ' + e.message));
    await p.goto(f(path.resolve(tmp))); await p.waitForTimeout(800);
    const H = await p.evaluate(() => document.documentElement.scrollHeight);
    for (let y = 0; y < H; y += 500) { await p.evaluate(y => window.scrollTo(0, y), y); await p.waitForTimeout(80); }
    await p.evaluate(() => window.scrollTo(0, 0)); await p.waitForTimeout(500);
    rep[name] = await p.evaluate(() => {
      const W = document.documentElement.clientWidth, small = [], wide = [];
      document.querySelectorAll('.utp *').forEach(e => {
        const r = e.getBoundingClientRect(); if (!r.width) return;
        if ((r.right > W + 2 || r.left < -2) && !e.closest('.utp-marquee,.utp-stage,.utp-ticker,[class*="marquee"]')) wide.push(e.tagName + '.' + e.className);
        const t = [...e.childNodes].filter(n => n.nodeType === 3 && /[؀-ۿ]/.test(n.textContent)).length;
        if (t && !e.closest('.utp-sr') && parseFloat(getComputedStyle(e).fontSize) < 14) small.push(e.tagName + '.' + e.className + ' ' + getComputedStyle(e).fontSize);
      });
      return { scrollWidth: document.documentElement.scrollWidth, viewport: W, overflow: [...new Set(wide)].slice(0, 10), smallUrdu: [...new Set(small)].slice(0, 10) };
    });
    await p.screenshot({ path: `${out}-${name}.png`, fullPage: true }); await ctx.close();
  }
  await b.close(); console.log(JSON.stringify(rep, null, 1));
})();
