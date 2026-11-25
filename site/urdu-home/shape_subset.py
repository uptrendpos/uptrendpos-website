# Keep only the Jameel Noori glyphs that our Urdu text really uses, including every in-between
# glyph the shaping steps pass through, so the subset renders exactly like the full font.
import sys, re, html, json, uharfbuzz as hb
from fontTools.ttLib import TTFont
src, textfile, out = sys.argv[1:4]
blob = hb.Blob.from_file_path(src); face = hb.Face(blob); font = hb.Font(face)
text = open(textfile, encoding='utf-8').read()
runs = set(re.findall(r'[؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿‌‍ ]+', text))
gids = set()
def msg(m):
    for gi in buf.glyph_infos: gids.add(gi.codepoint)
    return True
for r in runs:
    r = r.strip()
    if not r: continue
    buf = hb.Buffer(); buf.add_str(r); buf.direction = 'rtl'; buf.script = 'Arab'; buf.language = 'ur'
    buf.set_message_func(msg)
    hb.shape(font, buf, {})
    for gi in buf.glyph_infos: gids.add(gi.codepoint)
gids |= {0}
# space/nbsp glyphs
cmap = TTFont(src, lazy=True)['cmap'].getBestCmap()
order = TTFont(src, lazy=True).getGlyphOrder()
for cp in (0x20, 0xA0, 0x200C, 0x200D, 0x200E, 0x200F):
    if cp in cmap: gids.add(order.index(cmap[cp]))
print('runs', len(runs), 'glyphs', len(gids))
open(out, 'w').write(','.join(str(g) for g in sorted(gids)))
