# Builds the long Urdu overview page (UpTrendPos, 23 Nov 2026).
# Output: pos-software-urdu.html (UpTrendPos page code for one Elementor HTML widget).
# Rules: facts only from site/automation/FACTS.md, prices from the pricing page, no setup/installation charges,
# no competitor names, no "FBR approved", no customer counts, no iOS app, no free plan. 7-day free trial.
import json, html, re

ICON = json.load(open('/home/claude/arc/icons.json'))
ICON.update({
    'box': '<path d="M21 8l-9-5-9 5 9 5 9-5z"/><path d="M3 8v8l9 5 9-5V8M12 13v8"/>',
    'chart': '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    'users': '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3.5 6"/>',
    'receipt': '<path d="M6 2h12v20l-3-2-3 2-3-2-3 2z"/><path d="M9 7h6M9 11h6M9 15h4"/>',
    'ledger': '<path d="M4 4h11a3 3 0 0 1 3 3v13H7a3 3 0 0 1-3-3z"/><path d="M8 8h6M8 12h6"/>',
    'truck': '<path d="M3 6h11v10H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    'cal': '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    'branch': '<path d="M3 9l2-5h14l2 5"/><path d="M3 9h18v11H3zM9 20v-6h6v6"/>',
    'barcode': '<path d="M4 5v14M7 5v14M10 5v14M14 5v14M17 5v14M20 5v14"/>',
    'printer': '<path d="M6 9V3h12v6"/><rect x="3" y="9" width="18" height="8" rx="2"/><path d="M7 14h10v7H7z"/>',
    'sync': '<path d="M20 11a8 8 0 0 0-14.6-4.5L3 9M4 13a8 8 0 0 0 14.6 4.5L21 15"/><path d="M3 4v5h5M21 20v-5h-5"/>',
    'tag': '<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8.5" r="1.5"/>',
    'check': '<path d="M5 12.5l4.2 4.2L19 7"/>',
    'lock': '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
    'globe': '<circle cx="12" cy="12" r="9.5"/><path d="M2.5 12h19M12 2.5c2.6 2.6 4 6 4 9.5s-1.4 6.9-4 9.5c-2.6-2.6-4-6-4-9.5s1.4-6.9 4-9.5z"/>',
    'monitor': '<rect x="2.5" y="4" width="19" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>',
    'wa': '<path d="M12 3a9 9 0 0 0-7.7 13.6L3 21l4.5-1.2A9 9 0 1 0 12 3z"/><path d="M8.5 9c.3 2.8 2.7 5.3 5.6 5.8l1.2-1.4 2 .8-.4 1.8c-4.6.2-9.2-4.4-9-9l1.8-.4.8 2z"/>',
    'doc': '<path d="M6 2h9l5 5v15H6z"/><path d="M14 2v6h6M9 13h8M9 17h6"/>',
    'star': '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
})
SITE = 'https://uptrendpos.com'
WA = 'https://wa.me/923192223292?text='
LIVE = 'https://live.uptrendpos.com/'
IMG = SITE + '/wp-content/uploads/'


def ic(name, cls='ur-i'):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[name]}</svg>'


def wa_link(text, label, track, cls='utp-btn utp-btn-ghost ur-btn'):
    from urllib.parse import quote
    return f'<a class="{cls}" href="{WA}{quote(text)}" target="_blank" rel="noopener" data-track="{track}">{ic("wa")}<span>{label}</span></a>'


_E = html.escape
import re as _re
def E(t):
    t = _E(t)
    return _re.sub(r'(\d[\d,]*\+|\d+%)', r'<span class="ur-latin">\1</span>', t)

# ---------------- business groups (same grouping as Abdul's Urdu post images) ----------------
GROUPS = [
    ('grocery-mart', 'کریانہ اسٹور اور مارٹ کے لیے', 'روز کی خرید و فروخت، ادھار کھاتہ اور تیز بلنگ', 'g', [
        ('grocery-store-pos-software', 'کریانہ اسٹور اور مارٹ', '7,000+ پروڈکٹس تیار'),
        ('meat-shop-pos-software', 'پولٹری، گوشت اور سی فوڈ شاپ', 'کلو اور گرام میں بلنگ'),
        ('crockery-shop-pos-software', 'کراکری اور گھریلو سامان', '2,000+ پروڈکٹس تیار'),
        ('stationery-shop-pos-software', 'اسٹیشنری اور بک شاپ', '200+ پروڈکٹس تیار')]),
    ('pharmacy-beauty', 'فارمیسی اور بیوٹی اسٹورز کے لیے', 'بیچ نمبر، ایکسپائری اور فارمولا (سالٹ) سے تلاش', 't', [
        ('pharmacy-pos-software', 'فارمیسی اور میڈیکل اسٹور', '17,000+ ادویات تیار'),
        ('cosmetics-store-pos-software', 'کاسمیٹکس اور بیوٹی اسٹور', '5,500+ پروڈکٹس تیار'),
        ('baby-store-pos-software', 'بے بی شاپ اور ڈائپر اسٹور', '350+ پروڈکٹس تیار'),
        ('perfume-shop-pos-software', 'پرفیوم اور عطر شاپ', '300+ پروڈکٹس تیار')]),
    ('clothing-shoes', 'کپڑوں اور جوتوں کی دکانوں کے لیے', 'ہر سائز اور ہر رنگ کا الگ اسٹاک', 'n', [
        ('clothing-store-pos-software', 'کپڑوں اور گارمنٹس کی دکان', '950+ پروڈکٹس تیار'),
        ('shoe-store-pos-software', 'جوتوں کی دکان', '200+ پروڈکٹس تیار'),
        ('tailor-shop-pos-software', 'ٹیلر شاپ اور بوتیک', 'ناپ، آرڈر اور ڈیلیوری کی تاریخ'),
        ('undergarments-shop-pos-software', 'انڈر گارمنٹس اور ہوزری', '400+ پروڈکٹس تیار')]),
    ('jewellery-watch-bags', 'جیولری، گھڑیوں اور بیگز کی دکانوں کے لیے', 'ڈیزائن، ماڈل اور رنگ کے حساب سے اسٹاک', 'y', [
        ('jewellery-shop-pos-software', 'جیولری اور گولڈ شاپ', 'سونے کا ریٹ اور بنوائی'),
        ('artificial-jewellery-shop-pos-software', 'آرٹیفیشل جیولری شاپ', 'ڈیزائن اور لیبل'),
        ('watch-shop-pos-software', 'گھڑیوں کی دکان', '150+ پروڈکٹس تیار'),
        ('bag-shop-pos-software', 'بیگز اور سوٹ کیس شاپ', '680+ پروڈکٹس تیار')]),
    ('solar-electronics', 'سولر اور الیکٹرونکس شاپس کے لیے', 'سیریل نمبر، وارنٹی اور قسطوں پر فروخت', 'b', [
        ('solar-shop-pos-software', 'سولر شاپ', '1,100+ پروڈکٹس تیار'),
        ('electronics-store-pos-software', 'الیکٹرونکس، ہوم اپلائنسز اور CCTV', '1,100+ پروڈکٹس تیار'),
        ('mobile-shop-pos-software', 'موبائل اور کمپیوٹر شاپ', '700+ پروڈکٹس، IMEI'),
        ('electrical-store-pos-software', 'الیکٹریکل اور LED لائٹس شاپ', 'کارٹن، پیک اور پیس')]),
    ('vehicle-auto', 'بائیک، کار اور EV شوروم کے لیے', 'چیسس نمبر، وارنٹی اور قسطوں کا مکمل حساب', 'g', [
        ('vehicle-showroom-software', 'بائیک، کار اور EV شوروم', 'قسطوں کا مکمل حساب'),
        ('auto-parts-pos-software', 'آٹو پارٹس شاپ', 'ہر پارٹ فوراً تلاش'),
        ('tyre-shop-pos-software', 'ٹائر شاپ', 'سائز اور رِم کے حساب سے'),
        ('battery-shop-pos-software', 'بیٹری شاپ', 'وارنٹی اور قسطیں')]),
    ('hardware-building', 'ہارڈویئر اور تعمیراتی سامان کے لیے', 'ہزاروں آئٹمز، کوٹیشن اور ایڈوانس', 't', [
        ('hardware-store-pos-software', 'ہارڈویئر، سینیٹری اور بلڈنگ میٹریل', 'بوری، فٹ اور پیس'),
        ('paint-store-pos-software', 'پینٹ اسٹور', 'شیڈ اور پیک سائز'),
        ('glass-shop-pos-software', 'گلاس اور ایلومینیم شاپ', 'پہلے کوٹیشن، پھر بل'),
        ('furniture-shop-pos-software', 'فرنیچر شاپ', 'کوٹیشن، ایڈوانس اور قسط')]),
    ('gifts-sports-agri', 'گفٹ، اسپورٹس اور زرعی دکانوں کے لیے', 'سیزن کا رش اور سیزن کا ادھار، دونوں آسان', 'n', [
        ('toy-shop-pos-software', 'کھلونے اور گفٹ شاپ', '1,000+ پروڈکٹس تیار'),
        ('sports-shop-pos-software', 'اسپورٹس شاپ', '250+ پروڈکٹس تیار'),
        ('fertilizer-shop-pos-software', 'بیج، کھاد اور زرعی ادویات', 'بیچ، ایکسپائری اور سیزن ادھار'),
        ('veterinary-store-pos-software', 'ویٹرنری میڈیکل اسٹور', 'بیچ اور ایکسپائری')]),
]

FEATURES = [
    ('receipt', 'b', 'تیز بلنگ', 'بارکوڈ اسکین کریں یا نام سے تلاش کریں۔ بل ہولڈ کریں، ڈسکاؤنٹ دیں، کیش، بینک یا ادھار پر فروخت کریں۔'),
    ('box', 'g', 'اسٹاک کا مکمل کنٹرول', 'کارٹن، پیک، پیس، کلو یا میٹر، سب ایک بل پر۔ کم اسٹاک اور ایکسپائری سے پہلے الرٹ۔'),
    ('ledger', 'y', 'ادھار کھاتہ', 'ہر ادھار فروخت گاہک کے کھاتے میں خود جاتی ہے۔ وصولی درج کریں اور اسٹیٹمنٹ واٹس ایپ پر بھیجیں۔'),
    ('truck', 't', 'خریداری اور سپلائرز', 'پرچیز آرڈر، مال کی وصولی (GRN) اور پرچیز انوائس۔ ہر سپلائر کا بقایا ایک نظر میں۔'),
    ('chart', 'n', 'ڈبل انٹری حسابات', 'ہر فروخت اور خرچ خود حساب میں جاتا ہے۔ منافع و نقصان، ٹرائل بیلنس اور ڈے بک کسی بھی دن دیکھیں۔'),
    ('wa', 'g', 'واٹس ایپ پر بل', 'بل تصویر یا PDF کی صورت میں ایک ٹچ سے گاہک کو بھیجیں۔ کوٹیشن بھی واٹس ایپ پر۔'),
    ('printer', 'b', 'رسید اور A4 انوائس', '80mm تھرمل رسید یا فون کے ساتھ ٹائپ-C والا چھوٹا پرنٹر۔ لوگو کے ساتھ A4 انوائس بھی۔'),
    ('tag', 'y', 'سائز اور رنگ کے ویریئنٹس', 'سائز × رنگ یا شیڈ × سائز، تمام آئٹمز ایک ہی بار میں بنائیں، ہر ایک کا اپنا اسٹاک اور قیمت۔'),
    ('doc', 't', 'کوٹیشن سے فروخت', 'لوگو کے ساتھ A4 کوٹیشن بنائیں، واٹس ایپ کریں اور منظوری پر ایک ٹچ میں فروخت میں بدلیں۔'),
    ('users', 'n', 'عملہ اور کیش سیشن', 'ہر ملازم کا اپنا لاگ اِن اور اجازتیں۔ ہر شفٹ کا کیش الگ کھولیں اور بند کریں۔'),
    ('branch', 'g', 'ایک سے زیادہ برانچز', 'ہر برانچ کا اپنا اسٹاک اور قیمتیں۔ مالک ایک ہی اکاؤنٹ سے سب برانچز دیکھتا ہے۔'),
    ('lock', 'b', 'بیک اپ اور ڈیٹا کی حفاظت', 'ہر دکان کا ڈیٹا الگ اور محفوظ۔ بیک اپ اور ری اسٹور کی سہولت موجود ہے۔'),
]

PLUS = [  # Enterprise+ / Custom tools
    ('qr', 'FBR انوائس QR کوڈ کے ساتھ', 'انٹرپرائز اور کسٹم'),
    ('barcode', 'بارکوڈ لیبل پرنٹنگ', 'انٹرپرائز اور کسٹم'),
    ('cal', 'قسطوں پر فروخت (ضامن کے ساتھ)', 'انٹرپرائز اور کسٹم'),
    ('chart', 'منافع ڈیش بورڈ اور آڈٹ ٹریل', 'انٹرپرائز اور کسٹم'),
    ('star', 'اسٹاف کمیشن اور رپورٹ', 'انٹرپرائز اور کسٹم'),
    ('users', 'حاضری اور تنخواہیں', 'صرف کسٹم'),
]

PAINS = [
    ('ادھار بھول جاتا ہے', 'ہر ادھار فروخت گاہک کے کھاتے میں خود درج ہو جاتی ہے۔ ایک ٹچ میں دیکھیں کس نے کتنے پیسے دینے ہیں۔'),
    ('اسٹاک ختم یا ایکسپائر ہو جاتا ہے', 'کم اسٹاک، ختم اسٹاک اور قریب ایکسپائری والے آئٹمز کا پہلے سے الرٹ۔'),
    ('بجلی یا انٹرنیٹ چلا جاتا ہے', 'کیش بلنگ آف لائن چلتی رہتی ہے۔ انٹرنیٹ واپس آتے ہی سب کچھ خود سنک ہو جاتا ہے۔'),
    ('منافع کا صرف اندازہ ہوتا ہے', 'آج کی فروخت، خرچے اور اصل منافع ایک ہی اسکرین پر۔ کوئی حساب کتاب نہیں کرنا پڑتا۔'),
    ('رش میں بلنگ سست ہوتی ہے', 'بارکوڈ اسکین کریں یا پروڈکٹ پر ٹچ کریں۔ پیک یا پیس میں بیچیں اور سیکنڈوں میں بل پرنٹ کریں۔'),
    ('کیش پورا نہیں ملتا', 'ہر شفٹ کا کیش سیشن کھولیں اور بند کریں، اور دیکھیں ہر کیشیئر نے کتنا وصول کیا۔'),
]

STEPS = [
    ('سائن اپ کریں', 'live.uptrendpos.com پر اپنی دکان بنائیں اور اپنا کاروبار منتخب کریں۔'),
    ('پروڈکٹس شامل کریں', 'تیار کیٹلاگ سے تلاش کریں، ٹِک کریں اور شامل کریں، یا اپنی لسٹ ہمیں بھیج دیں۔'),
    ('بلنگ شروع کریں', 'بارکوڈ اسکینر اور رسید پرنٹر لگائیں اور پہلی فروخت کریں۔'),
    ('دکان پر نظر رکھیں', 'فروخت، اسٹاک، ادھار اور منافع اپنے فون پر کسی بھی وقت دیکھیں۔'),
]

PLANS = [
    ('Premium', 'پریمیم', 'ایک دکان کے لیے', '1,000', '12,000', '10,800', '1 برانچ', '3 یوزرز', False,
     'دکان چلانے کی ہر بنیادی چیز:', ['تیز بلنگ، ریٹرن اور ادھار', 'اسٹاک، پرچیز آرڈر اور GRN', 'ڈبل انٹری حسابات اور رپورٹس', 'آپ کے لوگو کے ساتھ بل', 'بیک اپ اور ری اسٹور']),
    ('Enterprise', 'انٹرپرائز', 'زیادہ تر دکانیں یہی لیتی ہیں', '2,000', '24,000', '21,600', '2 برانچز', '6 یوزرز', True,
     'پریمیم کی ہر چیز، اور:', ['FBR انوائس QR کوڈ کے ساتھ', 'بارکوڈ اور لیبل پرنٹنگ', 'گاہکوں کی قسطیں', 'منافع و نقصان ڈیش بورڈ', 'اسٹاف کمیشن اور رپورٹ', 'آڈٹ ٹریل اور سیکیورٹی الرٹس', 'بل پر UpTrendPos بیج کے بغیر']),
    ('Custom', 'کسٹم', 'بڑھتے ہوئے کاروبار کے لیے', '5,000', '60,000', '54,000', '3 برانچز', '9 یوزرز', False,
     'انٹرپرائز کی ہر چیز، اور:', ['اسٹاف کی حاضری', 'تنخواہیں اور پے رول', 'تمام ٹولز آن', 'مزید برانچز یا یوزرز کوٹیشن پر']),
]

FAQ = [
    ('UpTrendPos کیا ہے؟', 'UpTrendPos پاکستانی دکانوں کے لیے POS اور اکاؤنٹنگ سافٹ ویئر ہے۔ اس میں بلنگ، اسٹاک، ادھار کھاتہ، خریداری، حسابات اور FBR انوائس سب ایک ہی جگہ پر ہیں، اور یہ کمپیوٹر، موبائل اور ویب تینوں پر چلتا ہے۔'),
    ('کیا یہ انٹرنیٹ کے بغیر چلتا ہے؟', 'جی ہاں۔ ونڈوز اور اینڈرائیڈ ایپ انٹرنیٹ کے بغیر بھی کیش بلنگ کرتی رہتی ہیں اور انٹرنیٹ آتے ہی سب کچھ خود سنک ہو جاتا ہے۔ ادھار اور قسط کے لیے انٹرنیٹ ضروری ہے تاکہ ہر ڈیوائس پر ایک جیسا بیلنس نظر آئے۔ پہلی بار لاگ اِن کے لیے بھی انٹرنیٹ چاہیے۔'),
    ('کیا میں اسے موبائل پر چلا سکتا ہوں؟', 'جی ہاں۔ اینڈرائیڈ ایپ ڈاؤن لوڈ کریں یا کسی بھی براؤزر میں live.uptrendpos.com کھولیں۔ آئی فون پر سفاری میں ویب ایپ استعمال کریں۔ ایک ہی اکاؤنٹ سب ڈیوائسز پر چلتا ہے۔'),
    ('کیا اس میں FBR انوائس بنتی ہے؟', 'جی ہاں۔ FBR میں رجسٹرڈ دکان اپنی FBR POS آئی ڈی ایک بار درج کرے، پھر ہر بل پر FBR انوائس نمبر اور QR کوڈ آتا ہے۔ یہ سہولت انٹرپرائز اور کسٹم پلان میں ہے، اور ہر کاؤنٹر کی FBR تفصیل الگ رکھی جا سکتی ہے۔'),
    ('اس کی قیمت کتنی ہے؟', 'پریمیم Rs 1,000 ماہانہ، انٹرپرائز Rs 2,000 ماہانہ اور کسٹم Rs 5,000 ماہانہ ہے۔ سالانہ ادائیگی پر پہلے سال 10 فیصد رعایت ملتی ہے، اور ہر نئی دکان کو پہلے 7 دن کی مفت آزمائش ملتی ہے۔'),
    ('کیا میری دکان کے لیے پروڈکٹس پہلے سے موجود ہیں؟', 'جی ہاں۔ کئی کاروباروں کے لیے تیار کیٹلاگ موجود ہیں، جیسے فارمیسی کے لیے 17,000+ ادویات اور کریانہ کے لیے 7,000+ پروڈکٹس۔ آپ صرف اپنی چیزیں ٹِک کر کے شامل کریں اور اپنی قیمت اور اسٹاک لکھیں۔ کوئی بھی دکان UpTrendPos کے 38,000+ پروڈکٹس والے کیٹلاگ سے نام یا کیٹیگری کے ذریعے چیزیں شامل کر سکتی ہے۔'),
    ('کیا ایک سے زیادہ برانچز چلا سکتا ہوں؟', 'جی ہاں۔ ہر برانچ کا اپنا اسٹاک اور قیمتیں ہوتی ہیں اور مالک ایک ہی اکاؤنٹ سے سب دیکھتا ہے۔ پریمیم میں 1، انٹرپرائز میں 2 اور کسٹم میں 3 برانچز ہیں۔ مزید کے لیے ہم سے کوٹیشن لیں۔'),
    ('کیا میرا ڈیٹا محفوظ ہے؟', 'جی ہاں۔ ہر دکان کا ڈیٹا دوسری دکانوں سے بالکل الگ رہتا ہے اور صرف وہی عملہ دیکھ سکتا ہے جسے آپ اجازت دیں۔ بیک اپ اور ری اسٹور کی سہولت بھی موجود ہے۔'),
    ('کون سا پرنٹر اور اسکینر لوں؟', 'زیادہ تر دکانیں 80mm تھرمل رسید پرنٹر اور USB بارکوڈ اسکینر استعمال کرتی ہیں۔ چھوٹے کاؤنٹر پر فون کے ساتھ ٹائپ-C والا چھوٹا پرنٹر بھی چلتا ہے۔ خریدنے سے پہلے ہمیں واٹس ایپ کریں، ہم بتا دیں گے کیا بہتر رہے گا۔'),
    ('کیا آپ سیٹ اپ میں مدد کرتے ہیں؟', 'جی ہاں۔ ہماری ٹیم واٹس ایپ پر پروڈکٹس شامل کرنے، پرنٹر لگانے اور عملے کی تربیت میں مدد کرتی ہے۔ سپورٹ اردو اور انگریزی دونوں میں ہے۔'),
]

CUR = {'b': 'ur-c-b', 'g': 'ur-c-g', 'y': 'ur-c-y', 't': 'ur-c-t', 'n': 'ur-c-n'}

out = []
A = out.append
A('<div class="utp utp-ur" id="utp-urdu" lang="ur" dir="rtl" data-seo-title="اردو میں POS سافٹ ویئر | UpTrendPos پاکستان" '
  'data-seo-desc="UpTrendPos اردو میں: پاکستانی دکانوں کے لیے POS سافٹ ویئر۔ آف لائن بلنگ، ادھار کھاتہ، اسٹاک، حسابات اور FBR انوائس۔ 7 دن مفت آزمائیں۔" '
  'data-seo-kw="POS سافٹ ویئر, اردو POS سافٹ ویئر, UpTrendPos اردو, دکان کا سافٹ ویئر" data-seo-robots="index">')
A('<div class="ur-progress" aria-hidden="true"><span></span></div>')

# 1 HERO
A(f'''
  <section class="ur-hero" aria-labelledby="ur-h1">
    <div class="ur-blob b1" aria-hidden="true"></div><div class="ur-blob b2" aria-hidden="true"></div><div class="ur-blob b3" aria-hidden="true"></div>
    <div class="utp-wrap ur-hero-grid">
      <div class="ur-hero-copy">
        <p class="ur-kicker ur-up">{ic('globe')}<span>UpTrendPos اب اردو میں</span></p>
        <h1 id="ur-h1" class="ur-up">ہر دکان کا اپنا <span class="ur-latin">POS</span> <span class="ur-nw">سافٹ ویئر</span><span class="ur-hl">بلنگ سے منافع تک مکمل حساب</span></h1>
        <p class="ur-lead ur-up">UpTrendPos پاکستانی دکانداروں کے لیے بنایا گیا POS اور اکاؤنٹنگ سافٹ ویئر ہے۔ سیکنڈوں میں بل بنائیں، اسٹاک پر نظر رکھیں، ہر ادھار محفوظ رکھیں اور FBR انوائس پرنٹ کریں۔ کمپیوٹر، موبائل اور ویب پر، بجلی اور انٹرنیٹ نہ ہو تب بھی۔</p>
        <div class="ur-cta ur-up">
          <a class="utp-btn utp-btn-primary ur-btn" href="{LIVE}" target="_blank" rel="noopener" data-track="ur_hero_trial">{ic('star')}<span>7 دن مفت آزمائیں</span></a>
          {wa_link('Assalam o Alaikum, mujhe UpTrendPos ka free demo chahiye', 'واٹس ایپ پر فری ڈیمو', 'ur_hero_whatsapp')}
        </div>
        <ul class="ur-ticks ur-up">
          <li>{ic('check')}انٹرنیٹ کے بغیر بھی بلنگ</li>
          <li>{ic('check')}FBR انوائس QR کوڈ کے ساتھ</li>
          <li>{ic('check')}کمپیوٹر، موبائل اور ویب</li>
        </ul>
      </div>
      <figure class="ur-hero-art ur-up">
        <div class="ur-orbit" aria-hidden="true"><span></span><span></span><span></span></div>
        <img src="{IMG}uptrendpos-ur-overview.webp" width="1080" height="1080" fetchpriority="high" decoding="async" alt="UpTrendPos اردو: ہر دکان کا اپنا POS سافٹ ویئر، انٹرنیٹ کے بغیر بلنگ، ادھار، اسٹاک اور منافع کا درست حساب">
        <div class="ur-float f1">{ic('offline')}<span>آف لائن بلنگ</span></div>
        <div class="ur-float f2">{ic('ledger')}<span>ادھار کھاتہ</span></div>
        <div class="ur-float f3">{ic('qr')}<span>FBR انوائس</span></div>
      </figure>
    </div>
    <a class="ur-scroll" href="#ur-stats" aria-label="نیچے دیکھیں"><span></span></a>
  </section>''')

# 2 STATS (animated counters)
A(f'''
  <section class="ur-stats" id="ur-stats" aria-label="UpTrendPos ایک نظر میں">
    <div class="utp-wrap">
      <ul class="ur-stat-grid">
        <li class="ur-rv"><strong><span class="ur-latin"><span data-count="38000">38,000</span>+</span></strong><span>تیار پروڈکٹس کیٹلاگ میں</span></li>
        <li class="ur-rv"><strong><span class="ur-latin"><span data-count="30">30</span>+</span></strong><span>کاروباروں کے لیے تیار سیٹ اپ</span></li>
        <li class="ur-rv"><strong><span class="ur-latin"><span data-count="17000">17,000</span>+</span></strong><span>ادویات فارمیسی کے لیے</span></li>
        <li class="ur-rv"><strong><span class="ur-latin"><span data-count="7">7</span></span> دن</strong><span>مفت آزمائش، ہر نئی دکان کے لیے</span></li>
      </ul>
    </div>
  </section>''')

# 3 WHAT IS
A(f'''
  <section class="ur-sec" aria-labelledby="ur-what">
    <div class="utp-wrap ur-what">
      <div class="ur-head ur-rv">
        <span class="ur-eyebrow">تعارف</span>
        <h2 id="ur-what">UpTrendPos کیا ہے؟</h2>
        <p>یہ صرف بلنگ ایپ نہیں، پوری دکان کا نظام ہے۔ بلنگ سے شروع کریں، پھر جب چاہیں اسٹاک، ادھار، خریداری اور حسابات بھی اسی میں چلائیں۔ ہر چیز آپس میں جڑی ہے، اس لیے کوئی بھی چیز دو بار درج نہیں کرنی پڑتی۔</p>
      </div>
      <div class="ur-quad">
        <article class="ur-qcard ur-rv"><span class="ur-ico ur-c-b">{ic('offline')}</span><h3>انٹرنیٹ کے بغیر بھی بلنگ</h3><p>لوڈشیڈنگ ہو یا کمزور سگنل، کاؤنٹر نہیں رکتا۔</p></article>
        <article class="ur-qcard ur-rv"><span class="ur-ico ur-c-g">{ic('ledger')}</span><h3>ادھار، اسٹاک اور منافع کا درست حساب</h3><p>ہر فروخت کے ساتھ سب کچھ خود اپڈیٹ۔</p></article>
        <article class="ur-qcard ur-rv"><span class="ur-ico ur-c-y">{ic('box')}</span><h3><span class="ur-latin">38,000+</span> پروڈکٹس پہلے سے شامل</h3><p>تلاش کریں، ٹِک کریں اور اپنی دکان میں شامل کریں۔</p></article>
        <article class="ur-qcard ur-rv"><span class="ur-ico ur-c-t">{ic('monitor')}</span><h3>موبائل، کمپیوٹر اور ویب پر دستیاب</h3><p>ایک اکاؤنٹ، ہر ڈیوائس پر ایک جیسا ڈیٹا۔</p></article>
      </div>
    </div>
  </section>''')

# 4 PAINS -> FIX
cards = ''.join(f'<li class="ur-pain ur-rv"><span class="ur-tag">مسئلہ</span><h3>{E(p)}</h3><p class="ur-fix">{ic("check")}<span>{E(f)}</span></p></li>' for p, f in PAINS)
A(f'''
  <section class="ur-sec ur-alt" aria-labelledby="ur-pain">
    <div class="utp-wrap">
      <div class="ur-head ur-rv">
        <span class="ur-eyebrow">رجسٹر سے سافٹ ویئر تک</span>
        <h2 id="ur-pain">کیا آپ کی دکان اب بھی رجسٹر پر چل رہی ہے؟</h2>
        <p>چھوٹی چھوٹی غلطیاں روز دکاندار کا پیسہ کھا جاتی ہیں۔ UpTrendPos پہلے یہی مسئلے حل کرتا ہے۔</p>
      </div>
      <ul class="ur-pains">{cards}</ul>
    </div>
  </section>''')

# 5 BUSINESS GROUPS
names = []
for gi, (img, title, sub, col, items) in enumerate(GROUPS):
    for s, n, _ in items:
        names.append((s, n))
lis = ''.join(f'<li><a href="{SITE}/industries/{s}/" data-page="{s}">{E(n)}</a></li>' for s, n in names)
A(f'''
  <section class="ur-sec" id="ur-business" aria-labelledby="ur-biz">
    <div class="utp-wrap">
      <div class="ur-head ur-rv">
        <span class="ur-eyebrow">کاروبار</span>
        <h2 id="ur-biz"><span class="ur-latin">30+</span> قسم کی دکانوں کے لیے تیار سیٹ اپ</h2>
        <p>سائن اپ کرتے وقت اپنا کاروبار منتخب کریں۔ UpTrendPos آپ کی دکان کے حساب سے فیلڈز، یونٹس اور رپورٹس کے ساتھ کھلتا ہے، اس لیے آپ کو صفر سے شروع نہیں کرنا پڑتا۔</p>
      </div>
    </div>
    <div class="utp-marquee ur-names" dir="ltr" aria-hidden="true"><ul class="utp-mq-track">{''.join(f'<li dir="rtl">{E(n)}</li>' for _, n in names)}</ul></div>
    <div class="utp-wrap">''')
for gi, (img, title, sub, col, items) in enumerate(GROUPS):
    rows = ''.join(
        f'<li class="ur-biz-row"><span class="ur-dot {CUR[col]}">{ic("check")}</span><a href="{SITE}/industries/{s}/" data-page="{s}">{E(n)}</a><span class="ur-chip">{E(c)}</span></li>'
        for s, n, c in items)
    A(f'''
      <article class="ur-group {'flip' if gi % 2 else ''}">
        <figure class="ur-group-img ur-rv"><img src="{IMG}uptrendpos-ur-{img}.webp" width="1080" height="1080" loading="lazy" decoding="async" alt="{E(title)} UpTrendPos POS سافٹ ویئر"></figure>
        <div class="ur-group-body ur-rv">
          <span class="ur-num ur-latin">{gi + 1:02d}</span>
          <h3>{E(title)}</h3>
          <p>{E(sub)}</p>
          <ul class="ur-biz-list">{rows}</ul>
        </div>
      </article>''')
A('''
      <p class="ur-note ur-rv">ہر کاروبار کا مکمل صفحہ انگریزی میں موجود ہے۔ کسی بھی نام پر کلک کر کے تفصیل دیکھیں۔</p>
    </div>
  </section>''')

# 6 FEATURES
fc = ''.join(f'<article class="ur-fcard ur-rv"><span class="ur-ico {CUR[c]}">{ic(i)}</span><h3>{E(t)}</h3><p>{E(d)}</p></article>' for i, c, t, d in FEATURES)
pc = ''.join(f'<li class="ur-rv">{ic(i)}<span>{E(t)}</span><em>{E(p)}</em></li>' for i, t, p in PLUS)
A(f'''
  <section class="ur-sec ur-alt" id="ur-features" aria-labelledby="ur-feat">
    <div class="utp-wrap">
      <div class="ur-head ur-rv">
        <span class="ur-eyebrow">فیچرز</span>
        <h2 id="ur-feat">دکان کی ہر ضرورت ایک ہی ایپ میں</h2>
        <p>یہ سب سہولتیں ہر کاروبار اور ہر پلان میں شامل ہیں۔</p>
      </div>
      <div class="ur-fgrid">{fc}</div>
      <div class="ur-plus">
        <h3 class="ur-rv">بڑی دکانوں کے لیے مزید ٹولز</h3>
        <ul>{pc}</ul>
      </div>
    </div>
  </section>''')

# 7 OFFLINE + DEVICES
A(f'''
  <section class="ur-sec ur-dark" aria-labelledby="ur-off">
    <div class="utp-wrap ur-off">
      <div class="ur-off-copy ur-rv">
        <span class="ur-eyebrow">آف لائن فرسٹ</span>
        <h2 id="ur-off">لوڈشیڈنگ ہو یا انٹرنیٹ بند، بلنگ چلتی رہے گی</h2>
        <p>ہر فروخت پہلے آپ کی ڈیوائس پر محفوظ ہوتی ہے، پھر انٹرنیٹ آتے ہی آپ کے اکاؤنٹ میں سنک ہو جاتی ہے۔ نہ کچھ ضائع ہوتا ہے، نہ کچھ دو بار درج ہوتا ہے۔</p>
        <p class="ur-small">کیش بل آف لائن چلتے ہیں۔ ادھار اور قسط کے لیے انٹرنیٹ چاہیے تاکہ ہر ڈیوائس پر ایک جیسا بیلنس دکھے۔</p>
      </div>
      <div class="ur-sync ur-rv" aria-hidden="true">
        <div class="ur-node">{ic('monitor')}<b>دکان کا کاؤنٹر</b><span>انٹرنیٹ کے بغیر بل</span></div>
        <div class="ur-line"><i></i></div>
        <div class="ur-node cloud">{ic('cloud')}<b>آپ کا اکاؤنٹ</b><span>محفوظ آن لائن بیک اپ</span></div>
        <div class="ur-line"><i></i></div>
        <div class="ur-node">{ic('mobile')}<b>آپ کا فون</b><span>کہیں سے بھی فروخت دیکھیں</span></div>
      </div>
    </div>
    <div class="utp-wrap">
      <ul class="ur-devices">
        <li class="ur-rv">{ic('monitor')}<b>ونڈوز ایپ</b><span>کاؤنٹر کے کمپیوٹر کے لیے، بارکوڈ اسکینر اور رسید پرنٹر کے ساتھ</span></li>
        <li class="ur-rv">{ic('mobile')}<b>اینڈرائیڈ ایپ</b><span>فون سے بلنگ یا فروخت چیک کرنے کے لیے</span></li>
        <li class="ur-rv">{ic('globe')}<b>ویب ایپ</b><span><span class="ur-latin">live.uptrendpos.com</span> کسی بھی لیپ ٹاپ، میک یا آئی فون پر</span></li>
      </ul>
    </div>
  </section>''')

# 8 STEPS
st = ''.join(f'<li class="ur-step ur-rv"><span class="ur-step-n ur-latin">{i + 1}</span><h3>{E(t)}</h3><p>{E(d)}</p></li>' for i, (t, d) in enumerate(STEPS))
A(f'''
  <section class="ur-sec" aria-labelledby="ur-steps">
    <div class="utp-wrap">
      <div class="ur-head ur-rv">
        <span class="ur-eyebrow">آسان آغاز</span>
        <h2 id="ur-steps">صرف 4 آسان مراحل میں فروخت شروع کریں</h2>
        <p>کسی کمپیوٹر ماہر کی ضرورت نہیں۔ زیادہ تر دکانیں اسی دن پہلی فروخت کر لیتی ہیں۔</p>
      </div>
      <ol class="ur-steps">{st}</ol>
    </div>
  </section>''')

# 9 PLANS
pl = ''
for en, ur, tag, m, y, fy, br, us, rec, intro, feats in PLANS:
    fl = ''.join(f'<li>{ic("check")}<span>{E(f)}</span></li>' for f in feats)
    pl += f'''<article class="ur-plan ur-rv{' rec' if rec else ''}">{'<span class="ur-rec">تجویز کردہ</span>' if rec else ''}
          <h3>{ur} <small class="ur-latin">{en}</small></h3><p class="ur-ptag">{tag}</p>
          <p class="ur-price"><span class="ur-latin">Rs <b>{m}</b></span> ماہانہ</p>
          <p class="ur-year">یا <span class="ur-latin">Rs {y}</span> سالانہ · پہلا سال <span class="ur-latin">Rs {fy}</span> (<span class="ur-latin">10%</span> رعایت)</p>
          <p class="ur-limits"><span>{ic('branch')}{br}</span><span>{ic('users')}{us}</span></p>
          <p class="ur-intro">{E(intro)}</p><ul>{fl}</ul></article>'''
A(f'''
  <section class="ur-sec ur-alt" id="ur-plans" aria-labelledby="ur-plan">
    <div class="utp-wrap">
      <div class="ur-head ur-rv">
        <span class="ur-eyebrow">قیمتیں</span>
        <h2 id="ur-plan">آسان پلان، واضح قیمتیں</h2>
        <p>ماہانہ یا سالانہ ادائیگی کریں۔ سالانہ ادائیگی پر پہلے سال 10 فیصد رعایت۔ ہر پلان میں لامحدود بل، مفت اپڈیٹس اور واٹس ایپ سپورٹ۔</p>
      </div>
      <div class="ur-plans">{pl}</div>
      <p class="ur-note ur-rv">پہلے 7 دن مفت آزمائیں، پھر اپنی دکان کے حساب سے پلان چنیں۔ <a href="{SITE}/pos-software-pricing/" data-track="ur_pricing">مکمل قیمتیں اور موازنہ</a></p>
    </div>
  </section>''')

# 10 FAQ
fq = ''.join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in FAQ)
A(f'''
  <section class="ur-sec" aria-labelledby="ur-faq">
    <div class="utp-wrap">
      <div class="ur-head ur-rv">
        <span class="ur-eyebrow">سوال و جواب</span>
        <h2 id="ur-faq">اکثر پوچھے جانے والے سوالات</h2>
      </div>
      <div class="utp-faq-list ur-faq">{fq}</div>
    </div>
  </section>''')

# 11 FINAL / CONTACT
A(f'''
  <section class="ur-final" aria-labelledby="ur-final">
    <div class="ur-blob b1" aria-hidden="true"></div><div class="ur-blob b2" aria-hidden="true"></div>
    <div class="utp-wrap ur-final-grid">
      <div class="ur-final-copy ur-rv">
        <h2 id="ur-final">آج ہی رابطہ کریں، فری لائیو ڈیمو حاصل کریں</h2>
        <p>اپنی دکان کا کاروبار بتائیں، ہم آپ کو دکھائیں گے کہ UpTrendPos آپ کی دکان پر کیسے کام کرتا ہے۔ سیٹ اپ میں مدد اردو میں۔</p>
        <div class="ur-cta">
          {wa_link('Assalam o Alaikum, mujhe UpTrendPos ka free demo chahiye', 'واٹس ایپ کریں', 'ur_final_whatsapp', 'utp-btn utp-btn-primary ur-btn')}
          <a class="utp-btn utp-btn-ghost ur-btn" href="{LIVE}" target="_blank" rel="noopener" data-track="ur_final_trial">{ic('star')}<span>7 دن مفت آزمائیں</span></a>
        </div>
        <ul class="ur-contact">
          <li>{ic('phone')}<a class="ur-latin" href="tel:+923192223292" data-track="ur_call">0319 2223292</a></li>
          <li>{ic('globe')}<a class="ur-latin" href="{SITE}/" data-track="ur_home">uptrendpos.com</a></li>
          <li>{ic('monitor')}<a class="ur-latin" href="{LIVE}" target="_blank" rel="noopener" data-track="ur_live">live.uptrendpos.com</a></li>
          <li>{ic('pin')}<span>ہاؤس نمبر 193/A، عمر بلاک، شاداب ٹاؤن، ساہیوال</span></li>
        </ul>
      </div>
      <figure class="ur-final-img ur-rv"><img src="{IMG}uptrendpos-ur-contact.webp" width="1080" height="1080" loading="lazy" decoding="async" alt="UpTrendPos سے رابطہ: کال یا واٹس ایپ 0319 2223292، ویب سائٹ اور لائیو ڈیمو"></figure>
    </div>
  </section>
</div>''')

page = '\n'.join(out)
bad = re.findall(r'<script|<style|<!--|<iframe|<form|javascript:|\son[a-z]+\s*=', page, re.I)
assert not bad, bad
open('pos-software-urdu.html', 'w').write(page)
print(len(page), 'chars')
