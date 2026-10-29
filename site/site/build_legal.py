"""Builds Privacy Policy, Terms and Conditions and Support pages (Elementor HTML widget content, no style/script/comments)."""
import pathlib, re
P = pathlib.Path('/home/claude/site/pages')
UPDATED = '13 October 2026'
WA = 'https://wa.me/923192223292'
WA_SVG = '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.4.1-.6.3-.2.2-.8.8-.8 2s.8 2.3.9 2.5c.1.2 1.6 2.5 4 3.5 1.5.6 2 .7 2.8.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/></svg>'


def ul(items):
    return '<ul class="utp-checks">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


def table(head, rows):
    h = ''.join(f'<th scope="col">{x}</th>' for x in head)
    b = ''.join('<tr>' + f'<th scope="row">{r[0]}</th>' + ''.join(f'<td>{c}</td>' for c in r[1:]) + '</tr>' for r in rows)
    return f'<div class="utp-doc-table"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


def hero(root_cls, root_id, crumb, kicker, h1, lead, extra=''):
    return f'''<div class="utp {root_cls}" id="{root_id}">

  <section class="utp-hero utp-hero-sm" aria-labelledby="utp-h1">
    <div class="utp-wrap">
      <nav class="utp-crumb" aria-label="Breadcrumb">
        <ol>
          <li><a href="https://uptrendpos.com/">Home</a></li>
          <li><span aria-current="page">{crumb}</span></li>
        </ol>
      </nav>
      <p class="utp-kicker">{kicker}</p>
      <h1 id="utp-h1">{h1}</h1>
      <p class="utp-lead">{lead}</p>
{extra}    </div>
  </section>
'''


def doc(sections, short_title, short_items, related):
    toc = ''.join(f'<li><a href="#{sid}">{n}. {t}</a></li>' for n, (sid, t, _) in enumerate(sections, 1))
    body = ''.join(f'''
        <section class="utp-doc-sec" id="{sid}" aria-labelledby="{sid}-h">
          <h2 id="{sid}-h"><span class="utp-doc-n">{n}</span>{t}</h2>
          {html}
        </section>''' for n, (sid, t, html) in enumerate(sections, 1))
    rel = ''.join(f'<a href="{u}">{t}</a>' for t, u in related)
    return f'''
  <section class="utp-sec utp-doc-wrap" aria-label="Document">
    <div class="utp-wrap utp-doc">
      <aside class="utp-toc" aria-label="On this page">
        <p class="utp-toc-h">On this page</p>
        <ol>{toc}</ol>
        <div class="utp-toc-help">
          <p><strong>Questions?</strong> We reply in Urdu or English.</p>
          <a href="{WA}" target="_blank" rel="noopener" data-track="legal_toc_whatsapp">WhatsApp 0319 2223292</a>
          <a href="mailto:sales@uptrendpos.com">sales@uptrendpos.com</a>
        </div>
      </aside>
      <div class="utp-doc-body">
        <div class="utp-short">
          <p class="utp-short-h">{short_title}</p>
          {ul(short_items)}
        </div>{body}
        <div class="utp-doc-end">
          <p>Last updated: <strong>{UPDATED}</strong>. Read also:</p>
          <div class="utp-chips">{rel}</div>
        </div>
      </div>
    </div>
  </section>
</div>
'''


def updated_line(effective=True):
    return (f'      <ul class="utp-doc-meta">\n        <li>Last updated: <strong>{UPDATED}</strong></li>\n'
            + (f'        <li>Effective from: <strong>{UPDATED}</strong></li>\n' if effective else '')
            + '        <li>Applies to: uptrendpos.com, live.uptrendpos.com, Android and Windows apps</li>\n      </ul>\n')


CONTACT_BLOCK = ('<div class="utp-doc-contact"><p><strong>UpTrendPos</strong><br>House No 193/A, Umer Block, Shadab Town, Sahiwal 57000, Punjab, Pakistan</p>'
                 '<p>Email: <a href="mailto:sales@uptrendpos.com">sales@uptrendpos.com</a><br>Phone and WhatsApp: <a href="tel:+923192223292">+92 319 2223292</a><br>'
                 'In the app: Menu &gt; Help &amp; Support</p></div>')

# ======================================================================= PRIVACY
privacy = [
    ('pp-who', 'Who we are', '<p>UpTrendPos is point of sale (POS), inventory and accounting software for shops and businesses in Pakistan. It is built and run by the UpTrendPos team in Sahiwal, Punjab. In this policy, "we", "us" and "our" mean UpTrendPos. "You" means the shop owner, the staff who use the app, and visitors to our website.</p><p>This policy covers our website uptrendpos.com, the web app at live.uptrendpos.com, and the UpTrendPos Android and Windows apps.</p>'),
    ('pp-role', 'Our role with your data', '<p>There are two kinds of data, and our role is different for each:</p>' + ul([
        '<strong>Your shop records</strong> (products, sales, customers, udhaar, staff, suppliers): you decide what to save and why. We store and process this data only to run the service for you, and only on your instructions.',
        '<strong>Your account and our website</strong> (owner details, payments, support chats, website visits): we decide how this data is used, as explained in this policy.'])),
    ('pp-collect', 'Information we collect', '<h3>Account and business details</h3>' + ul(['Owner name, verified mobile number and email', 'Shop name, business type, address, branches and logo', 'NTN, STRN, POS ID and FBR token, only if you turn on FBR invoicing'])
     + '<h3>Shop records you enter</h3>' + ul(['Products, prices, stock, batches and expiry dates', 'Sales, returns, purchases, expenses and account entries', 'We never ask for your online banking password or card PIN'])
     + '<h3>Staff records</h3>' + ul(['Name, phone, role, PIN login and access rights', 'CNIC, attendance and salary, only if you use these features'])
     + '<h3>Your customers and suppliers</h3>' + ul(['Name, phone and address you save', 'Udhaar balances, payments and installment plans', 'Guarantor details, only if you add them for installments'])
     + '<h3>Delivery riders</h3>' + ul(['Name, phone and CNIC photos when a rider applies to a shop. These are shared only with that shop.'])
     + '<h3>Device and usage data</h3>' + ul(['Device type, app version, IP address and error reports', 'Login and sync history, audit trail of changes and a notification token'])
     + '<h3>Files and payments</h3>' + ul(['Logos, bills, receipts and screenshots you upload or send to support', 'Plan, amount, date and payment reference. We do not store card numbers.'])
     + '<h3>Website visitors</h3>' + ul(['Details you type in our demo or contact form (name, phone, city, business type)', 'Basic visit data from analytics, such as pages viewed and device type'])),
    ('pp-never', 'What we never do', ul(['We never sell your data or your customers\' data', 'We never show ads inside the app or use shop records for advertising', 'We do not collect your location, phone contacts or microphone recordings', 'We do not look at your shop records unless you ask for support or the law requires it'])),
    ('pp-perm', 'App permissions', '<p>The apps ask for these permissions only when you use the feature. You can turn them off in your device settings at any time.</p>'
     + table(['Permission', 'Why we need it'], [('Camera', 'Scan barcodes and take product or bill photos'), ('Photos and files', 'Attach images, save exports and make backups'), ('Bluetooth and USB', 'Connect receipt printers, label printers and barcode scanners, including a printer on your phone\'s Type-C port'), ('Notifications', 'Low stock, expiry, payment and sync alerts')])),
    ('pp-use', 'How we use your information', ul(['Run the app: billing, stock, udhaar, purchases, reports and accounts', 'Keep your devices, counters and branches in sync', 'Send invoices to FBR, only when you turn FBR on', 'Manage your plan, payments and invoices', 'Give support and train your staff when you ask', 'Keep the service safe and stop misuse or fraud', 'Send service messages, such as payment reminders and important changes', 'Send product news only if you agree. You can stop it any time.'])),
    ('pp-offline', 'Offline data on your devices', ul(['Your shop data is saved on your phone or PC so you can sell without internet. It uploads when you are back online.', 'Data that is lost, reset or uninstalled before it syncs cannot be recovered. Connect to the internet daily if you can.', 'Offline sign-in uses a one-way hash. Your password is not saved in plain text.', 'When you switch to another shop on the same device, the old shop\'s data is removed from that device.'])),
    ('pp-share', 'Who we share data with', '<p>We share data only with the services we need to run UpTrendPos, and only as much as they need:</p>'
     + table(['Who', 'Why'], [('Supabase (cloud database)', 'Stores your synced shop data and logins'), ('Google Firebase', 'Sends app notifications'), ('Hostinger', 'Hosts our website and web app'), ('SMS and OTP provider', 'Sends login and verification codes'), ('FBR', 'Receives your invoices, only when you turn FBR on'), ('People you add', 'Your staff see what their role allows'), ('Government and courts', 'Only when Pakistani law requires it, such as a lawful request under PECA 2016')])
     + '<p>If UpTrendPos is ever merged or sold, your data would move to the new owner under this same policy, and we would tell you first.</p>'),
    ('pp-whatsapp', 'WhatsApp, SMS and sharing', ul(['When you send a bill, statement or report on WhatsApp, it goes from your own phone through your own WhatsApp. WhatsApp\'s own privacy policy applies to that message.', 'Check the customer\'s number before you send. We cannot see or recall messages sent from your phone.', 'Login codes come by SMS. We never ask for your code by phone or chat.'])),
    ('pp-where', 'Where your data is stored', '<p>Our cloud providers may store data on servers outside Pakistan. They are large, well-known providers that protect data with strong security. We choose providers that keep each customer\'s data private and only process it for us.</p>'),
    ('pp-protect', 'How we protect your data', ul(['HTTPS encryption for all data sent between your device and our servers', 'Each shop\'s data is kept separate from every other shop at database level', 'Role-based staff access and PIN lock', 'Audit trail of deletes and changes (Enterprise and Custom plans)', 'Support access to a shop is limited and logged', 'Regular backups on the cloud, depending on your plan'])),
    ('pp-breach', 'If something goes wrong', '<p>If a security incident affects your data, we will tell the affected shops without undue delay. We will explain what happened, what data was affected and what you should do. We will also take steps to stop it from happening again.</p>'),
    ('pp-keep', 'How long we keep data', table(['Data', 'How long'], [('Shop records', 'While your account is active'), ('After you delete your account', 'Removed from live systems within 30 days. Backups clear on their normal cycle.'), ('Records the law requires', 'Kept as long as Pakistani law requires, for example invoices already reported to FBR'), ('Support chats and form messages', 'As long as needed to help you, then deleted'), ('Usage statistics', 'May be kept only in a form that does not identify you')])),
    ('pp-rights', 'Your rights and choices', ul(['<strong>See and export</strong> your records as PDF or CSV from the app', '<strong>Correct</strong> wrong details in the app or by asking us', '<strong>Delete</strong> your account from the app menu, or by email', '<strong>Stop</strong> product news and marketing messages any time', '<strong>Turn off</strong> app permissions in your device settings'])
     + '<p>To make a privacy request, email <a href="mailto:sales@uptrendpos.com?subject=Privacy%20request">sales@uptrendpos.com</a> with the subject "Privacy request" from your registered email or phone, and add your shop name. We may ask you to confirm it is you. We aim to reply within 30 days.</p>'),
    ('pp-yours', 'Your duty for customer and staff data', ul(['You decide what customer and staff data to save. Save only what you need.', 'Get permission where the law needs it, for example before saving CNIC copies or guarantor details.', 'Tell staff and customers how you use their data if they ask.', 'Remove data you no longer need.'])),
    ('pp-cookies', 'Cookies and browser storage', table(['Used for', 'Why'], [('Staying signed in', 'Keeps you logged in to the web app'), ('Offline data', 'Lets the web app keep working during short internet breaks'), ('Settings', 'Remembers your theme and screen choices'), ('One active tab', 'Stops two tabs from saving the same sale twice'), ('Website analytics', 'Counts visits so we can improve the website')]) + '<p>We do not use advertising or cross-site tracking cookies.</p>'),
    ('pp-kids', 'Children', '<p>UpTrendPos is for businesses. You must be 18 or older to create an account. We do not knowingly collect data from children. If you think a child has given us data, contact us and we will delete it.</p>'),
    ('pp-law', 'Pakistani law', '<p>We follow the laws of Pakistan, including the Prevention of Electronic Crimes Act 2016 and the Electronic Transactions Ordinance 2002. If a personal data protection law comes into force in Pakistan, we will update this policy to follow it.</p>'),
    ('pp-change', 'Changes to this policy', '<p>When we change this policy, we update the date at the top. For important changes, we tell you in the app or by email before they take effect.</p>'),
    ('pp-contact', 'Contact us', '<p>For any question about your privacy or your data, contact us:</p>' + CONTACT_BLOCK),
]
privacy_html = (hero('utp-legal', 'utp-privacy', 'Privacy Policy', 'Legal', 'UpTrendPos <span class="utp-hl">Privacy Policy</span>',
                     'This privacy policy explains, in simple words, what data UpTrendPos collects, why we need it, who we share it with and how you stay in control. Your shop data belongs to you.', updated_line())
                + doc(privacy, 'The short version', ['Your shop data is yours. We never sell it or use it for ads.', 'We collect only what we need to run the app and help you.', 'Each shop\'s data is kept separate and sent over HTTPS.', 'You can export your data or delete your account any time.', 'Questions? Email sales@uptrendpos.com or WhatsApp 0319 2223292.'],
                      [('Terms and Conditions', 'https://uptrendpos.com/terms-and-conditions/'), ('Support', 'https://uptrendpos.com/support/'), ('Contact us', 'https://uptrendpos.com/contact-us/')]))

# ======================================================================= TERMS
terms = [
    ('tc-agree', 'About these terms', '<p>These terms are an agreement between you and UpTrendPos, House No 193/A, Umer Block, Shadab Town, Sahiwal, Pakistan. They cover the UpTrendPos website, web app, Android app and Windows app, and every plan and service we provide.</p>' + ul(['By creating an account, starting a trial or using the app, you accept these terms and our <a href="https://uptrendpos.com/privacy-policy/">Privacy Policy</a>.', 'Accepting online is valid, in line with the Electronic Transactions Ordinance 2002.', 'If you use UpTrendPos for a business, you accept these terms for that business.'])),
    ('tc-who', 'Who can use UpTrendPos', ul(['You must be 18 years or older.', 'You must have the right to accept these terms for your business.', 'You must use UpTrendPos only for a lawful business in Pakistan or abroad.'])),
    ('tc-account', 'Your account and logins', ul(['Give correct details. Your verified mobile number becomes the shop owner login.', 'One verified mobile number can own one shop account. More branches go under the same account.', 'Each staff member should have their own login. Do not share logins or PINs.', 'You are responsible for everything done under your account, including by staff you add.', 'Tell us at once if you think someone is misusing your account.'])),
    ('tc-trial', 'Free trial and grace period', ul(['Every new shop gets a 14-day free trial of paid-plan features, once per verified mobile number and business.', 'When a trial or paid plan ends, you get a 5-day grace period with full access and reminders to renew.', 'If you do not renew, your shop moves to limited access with fewer invoices, users, branches and features. Your data is kept, and paying for a plan restores full access.', 'Making extra accounts to repeat the trial is not allowed. Such accounts may be merged or suspended.'])),
    ('tc-pay', 'Plans, setup fee and payments', ul(['Plans, limits and prices in Pakistani Rupees (PKR) are shown on our <a href="https://uptrendpos.com/pos-software-pricing/">pricing page</a> and in the app.', 'Monthly and yearly plans are paid in advance. Add-ons are charged when you add them.', 'A one-time setup fee covers onboarding: account setup, help loading your items and staff training. The amount is on your quote or invoice.', 'Payment methods, such as bank transfer, are shown on your invoice. Your plan starts after we confirm payment.', 'Any government tax that applies is shown on your invoice.', 'If we change prices, we tell you at least 30 days before. New prices apply from your next billing period.'])),
    ('tc-refund', 'Cancellation and refunds', ul(['You can cancel any time from the app or by contacting us.', 'After you cancel, paid features continue until the end of the period you already paid for.', 'Plan payments are non-refundable once the plan is active.', 'The setup fee is non-refundable once setup work has started.', 'If you were charged twice or by mistake, we refund it within 10 working days after we check it.'])),
    ('tc-offline', 'Working offline', ul(['You can keep selling without internet. Sales sync when you are back online.', 'Each device must connect at least once every 7 days on a paid plan, or every 3 days during the trial, to check the plan and sync.', 'A device that stays offline too long locks until it connects again. Data on the device is kept.', 'Changing the device date or time to get around these checks is not allowed and may lock the app.', 'These always need internet: udhaar (credit) sales and credit limits, FBR invoice reporting, adding users or branches, password resets and plan changes.'])),
    ('tc-branch', 'Counters, branches and invoice numbers', ul(['Each device works and syncs on its own.', 'A sale made offline gets a provisional number. Its final invoice number is given when it syncs, and numbers never repeat.', 'Two offline counters may sell the last unit of the same item. Stock can then go below zero for a short time, and the reports flag it for you to fix.', 'Unsynced sales on a lost, reset or uninstalled device cannot be recovered.'])),
    ('tc-data', 'Your data and records', ul(['You own your business data. We store and process it only to provide the service, as our Privacy Policy explains.', 'You are responsible for the prices, stock, taxes and accounts you enter.', 'Reports and accounting tools help you run your shop. They are not professional accounting, tax or legal advice.', 'Cloud backup depends on your plan. We recommend you export important records regularly.', 'If you leave, you can export your data. After an account is closed, you have 30 days to export before deletion.'])),
    ('tc-fbr', 'FBR integration', ul(['FBR integration is optional and comes with the Enterprise and Custom plans.', 'You must enter correct NTN, STRN, POS ID and token details, and keep your FBR registration active.', 'You are responsible for your FBR compliance and for the invoice data you send.', 'The FBR POS service fee on each bill is set by FBR, not by UpTrendPos.', 'We are not responsible for FBR penalties caused by wrong data, or for delays caused by FBR systems or your internet.', 'UpTrendPos is a software provider. We do not file tax returns for you.'])),
    ('tc-third', 'Hardware and other services', ul(['UpTrendPos is software. We do not sell, repair or guarantee printers, scanners, phones or computers, unless we say so in writing.', 'WhatsApp, SMS, FBR, internet and power are services from other companies. Their terms apply, and we are not responsible when they fail.', 'We tell you which devices work well, but the final choice of hardware is yours.'])),
    ('tc-use', 'Acceptable use', '<p>You must not use UpTrendPos to:</p>' + ul(['Sell goods or services that are illegal in Pakistan', 'Make fake invoices, hide sales or avoid taxes', 'Share logins, resell the service, copy the software or reverse-engineer it', 'Attack, overload or try to break the security of the service', 'Change device time or tamper with the app to get around limits', 'Send spam or harmful messages to customers through the app'])
     + '<p>We may suspend accounts that break these rules.</p>'),
    ('tc-service', 'Service, updates and support', ul(['We work to keep UpTrendPos available. Planned maintenance is kept short and announced in the app when possible.', 'Offline mode keeps your billing running during internet outages.', 'We improve the app often. Features may change, but we will not remove a core paid feature during a period you have paid for.', 'Support hours, channels and response targets are on our <a href="https://uptrendpos.com/support/">Support page</a>.'])),
    ('tc-close', 'Suspension and closing an account', ul(['You can close your account any time from the app or by contacting us.', 'We may suspend or close an account for serious or repeated breaches of these terms, fraud or misuse, or non-payment after the grace period. We warn you first where we can.', 'After closing, you have 30 days to export your data. Then it is deleted, except records the law requires us to keep.'])),
    ('tc-ip', 'Ownership of the software', ul(['The UpTrendPos software, name, logo, designs and content belong to UpTrendPos.', 'While your account is active, you get a limited, non-transferable right to use the software for your business.', 'If you send us ideas or feedback, we may use them to improve UpTrendPos without any duty to you.'])),
    ('tc-liability', 'Limits of our liability', ul(['UpTrendPos is provided "as is". We work hard to make it correct, but we cannot promise it will be free of every error.', 'We are not liable for indirect losses or lost profit, or for losses caused by lost or reset devices, unsynced data, internet or power failures, third-party hardware or services, or FBR penalties.', 'Our total liability for any claim is limited to the fees you paid us in the 3 months before the claim.', 'Nothing in these terms removes rights that Pakistani law does not allow us to remove.'])),
    ('tc-indemnity', 'Your promise to us', '<p>If someone makes a claim against UpTrendPos because of your illegal use of the service, or because of data you saved without permission, you agree to cover the losses and costs this causes us.</p>'),
    ('tc-force', 'Events outside our control', '<p>We are not responsible for delays or failures caused by events we cannot control. These include load-shedding, internet or mobile network outages, problems at FBR or other providers, government orders, strikes, natural disasters and similar events.</p>'),
    ('tc-change', 'Changes to these terms', ul(['We may update these terms from time to time and change the date at the top.', 'For important changes, we tell you in the app or by email at least 7 days before they take effect.', 'If you keep using UpTrendPos after that, you accept the new terms.'])),
    ('tc-law', 'Governing law and disputes', ul(['These terms are governed by the laws of Pakistan.', 'If you have a complaint, contact us first. We aim to solve it within 30 days.', 'If it is not solved, either side may take it to the competent courts of Pakistan.'])),
    ('tc-general', 'General', ul(['These terms, our Privacy Policy and your plan invoice are the full agreement between us.', 'If one part of these terms cannot be enforced, the rest still applies.', 'If we do not enforce a right at once, we have not given it up.', 'You may not transfer your account to someone else without our written approval.', 'We send notices in the app, by email or by WhatsApp to the details on your account.', 'These terms are written in English. Our team can explain them in Urdu.'])),
    ('tc-contact', 'Contact us', '<p>For any question about these terms, contact us:</p>' + CONTACT_BLOCK),
]
terms_html = (hero('utp-legal', 'utp-terms', 'Terms and Conditions', 'Legal', 'UpTrendPos <span class="utp-hl">Terms and Conditions</span>',
                   'These terms and conditions explain the rules for using UpTrendPos: your account, trial, plans and payments, offline use, FBR, your data and our responsibilities. Please read them before you start.', updated_line())
              + doc(terms, 'The short version', ['14-day free trial once per shop, then a 5-day grace period.', 'Plans are paid in advance. Payments are non-refundable once active.', 'Cancel any time. Paid features run until your paid period ends.', 'You own your data and can export it. You are responsible for prices, taxes and FBR data.', 'Pakistani law applies. Talk to us first if there is a problem.'],
                    [('Privacy Policy', 'https://uptrendpos.com/privacy-policy/'), ('Support', 'https://uptrendpos.com/support/'), ('Pricing', 'https://uptrendpos.com/pos-software-pricing/')]))

# ======================================================================= SUPPORT
ICON = {
    'wa': '<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2z"/>',
    'call': '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    'app': '<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2M10 8h4M10 11h4"/>',
    'sync': '<path d="M21 12a9 9 0 0 1-15.5 6.2M3 12A9 9 0 0 1 18.5 5.8"/><path d="M21 4v5h-5M3 20v-5h5"/>',
    'printer': '<path d="M6 9V3h12v6"/><rect x="3" y="9" width="18" height="8" rx="2"/><path d="M7 14h10v7H7z"/>',
    'lock': '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
    'wifi': '<path d="M5 12.5a10 10 0 0 1 14 0M8.5 16a5 5 0 0 1 7 0"/><circle cx="12" cy="19.5" r="1"/><path d="M3 3l18 18"/>',
    'qr': '<path d="M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h3v3h-3zM20 14v6h-3"/>',
    'scan': '<path d="M3 7V4h3M21 7V4h-3M3 17v3h3M21 17v3h-3M7 8v8M10 8v8M13 8v8M16 8v8"/>',
    'shield': '<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
}


def ico(n, c):
    return f'<div class="utp-ico sm {c}"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[n]}</svg></div>'


channels = [
    ('wa', 'g', 'WhatsApp', 'Fastest for most questions. Send screenshots and videos.', '0319 2223292', WA + '?text=Hi%2C%20I%20need%20help%20with%20UpTrendPos', 'sup_wa'),
    ('call', 'b', 'Phone', 'Talk to a person when billing has stopped.', '+92 319 2223292', 'tel:+923192223292', 'sup_call'),
    ('mail', 't', 'Email', 'Best for invoices, data requests and long questions.', 'sales@uptrendpos.com', 'mailto:sales@uptrendpos.com', 'sup_email'),
    ('app', 'y', 'In the app', 'Menu &gt; Help &amp; Support. Shop and device details go with your message.', 'Open the app', 'https://live.uptrendpos.com/', 'sup_app'),
]
ch_html = ''.join(f'''        <a class="utp-fcard utp-ct-card" href="{u}"{' target="_blank" rel="noopener"' if u.startswith('http') else ''} data-track="{tr}">
          {ico(i, c)}
          <h3>{h}</h3>
          <p>{p}</p>
          <span class="utp-ct-val">{v}</span>
        </a>
''' for i, c, h, p, v, u, tr in channels)

fixes = [
    ('sync', 'b', 'Sales are not syncing', ['Check the internet on that device', 'Open the app and wait on the home screen for a minute', 'Look for the sync banner and its message', 'Still stuck? Do not uninstall. Send us a screenshot.']),
    ('printer', 'y', 'Printer is not printing', ['Check paper, power and the cable or Bluetooth', 'On a phone, plug the Type-C cable in again', 'Select the printer again in print settings', 'Print a test receipt, then send us the model']),
    ('lock', 'n', 'Cannot log in', ['Owners: use Forgot Password on the login screen', 'Staff: ask the owner or admin to reset your PIN', 'Check the mobile number you are typing', 'Login needs internet the first time']),
    ('wifi', 't', 'App says offline too long', ['Connect the device to the internet', 'Open the app and let it check your plan', 'Do not change the phone date or time', 'Your data on the device is safe']),
    ('qr', 'g', 'FBR invoice not reported', ['FBR reporting needs internet', 'Check NTN, STRN, POS ID and token in FBR settings', 'Test in sandbox before production', 'Send us the invoice number and error']),
    ('scan', 'b', 'Scanner is not reading', ['Click inside the search box first', 'Try a different barcode to test', 'Re-plug the USB scanner', 'Check the barcode is saved on the item']),
]
fx_html = ''.join(f'''        <article class="utp-fgroup">
          <div class="utp-fgroup-head">{ico(i, c)}<h3>{h}</h3></div>
          <ol class="utp-steps-sm">{''.join(f'<li>{x}</li>' for x in l)}</ol>
        </article>
''' for i, c, h, l in fixes)

sup_faq = [
    ('What are your support hours?', 'Our support hours are Monday to Saturday, 10 am to 7 pm, Pakistan time. Messages sent on Sunday, public holidays or after hours are answered on the next working day. When billing has fully stopped, we handle it first.'),
    ('Is support free?', 'Yes. Support is included in every paid plan at no extra cost. That covers how-to questions, sync and printer help, FBR setup help and fixing problems in the app. Custom work, data entry for you and on-site visits are quoted separately if you need them.'),
    ('Can you help me set up my shop?', 'Yes. After you sign up, our team helps you add your items, connect your printer and scanner, set up staff logins and branches, and train your staff. Send your item list in Excel or a clear photo and we help you load it.'),
    ('How do I export my data or delete my account?', 'Export lists and reports as PDF or CSV from the app. To delete your account, the shop admin can use the app menu, or email us from your registered contact with your shop name. Export what you need first, because deleted data cannot be brought back.'),
    ('Do you give support in Urdu?', 'Yes. Our team supports you in Urdu and English on WhatsApp, phone and email. You can send voice notes, screenshots or short videos on WhatsApp, which is often the fastest way to show us the problem.'),
    ('Can you see my shop data when I ask for help?', 'Only when you ask for help and only what we need to fix the problem. Support access to a shop is limited and logged. We never ask for your password or login code. If someone asks for them, it is not us.'),
]
faq_html = ''.join(f'        <details{" open" if n == 0 else ""}>\n          <summary>{q}</summary>\n          <p>{a}</p>\n        </details>\n' for n, (q, a) in enumerate(sup_faq))

support_html = hero('utp-sup', 'utp-support', 'Support', 'Help center', 'UpTrendPos <span class="utp-hl">support</span>, in Urdu or English.',
                    'Get help with UpTrendPos on WhatsApp, phone or email. Our support team helps with setup, printers, sync, FBR and anything in the app. Support hours are Monday to Saturday, 10 am to 7 pm, Pakistan time.',
                    f'''      <div class="utp-cta">
        <a class="utp-btn utp-btn-primary" href="{WA}?text=Hi%2C%20I%20need%20help%20with%20UpTrendPos" target="_blank" rel="noopener" data-track="sup_hero_wa">{WA_SVG} WhatsApp support</a>
        <a class="utp-btn utp-btn-ghost" href="tel:+923192223292" data-track="sup_hero_call">Call 0319 2223292</a>
      </div>
      <ul class="utp-ticks">
        <li>Mon-Sat, 10 am-7 pm</li>
        <li>Urdu or English</li>
        <li>Included in every paid plan</li>
      </ul>
''') + f'''
  <section class="utp-sec" aria-labelledby="utp-ch-title">
    <div class="utp-wrap">
      <div class="utp-head">
        <span class="utp-eyebrow">Contact support</span>
        <h2 id="utp-ch-title">Four ways to reach the support team</h2>
        <p>The same team answers every channel. Pick the one that is easiest for you.</p>
      </div>
      <div class="utp-fgrid c4">
{ch_html}      </div>
    </div>
  </section>

  <section class="utp-sec utp-alt" aria-labelledby="utp-pr-title">
    <div class="utp-wrap">
      <div class="utp-head">
        <span class="utp-eyebrow">Hours and replies</span>
        <h2 id="utp-pr-title">Support hours and reply times</h2>
        <p>We answer the most serious problems first. These are our targets during support hours, Monday to Saturday, 10 am to 7 pm.</p>
      </div>
      <div class="utp-cmp-box utp-vs-box">
        <table class="utp-cmp utp-vs utp-prio">
          <caption class="utp-sr">Support priority levels and reply targets</caption>
          <thead><tr><th scope="col">Priority</th><th scope="col">Example</th><th scope="col" class="is-rec">First reply target</th></tr></thead>
          <tbody>
            <tr><th scope="row"><span class="utp-pill red">Urgent</span></th><td>Billing has stopped on all counters</td><td class="is-rec">Within 2 working hours</td></tr>
            <tr><th scope="row"><span class="utp-pill amber">High</span></th><td>Printer, sync or FBR problem on one device</td><td class="is-rec">Same working day</td></tr>
            <tr><th scope="row"><span class="utp-pill blue">Normal</span></th><td>How-to questions, reports, settings</td><td class="is-rec">Within 1 working day</td></tr>
            <tr><th scope="row"><span class="utp-pill grey">Request</span></th><td>New feature ideas and changes</td><td class="is-rec">Within 3 working days</td></tr>
          </tbody>
        </table>
      </div>
      <p class="utp-note">Sunday and public holidays: messages are answered on the next working day. Billing keeps working offline, so a short internet problem will not stop your shop.</p>
    </div>
  </section>

  <section class="utp-sec" aria-labelledby="utp-ready-title">
    <div class="utp-wrap utp-split">
      <div>
        <div class="utp-head left">
          <span class="utp-eyebrow">Before you contact us</span>
          <h2 id="utp-ready-title">Send these details for a faster fix</h2>
        </div>
        <p class="utp-body">With these details we can find your shop and the problem at once, without asking you again.</p>
        {ul(['Shop name and registered mobile number', 'Device: Android, Windows or web browser', 'App version (at the bottom of the app menu)', 'What you did and what happened', 'A screenshot or short video of the error', 'Invoice number, if the problem is with a bill'])}
      </div>
      <div class="utp-fgroup utp-fgroup-dark">
        <div class="utp-fgroup-head">{ico('shield', 'y')}<h3>Stay safe</h3></div>
        {ul(['We never ask for your password or login code', 'We never ask you to pay into a personal account', 'Our only support number is 0319 2223292', 'Report anything strange to sales@uptrendpos.com'])}
      </div>
    </div>
  </section>

  <section class="utp-sec utp-alt" aria-labelledby="utp-fix-title">
    <div class="utp-wrap">
      <div class="utp-head">
        <span class="utp-eyebrow">Quick fixes</span>
        <h2 id="utp-fix-title">Fix common problems in a minute</h2>
        <p>Try these steps first. If the problem stays, send us a WhatsApp message with a screenshot.</p>
      </div>
      <div class="utp-fgroups">
{fx_html}      </div>
    </div>
  </section>

  <section class="utp-sec" aria-labelledby="utp-scope-title">
    <div class="utp-wrap">
      <div class="utp-head">
        <span class="utp-eyebrow">What support covers</span>
        <h2 id="utp-scope-title">What our support includes</h2>
      </div>
      <div class="utp-duo">
        <article class="utp-fgroup">
          <div class="utp-fgroup-head">{ico('shield', 'g')}<h3>Included in every paid plan</h3></div>
          {ul(['Help to set up your shop, items, staff and branches', 'Printer, scanner and Type-C phone printer setup', 'Sync, offline and login problems', 'FBR setup help and testing', 'How-to questions about any screen', 'Staff training on billing, returns and udhaar', 'Fixing problems in the UpTrendPos app'])}
        </article>
        <article class="utp-fgroup">
          <div class="utp-fgroup-head">{ico('app', 'n')}<h3>Not included, or quoted separately</h3></div>
          {ul(['Repair of printers, scanners, phones or computers', 'Windows, Android or internet problems not caused by UpTrendPos', 'Entering your full product list or old records for you', 'Custom features made only for your shop', 'Visits to your shop, depending on your city', 'Tax, accounting or legal advice'])}
        </article>
      </div>
    </div>
  </section>

  <section class="utp-sec utp-alt" aria-labelledby="utp-data-title">
    <div class="utp-wrap">
      <div class="utp-head">
        <span class="utp-eyebrow">Your data</span>
        <h2 id="utp-data-title">Backup, export and account deletion</h2>
      </div>
      <ol class="utp-rep c2">
        <li><strong>Export</strong><span>Save lists and reports as PDF or CSV from the app, any time.</span></li>
        <li><strong>Backup</strong><span>Cloud backup depends on your plan. On Android and Windows, use Settings &amp; Data &gt; Backup &amp; Restore for a device backup.</span></li>
        <li><strong>Delete account</strong><span>The shop admin can delete the account from the app menu, or email us from the registered contact with the shop name.</span></li>
        <li><strong>After deletion</strong><span>Data is removed within 30 days, except records the law requires, such as invoices reported to FBR. Export first.</span></li>
      </ol>
      <p class="utp-note">Read how we handle your data in our <a class="utp-link" href="https://uptrendpos.com/privacy-policy/">Privacy Policy</a> and the rules of the service in our <a class="utp-link" href="https://uptrendpos.com/terms-and-conditions/">Terms and Conditions</a>.</p>
    </div>
  </section>

  <section class="utp-sec" aria-labelledby="utp-esc-title">
    <div class="utp-wrap">
      <div class="utp-band">
        <div>
          <span class="utp-eyebrow">Not solved?</span>
          <h2 id="utp-esc-title">Escalate a problem or share feedback</h2>
          <p>If your problem is not solved in the target time, email sales@uptrendpos.com with the subject "Escalation" and your shop name. A senior team member will take it over. Ideas for new features are welcome on the same email or WhatsApp.</p>
          <p>Found a security problem? Email us with the subject "Security". Please do not share it publicly until we fix it.</p>
        </div>
        <div class="utp-partner-cta">
          <a class="utp-btn utp-btn-primary" href="mailto:sales@uptrendpos.com?subject=Escalation" data-track="sup_escalate">Email an escalation</a>
          <small>Include your shop name and invoice numbers</small>
        </div>
      </div>
    </div>
  </section>

  <section class="utp-sec utp-alt" aria-labelledby="utp-faq-title">
    <div class="utp-wrap">
      <div class="utp-head">
        <span class="utp-eyebrow">FAQ</span>
        <h2 id="utp-faq-title">Support questions</h2>
      </div>
      <div class="utp-faq-list">
{faq_html}      </div>
    </div>
  </section>

  <section class="utp-final" aria-labelledby="utp-final-title">
    <div class="utp-wrap">
      <div class="utp-final-box">
        <h2 id="utp-final-title">Need help right now?</h2>
        <p>Send us a WhatsApp message with your shop name and a screenshot. We will take it from there.</p>
        <div class="utp-cta">
          <a class="utp-btn utp-btn-primary" href="{WA}?text=Hi%2C%20I%20need%20help%20with%20UpTrendPos" target="_blank" rel="noopener" data-track="sup_final_wa">WhatsApp support</a>
          <a class="utp-btn utp-btn-ghost" href="https://uptrendpos.com/contact-us/" data-track="sup_final_contact">Contact page</a>
        </div>
      </div>
    </div>
  </section>
</div>
'''

for name, html in [('website_privacy_v1', privacy_html), ('website_terms_v1', terms_html), ('website_support_v1', support_html)]:
    assert '<!--' not in html and '<style' not in html and '<script' not in html
    (P / f'{name}.html').write_text(html)
    txt = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', re.sub(r'<svg.*?</svg>', '', html, flags=re.S)))
    print(name, len(txt.split()), 'words')
