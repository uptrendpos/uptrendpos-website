# /ur/ - Urdu copy of the Home page (Site Kit 1.6.8, 25 Nov 2026)

- `home_live.html` = live English Home page code the Urdu copy was made from (md5 395c9107...).
- `build_ur_home.py home_live.html ur.html` = same sections and classes, Urdu words, RTL root
  (`class="utp utp-home utp-urdu" id="utp-home-ur" lang="ur" dir="rtl"`), Urdu hero items via `data-stage-items`,
  numbers and Latin runs wrapped in `<bdi>` (and U+2066/U+2069 inside the hero items).
- Publish: `POST /utpk/v1/page {"slug":"ur","html_url":"<raw assets>/pages/ur.html","publish":true}`.
- Header/footer words in Urdu: `kit/.../inc/urdu.php` (`utpk_ur_map()`).

## Font (Jameel Noori Nastaleeq)
Full font is 9.8 MB / 40k glyphs. We ship only what the text uses:
```
python3 -c "from fontTools.ttLib import TTFont as T;f=T('jameel-noori-nastaleeq4.woff2');f.flavor=None;f.save('jnn.ttf')"
cat ur.html ../../kit/uptrendpos-site-kit/inc/urdu.php > text.txt   # + any new Urdu text
python3 shape_subset.py jnn.ttf text.txt gids.txt                   # HarfBuzz, keeps every in-between glyph
pyftsubset jnn.ttf --gids-file=gids.txt --text-file=ur_chars.txt --unicodes="U+0020,U+00A0,U+200C-200F" \
  --no-layout-closure --layout-features='*' --flavor=woff2 --no-hinting --drop-tables+=FFTM \
  --output-file=jameel-noori-nastaleeq-ur.woff2
```
Rebuild the subset whenever the Urdu text changes, or new words may show in a fallback font.
Source: npm `jameel-noori` 1.1.2 ("Free Of Charge For Urdu Lovers").
