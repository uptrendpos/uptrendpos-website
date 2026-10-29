
(function () {
  'use strict';

  /* ===================== EDIT 1: LIVE PAGES =====================
     Add a page slug here on the day that page is designed and set to "index".
     Until then, links to it show as plain text (no click), so visitors never land on an empty page. */
  var UTP_LIVE_PAGES = [
    'industries',
    'grocery-store-pos-software',
    'pharmacy-pos-software',
    'fbr-pos-integration',
    'tailor-shop-pos-software',
    'mobile-shop-pos-software',
    'solar-shop-pos-software',
    'electronics-store-pos-software',
  ];

  /* ===================== EDIT 2: DOWNLOAD FILES =====================
     apk / exe : full file URL. Leave '' and the button shows "Coming soon". */
  var UTP_LINKS = {
    apk: 'https://uptrendpos.com/downloadapk/app-release.apk',
    apkVersion: '',     /* e.g. '1.0.0' */
    apkSize: '',        /* e.g. '58 MB' */
    apkMinAndroid: '',  /* e.g. 'Android 8.0 or newer' */
    exe: 'https://uptrendpos.com/wp-content/uploads/UpTrendPOS_Setup_1.0.0.zip',
    exeVersion: '',
    exeSize: '',
    updated: ''         /* e.g. '12 Oct 2026' */
  };
  /* ================================================================== */

  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  ready(function () {
    /* Global footer (works on every page, also pages without our page design) */
    var foot = document.querySelector('.utp-foot');
    if (foot) {
      foot.querySelectorAll('[data-utp-year]').forEach(function (y) { y.textContent = new Date().getFullYear(); });
      foot.querySelectorAll('a[data-page]').forEach(function (a) {
        if (UTP_LIVE_PAGES.indexOf(a.getAttribute('data-page')) !== -1) return;
        var sp = document.createElement('span');
        sp.innerHTML = a.innerHTML;
        a.parentNode.replaceChild(sp, a);
      });
      foot.querySelectorAll('a').forEach(function (a) {
        a.addEventListener('click', function () {
          var h = a.getAttribute('href') || '';
          var kind = a.getAttribute('data-track') || (h.indexOf('tel:') === 0 ? 'footer_call' : (h.indexOf('mailto:') === 0 ? 'footer_email' : 'footer_link'));
          window.dataLayer = window.dataLayer || [];
          window.dataLayer.push({ event: (h.indexOf('tel:') === 0 || h.indexOf('mailto:') === 0 || h.indexOf('wa.me/') !== -1) ? 'utp_contact_click' : 'utp_cta_click', utp_target: kind, utp_page: location.pathname });
        });
      });
    }

    var root = document.querySelector('.utp');
    if (!root) return;

    /* Full width, no white gap above the page, and the right space under an overlay header.
       Waits for the header logo to load, then re-checks whenever the header changes size, so content never jumps onto the logo. */
    var HSEL = 'header, .elementor-location-header, [data-elementor-type="header"], [data-elementor-type="jkit-header"], .jkit-header, #masthead, .site-header';
    function headers() {
      var list = [];
      document.querySelectorAll(HSEL).forEach(function (h) {
        if (root.contains(h) || h.contains(root) || !h.offsetHeight) return;
        list.push(h);
      });
      return list;
    }
    function headerImagesReady(list) {
      for (var i = 0; i < list.length; i++) {
        var imgs = list[i].querySelectorAll('img');
        for (var j = 0; j < imgs.length; j++) {
          if (!imgs[j].complete) return false;
        }
      }
      return true;
    }
    var pageLoaded = document.readyState === 'complete';
    function layout() {
      root.style.setProperty('--utp-vw', document.documentElement.clientWidth + 'px');
      var list = headers();
      if (!pageLoaded && !headerImagesReady(list)) return;
      root.style.marginTop = '';
      var sy = window.scrollY;
      var top = root.getBoundingClientRect().top + sy;
      var hTop = Infinity, hBottom = 0;
      list.forEach(function (h) {
        var r = h.getBoundingClientRect();
        var fixed = getComputedStyle(h).position === 'fixed';
        var t = fixed ? r.top : r.top + sy;
        var b = fixed ? r.bottom : r.bottom + sy;
        if (t > top + 300) return;
        if (t < hTop) hTop = t;
        if (b > hBottom) hBottom = b;
      });
      if (hBottom === 0) return;
      if (hBottom > top + 4) {
        var gap = Math.round(top - hTop);
        if (gap > 0 && gap < 300) root.style.marginTop = (-gap) + 'px';
        root.style.setProperty('--utp-top', Math.round(hBottom - Math.min(hTop, top) + 40) + 'px');
      } else {
        root.style.setProperty('--utp-top', '56px');
      }
      root.classList.add('utp-ready');
    }
    layout();
    window.addEventListener('load', function () { pageLoaded = true; layout(); });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(layout);
    headers().forEach(function (h) {
      h.querySelectorAll('img').forEach(function (im) {
        if (!im.complete) { im.addEventListener('load', layout); im.addEventListener('error', layout); }
      });
      if (window.ResizeObserver) new ResizeObserver(function () { layout(); }).observe(h);
    });
    var rt;
    window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(layout, 100); });

    /* Endless scroll strips: copies are added here (hidden from screen readers), so the page text is not repeated */
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (!reduce) {
      root.querySelectorAll('.utp-marquee').forEach(function (box) {
        var track = box.querySelector('.utp-mq-track');
        if (!track || track.getAttribute('data-ready')) return;
        var items = Array.prototype.slice.call(track.children);
        function addCopy() {
          items.forEach(function (li) {
            var c = li.cloneNode(true);
            c.setAttribute('aria-hidden', 'true');
            c.querySelectorAll('img').forEach(function (im) { im.setAttribute('alt', ''); });
            c.querySelectorAll('a').forEach(function (a) { a.setAttribute('tabindex', '-1'); });
            track.appendChild(c);
          });
        }
        var guard = 0;
        while (track.scrollWidth < box.offsetWidth && guard < 10) { addCopy(); guard++; }
        var half = Array.prototype.slice.call(track.children);
        half.forEach(function (li) {
          var c = li.cloneNode(true);
          c.setAttribute('aria-hidden', 'true');
          c.querySelectorAll('img').forEach(function (im) { im.setAttribute('alt', ''); });
          track.appendChild(c);
        });
        track.style.setProperty('--utp-mq', Math.max(20, Math.round(track.scrollWidth / 2 / 45)) + 's');
        track.setAttribute('data-ready', '1');
      });
    }

    /* Links to pages that are not live yet become plain text (or are hidden) */
    root.querySelectorAll('a[data-page]').forEach(function (a) {
      var slug = a.getAttribute('data-page');
      if (UTP_LIVE_PAGES.indexOf(slug) !== -1) return;
      if (a.hasAttribute('data-hide-until-live')) { a.parentNode.removeChild(a); return; }
      var s = document.createElement('span');
      s.className = a.className;
      s.innerHTML = a.innerHTML;
      a.parentNode.replaceChild(s, a);
    });

    /* Device detection (used by the downloads page) */
    var ua = navigator.userAgent || '';
    var os = 'other';
    if (/Android/i.test(ua)) os = 'android';
    else if (/iPhone|iPad|iPod/i.test(ua) || (/Macintosh/i.test(ua) && navigator.maxTouchPoints > 1)) os = 'ios';
    else if (/Windows/i.test(ua)) os = 'windows';

    var isDl = root.id === 'utp-downloads';
    var target = 'web';

    if (isDl) {
      var L = UTP_LINKS;
      var meta = function (v, s) {
        var p = [];
        if (v) p.push('Version ' + v);
        if (s) p.push(s);
        if (L.updated) p.push('Updated ' + L.updated);
        return p.join(' · ');
      };
      ['apk', 'exe'].forEach(function (key) {
        root.querySelectorAll('[data-dl="' + key + '"]').forEach(function (a) {
          if (L[key]) {
            a.setAttribute('href', L[key]);
            a.removeAttribute('aria-disabled');
          } else {
            a.setAttribute('href', '#utp-get');
            a.setAttribute('aria-disabled', 'true');
            a.textContent = 'Coming soon';
          }
        });
      });
      var mApk = root.querySelector('[data-meta="apk"]');
      var mExe = root.querySelector('[data-meta="exe"]');
      if (mApk) mApk.textContent = meta(L.apkVersion, L.apkSize);
      if (mExe) mExe.textContent = meta(L.exeVersion, L.exeSize);
      var rApk = root.querySelector('[data-req="apk"]');
      if (rApk && L.apkMinAndroid) rApk.textContent = L.apkMinAndroid;

      if (os === 'android' && L.apk) target = 'apk';
      if (os === 'windows' && L.exe) target = 'exe';

      var smart = document.getElementById('utp-smart');
      var smartText = document.getElementById('utp-smart-text');
      var smartNote = document.getElementById('utp-smart-note');
      if (smart && smartText) {
        if (target === 'apk') {
          smart.href = L.apk;
          smartText.textContent = 'Download for Android';
          if (smartNote) smartNote.textContent = (meta(L.apkVersion, L.apkSize) || 'Android APK') + ' · 14-day free trial';
        } else if (target === 'exe') {
          smart.href = L.exe;
          smartText.textContent = 'Download for Windows';
          if (smartNote) smartNote.textContent = (meta(L.exeVersion, L.exeSize) || 'Windows 10 / 11') + ' · 14-day free trial';
        }
      }
      if (os === 'ios') {
        var ios = document.getElementById('utp-ios');
        if (ios) ios.classList.add('is-rec');
      } else {
        var recKey = target === 'apk' ? 'android' : (target === 'exe' ? 'windows' : 'web');
        var card = root.querySelector('.utp-card[data-os="' + recKey + '"]');
        if (card) card.classList.add('is-rec');
      }
    }

    /* Tabs */
    var tabs = root.querySelectorAll('[role="tab"]');
    function openTab(name) {
      tabs.forEach(function (t) {
        var on = t.getAttribute('data-tab') === name;
        t.setAttribute('aria-selected', on ? 'true' : 'false');
        var pan = document.getElementById(t.getAttribute('aria-controls'));
        if (pan) pan.hidden = !on;
      });
    }
    tabs.forEach(function (t) {
      t.addEventListener('click', function () { openTab(t.getAttribute('data-tab')); });
    });
    if (tabs.length) {
      var want = os === 'android' ? 'android' : (os === 'windows' ? 'windows' : 'web');
      var has = root.querySelector('[role="tab"][data-tab="' + want + '"]');
      openTab(has ? want : tabs[0].getAttribute('data-tab'));
    }

    /* Pricing: monthly / yearly switch. Each price holds both values in data-m and data-y */
    var billBtns = root.querySelectorAll('[data-bill]');
    function setBill(mode) {
      billBtns.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-bill') === mode ? 'true' : 'false'); });
      root.querySelectorAll('.utp-amt[data-' + mode + '], .utp-bill-note[data-' + mode + ']').forEach(function (el) {
        el.textContent = el.getAttribute('data-' + mode);
      });
    }
    billBtns.forEach(function (b) {
      b.addEventListener('click', function () {
        setBill(b.getAttribute('data-bill'));
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({ event: 'utp_cta_click', utp_target: 'billing_' + b.getAttribute('data-bill'), utp_page: location.pathname });
      });
    });

    /* Branded images: no right-click save or drag (light protection; the watermark is the real one) */
    root.querySelectorAll('.utp-hw-card img, .utp-hero-img img').forEach(function (im) {
      im.addEventListener('contextmenu', function (e) { e.preventDefault(); });
      im.addEventListener('dragstart', function (e) { e.preventDefault(); });
    });

    /* Contact page: move the Fluent Forms widget (placed right under this HTML widget) into the designed form card */
    var slot = root.querySelector('#utp-form-slot');
    if (slot && !document.body.classList.contains('elementor-editor-active')) {
      var ff = document.querySelector('.fluentform_wrapper_' + (slot.getAttribute('data-form-id') || '1'));
      if (ff && root.contains(ff)) ff = null;
      if (!ff) document.querySelectorAll('.fluentform').forEach(function (f) { if (!ff && !root.contains(f)) ff = f; });
      if (ff) {
        var holder = ff.closest('.elementor-widget');
        slot.innerHTML = '';
        slot.appendChild(ff);
        if (holder && !holder.contains(root)) holder.style.display = 'none';
      }
    }

    /* FBR page: Tier-1 checker (message + WhatsApp text follow the ticks) */
    root.querySelectorAll('[data-utp-checker]').forEach(function (box) {
      var msg = box.querySelector('.utp-check-msg');
      var res = box.querySelector('.utp-check-result');
      var wa = box.querySelector('[data-utp-check-wa]');
      var base = wa ? wa.getAttribute('href').split('?text=')[0] : '';
      var upd = function () {
        var on = [];
        box.querySelectorAll('input[type="checkbox"]:checked').forEach(function (c) { on.push(c.value); });
        if (msg) msg.textContent = msg.getAttribute(on.length ? 'data-yes' : 'data-none');
        if (res) res.classList.toggle('is-yes', on.length > 0);
        if (wa) {
          var t = on.length ? 'Hi, I checked the Tier-1 list on your website. True for my shop: ' + on.join(', ') + '. I need FBR POS integration.' : 'Hi, I checked the Tier-1 list on your website and need help with FBR POS integration';
          wa.setAttribute('href', base + '?text=' + encodeURIComponent(t));
        }
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({ event: 'utp_tier1_check', utp_ticks: on.length, utp_page: location.pathname });
      };
      box.addEventListener('change', upd);
    });

    /* Lead tracking: every WhatsApp, call and email link on the page, even without data-track (map to GA4 key events in GTM) */
    root.querySelectorAll('a[href^="tel:"], a[href^="mailto:"], a[href*="wa.me/"]').forEach(function (a) {
      if (a.hasAttribute('data-track')) return;
      a.addEventListener('click', function () {
        var h = a.getAttribute('href') || '';
        var kind = h.indexOf('tel:') === 0 ? 'call' : (h.indexOf('mailto:') === 0 ? 'email' : 'whatsapp');
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({ event: 'utp_contact_click', utp_target: kind, utp_page: location.pathname });
      });
    });

    /* Click tracking for Google Tag Manager */
    root.querySelectorAll('[data-track]').forEach(function (a) {
      a.addEventListener('click', function () {
        if (a.getAttribute('aria-disabled') === 'true') return;
        var t = a.getAttribute('data-track');
        if (a.id === 'utp-smart') t = 'hero_' + target;
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({ event: isDl ? 'utp_download_click' : 'utp_cta_click', utp_target: t, utp_page: location.pathname });
      });
    });
  });
})();
