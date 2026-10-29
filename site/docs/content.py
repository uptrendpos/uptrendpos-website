"""UpTrendPos Product Guide - content (simple English). Rendered by build_docs.py."""

STATS = [('17,000+', 'medicines ready for pharmacies'), ('5,000+', 'beauty and cosmetics items'), ('1,100+', 'electronics, solar and camera products'),
         ('30+', 'business types with ready setups'), ('3', 'apps, one account: Windows, Android, Web')]

GAPS = [
    ('pill', 'b', 'Typing thousands of products by hand', 'Ready catalogs, added in one click',
     'Pharmacy, beauty, electronics, solar, cameras and most other business types start with products already loaded. Search, tick and add them to your shop.'),
    ('printer', 'g', 'No printer, or no space for one', 'Print straight from your phone',
     'Plug a small thermal printer into your Android phone with a USB Type-C cable and print receipts. No computer needed.'),
    ('wa', 'y', 'Paper bills get lost or torn', 'WhatsApp invoices with your signature',
     'Send any bill on WhatsApp as a picture or PDF, in your own invoice style, with your electronic signature on it.'),
    ('offline', 'b', 'Light or internet goes off', 'Billing keeps working offline',
     'Sales save on your device first and sync to your account on their own when the internet is back. Nothing is entered twice.'),
    ('cal', 'g', 'Qist written in a diary', 'Installments with a receipt for every payment',
     'Make your own installment plan, with or without markup. Every payment gets a receipt and the last one gets a full-payment certificate.'),
    ('shield', 'y', 'Staff change stock without asking', 'Manager PIN approvals',
     'Stock reversals and other risky changes need the manager PIN, and every change is written in the audit trail.'),
    ('users', 'b', 'One computer for the whole staff', 'Every employee gets their own login',
     'When you add an employee, their login is made at the same time. Staff can sell from their own phone, the web or the desktop app.'),
    ('chart', 'g', 'Profit is just a guess', 'Real double-entry accounts',
     'Every sale, purchase, expense and payment posts to your accounts on its own. Trial balance, balance sheet and profit and loss are always ready.'),
    ('qr', 'y', 'FBR rules feel hard', 'FBR fiscalization built in',
     'Registered shops add their FBR details once. Every bill then carries the FBR invoice number and QR code.'),
    ('scan', 'b', 'No barcode scanner', 'Scan with the phone camera',
     'Small shops can scan barcodes with the camera inside the app, so a separate scanner is not a must.'),
]

STEPS = [
    ('Add your bank', 'Add the bank accounts or wallets your shop uses, so payments go to the right place.'),
    ('Add your cashier and cash drawer', 'Create a cash drawer and set the cashier who works on it.'),
    ('Set the manager PIN', 'This PIN approves stock reversals and other sensitive changes.'),
    ('Add your first vendor', 'The supplier you buy from. Their invoices and payments stay in one place.'),
    ('Check categories', 'If your business type has a ready catalog, categories are already filled. Add your own if you need more.'),
    ('Add brands', 'Add the brands you sell, or use the ones that came with the catalog.'),
    ('Register your first product', 'Add a product, or pick it from the ready catalog. Set loose or pack sale, low stock alert and more.'),
    ('Receive stock with PO and GRN', 'Make a purchase order, receive the goods on a GRN and your stock goes up with the right cost.'),
    ('Make your first sale', 'Open the sale page, add items, take payment and print or send the bill on WhatsApp.'),
]

# module: id, icon, colour, title, one-line intro, groups [(group title, [items])], why-it-matters
MODULES = [
 ('sale', 'cart', 'y', 'Sale page (the counter)', 'The screen your cashier uses all day. Fast, simple and made for Pakistani counters.', [
    ('Selling', ['Loose sale (single pieces, kg, metre)', 'Pack sale (carton, box, strip, dozen)', 'Quick bill for walk-in customers', 'Walk-in customer, or a customer with name and phone number']),
    ('Payment and control', ['Discount options on the item or the whole bill', 'Ledger sale (udhaar) or normal cash sale', 'Built-in calculator', 'Cashier and cash drawer on every sale', 'Delete bills, with a record of who did it']),
 ], 'A bill is made in seconds, and the same screen handles a kiryana counter, a pharmacy or a mobile shop.'),
 ('sales', 'bill', 'b', 'Sales', 'Everything after the sale: history, returns, bills and sharing.', [
    ('Records', ['Sales history with search and filters', 'Return history', 'Cashier record: what each person sold and collected', 'Cash sessions: open and close the drawer for every shift']),
    ('Invoices', ['Invoice customization with a live preview', 'Your own invoice styles and your electronic signature', 'PDF with a live preview', 'Thermal, A4 and WhatsApp versions of every bill']),
    ('Sharing and printing', ['Send invoices on WhatsApp as a picture or PDF', 'Share with images', 'Print from your phone to a thermal printer by USB Type-C', 'Quick billing for busy hours']),
 ], 'Customers get a clean bill on WhatsApp, and the owner can see every rupee each cashier collected.'),
 ('inventory', 'box', 'g', 'Inventory and ready catalogs', 'Your stock, counted for you, with catalogs that save weeks of typing.', [
    ('Ready catalogs (add in one click)', ['Pharmacy: 17,000+ medicines', 'Beauty and cosmetics: 5,000+ items', 'Electronics, cameras and solar: 1,100+ products', 'Mobile and computer: 670+ products', 'Grocery and kiryana: ready catalog', 'Almost every business type has some ready catalog']),
    ('Stock control', ['Stock mismatch report', 'Demand list: what to reorder', 'Low stock and expiry alerts', 'Stock valuation at cost and sale price', 'Inventory movement: damage, sample, adjustment and stock audit']),
    ('Units and labels', ['Units of measure (UOM) for shops and warehouses', 'Barcodes and labels', 'Barcode scanner inside the app (phone camera)']),
 ], 'You start selling on day one instead of spending weeks typing product names.'),
 ('procurement', 'truck', 'b', 'Procurement (buying stock)', 'From purchase order to stock on the shelf, with every supplier payment tracked.', [
    ('Vendors', ['Complete vendor management', 'Vendor invoices with full and partial payments', 'Invoices in thermal, A4 and WhatsApp formats']),
    ('Purchase order', ['Select many items at once', 'Set loose sale or UOM (pack) sale', 'Set low stock alert and expiry date for alerts', 'Set batch number, category and sub-category', 'Set the rack and shelf number once', 'Optional notes']),
    ('GRN and invoice', ['Goods received note (GRN) adds stock', 'Purchase invoice (PI) made from the GRN', 'Reverse GRN to return stock', 'Barcode labels printed in one click when the GRN is received', 'Batch and expiry saved on receipt']),
 ], 'Stock, cost and what you owe each supplier always match, without a separate register.'),
 ('customers', 'book', 'y', 'Customers, udhaar and installments', 'Every customer balance and every qist, clear and shareable.', [
    ('Customer ledger (udhaar khata)', ['Ledger for every customer', 'Partial and full payments', 'Statements and invoices on WhatsApp', 'Thermal and A4 print options']),
    ('Installments (qist)', ['Make your own installment plan', 'Choose interest or markup options', 'A receipt for every installment received', 'A full-payment certificate at the end', 'All invoice types for every payment']),
    ('Reminders', ['Upcoming installment notifications for the owner', 'Notifications for the customer']),
 ], 'No more diaries. Every customer knows what they owe, and you know who to call.'),
 ('hrm', 'users', 'b', 'HRM (staff)', 'Staff, logins, attendance, salaries and commission in one place.', [
    ('Employees and logins', ['Add employees with full details', 'Login details are made when the employee is created', 'Each employee can sell from their own phone, the web or the desktop app', 'Create your own employee types', 'Departments and designations', 'Dynamic shifts']),
    ('Control', ['Manager PIN for stock reversal approval']),
    ('Attendance and salary', ['Attendance with arrival and leaving time', 'Monthly salaries set by you', 'Advance payments', 'Pay a salary in parts until it is fully paid', 'Month closing for salaries', 'Printing and WhatsApp sharing for every salary slip']),
    ('Commission', ['Staff commission on all types of sales', 'Commission reports', 'Share commission reports']),
 ], 'Every person has their own login and their own record, so nothing is shared or guessed.'),
 ('accounts', 'chart', 'g', 'Accounts and finance', 'Real double-entry accounting, written so a shop owner can use it.', [
    ('Reports', ['Sales report', 'Purchase report', 'Stock report', 'Batch report', 'Profit and loss', 'Trial balance', 'Balance sheet', 'Day book', 'Cash flow', 'Customer report', 'AR aging (who owes and for how long)', 'Vendor report', 'Expense report']),
    ('Manual entries in plain words', ['Paid rent, a bill, tea or a repair', 'A customer paid an old udhaar balance', 'Paid a supplier', 'Paid salary, an expense or an advance', 'Owner put money in or took money out', 'Deposited cash in the bank', 'Took cash out of the bank', 'The bank cut charges', 'Got cash that is not a sale (rent from a tenant, commission)', 'Received a loan in the bank', 'I made a wrong entry', 'History of all manual entries']),
    ('Advanced vouchers (choose the type yourself)', ['Cash payment (CPV)', 'Cash receipt (CRV)', 'Bank payment (BPV)', 'Bank receipt (BRV)', 'Transfer or contra (CV)', 'Journal voucher (JV)']),
    ('Books and controls', ['Day end sweep', 'Account ledger', 'Installment aging', 'Markup income', 'Chart of accounts', 'Opening balances', 'Owner capital', 'Year-end close', 'Period lock', 'Held postings', 'Reversal approval']),
 ], 'Forms are already filled for common entries, so you only type the amount. The trial balance always ties.'),
 ('cash', 'wallet', 't', 'Bank and cash accounts', 'Know where every rupee is: in which drawer, in which bank.', [
    ('Accounts', ['Add cash drawers and set the cashier for each', 'Bank and wallet accounts for bank management']),
 ], 'Cash and bank balances come from your accounts, so they are always right.'),
 ('expenses', 'receipt', 'y', 'Expenses', 'Every shop expense, with a photo of the bill.', [
    ('Expenses', ['Add your own expense categories', 'Add and manage expenses', 'Attach a picture of the expense bill', 'Pay from a cash drawer or a bank in one tap']),
 ], 'Expenses go straight into profit and loss, so your profit is real.'),
 ('income', 'trend', 'b', 'Income report and analytics', 'The whole business on one screen, with graphs.', [
    ('Income report', ['All income and transactions with graphs', 'Sales, installments and expenses', 'Vendor paid and customer paid', 'Operating results and profit margin graph']),
    ('Profit dashboard', ['Revenue', 'Gross profit', 'Markup income', 'Total income', 'Salaries', 'Operating expenses', 'Net profit', 'Monthly closing']),
 ], 'The owner sees real profit any day, from the shop or from home.'),
 ('quotes', 'doc', 'g', 'Quotations', 'Give a price first, sell later, without typing it twice.', [
    ('Quotations', ['Quotations list', 'Estimates register', 'Quotation POS for making quotes fast', 'A4 quotation, sent on WhatsApp', 'Convert a quotation to a sale in one tap']),
 ], 'Solar systems, CCTV kits, furniture and big orders are quoted and closed faster.'),
 ('vertical', 'layers', 'y', 'Tools for your business type', 'Extra tools that switch on for the trades that need them.', [
    ('Tools', ['Warranty lookup', 'Job cards', 'Appointment booking', 'Units of measure (UOM)', 'Variant matrix generator (size, colour and more)', 'Quotations', 'Membership and locker', 'Gold rate and making charge']),
 ], 'Your shop opens with the tools of your trade, not a generic billing app.'),
 ('compliance', 'shield', 'b', 'Compliance and security', 'Stay on the right side of FBR and keep every change on record.', [
    ('Compliance', ['FBR fiscalization: FBR invoice number and QR code on the bill']),
    ('Security', ['Audit trail of deletes and changes', 'Security and activity log', 'Reconciliation check', 'POS to GL check (sales match the accounts)']),
 ], 'Owners can trust the numbers and see who did what.'),
 ('notify', 'bell', 'g', 'Notifications', 'The right person hears about the right event.', [
    ('Inside the app', ['Notifications for the owner, employees, customers and vendors', 'On every module: sales, stock, installments, payments and more']),
 ], 'Nothing important waits for someone to open a report.'),
 ('settings', 'gear', 't', 'Settings and data', 'Make the app look and work the way your shop works.', [
    ('Look and fields', ['Appearance: black, white, orange, yellow and more themes', 'Customize counter fields', 'Notes']),
    ('Users and branches', ['User management that works with employees', 'Create branches']),
    ('Data', ['Backup and restore', 'Developer tools: a sync panel the support team uses to check errors', 'Delete account', 'Log out']),
 ], 'Your shop, your colours, your fields, and your data always backed up.'),
 ('support', 'help', 'y', 'Help and support', 'Real people who know the app, in Urdu or English.', [
    ('Support', ['Support tickets from inside the app', 'WhatsApp, phone and email help', 'Monday to Saturday, 10 am to 7 pm']),
 ], 'If something goes wrong, you raise a ticket and the same team that builds the app answers.'),
]

PLANS = [
    ('Premium', 'One shop', ['1 branch, 3 users', 'Unlimited invoices', 'Billing, returns and udhaar', 'Stock, purchase orders and GRN', 'Double-entry accounts and reports', 'Backup and restore']),
    ('Enterprise', 'Busy shops and FBR sellers', ['2 branches, 6 users', 'Everything in Premium', 'FBR invoices with QR code', 'Barcode and label printing', 'Customer installments', 'Staff commission', 'Profit and loss dashboard', 'Audit trail and security alerts']),
    ('Custom', 'Bigger shops with more staff', ['3 branches, 9 users', 'Everything in Enterprise', 'Staff attendance', 'Staff salaries (payroll)', 'Every tool switched on', 'More branches on request']),
]

GLOSSARY = [
    ('Udhaar / khata', 'Goods given on credit, and the customer ledger that keeps the balance.'),
    ('Qist', 'An installment. A big sale paid in parts, often monthly.'),
    ('PO', 'Purchase order. What you plan to buy from a vendor.'),
    ('GRN', 'Goods received note. Made when stock arrives; it adds the stock.'),
    ('PI', 'Purchase invoice. The vendor bill made from the GRN.'),
    ('Reverse GRN', 'Sends stock back to the vendor and corrects stock and the vendor balance.'),
    ('UOM', 'Unit of measure: piece, pack, carton, kg, metre and so on.'),
    ('Loose sale', 'Selling single units out of a pack, like one tablet or one biscuit packet.'),
    ('Cash session', 'Opening and closing a cash drawer for one shift, with the count.'),
    ('Manager PIN', 'A code only the manager knows, needed to approve risky changes.'),
    ('CPV / CRV', 'Cash payment voucher / cash receipt voucher.'),
    ('BPV / BRV', 'Bank payment voucher / bank receipt voucher.'),
    ('CV (contra)', 'Moving money between your own cash and bank accounts.'),
    ('JV', 'Journal voucher, for adjustments that are not cash or bank.'),
    ('Day end sweep', 'The end-of-day step that moves the day\'s cash to the right accounts.'),
    ('Period lock', 'Closes past days so nobody can change them.'),
    ('Year-end close', 'Closes the financial year and carries balances forward.'),
    ('Held postings', 'Entries waiting for approval before they reach the accounts.'),
    ('Markup income', 'The extra earned on installment sales, counted as it is earned.'),
    ('AR aging', 'Who owes you money and for how long.'),
    ('Trial balance', 'A check that all debits equal all credits in your accounts.'),
    ('FBR fiscalization', 'Sending each bill to FBR so it gets an FBR invoice number and QR code.'),
]
