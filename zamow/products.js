// Product catalog. No prices – each client has an individual price list.
// img: optional photo path (relative to /zamow/); otherwise the emoji is shown.
// step: quick-add amount; unit: kg | karton | szt | pęczek | doniczka
window.CATEGORIES = [
  { id: "obrane", name: "Obrane", icon: "🔪" },
  { id: "warzywa", name: "Warzywa", icon: "🥕" },
  { id: "owoce", name: "Owoce", icon: "🍎" },
  { id: "salaty", name: "Sałaty i zioła", icon: "🥬" },
  { id: "kiszonki", name: "Kiszonki", icon: "🫙" },
];

window.PRODUCTS = [
  // Warzywa obierane
  { id: "ziemniak-ob", cat: "obrane", name: "Ziemniaki obrane", emoji: "🥔", img: "img/ziemniaki-obrane.webp", unit: "kg", peeled: true },
  { id: "marchew-ob", cat: "obrane", name: "Marchew obrana", emoji: "🥕", img: "img/marchew-obrana.webp", unit: "kg", peeled: true },
  { id: "seler-ob", cat: "obrane", name: "Seler obrany", emoji: "🥔", img: "img/seler-obrany.webp", unit: "kg", peeled: true },
  { id: "pietruszka-ob", cat: "obrane", name: "Pietruszka obrana", emoji: "🥕", img: "img/pietruszka-obrana.webp", unit: "kg", peeled: true },
  { id: "cebula-ob", cat: "obrane", name: "Cebula obrana", emoji: "🧅", img: "img/cebula-obrana.webp", unit: "kg", peeled: true },
  { id: "burak-ob", cat: "obrane", name: "Buraki obrane", emoji: "🟣", img: "img/buraki-obrane.webp", unit: "kg", peeled: true },

  // Warzywa
  { id: "ziemniak", cat: "warzywa", name: "Ziemniaki", emoji: "🥔", img: "img/ziemniaki.webp", unit: "kg" },
  { id: "marchew", cat: "warzywa", name: "Marchew", emoji: "🥕", img: "img/marchew.webp", unit: "kg" },
  { id: "cebula", cat: "warzywa", name: "Cebula", emoji: "🧅", img: "img/cebula.webp", unit: "kg" },
  { id: "pomidor", cat: "warzywa", name: "Pomidor", emoji: "🍅", img: "img/pomidor.webp", unit: "kg" },
  { id: "papryka-cz", cat: "warzywa", name: "Papryka czerwona", emoji: "🫑", img: "img/papryka-czerwona.webp", unit: "kg" },
  { id: "ogorek", cat: "warzywa", name: "Ogórek", emoji: "🥒", img: "img/ogorek.webp", unit: "karton" },
  { id: "cukinia", cat: "warzywa", name: "Cukinia", emoji: "🥒", img: "img/cukinia.webp", unit: "kg" },
  { id: "kapusta", cat: "warzywa", name: "Kapusta biała", emoji: "🥬", img: "img/kapusta-biala.webp", unit: "kg" },
  { id: "czosnek", cat: "warzywa", name: "Czosnek", emoji: "🧄", img: "img/czosnek.webp", unit: "kg" },
  { id: "brokul", cat: "warzywa", name: "Brokuł", emoji: "🥦", img: "img/brokul.webp", unit: "szt" },

  // Owoce
  { id: "mandarynki", cat: "owoce", name: "Mandarynki", emoji: "🍊", img: "../img/mandarynki.webp", unit: "kg" },
  { id: "banan", cat: "owoce", name: "Banany", emoji: "🍌", img: "img/banany.webp", unit: "kg" },
  { id: "sliwki", cat: "owoce", name: "Śliwki", emoji: "🫐", img: "img/sliwki.webp", unit: "kg" },
  { id: "cytryna", cat: "owoce", name: "Cytryny", emoji: "🍋", img: "img/cytryny.webp", unit: "kg" },
  { id: "jablka", cat: "owoce", name: "Jabłka", emoji: "🍎", img: "img/jablka.webp", unit: "kg" },
  { id: "pomarancze", cat: "owoce", name: "Pomarańcze", emoji: "🍊", img: "img/pomarancze.webp", unit: "kg" },
  { id: "winogrona", cat: "owoce", name: "Winogrona", emoji: "🍇", img: "img/winogrona.webp", unit: "kg" },
  { id: "miechunka", cat: "owoce", name: "Miechunka", emoji: "🟠", img: "../img/miechunka.webp", unit: "szt" },

  // Sałaty i zioła
  { id: "salata-lod", cat: "salaty", name: "Sałata lodowa", emoji: "🥬", img: "img/salata-lodowa.webp", unit: "karton" },
  { id: "rukola", cat: "salaty", name: "Rukola", emoji: "🌿", img: "img/rukola.webp", unit: "karton" },
  { id: "jarmuz", cat: "salaty", name: "Jarmuż", emoji: "🥬", img: "../img/jarmuz.webp", unit: "kg" },
  { id: "koper", cat: "salaty", name: "Koper", emoji: "🌿", img: "img/koper.webp", unit: "kg" },
  { id: "natka", cat: "salaty", name: "Natka pietruszki", emoji: "🌿", img: "img/natka.webp", unit: "pęczek" },
  { id: "bazylia", cat: "salaty", name: "Bazylia", emoji: "🌿", img: "../img/bazylia.webp", unit: "doniczka" },
  { id: "mieta", cat: "salaty", name: "Mięta", emoji: "🌿", img: "../img/mieta.webp", unit: "doniczka" },

  // Kiszonki
  { id: "kapusta-kisz", cat: "kiszonki", name: "Kapusta kiszona", emoji: "🥬", img: "img/kapusta-kiszona.webp", unit: "kg" },
  { id: "ogorek-kisz", cat: "kiszonki", name: "Ogórki kiszone", emoji: "🥒", img: "img/ogorki-kiszone.webp", unit: "kg" },
];

// Demo client – real accounts come with login.
window.CLIENT = { name: "Klient demo" };
