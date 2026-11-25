# Builds the Urdu copy of the UpTrendPos Home page (/ur/) from the live English Home page code.
# Same sections, same classes, same links; only the words change. RTL, Jameel Noori Nastaleeq.
# Run: python3 build_ur_home.py home_live.html ur.html
import re, sys, json, html as H

src, out = sys.argv[1], sys.argv[2]
h = open(src, encoding='utf-8').read().replace('\r\n', '\n')

# ---- root wrapper ----
h = re.sub(r'<div class="utp utp-home" id="utp-home"[^>]*>',
           '<div class="utp utp-home utp-urdu" id="utp-home-ur" lang="ur" dir="rtl" '
           'data-seo-title="پاکستان میں POS سافٹ ویئر: آسان اور FBR ریڈی | UpTrendPos" '
           'data-seo-desc="UpTrendPos ہر دکان کے لیے آسان POS سافٹ ویئر ہے: تیز بلنگ، اسٹاک، ادھار کھاتہ اور FBR انوائس۔ کمپیوٹر، موبائل اور ویب پر، انٹرنیٹ کے بغیر بھی۔" '
           'data-seo-kw="POS سافٹ ویئر, پاکستان میں POS سافٹ ویئر, بلنگ سافٹ ویئر, ادھار کھاتہ ایپ" data-seo-robots="index">', h, count=1)

# ---- hero stage: Urdu items (problem, icon, colour, fix title, fix line, short label) ----
stage = [
    ['ہزاروں پروڈکٹس ہاتھ سے لکھنا', 'pill', 'b', 'تیار کیٹلاگ، ایک کلک', '17,000+ ادویات، 5,500+ بیوٹی، 1,100+ الیکٹرونکس', 'تیار کیٹلاگ'],
    ['چھوٹے کاؤنٹر پر پرنٹر نہیں', 'printer', 'g', 'فون سے پرنٹ کریں', 'USB Type-C کیبل سے تھرمل پرنٹر', 'فون سے پرنٹ'],
    ['کاغذی بل گم ہو جاتے ہیں', 'wa', 'y', 'واٹس ایپ انوائس', 'آپ کے دستخط اور انوائس اسٹائل کے ساتھ', 'واٹس ایپ بل'],
    ['بجلی یا انٹرنیٹ چلا جاتا ہے', 'offline', 'b', 'بلنگ آف لائن چلتی رہتی ہے', 'ڈیوائس پر محفوظ، بعد میں سنک', 'آف لائن'],
    ['قسطیں ڈائری میں لکھی جاتی ہیں', 'cal', 'g', 'رسید کے ساتھ قسطیں', 'ہر ادائیگی کی رسید، آخر میں سرٹیفکیٹ', 'قسط کی رسید'],
    ['عملہ پوچھے بغیر اسٹاک بدل دیتا ہے', 'shield', 'y', 'مینیجر PIN سے منظوری', 'اسٹاک واپس کرنے کے لیے مینیجر PIN', 'مینیجر PIN'],
]
LRI, PDI = '⁦', '⁩'
RUN = re.compile(r'(?<![A-Za-z0-9.@])(?:Rs\s)?[A-Za-z0-9][A-Za-z0-9.,+%:/@-]*(?:\s[A-Za-z0-9][A-Za-z0-9.,+%:/@-]*)*')
def iso(t):
    # isolate Latin/number runs that hold a digit or symbol so "17,000+" or "Tier-1" never flip in RTL text
    return RUN.sub(lambda m: LRI + m.group(0) + PDI if re.search(r'[0-9+%-]', m.group(0)) else m.group(0), t)
stage = [[x if i in (1, 2) else iso(x) for i, x in enumerate(r)] for r in stage]
h = re.sub(r'<div class="utp-stage" data-stage="home"[^>]*></div>',
           '<div class="utp-stage" data-stage="home-ur" data-stage-items="' + H.escape(json.dumps(stage, ensure_ascii=False)) + '" role="img" '
           'aria-label="اینیمیٹڈ خاکہ: درمیان میں UpTrendPos اور اس کے گرد اس کے ٹولز۔ تیار کیٹلاگ، فون سے پرنٹ، واٹس ایپ انوائس، آف لائن بلنگ، رسید کے ساتھ قسطیں اور مینیجر PIN۔"></div>', h, count=1)

T = [
    # hero
    ('Made for Pakistani shops', 'پاکستانی دکانوں کے لیے بنایا گیا'),
    ('Easy POS software in Pakistan for <span class="utp-hl">every shop.</span>', 'ہر دکان کے لیے آسان <span class="utp-hl">POS سافٹ ویئر</span>'),
    ('UpTrendPos is POS software in Pakistan for every counter. Make bills in seconds, control your stock, keep every udhaar safe and print FBR invoices on your computer, phone and the web, even when the internet is off.',
     'UpTrendPos پاکستان کی ہر دکان کے کاؤنٹر کے لیے POS سافٹ ویئر ہے۔ سیکنڈوں میں بل بنائیں، اسٹاک قابو میں رکھیں، ہر ادھار محفوظ رکھیں اور کمپیوٹر، موبائل اور ویب پر FBR انوائس پرنٹ کریں، انٹرنیٹ بند ہو تب بھی۔'),
    ('Start 7-day free trial', '7 دن مفت آزمائیں'),
    ('Free demo on WhatsApp', 'واٹس ایپ پر مفت ڈیمو'),
    ('7-day free trial · Setup help on WhatsApp', '7 دن مفت آزمائش · واٹس ایپ پر سیٹ اپ میں مدد'),
    ('Works without internet', 'انٹرنیٹ کے بغیر چلتا ہے'),
    ('FBR invoice with QR code', 'QR کوڈ کے ساتھ FBR انوائس'),
    ('Windows, Android &amp; Web', 'ونڈوز، اینڈرائیڈ اور ویب'),
    # customers
    ('Our customers', 'ہمارے کسٹمر'),
    ('Businesses that trust <span class="utp-hl">UpTrendPos</span>', 'کاروبار جو <span class="utp-hl">UpTrendPos</span> پر بھروسہ کرتے ہیں'),
    ('Real shops already run their daily billing, stock and udhaar on UpTrendPos, POS software in Pakistan made for local counters.',
     'اصل دکانیں اپنی روزانہ کی بلنگ، اسٹاک اور ادھار UpTrendPos پر چلا رہی ہیں، جو مقامی کاؤنٹرز کے لیے بنا پاکستانی POS سافٹ ویئر ہے۔'),
    ('UpTrendPos customer logo', 'UpTrendPos کسٹمر کا لوگو'),
    ('Hamza Pharmacy logo, an UpTrendPos customer', 'حمزہ فارمیسی کا لوگو، UpTrendPos کسٹمر'),
    # industries
    ('>Industries<', '>کاروبار<'),
    ('POS software in Pakistan for 30+ types of shops', '30+ قسم کی دکانوں کے لیے POS سافٹ ویئر'),
    ('Pick your business type when you sign up. UpTrendPos opens with the right fields, units and reports for your shop, so you do not start from zero.',
     'سائن اپ کرتے وقت اپنا کاروبار منتخب کریں۔ UpTrendPos آپ کی دکان کے حساب سے فیلڈز، یونٹس اور رپورٹس کے ساتھ کھلتا ہے، اس لیے صفر سے شروع نہیں کرنا پڑتا۔'),
    ('>Daily needs<', '>روزمرہ کی ضروریات<'),
    ('>Grocery &amp; Kiryana Store<', '>کریانہ اسٹور اور مارٹ<'),
    ('>Poultry, Meat &amp; Seafood<', '>پولٹری، گوشت اور سی فوڈ<'),
    ('>Crockery &amp; Household Shop<', '>کراکری اور گھریلو سامان<'),
    ('>Vape &amp; Pan Shop<', '>ویپ اور پان شاپ<'),
    ('>Health and beauty<', '>صحت اور خوبصورتی<'),
    ('>Pharmacy &amp; Medical Store<', '>فارمیسی اور میڈیکل اسٹور<'),
    ('>Cosmetics &amp; Beauty Store<', '>کاسمیٹکس اور بیوٹی اسٹور<'),
    ('>Baby &amp; Diaper Store<', '>بے بی شاپ اور ڈائپر اسٹور<'),
    ('>Perfume &amp; Attar Shop<', '>پرفیوم اور عطر شاپ<'),
    ('>Fashion and accessories<', '>فیشن اور ایکسیسریز<'),
    ('>Clothing &amp; Garments<', '>کپڑے اور گارمنٹس<'),
    ('>Shoes &amp; Footwear<', '>جوتوں کی دکان<'),
    ('>Tailoring &amp; Boutique<', '>ٹیلر شاپ اور بوتیک<'),
    ('>Undergarments &amp; Hosiery<', '>انڈر گارمنٹس اور ہوزری<'),
    ('>Bags &amp; Luggage<', '>بیگز اور سوٹ کیس<'),
    ('>Watch Shop<', '>گھڑیوں کی دکان<'),
    ('>Jewellery &amp; Gold Shop<', '>جیولری اور گولڈ شاپ<'),
    ('>Artificial Jewellery Shop<', '>آرٹیفیشل جیولری شاپ<'),
    ('>Electronics and electrical<', '>الیکٹرونکس اور الیکٹریکل<'),
    ('>Electronics, Appliances &amp; CCTV<', '>الیکٹرونکس، ہوم اپلائنسز اور CCTV<'),
    ('>Solar Shop<', '>سولر شاپ<'),
    ('>Electrical &amp; LED Lighting<', '>الیکٹریکل اور LED لائٹس<'),
    ('>Mobile &amp; Computer Shop<', '>موبائل، کمپیوٹر اور پرنٹر شاپ<'),
    ('>Mobile, Computer &amp; Printer Shop<', '>موبائل، کمپیوٹر اور پرنٹر شاپ<'),
    ('>Battery Shop<', '>بیٹری شاپ<'),
    ('>Hardware, auto and home<', '>ہارڈویئر، آٹو اور گھر<'),
    ('>Hardware, Sanitary &amp; Building Material<', '>ہارڈویئر، سینیٹری اور بلڈنگ میٹریل<'),
    ('>Paint Store<', '>پینٹ اسٹور<'),
    ('>Glass &amp; Aluminium Shop<', '>گلاس اور ایلومینیم شاپ<'),
    ('>Furniture Shop<', '>فرنیچر شاپ<'),
    ('>Auto Spare Parts<', '>آٹو اسپیئر پارٹس<'),
    ('>Tyre Shop<', '>ٹائر شاپ<'),
    ('>Vehicle Showroom (Bikes, Cars &amp; EVs)<', '>وہیکل شوروم (بائیک، کار اور EV)<'),
    ('>Gifts, stationery and sports<', '>گفٹ، اسٹیشنری اور اسپورٹس<'),
    ('>Toys &amp; Gift Shop<', '>کھلونے اور گفٹ شاپ<'),
    ('>Sports Goods<', '>اسپورٹس کا سامان<'),
    ('>Stationery &amp; Book Shop<', '>اسٹیشنری اور بک شاپ<'),
    ('>Agri and veterinary<', '>زرعی اور ویٹرنری<'),
    ('>Agri Inputs (Seed, Fertilizer &amp; Pesticides)<', '>بیج، کھاد اور زرعی ادویات<'),
    ('>Veterinary Store<', '>ویٹرنری میڈیکل اسٹور<'),
    ('<strong>Running a pharmacy?</strong> Start with 17,000+ medicines already loaded. Just add your stock and start selling. Any shop can also add products from the full UpTrendPos catalog of 38,000+ products, by name or category.',
     '<strong>فارمیسی چلاتے ہیں؟</strong> 17,000+ ادویات پہلے سے موجود ہیں۔ بس اپنا اسٹاک لکھیں اور فروخت شروع کریں۔ کوئی بھی دکان UpTrendPos کے 38,000+ پروڈکٹس والے کیٹلاگ سے نام یا کیٹیگری کے ذریعے پروڈکٹس شامل کر سکتی ہے۔'),
    ('Get a pharmacy demo', 'فارمیسی کا ڈیمو لیں'),
    ('See all business types', 'تمام کاروبار دیکھیں'),
    # pains
    ('Why UpTrendPos', 'UpTrendPos کیوں'),
    ('Is your shop still running on a register?', 'کیا آپ کی دکان اب بھی رجسٹر پر چل رہی ہے؟'),
    ('Small mistakes cost shop owners money every day. Good POS software in Pakistan should fix these problems first. UpTrendPos does.',
     'چھوٹی چھوٹی غلطیاں روز دکاندار کا پیسہ کھا جاتی ہیں۔ اچھا POS سافٹ ویئر سب سے پہلے یہی مسئلے حل کرے۔ UpTrendPos یہی کرتا ہے۔'),
    ('>The problem<', '>مسئلہ<'),
    ('Udhaar gets forgotten', 'ادھار بھول جاتا ہے'),
    ("Every credit sale goes into the customer's khata on its own. See who owes you money in one tap.", 'ہر ادھار فروخت گاہک کے کھاتے میں خود درج ہوتی ہے۔ ایک ٹچ میں دیکھیں کس نے کتنا دینا ہے۔'),
    ('Stock runs out or expires', 'اسٹاک ختم یا ایکسپائر ہو جاتا ہے'),
    ('Get alerts for low stock, out of stock and items close to their expiry date.', 'کم اسٹاک، ختم اسٹاک اور قریب ایکسپائری والے آئٹمز کا پہلے سے الرٹ۔'),
    ('Light or internet goes off', 'بجلی یا انٹرنیٹ چلا جاتا ہے'),
    ('Billing keeps running offline. Your sales sync on their own when the internet is back.', 'بلنگ آف لائن چلتی رہتی ہے۔ انٹرنیٹ واپس آتے ہی فروخت خود سنک ہو جاتی ہے۔'),
    ('Profit is just a guess', 'منافع صرف اندازہ ہوتا ہے'),
    ("See today's sales, expenses and real profit on one screen. No maths needed.", 'آج کی فروخت، خرچے اور اصل منافع ایک ہی اسکرین پر۔ کوئی حساب کتاب نہیں۔'),
    ('Billing is slow at rush hour', 'رش میں بلنگ سست ہوتی ہے'),
    ('Scan a barcode or tap a product. Sell by pack or by piece and print the bill in seconds.', 'بارکوڈ اسکین کریں یا پروڈکٹ پر ٹچ کریں۔ پیک یا پیس میں بیچیں اور سیکنڈوں میں بل پرنٹ کریں۔'),
    ('Cash does not match', 'کیش پورا نہیں ملتا'),
    ('Open and close a cash session for each shift and see what every cashier collected.', 'ہر شفٹ کا کیش سیشن کھولیں اور بند کریں، اور دیکھیں ہر کیشیئر نے کتنا وصول کیا۔'),
    ('Supplier bills get mixed up', 'سپلائر کے بل آپس میں مل جاتے ہیں'),
    ('Purchase orders, stock received and supplier payments stay together in one ledger.', 'پرچیز آرڈر، آنے والا مال اور سپلائر کی ادائیگیاں ایک ہی کھاتے میں۔'),
    ('FBR rules feel hard', 'FBR کے اصول مشکل لگتے ہیں'),
    ('Add your FBR POS ID once. Bills then print the FBR invoice number and QR code.', 'اپنی FBR POS آئی ڈی ایک بار لکھیں۔ پھر ہر بل پر FBR انوائس نمبر اور QR کوڈ پرنٹ ہوتا ہے۔'),
    ('Stuck on one computer', 'صرف ایک کمپیوٹر تک محدود'),
    ('Use the same account on Windows, Android and the web. Check sales from your phone, anywhere.', 'ایک ہی اکاؤنٹ ونڈوز، اینڈرائیڈ اور ویب پر چلائیں۔ کہیں سے بھی فون پر فروخت دیکھیں۔'),
    ('Two branches, two registers', 'دو برانچیں، دو رجسٹر'),
    ('Each branch keeps its own stock and prices. The owner sees every branch from one account.', 'ہر برانچ کا اپنا اسٹاک اور قیمتیں۔ مالک ایک ہی اکاؤنٹ سے سب برانچیں دیکھتا ہے۔'),
    ('Software does not fit your shop', 'سافٹ ویئر آپ کی دکان کے مطابق نہیں'),
    ('Pick from 30+ business types. Your shop opens with the right fields, units and reports.', '30+ کاروباروں میں سے اپنا چنیں۔ دکان صحیح فیلڈز، یونٹس اور رپورٹس کے ساتھ کھلتی ہے۔'),
    ('Paying again for every update', 'ہر اپڈیٹ پر دوبارہ پیسے'),
    ('New features and fixes come to every plan at no extra cost.', 'نئے فیچرز اور درستیاں ہر پلان میں بغیر اضافی خرچ کے۔'),
    # features
    ('>Features<', '>فیچرز<'),
    ('All the tools your shop needs in one app', 'دکان کے تمام ٹولز ایک ہی ایپ میں'),
    ('UpTrendPos is complete POS software in Pakistan, not just a billing app. Start with billing, then add stock, udhaar, purchases and accounts when you are ready. Everything is connected, so you enter each thing only once.',
     'UpTrendPos صرف بلنگ ایپ نہیں، مکمل POS سافٹ ویئر ہے۔ بلنگ سے شروع کریں، پھر جب چاہیں اسٹاک، ادھار، خریداری اور حسابات بھی شامل کریں۔ ہر چیز آپس میں جڑی ہے، اس لیے کوئی چیز دو بار نہیں لکھنی پڑتی۔'),
    ('>Fast billing<', '>تیز بلنگ<'),
    ('Scan barcodes, sell by pack or by piece, and print a thermal receipt in seconds.', 'بارکوڈ اسکین کریں، پیک یا پیس میں بیچیں اور سیکنڈوں میں تھرمل رسید پرنٹ کریں۔'),
    ('>Stock control<', '>اسٹاک کنٹرول<'),
    ('Know what is in stock at every branch. Get low-stock and expiry alerts before it is too late.', 'ہر برانچ کا اسٹاک معلوم رکھیں۔ دیر ہونے سے پہلے کم اسٹاک اور ایکسپائری کے الرٹ پائیں۔'),
    ('>Udhaar khata<', '>ادھار کھاتہ<'),
    ('Credit sales go to the customer ledger. Take payments and share a clear statement.', 'ادھار فروخت گاہک کے کھاتے میں جاتی ہے۔ وصولی درج کریں اور صاف اسٹیٹمنٹ بھیجیں۔'),
    ('>Purchases and suppliers<', '>خریداری اور سپلائرز<'),
    ('Make purchase orders, receive stock and see how much you owe each supplier.', 'پرچیز آرڈر بنائیں، مال وصول کریں اور دیکھیں ہر سپلائر کا کتنا دینا ہے۔'),
    ('>Accounts and profit<', '>حسابات اور منافع<'),
    ('Every sale and expense goes into your accounts on its own. Check profit and loss any day.', 'ہر فروخت اور خرچ خود حساب میں جاتا ہے۔ کسی بھی دن نفع و نقصان دیکھیں۔'),
    ('>More than one branch<', '>ایک سے زیادہ برانچیں<'),
    ('Each branch keeps its own stock and prices. You see all branches from one owner account.', 'ہر برانچ کا اپنا اسٹاک اور قیمتیں۔ مالک کے ایک اکاؤنٹ سے سب برانچیں نظر آتی ہیں۔'),
    ('>Installments (qist)<', '>قسطیں<'),
    ('Sell on installments, track every due date and see what is still left to collect.', 'قسطوں پر بیچیں، ہر قسط کی تاریخ پر نظر رکھیں اور دیکھیں ابھی کتنی وصولی باقی ہے۔'),
    ('>FBR invoices<', '>FBR انوائس<'),
    ('Add your FBR POS ID once. Bills then show the FBR invoice number and QR code.', 'اپنی FBR POS آئی ڈی ایک بار لکھیں۔ پھر بلوں پر FBR انوائس نمبر اور QR کوڈ آتا ہے۔'),
    ('>Staff and salary<', '>عملہ اور تنخواہ<'),
    ('Mark attendance, pay salaries and give staff commission on their sales.', 'حاضری لگائیں، تنخواہیں دیں اور عملے کو ان کی فروخت پر کمیشن دیں۔'),
    ('Some features depend on your plan.', 'کچھ فیچرز آپ کے پلان پر منحصر ہیں۔'),
    ('>Compare plans<', '>پلان کا موازنہ کریں<'),
    # offline
    ('>Offline first<', '>آف لائن فرسٹ<'),
    ('Works offline on PC, phone and web', 'کمپیوٹر، فون اور ویب پر آف لائن بھی چلتا ہے'),
    ('Load-shedding and weak internet are part of daily life in Pakistan. That is why we built UpTrendPos as offline-first POS software in Pakistan. Every sale is saved on your device first, then synced to your account when you are online. Nothing is lost and nothing is entered twice.',
     'لوڈشیڈنگ اور کمزور انٹرنیٹ پاکستان میں روز کی بات ہے۔ اسی لیے ہم نے UpTrendPos کو آف لائن فرسٹ بنایا ہے۔ ہر فروخت پہلے آپ کی ڈیوائس پر محفوظ ہوتی ہے، پھر انٹرنیٹ آنے پر آپ کے اکاؤنٹ میں سنک ہو جاتی ہے۔ نہ کچھ ضائع ہوتا ہے، نہ کچھ دو بار لکھنا پڑتا ہے۔'),
    ('Windows app for the shop counter, with barcode scanner and receipt printer', 'دکان کے کاؤنٹر کے لیے ونڈوز ایپ، بارکوڈ اسکینر اور رسید پرنٹر کے ساتھ'),
    ('Android app to bill or check sales from your phone', 'فون سے بلنگ یا فروخت دیکھنے کے لیے اینڈرائیڈ ایپ'),
    ('Web app at live.uptrendpos.com for any laptop, Mac or iPhone', 'کسی بھی لیپ ٹاپ، میک یا آئی فون کے لیے ویب ایپ: live.uptrendpos.com'),
    ('>Download the app<', '>ایپ ڈاؤن لوڈ کریں<'),
    ('>Open web app<', '>ویب ایپ کھولیں<'),
    ('Offline POS software in Pakistan: UpTrendPos billing on an Android phone with a small Type-C thermal printer', 'آف لائن POS سافٹ ویئر: اینڈرائیڈ فون اور چھوٹے Type-C تھرمل پرنٹر پر UpTrendPos بلنگ'),
    # hardware
    ('>Hardware<', '>ہارڈویئر<'),
    ('Works with the hardware you already have', 'جو ہارڈویئر آپ کے پاس ہے، اسی پر چلتا ہے'),
    ('You do not need a special machine. UpTrendPos is POS software in Pakistan that runs on common devices from any computer market, so you can start with what is already on your counter.',
     'کسی خاص مشین کی ضرورت نہیں۔ UpTrendPos کسی بھی کمپیوٹر مارکیٹ میں ملنے والی عام ڈیوائسز پر چلتا ہے، اس لیے جو کاؤنٹر پر پہلے سے موجود ہے اسی سے شروع کریں۔'),
    ('Windows 10 or 11 PC or laptop for the main counter', 'مین کاؤنٹر کے لیے ونڈوز 10 یا 11 والا کمپیوٹر یا لیپ ٹاپ'),
    ('80mm thermal receipt printer by USB or Bluetooth', 'USB یا بلوٹوتھ والا 80mm تھرمل رسید پرنٹر'),
    ('USB barcode scanner for fast billing', 'تیز بلنگ کے لیے USB بارکوڈ اسکینر'),
    ('Android phone or tablet for a small counter or for the owner', 'چھوٹے کاؤنٹر یا مالک کے لیے اینڈرائیڈ فون یا ٹیبلٹ'),
    ('>See the hardware guide<', '>ہارڈویئر گائیڈ دیکھیں<'),
    ('>Ask before you buy<', '>خریدنے سے پہلے پوچھیں<'),
    ('UpTrendPos running on a Windows PC, Android tablet, phone, thermal receipt printer and barcode scanner', 'ونڈوز کمپیوٹر، اینڈرائیڈ ٹیبلٹ، فون، تھرمل رسید پرنٹر اور بارکوڈ اسکینر پر چلتا UpTrendPos'),
    # FBR
    ('>FBR compliance<', '>FBR کی پابندی<'),
    ('FBR invoices without the headache', 'FBR انوائس، بغیر کسی پریشانی کے'),
    ('UpTrendPos is FBR-ready POS software in Pakistan. Is your shop registered with FBR as a Tier-1 retailer? Add your FBR POS ID once. After that, every bill carries an FBR invoice number and a QR code that buyers can check.',
     'UpTrendPos ایک FBR ریڈی POS سافٹ ویئر ہے۔ کیا آپ کی دکان FBR میں Tier-1 ریٹیلر کے طور پر رجسٹرڈ ہے؟ اپنی FBR POS آئی ڈی ایک بار لکھیں۔ اس کے بعد ہر بل پر FBR انوائس نمبر اور QR کوڈ آئے گا جسے خریدار چیک کر سکتا ہے۔'),
    ('<p>See <a', '<p>دیکھیں <a'),
    ('how FBR POS integration works in UpTrendPos', 'UpTrendPos میں FBR POS انٹیگریشن کیسے کام کرتی ہے'),
    (', or read the rules on the official', '، یا سرکاری'),
    ('>FBR website</a>.', '>FBR ویب سائٹ</a> پر اصول پڑھیں۔'),
    ('>Ask about FBR setup<', '>FBR سیٹ اپ کے بارے میں پوچھیں<'),
    ('Our team replies on WhatsApp', 'ہماری ٹیم واٹس ایپ پر جواب دیتی ہے'),
    # register vs app
    ('>Register vs app<', '>رجسٹر یا ایپ<'),
    ('Paper register vs POS software in Pakistan', 'کاغذی رجسٹر اور POS سافٹ ویئر کا موازنہ'),
    ('A register worked for years. Here is what changes when the same counter moves to UpTrendPos, POS software in Pakistan built for shops like yours.',
     'رجسٹر برسوں چلا۔ دیکھیں جب وہی کاؤنٹر UpTrendPos پر آتا ہے تو کیا بدلتا ہے۔'),
    ('Paper register compared with UpTrendPos', 'کاغذی رجسٹر اور UpTrendPos کا موازنہ'),
    ('>At your counter<', '>آپ کے کاؤنٹر پر<'),
    ('>Paper register<', '>کاغذی رجسٹر<'),
    ('>Making a bill<', '>بل بنانا<'),
    ('Write by hand and add on a calculator', 'ہاتھ سے لکھیں اور کیلکولیٹر پر جمع کریں'),
    ('Scan or tap, total in seconds', 'اسکین یا ٹچ کریں، سیکنڈوں میں ٹوٹل'),
    ('>Udhaar<', '>ادھار<'),
    ('Pages get lost, torn or argued about', 'صفحے گم ہوتے ہیں، پھٹتے ہیں یا جھگڑا ہوتا ہے'),
    ('Customer ledger with every payment', 'ہر ادائیگی کے ساتھ گاہک کا کھاتہ'),
    ('>Stock<', '>اسٹاک<'),
    ('Count by hand when something runs out', 'چیز ختم ہونے پر ہاتھ سے گنتی'),
    ('Updates with every sale and purchase', 'ہر فروخت اور خریداری کے ساتھ اپڈیٹ'),
    ('>Expiry<', '>ایکسپائری<'),
    ('Found when a customer complains', 'جب گاہک شکایت کرے تب پتا چلتا ہے'),
    ('Alerts before items expire', 'ایکسپائری سے پہلے الرٹ'),
    ('>Daily sales total<', '>روزانہ کی فروخت کا ٹوٹل<'),
    ('Count cash and add up the pages', 'کیش گنیں اور صفحے جمع کریں'),
    ('Ready on your phone any time', 'کسی بھی وقت فون پر تیار'),
    ('>Backup<', '>بیک اپ<'),
    ('One copy that can burn or get wet', 'ایک ہی کاپی جو جل یا بھیگ سکتی ہے'),
    ('Saved on your device and online', 'ڈیوائس پر اور آن لائن محفوظ'),
    ('>FBR invoice<', '>FBR انوائس<'),
    ('>Not possible<', '>ممکن نہیں<'),
    ('FBR number and QR code on the bill', 'بل پر FBR نمبر اور QR کوڈ'),
    ('>Load-shedding<', '>لوڈشیڈنگ<'),
    ('>Keeps working<', '>چلتا رہتا ہے<'),
    ('Keeps working: billing runs offline', 'چلتا رہتا ہے: بلنگ آف لائن ہوتی ہے'),
    ('FBR invoices come with the Enterprise and Custom plans.', 'FBR انوائس انٹرپرائز اور کسٹم پلان میں شامل ہیں۔'),
    # steps
    ('>Easy start<', '>آسان آغاز<'),
    ('Start selling in 4 easy steps', '4 آسان مراحل میں فروخت شروع کریں'),
    ('Getting started with our POS software in Pakistan is simple. You do not need a computer expert, and most shops make their first sale on the same day.',
     'شروع کرنا آسان ہے۔ کسی کمپیوٹر ماہر کی ضرورت نہیں، اور زیادہ تر دکانیں اسی دن پہلی فروخت کر لیتی ہیں۔'),
    ('<h3>Sign up</h3>', '<h3>سائن اپ کریں</h3>'),
    ('<p>Create your shop at <a', '<p><a'),
    ('>live.uptrendpos.com</a> and choose your business type.', '>live.uptrendpos.com</a> پر اپنی دکان بنائیں اور اپنا کاروبار منتخب کریں۔'),
    ('<h3>Add products</h3>', '<h3>پروڈکٹس شامل کریں</h3>'),
    ('Add items yourself, or send us your list and our team helps you load it.', 'خود آئٹمز شامل کریں، یا اپنی لسٹ ہمیں بھیجیں، ہماری ٹیم شامل کرنے میں مدد کرے گی۔'),
    ('<h3>Start billing</h3>', '<h3>بلنگ شروع کریں</h3>'),
    ('Connect your barcode scanner and receipt printer, then make your first sale.', 'بارکوڈ اسکینر اور رسید پرنٹر لگائیں اور پہلی فروخت کریں۔'),
    ('<h3>Track your shop</h3>', '<h3>دکان پر نظر رکھیں</h3>'),
    ('Check sales, stock, udhaar and profit from your phone, any time.', 'فروخت، اسٹاک، ادھار اور منافع کسی بھی وقت اپنے فون پر دیکھیں۔'),
    # about
    ('>About UpTrendPos<', '>UpTrendPos کے بارے میں<'),
    ('Built in Pakistan, for Pakistani shops', 'پاکستان میں بنا، پاکستانی دکانوں کے لیے'),
    ('UpTrendPos is POS software in Pakistan, built by our own team in Sahiwal, Punjab. We build every feature around how shops here really work: udhaar, pack and piece, load-shedding and FBR rules. You talk to the same team that builds the software.',
     'UpTrendPos کو ہماری اپنی ٹیم نے ساہیوال، پنجاب میں بنایا ہے۔ ہم ہر فیچر یہاں کی دکانوں کے اصل کام کے مطابق بناتے ہیں: ادھار، پیک اور پیس، لوڈشیڈنگ اور FBR کے اصول۔ آپ اسی ٹیم سے بات کرتے ہیں جو سافٹ ویئر بناتی ہے۔'),
    ('>About us<', '>ہمارے بارے میں<'),
    ('>Contact us<', '>رابطہ کریں<'),
    ('<strong>Local support</strong>', '<strong>مقامی سپورٹ</strong>'),
    ('Help on WhatsApp and phone from people who know Pakistani shops.', 'واٹس ایپ اور فون پر ان لوگوں سے مدد جو پاکستانی دکانوں کو جانتے ہیں۔'),
    ('<strong>Your data, only yours</strong>', '<strong>آپ کا ڈیٹا، صرف آپ کا</strong>'),
    ("Each shop's data is kept separate. Only your staff with the right access can see it.", 'ہر دکان کا ڈیٹا الگ رکھا جاتا ہے۔ صرف آپ کا وہ عملہ دیکھ سکتا ہے جسے اجازت ہو۔'),
    ('<strong>Free updates</strong>', '<strong>مفت اپڈیٹس</strong>'),
    ('New features come to every plan at no extra cost.', 'نئے فیچرز ہر پلان میں بغیر اضافی خرچ کے آتے ہیں۔'),
    # plans strip
    ('Simple plans for every shop size', 'ہر دکان کے لیے آسان پلان'),
    ('Clear prices for POS software in Pakistan: monthly or yearly plans for one shop or many branches. Every new shop gets a 7-day free trial.',
     'واضح قیمتیں: ایک دکان ہو یا کئی برانچیں، ماہانہ یا سالانہ پلان۔ ہر نئی دکان کو 7 دن کی مفت آزمائش ملتی ہے۔'),
    ('>See pricing<', '>قیمتیں دیکھیں<'),
    # FAQ
    ('>FAQ<', '>سوال و جواب<'),
    ('Questions about POS software in Pakistan', 'POS سافٹ ویئر کے بارے میں سوالات'),
    ('What is POS software?', 'POS سافٹ ویئر کیا ہے؟'),
    ('POS (point of sale) software is what you use at the counter to make bills. Good POS software does more than print a bill. It also updates your stock, customer udhaar, purchases and accounts with every sale, so the owner can see the whole shop on one screen.',
     'POS (پوائنٹ آف سیل) سافٹ ویئر وہ ہے جس سے کاؤنٹر پر بل بنتا ہے۔ اچھا POS سافٹ ویئر صرف بل پرنٹ نہیں کرتا، بلکہ ہر فروخت کے ساتھ اسٹاک، گاہکوں کا ادھار، خریداری اور حسابات بھی اپڈیٹ کرتا ہے، تاکہ مالک پوری دکان ایک اسکرین پر دیکھ سکے۔'),
    ('Which is the best POS software in Pakistan for a small shop?', 'چھوٹی دکان کے لیے بہترین POS سافٹ ویئر کون سا ہے؟'),
    ('The best one is the one that fits your shop. Check four things: it works without internet, it keeps udhaar, it sells by pack and piece, and your staff find it easy. UpTrendPos does all four, and you can test it free for 7 days.',
     'بہترین وہی ہے جو آپ کی دکان کے مطابق ہو۔ چار باتیں دیکھیں: انٹرنیٹ کے بغیر چلے، ادھار رکھے، پیک اور پیس میں بیچے، اور عملے کے لیے آسان ہو۔ UpTrendPos چاروں کام کرتا ہے، اور آپ اسے 7 دن مفت آزما سکتے ہیں۔'),
    ('Does UpTrendPos work without internet?', 'کیا UpTrendPos انٹرنیٹ کے بغیر چلتا ہے؟'),
    ('Yes. The Windows and Android apps keep billing offline. When the internet comes back, your sales sync to your account on their own, with no double entries. You need internet only for the first login.',
     'جی ہاں۔ ونڈوز اور اینڈرائیڈ ایپ آف لائن بلنگ کرتی رہتی ہیں۔ انٹرنیٹ واپس آنے پر فروخت خود آپ کے اکاؤنٹ میں سنک ہو جاتی ہے، کوئی ڈبل انٹری نہیں۔ انٹرنیٹ صرف پہلی بار لاگ اِن کے لیے چاہیے۔'),
    ('Is UpTrendPos integrated with FBR?', 'کیا UpTrendPos میں FBR انٹیگریشن ہے؟'),
    ('Yes. Shops registered with FBR as Tier-1 retailers can add their FBR POS ID once. Each bill then shows an FBR invoice number and a QR code that buyers can check. Your shop must be registered with FBR first, and FBR invoices come with the Enterprise and Custom plans.',
     'جی ہاں۔ FBR میں Tier-1 ریٹیلر کے طور پر رجسٹرڈ دکانیں اپنی FBR POS آئی ڈی ایک بار لکھیں۔ پھر ہر بل پر FBR انوائس نمبر اور QR کوڈ آتا ہے جسے خریدار چیک کر سکتا ہے۔ اس کے لیے دکان کا FBR میں رجسٹرڈ ہونا ضروری ہے، اور FBR انوائس انٹرپرائز اور کسٹم پلان میں ہیں۔'),
    ('Can I use it on my mobile phone?', 'کیا میں اسے موبائل فون پر چلا سکتا ہوں؟'),
    ('Yes. Use the Android app, or open live.uptrendpos.com in any browser. On iPhone, use the web app in Safari. All your devices share one account. See the <a',
     'جی ہاں۔ اینڈرائیڈ ایپ استعمال کریں، یا کسی بھی براؤزر میں live.uptrendpos.com کھولیں۔ آئی فون پر سفاری میں ویب ایپ استعمال کریں۔ آپ کی سب ڈیوائسز پر ایک ہی اکاؤنٹ چلتا ہے۔ دیکھیں <a'),
    ('>download page</a>.', '>ڈاؤن لوڈ صفحہ</a>۔'),
    ('How much does UpTrendPos cost?', 'UpTrendPos کی قیمت کتنی ہے؟'),
    ('Premium is Rs 1,000 a month, Enterprise is Rs 2,000 a month and Custom is Rs 5,000 a month. You can pay monthly or yearly, and every new shop gets a 7-day free trial of our POS software in Pakistan first. See what each plan includes on our <a',
     'پریمیم Rs 1,000 ماہانہ، انٹرپرائز Rs 2,000 ماہانہ اور کسٹم Rs 5,000 ماہانہ ہے۔ آپ ماہانہ یا سالانہ ادائیگی کر سکتے ہیں، اور ہر نئی دکان کو پہلے 7 دن کی مفت آزمائش ملتی ہے۔ ہر پلان میں کیا شامل ہے، ہمارے <a'),
    ('>pricing page</a>.', '>قیمتوں کے صفحے</a> پر دیکھیں۔'),
    ('Can I run more than one branch?', 'کیا میں ایک سے زیادہ برانچیں چلا سکتا ہوں؟'),
    ('Yes. Each branch has its own stock and prices, and you see all branches from one owner account. Premium has 1 branch, Enterprise has 2 and Custom has 3. If you need more, ask us for a custom quote.',
     'جی ہاں۔ ہر برانچ کا اپنا اسٹاک اور قیمتیں ہوتی ہیں، اور مالک کے ایک اکاؤنٹ سے سب برانچیں نظر آتی ہیں۔ پریمیم میں 1، انٹرپرائز میں 2 اور کسٹم میں 3 برانچیں ہیں۔ مزید کے لیے ہم سے کوٹیشن لیں۔'),
    ('Is my shop data safe?', 'کیا میری دکان کا ڈیٹا محفوظ ہے؟'),
    ("Yes. Each shop's data is kept separate from every other shop, and only staff you allow can see it. Sales are saved on your device first and then backed up to your online account, so a broken computer does not mean lost sales.",
     'جی ہاں۔ ہر دکان کا ڈیٹا باقی دکانوں سے الگ رہتا ہے اور صرف وہی عملہ دیکھ سکتا ہے جسے آپ اجازت دیں۔ فروخت پہلے ڈیوائس پر محفوظ ہوتی ہے، پھر آن لائن اکاؤنٹ میں بیک اپ ہوتی ہے، اس لیے کمپیوٹر خراب ہونے سے فروخت ضائع نہیں ہوتی۔'),
    ('Will you help me set it up?', 'کیا آپ سیٹ اپ میں مدد کریں گے؟'),
    ('Yes. Our team helps you on WhatsApp to add products, connect your printer and train your staff. Message us on <a',
     'جی ہاں۔ ہماری ٹیم واٹس ایپ پر پروڈکٹس شامل کرنے، پرنٹر لگانے اور عملے کی تربیت میں مدد کرتی ہے۔ ہمیں میسج کریں: <a'),
    ('>0319 2223292</a>.</p>', '>0319 2223292</a></p>'),
    # reviewed
    ('aria-label="About this page"', 'aria-label="اس صفحے کے بارے میں"'),
    ('Written and checked against the live app by the <strong>UpTrendPos team</strong> in Sahiwal, Pakistan. Last updated <time datetime="2026-10-29">29 October 2026</time>. Something not clear? <a',
     'یہ صفحہ ساہیوال، پاکستان میں <strong>UpTrendPos ٹیم</strong> نے لکھا اور لائیو ایپ سے چیک کیا۔ آخری اپڈیٹ <time datetime="2026-11-25">25 نومبر 2026</time>۔ کچھ سمجھ نہ آئے؟ <a'),
    ('>Ask us<', '>ہم سے پوچھیں<'),
    ('Only features that are live', 'صرف وہ فیچرز جو لائیو ہیں'),
    ('Local team in Sahiwal', 'ساہیوال میں مقامی ٹیم'),
    ('Support in Urdu and English', 'اردو اور انگریزی میں سپورٹ'),
    # final
    ('Try UpTrendPos free for 7 days', 'UpTrendPos کو 7 دن مفت آزمائیں'),
    ('Set up your shop today, or message us on WhatsApp and we will help you start. Simple POS software in Pakistan, made for your counter.',
     'آج ہی اپنی دکان سیٹ اپ کریں، یا واٹس ایپ پر میسج کریں، ہم شروع کرنے میں مدد کریں گے۔ آپ کے کاؤنٹر کے لیے آسان POS سافٹ ویئر۔'),
    ('>Call 0319 2223292<', '>کال کریں: 0319 2223292<'),
]
miss = []
for a, b in sorted(T, key=lambda p: -len(p[0])):
    if a in h:
        h = h.replace(a, b)
    elif a not in ('>Mobile, Computer &amp; Printer Shop<',):
        miss.append(a[:70])
# WhatsApp prefilled texts in Roman Urdu so the team knows the visitor came from the Urdu page
h = h.replace('text=Hi%2C%20I%20want%20a%20free%20demo%20of%20UpTrendPos', 'text=Assalam%20o%20Alaikum%2C%20mujhe%20UpTrendPos%20ka%20free%20demo%20chahiye')
h = h.replace('text=Hi%2C%20I%20want%20a%20pharmacy%20demo%20of%20UpTrendPos', 'text=Assalam%20o%20Alaikum%2C%20mujhe%20pharmacy%20ka%20demo%20chahiye')
def wrap_text(m):
    t = m.group(1)
    if not re.search(r'[؀-ۿ]', t):
        return m.group(0)
    return '>' + RUN.sub(lambda r: '<bdi>' + r.group(0) + '</bdi>' if re.search(r'[0-9+%-]', r.group(0)) else r.group(0), t) + '<'
h = re.sub(r'>([^<>]+)<', wrap_text, h)
# Latin runs keep their own direction inside Urdu text
left = []
for m in re.finditer(r'>([^<>]+)<', h):
    t = H.unescape(m.group(1)).strip()
    w = set(re.findall(r'[A-Za-z]{3,}', t)) - {'UpTrendPos','live','uptrendpos','com','sales','FBR','POS','CCTV','LED','Tier','Rs','USB','Type'}
    if w: left.append(t)
bad = re.findall(r'<script|<style|<!--|<iframe|<form|javascript:|\son[a-z]+\s*=', h, re.I)
assert not bad, bad
open(out, 'w', encoding='utf-8').write(h)
print('missing:', miss)
print('english left:', left)
print(len(h))
