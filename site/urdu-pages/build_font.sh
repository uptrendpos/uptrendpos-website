#!/usr/bin/env bash
# Rebuild the Jameel Noori Nastaleeq page-text subset from EVERY Urdu page + the header/footer words.
# Output: $ASSETS/fonts/jameel-noori-nastaleeq-ur.woff2 (then POST /utpk/v1/font installs it on the site).
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd -P)"
ASSETS="${ASSETS:-/home/claude/assets}"
KIT="${KIT:-$HERE/../../kit/uptrendpos-site-kit}"
W="${TMPDIR:-/tmp}/jnn-build"; mkdir -p "$W"
pip install -q --break-system-packages fonttools brotli uharfbuzz >/dev/null 2>&1 || true
if [ ! -f "$W/jnn.ttf" ]; then
  (cd "$W" && npm pack jameel-noori@1.1.2 >/dev/null 2>&1 && mkdir -p pkg && tar -xzf jameel-noori-1.1.2.tgz -C pkg)
  python3 -c "from fontTools.ttLib import TTFont as T;f=T('$W/pkg/package/fonts/jameel-noori-nastaleeq4.woff2');f.flavor=None;f.save('$W/jnn.ttf')"
fi
python3 - "$ASSETS" "$KIT" "$W/text.txt" <<'PY'
import sys, glob, html
a, k, out = sys.argv[1:4]
files = [a + '/pages/ur.html'] + sorted(glob.glob(a + '/pages/ur/*.html')) + [k + '/inc/urdu.php']
open(out, 'w', encoding='utf-8').write(html.unescape('\n'.join(open(f, encoding='utf-8').read() for f in files)))
print('text from', len(files), 'files')
PY
python3 "$HERE/shape_subset.py" "$W/jnn.ttf" "$W/text.txt" "$W/gids.txt"
pyftsubset "$W/jnn.ttf" --gids-file="$W/gids.txt" --text-file="$HERE/ur_chars.txt" --unicodes="U+0020,U+00A0,U+200C-200F" \
  --no-layout-closure --layout-features='*' --flavor=woff2 --no-hinting --drop-tables+=FFTM \
  --output-file="$ASSETS/fonts/jameel-noori-nastaleeq-ur.woff2"
python3 "$HERE/verify_font.py" "$W/jnn.ttf" "$ASSETS/fonts/jameel-noori-nastaleeq-ur.woff2" "$W/text.txt"
ls -la "$ASSETS/fonts/jameel-noori-nastaleeq-ur.woff2"
