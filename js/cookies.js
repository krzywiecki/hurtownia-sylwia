/* Minimal cookie notice. Choice: localStorage "cookie-consent" = "all" | "necessary".
   Load optional scripts (e.g. analytics) only when cookieConsent() === "all"
   or on the "cookieconsent" event. */
(function () {
  var KEY = 'cookie-consent';
  function get() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function set(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }
  window.cookieConsent = get;

  var box;
  function hide() {
    if (!box) return;
    box.classList.remove('in');
    setTimeout(function () { box && box.remove(); box = null; }, 300);
  }
  function choose(v) {
    set(v);
    hide();
    document.dispatchEvent(new CustomEvent('cookieconsent', { detail: v }));
  }
  function show() {
    if (box) return;
    box = document.createElement('div');
    box.className = 'cookie';
    box.setAttribute('role', 'region');
    box.setAttribute('aria-label', 'Pliki cookie');
    box.innerHTML =
      '<p>Używamy plików cookie, żeby strona działała sprawnie.</p>' +
      '<div class="cookie-btns">' +
      '<button type="button" class="cookie-ok">OK</button>' +
      '<button type="button" class="cookie-min">Tylko niezbędne</button>' +
      '</div>';
    box.querySelector('.cookie-ok').onclick = function () { choose('all'); };
    box.querySelector('.cookie-min').onclick = function () { choose('necessary'); };
    document.body.appendChild(box);
    requestAnimationFrame(function () { requestAnimationFrame(function () { box.classList.add('in'); }); });
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('[data-cookie-settings]');
    if (a) { e.preventDefault(); show(); }
  });
  if (!get()) setTimeout(show, 1200);
})();
