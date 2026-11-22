/* Hurtownia Sylwia – client ordering PWA (no backend yet: orders are stored on the device). */
(() => {
  "use strict";

  const KEY = { orders: "sylwia.orders.v1", cart: "sylwia.cart.v1", profile: "sylwia.profile.v1" };
  const byId = Object.fromEntries(PRODUCTS.map(p => [p.id, p]));
  const $view = document.getElementById("view");
  const $bar = document.getElementById("cartbar");
  const $sheet = document.getElementById("sheet");
  const $toast = document.getElementById("toast");

  // ---------- storage ----------
  const load = (k, d) => { try { const v = JSON.parse(localStorage.getItem(k)); return v ?? d; } catch { return d; } };
  const save = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch { /* storage unavailable */ } };

  let orders = load(KEY.orders, []);          // newest first
  let cart = load(KEY.cart, { items: {}, delivery: null, time: "8:00", note: "" });
  let profile = load(KEY.profile, { company: "" });
  const persistCart = () => { save(KEY.cart, cart); renderBar(); };

  // ---------- helpers ----------
  const esc = s => String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const num = n => Number(n).toLocaleString("pl-PL", { maximumFractionDigits: 2 });
  const money = n => Number(n).toLocaleString("pl-PL", { style: "currency", currency: "PLN", maximumFractionDigits: 0 });
  const money2 = n => Number(n).toLocaleString("pl-PL", { style: "currency", currency: "PLN", minimumFractionDigits: 2 });
  const price = p => p.price * CLIENT.priceFactor;
  const unitLabel = (u, q) => {
    if (u === "karton") return q === 1 ? "karton" : (q % 10 >= 2 && q % 10 <= 4 && (q % 100 < 10 || q % 100 >= 20) ? "kartony" : "kartonów");
    if (u === "doniczka") return q === 1 ? "doniczka" : (q % 10 >= 2 && q % 10 <= 4 && (q % 100 < 10 || q % 100 >= 20) ? "doniczki" : "doniczek");
    if (u === "pęczek") return q === 1 ? "pęczek" : (q % 10 >= 2 && q % 10 <= 4 && (q % 100 < 10 || q % 100 >= 20) ? "pęczki" : "pęczków");
    return u;
  };
  const qtyText = (q, u) => `${num(q)} ${unitLabel(u, q)}`;
  const pic = (p, extra = "") => `<div class="pic ${extra}">${p.img ? `<img src="${p.img}" alt="" loading="lazy">` : `<span aria-hidden="true">${p.emoji}</span>`}${p.peeled && !extra ? '<span class="peeled">obrane</span>' : ""}</div>`;
  const cartLines = () => Object.entries(cart.items).filter(([id]) => byId[id]);
  const cartTotal = () => cartLines().reduce((s, [id, it]) => s + price(byId[id]) * it.qty, 0);
  const toast = msg => { $toast.textContent = msg; $toast.classList.add("show"); clearTimeout(toast.t); toast.t = setTimeout(() => $toast.classList.remove("show"), 2200); };

  const dayName = d => d.toLocaleDateString("pl-PL", { weekday: "long" });
  const dateShort = d => d.toLocaleDateString("pl-PL", { day: "numeric", month: "long" });
  const iso = d => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
  const fromIso = s => { const [y, m, d] = s.split("-").map(Number); return new Date(y, m - 1, d); };
  const addDays = n => { const d = new Date(); d.setHours(0, 0, 0, 0); d.setDate(d.getDate() + n); return d; };

  // ---------- "smart" memory: built from saved orders ----------
  function memory() {
    const last = {}, count = {};
    for (const o of orders) {               // newest first → first hit is the latest qty
      for (const it of o.items) {
        if (!(it.id in last)) last[it.id] = it;
        count[it.id] = (count[it.id] || 0) + 1;
      }
    }
    const favourites = Object.keys(count).filter(id => byId[id]).sort((a, b) => count[b] - count[a]);
    return { last, count, favourites };
  }

  function loadOrderIntoCart(order) {
    cart.items = {};
    for (const it of order.items) if (byId[it.id]) cart.items[it.id] = { qty: it.qty, note: it.note || "" };
    persistCart();
  }

  // ---------- router ----------
  let catState = { cat: null, q: "" };
  let justSent = null;
  function route() {
    const h = location.hash.replace(/^#\/?/, "");
    const [page, arg] = h.split("/");
    if (page === "katalog") renderCatalog();
    else if (page === "koszyk") renderCart();
    else if (page === "zamowienie" && arg) renderOrder(arg);
    else renderHome();
    renderBar();
    window.scrollTo(0, 0);
  }
  window.addEventListener("hashchange", route);

  // ---------- views ----------
  function renderHome() {
    const last = orders[0];
    const hello = profile.company ? `Dzień dobry, ${esc(profile.company)}!` : "Dzień dobry!";
    let html = `<h1>${hello}</h1><p class="muted">Co dziś zamawiamy?</p>`;

    if (last) {
      const shown = last.items.slice(0, 6);
      html += `<section class="card repeat stack">
        <div class="label">Twoje ostatnie zamówienie</div>
        <div class="muted small">${dateShort(new Date(last.createdAt))} · ${last.items.length} poz.</div>
        <ul>${shown.map(it => `<li><span>${esc(byId[it.id]?.name || it.name)}</span><b>${qtyText(it.qty, it.unit)}</b></li>`).join("")}
        ${last.items.length > shown.length ? `<li class="muted"><span>…i ${last.items.length - shown.length} więcej</span></li>` : ""}</ul>
        <button class="btn btn-green" data-act="repeat" data-id="${last.id}">↻ Zamów to samo</button>
        <p class="muted small" style="margin:0">Ilości możesz zmienić przed wysłaniem.</p>
      </section>`;
    }

    html += `<div class="stack" style="margin-top:16px">
      <a href="#/katalog" class="btn ${last ? "btn-ghost" : "btn-red"}">${cartLines().length ? "Dokończ zamówienie" : "+ Nowe zamówienie"}</a>
    </div>`;

    if (orders.length) {
      html += `<h2>Historia zamówień</h2>` + orders.slice(0, 15).map(o => `
        <a class="card history-item" href="#/zamowienie/${o.id}">
          <div><div class="when">${dateShort(new Date(o.createdAt))}</div>
          <div class="muted small">${o.items.length} poz. · dostawa ${dayName(fromIso(o.delivery))} ${dateShort(fromIso(o.delivery))}</div></div>
          <span class="chev" aria-hidden="true">›</span>
        </a>`).join("");
    } else {
      html += `<p class="muted center" style="margin-top:28px">Twoje zamówienia pojawią się tutaj.<br>Następnym razem wystarczy jedno kliknięcie, żeby zamówić to samo.</p>`;
    }
    $view.innerHTML = html;
  }

  function renderCatalog() {
    const mem = memory();
    const cats = [...(mem.favourites.length ? [{ id: "fav", name: "Twoje produkty", icon: "⭐" }] : []), ...CATEGORIES];
    if (!catState.cat || !cats.some(c => c.id === catState.cat)) catState.cat = cats[0].id;

    const showBanner = !cartLines().length && orders.length;
    $view.innerHTML = `
      <div class="searchbar">
        <input class="search" type="search" placeholder="Szukaj, np. pomidor" value="${esc(catState.q)}" aria-label="Szukaj produktu" enterkeyhint="search">
        <div class="cats" role="toolbar" aria-label="Kategorie">${cats.map(c =>
          `<button class="cat" data-cat="${c.id}" aria-pressed="${c.id === catState.cat}">${c.icon} ${c.name}</button>`).join("")}</div>
      </div>
      ${showBanner ? `<div class="banner"><p>Zacząć od ostatniego zamówienia? Wczytamy te same produkty i ilości.</p>
        <button class="btn btn-green" data-act="repeat" data-id="${orders[0].id}">↻ Wczytaj ostatnie</button></div>` : ""}
      <div class="grid" id="grid"></div>`;
    const input = $view.querySelector(".search");
    input.addEventListener("input", () => { catState.q = input.value; drawGrid(); });
    drawGrid();

    function drawGrid() {
      const q = catState.q.trim().toLowerCase();
      let list;
      if (q) list = PRODUCTS.filter(p => p.name.toLowerCase().includes(q));
      else if (catState.cat === "fav") list = mem.favourites.map(id => byId[id]);
      else list = PRODUCTS.filter(p => p.cat === catState.cat);
      const grid = document.getElementById("grid");
      grid.innerHTML = list.length ? list.map(p => {
        const inCart = cart.items[p.id];
        const last = mem.last[p.id];
        return `<button class="tile${inCart ? " in" : ""}" data-prod="${p.id}">
          ${pic(p)}
          ${inCart ? `<span class="qty-badge">${qtyText(inCart.qty, p.unit)}</span>` : ""}
          <div class="tile-body">
            <div class="tile-name">${esc(p.name)}</div>
            <div class="tile-price">${money2(price(p))} / ${p.unit}</div>
            ${last && !inCart ? `<div class="tile-last">Ostatnio: ${qtyText(last.qty, p.unit)}</div>` : ""}
          </div></button>`;
      }).join("") : `<p class="empty" style="grid-column:1/-1">Nie znaleźliśmy „${esc(catState.q)}”.<br>Zadzwoń – sprawdzimy, czy mamy.</p>`;
    }
    renderCatalog.redraw = drawGrid;
  }

  function renderCart() {
    const lines = cartLines();
    if (!lines.length) {
      $view.innerHTML = `<a href="#/katalog" class="back">‹ Produkty</a><h1>Koszyk</h1>
        <p class="empty">Koszyk jest pusty.</p><a href="#/katalog" class="btn btn-red">Wybierz produkty</a>`;
      return;
    }
    if (!cart.delivery || fromIso(cart.delivery) < addDays(1)) cart.delivery = iso(addDays(1));
    const opts = [1, 2, 3].map(addDays);
    const chosenIsPreset = opts.some(d => iso(d) === cart.delivery);
    const hours = ["6:00", "7:00", "8:00", "9:00", "10:00", "12:00", "14:00"];

    $view.innerHTML = `<a href="#/katalog" class="back">‹ Dodaj produkty</a>
      <h1>Twoje zamówienie</h1>
      <p class="muted small" style="margin-top:0">Dotknij pozycji, żeby zmienić ilość.</p>
      ${lines.map(([id, it]) => { const p = byId[id]; return `
        <div class="line" data-prod="${id}" role="button" tabindex="0" aria-label="Zmień: ${esc(p.name)}">
          ${pic(p, "sm")}
          <div class="line-main">
            <div class="line-name">${esc(p.name)}</div>
            ${it.note ? `<div class="line-note">${esc(it.note)}</div>` : ""}
          </div>
            <div class="line-row">
              <div class="stepper">
                <button class="stp" data-act="dec" data-id="${id}" aria-label="Mniej: ${esc(p.name)}" ${it.qty - 1 <= 0 ? "disabled" : ""}>−</button>
                <b class="line-qty">${qtyText(it.qty, p.unit)}</b>
                <button class="stp" data-act="inc" data-id="${id}" aria-label="Więcej: ${esc(p.name)}">+</button>
              </div>
              <span class="line-price">${money(price(p) * it.qty)}</span>
            </div>
          <button class="line-del" data-act="del" data-id="${id}" aria-label="Usuń: ${esc(p.name)}">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 3h6l1 2h4v2H4V5h4zm-3 6h12l-1 12H7zm4 2v8h2v-8zm4 0v8h2v-8z"/></svg>
          </button>
        </div>`; }).join("")}

      <a href="#/katalog" class="btn btn-ghost add-more">+ Dodaj produkty</a>

      <label class="field"><span>Dzień dostawy</span></label>
      <div class="seg">${opts.map((d, i) => `<button data-day="${iso(d)}" aria-pressed="${iso(d) === cart.delivery}">${i === 0 ? "Jutro" : dayName(d)}<small>${d.getDate()}.${String(d.getMonth() + 1).padStart(2, "0")}</small></button>`).join("")}</div>
      <label class="field"><span>…lub inny dzień</span><input type="date" id="dday" min="${iso(addDays(1))}" value="${chosenIsPreset ? "" : cart.delivery}"></label>
      <label class="field"><span>Od której godziny ktoś będzie na miejscu?</span>
        <select id="dtime">${hours.map(h => `<option ${h === cart.time ? "selected" : ""}>${h}</option>`).join("")}</select></label>
      <label class="field"><span>Uwagi do zamówienia</span><textarea id="dnote" rows="2" placeholder="np. wejście od zaplecza">${esc(cart.note)}</textarea></label>
      <label class="field"><span>Nazwa lokalu / firmy</span><input id="dcomp" autocomplete="organization" placeholder="np. Berlin Doner Kebap, Galeria Piastów" value="${esc(profile.company)}"></label>

      <div class="total"><span>Razem (szac.)</span><span id="ctotal">${money(cartTotal())}</span></div>
      <p class="muted small" style="margin-top:0">Ceny według Twojego cennika. Kwota końcowa wg wagi na fakturze.</p>
      <button class="btn btn-red" data-act="submit" style="margin-top:12px">Wyślij zamówienie ✓</button>
      <button class="btn btn-light" data-act="clear" style="margin-top:10px">Wyczyść koszyk</button>`;

    $view.querySelector("#dday").addEventListener("change", e => { if (e.target.value) { cart.delivery = e.target.value; persistCart(); renderCart(); } });
    $view.querySelector("#dtime").addEventListener("change", e => { cart.time = e.target.value; persistCart(); });
    $view.querySelector("#dnote").addEventListener("input", e => { cart.note = e.target.value; persistCart(); });
    $view.querySelector("#dcomp").addEventListener("input", e => { profile.company = e.target.value.trim(); save(KEY.profile, profile); });
  }

  function renderOrder(id) {
    const o = orders.find(x => x.id === id);
    if (!o) { location.hash = "#/"; return; }
    const fresh = justSent === id;
    const d = fromIso(o.delivery);
    $view.innerHTML = `${fresh ? `<div class="done-icon" aria-hidden="true">✓</div><h1 class="center">Zamówienie zapisane!</h1>
        <p class="center muted">Dziękujemy. Dostawa: <b>${dayName(d)} ${dateShort(d)}</b>, od godz. ${o.time}.</p>`
      : `<a href="#/" class="back">‹ Start</a><h1>Zamówienie z ${dateShort(new Date(o.createdAt))}</h1>
        <p class="muted" style="margin-top:0">Dostawa: ${dayName(d)} ${dateShort(d)}, od godz. ${o.time}</p>`}
      <div class="card">${o.items.map(it => `<div style="display:flex;justify-content:space-between;gap:10px;padding:6px 0;border-bottom:1px dashed var(--line)">
        <span>${esc(it.name)}${it.note ? `<br><i class="muted small">${esc(it.note)}</i>` : ""}</span><b style="white-space:nowrap">${qtyText(it.qty, it.unit)}</b></div>`).join("")}
        ${o.note ? `<p class="muted small" style="margin:10px 0 0">Uwagi: ${esc(o.note)}</p>` : ""}
        <div class="total" style="margin-bottom:0"><span>Razem (szac.)</span><span>${money(o.total)}</span></div>
      </div>
      <div class="stack" style="margin-top:16px">
        <button class="btn btn-green" data-act="repeat" data-id="${o.id}">↻ Zamów to samo jeszcze raz</button>
        <a href="#/" class="btn btn-ghost">Wróć na start</a>
      </div>`;
    justSent = null;
  }

  function renderBar() {
    const lines = cartLines();
    const onCart = /^#\/koszyk/.test(location.hash) || /^#\/zamowienie/.test(location.hash);
    if (!lines.length || onCart) { $bar.hidden = true; return; }
    $bar.hidden = false;
    $bar.innerHTML = `<span>Koszyk: ${lines.length} poz.<small>ok. ${money(cartTotal())}</small></span><span class="go">Dalej ›</span>`;
  }

  // ---------- quantity sheet ----------
  function openSheet(id) {
    const p = byId[id];
    const mem = memory();
    const last = mem.last[id];
    const cur = cart.items[id];
    let val = cur ? String(cur.qty).replace(".", ",") : "";
    const steps = p.unit === "kg" ? [1, 5, 10, 25] : [1, 2, 5, 10];

    $sheet.innerHTML = `<div class="sheet-inner">
      <div class="sheet-head">${pic(p, "sm")}<div><h3>${esc(p.name)}</h3><div class="muted">${money2(price(p))} / ${p.unit}</div></div>
        <button class="sheet-close" data-s="close" aria-label="Zamknij">×</button></div>
      <label class="display"><input class="num" id="snum" type="text" inputmode="decimal" autocomplete="off" enterkeyhint="done" placeholder="0" aria-label="Ilość"><span class="unit" id="sunit"></span></label>
      ${last ? `<div class="chips"><button class="chip chip-last" data-s="set" data-v="${last.qty}">Jak ostatnio: ${qtyText(last.qty, p.unit)}</button></div>` : ""}
      <div class="steps">
        ${[...steps].reverse().map(s => `<button class="step step-minus" data-s="add" data-v="-${s}" aria-label="Odejmij ${s}">−${s}</button>`).join("")}
        ${steps.map(s => `<button class="step" data-s="add" data-v="${s}" aria-label="Dodaj ${s}">+${s}</button>`).join("")}
      </div>
      <div class="keypad">${["1", "2", "3", "4", "5", "6", "7", "8", "9", ",", "0", "⌫"].map(k =>
        `<button class="key" data-s="key" data-v="${k}" ${k === "⌫" ? 'aria-label="Usuń cyfrę"' : ""}>${k}</button>`).join("")}</div>
      <input class="note-in" id="snote" placeholder="Uwagi, np. może być II klasa" value="${esc(cur?.note ?? (last?.note || ""))}">
      <div class="sheet-actions">
        ${cur ? `<button class="btn btn-remove" data-s="remove">Usuń</button>` : "<span></span>"}
        <button class="btn btn-green" data-s="ok" id="sok"></button>
      </div></div>`;
    if (!cur) $sheet.querySelector(".sheet-actions").style.gridTemplateColumns = "1fr";

    let fresh = !!cur;            // first key press replaces the existing amount
    const $num = $sheet.querySelector("#snum");
    const parsed = () => parseFloat(val.replace(",", ".")) || 0;
    const draw = (fromInput) => {
      if (!fromInput) $num.value = val;
      $sheet.querySelector("#sunit").textContent = unitLabel(p.unit, parsed());
      const ok = $sheet.querySelector("#sok");
      ok.textContent = parsed() > 0 ? (cur ? "Zapisz" : "Dodaj do zamówienia") : (cur ? "Usuń z zamówienia" : "Wpisz ilość");
      ok.disabled = !cur && parsed() <= 0;
      ok.style.opacity = ok.disabled ? .5 : 1;
    };
    draw();
    $num.addEventListener("focus", () => { $num.select(); fresh = false; });
    $num.addEventListener("input", () => {
      let v = $num.value.replace(".", ",").replace(/[^0-9,]/g, "");
      const i = v.indexOf(","); if (i !== -1) v = v.slice(0, i + 1) + v.slice(i + 1).replace(/,/g, "").slice(0, 2);
      val = v.slice(0, 7); if ($num.value !== val) $num.value = val;
      draw(true);
    });
    $num.addEventListener("keydown", e => { if (e.key === "Enter") { e.preventDefault(); $sheet.querySelector("#sok").click(); } });

    $sheet.onclick = e => {
      if (e.target === $sheet) return close();
      const b = e.target.closest("[data-s]"); if (!b) return;
      const a = b.dataset.s, v = b.dataset.v;
      if (a === "close") return close();
      if (a === "key") {
        if (fresh) { val = ""; fresh = false; }
        if (v === "⌫") val = val.slice(0, -1);
        else if (v === ",") { if (!val.includes(",")) val = (val || "0") + ","; }
        else if (val.length < 6) val = val === "0" ? v : val + v;
      }
      if (a === "add" || a === "set") fresh = false;
      if (a === "add") { const n = +(parsed() + +v).toFixed(2); val = n > 0 ? String(n).replace(".", ",") : ""; }
      if (a === "set") val = String(v).replace(".", ",");
      if (a === "remove") { delete cart.items[id]; persistCart(); toast(`Usunięto: ${p.name}`); return close(true); }
      if (a === "ok") {
        const q = parsed();
        if (q > 0) { cart.items[id] = { qty: q, note: $sheet.querySelector("#snote").value.trim() }; toast(`${p.name}: ${qtyText(q, p.unit)}`); }
        else delete cart.items[id];
        persistCart(); return close(true);
      }
      draw();
    };
    function close(changed) {
      $sheet.close();
      if (changed) { if (location.hash.startsWith("#/koszyk")) renderCart(); else renderCatalog.redraw?.(); }
    }
    $sheet.showModal();
    $sheet.querySelector(".sheet-close").focus({ preventScroll: true }); // don't pop the keyboard on open
  }

  document.addEventListener("keydown", e => {
    if ((e.key === "Enter" || e.key === " ") && e.target.matches?.(".line[data-prod]")) { e.preventDefault(); openSheet(e.target.dataset.prod); }
  });

  // ---------- global clicks ----------
  document.addEventListener("click", e => {
    const t = e.target.closest("[data-prod],[data-cat],[data-act],[data-day]");
    if (!t || $sheet.contains(t)) return;
    if (t.dataset.prod) return openSheet(t.dataset.prod);
    if (t.dataset.cat) { catState = { cat: t.dataset.cat, q: "" }; return renderCatalog(); }
    if (t.dataset.day) { cart.delivery = t.dataset.day; persistCart(); return renderCart(); }
    const act = t.dataset.act;
    if (act === "repeat") {
      const o = orders.find(x => x.id === t.dataset.id);
      if (o) { loadOrderIntoCart(o); toast("Wczytano poprzednie zamówienie"); location.hash = "#/koszyk"; }
    }
    if (act === "inc" || act === "dec") {
      const it = cart.items[t.dataset.id]; if (!it) return;
      const n = +(it.qty + (act === "inc" ? 1 : -1)).toFixed(2);
      if (n > 0) {
        it.qty = n; persistCart();
        // update just this row (re-rendering the basket would reload the photos and make them blink)
        const p = byId[t.dataset.id], row = t.closest(".line");
        row.querySelector(".line-qty").textContent = qtyText(n, p.unit);
        row.querySelector(".line-price").textContent = money(price(p) * n);
        row.querySelector('[data-act="dec"]').disabled = n - 1 <= 0;
        document.getElementById("ctotal").textContent = money(cartTotal());
      }
      return;
    }
    if (act === "del") {
      const p = byId[t.dataset.id];
      delete cart.items[t.dataset.id]; persistCart(); toast(`Usunięto: ${p.name}`);
      if (!cartLines().length) return renderCart();
      t.closest(".line").remove();   // remove in place – no re-render, no blinking photos
      document.getElementById("ctotal").textContent = money(cartTotal());
      return;
    }
    if (act === "clear" && confirm("Wyczyścić cały koszyk?")) { cart.items = {}; persistCart(); renderCart(); }
    if (act === "submit") submit();
  });

  function submit() {
    const lines = cartLines();
    if (!lines.length) return;
    const o = {
      id: Date.now().toString(36),
      createdAt: new Date().toISOString(),
      client: CLIENT.name,
      company: profile.company,
      delivery: cart.delivery, time: cart.time, note: cart.note.trim(),
      items: lines.map(([id, it]) => ({ id, name: byId[id].name, unit: byId[id].unit, qty: it.qty, note: it.note, price: price(byId[id]) })),
      total: cartTotal(),
      status: "zapisane",
    };
    // TODO: POST to backend when accounts/API exist. For now orders live on this device.
    orders.unshift(o);
    save(KEY.orders, orders);
    cart = { items: {}, delivery: null, time: cart.time, note: "" };
    persistCart();
    justSent = o.id;
    location.hash = `#/zamowienie/${o.id}`;
  }

  // ---------- PWA ----------
  if ("serviceWorker" in navigator) navigator.serviceWorker.register("sw.js").catch(() => {});

  route();
})();
