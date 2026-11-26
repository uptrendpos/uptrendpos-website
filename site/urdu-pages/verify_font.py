# Every Urdu run must shape glyph-for-glyph the same with the subset as with the full font.
import re, sys, uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.hashPointPen import HashPointPen
full_p, sub_p, text_p = sys.argv[1:4]
S = TTFont(sub_p); S.flavor = None; S.save(sub_p + '.ttf')
F, S = TTFont(full_p), TTFont(sub_p + '.ttf')
def gh(T, name):
    gs = T.getGlyphSet(); p = HashPointPen(gs[name].width, gs); gs[name].drawPoints(p); return p.hash
fonts = [(hb.Font(hb.Face(hb.Blob.from_file_path(full_p))), F), (hb.Font(hb.Face(hb.Blob.from_file_path(sub_p + '.ttf'))), S)]
runs = set(r.strip() for r in re.findall(r'[؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿‌‍ ]+', open(text_p, encoding='utf-8').read()) if r.strip())
bad = 0
for r in runs:
    out = []
    for f, T in fonts:
        b = hb.Buffer(); b.add_str(r); b.direction = 'rtl'; b.script = 'Arab'; b.language = 'ur'; hb.shape(f, b, {})
        order = T.getGlyphOrder()
        out.append([(gh(T, order[g.codepoint]), p.x_advance, p.x_offset, p.y_offset) for g, p in zip(b.glyph_infos, b.glyph_positions)])
    bad += out[0] != out[1]
print('font check: %d runs, %d mismatches' % (len(runs), bad))
sys.exit(1 if bad else 0)
