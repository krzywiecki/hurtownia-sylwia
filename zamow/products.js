// Fake product catalog + demo client price list.
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
  { id: "ziemniak-ob", cat: "obrane", name: "Ziemniaki obrane", emoji: "🥔", img: "img/ziemniaki-obrane.webp", unit: "kg", price: 3.2, peeled: true },
  { id: "marchew-ob", cat: "obrane", name: "Marchew obrana", emoji: "🥕", img: "img/marchew-obrana.webp", unit: "kg", price: 3.9, peeled: true },
  { id: "seler-ob", cat: "obrane", name: "Seler obrany", emoji: "🥔", img: "img/seler-obrany.webp", unit: "kg", price: 5.5, peeled: true },
  { id: "pietruszka-ob", cat: "obrane", name: "Pietruszka obrana", emoji: "🥕", img: "img/pietruszka-obrana.webp", unit: "kg", price: 8.9, peeled: true },
  { id: "cebula-ob", cat: "obrane", name: "Cebula obrana", emoji: "🧅", img: "img/cebula-obrana.webp", unit: "kg", price: 4.2, peeled: true },
  { id: "burak-ob", cat: "obrane", name: "Buraki obrane", emoji: "🟣", img: "img/buraki-obrane.webp", unit: "kg", price: 4.5, peeled: true },

  // Warzywa
  { id: "ziemniak", cat: "warzywa", name: "Ziemniaki", emoji: "🥔", img: "img/ziemniaki.webp", unit: "kg", price: 1.6 },
  { id: "marchew", cat: "warzywa", name: "Marchew", emoji: "🥕", img: "img/marchew.webp", unit: "kg", price: 2.1 },
  { id: "cebula", cat: "warzywa", name: "Cebula", emoji: "🧅", img: "img/cebula.webp", unit: "kg", price: 2.3 },
  { id: "pomidor", cat: "warzywa", name: "Pomidor", emoji: "🍅", img: "img/pomidor.webp", unit: "kg", price: 8.5 },
  { id: "papryka-cz", cat: "warzywa", name: "Papryka czerwona", emoji: "🫑", img: "img/papryka-czerwona.webp", unit: "kg", price: 11.0 },
  { id: "ogorek", cat: "warzywa", name: "Ogórek", emoji: "🥒", unit: "karton", price: 42.0 },
  { id: "cukinia", cat: "warzywa", name: "Cukinia", emoji: "🥒", img: "img/cukinia.webp", unit: "kg", price: 7.5 },
  { id: "kapusta", cat: "warzywa", name: "Kapusta biała", emoji: "🥬", img: "img/kapusta-biala.webp", unit: "kg", price: 2.4 },
  { id: "czosnek", cat: "warzywa", name: "Czosnek", emoji: "🧄", unit: "kg", price: 19.0 },
  { id: "brokul", cat: "warzywa", name: "Brokuł", emoji: "🥦", img: "img/brokul.webp", unit: "szt", price: 5.5 },

  // Owoce
  { id: "mandarynki", cat: "owoce", name: "Mandarynki", emoji: "🍊", img: "../img/mandarynki.webp", unit: "kg", price: 6.9 },
  { id: "banan", cat: "owoce", name: "Banany", emoji: "🍌", unit: "kg", price: 5.4 },
  { id: "sliwki", cat: "owoce", name: "Śliwki", emoji: "🫐", unit: "kg", price: 6.5 },
  { id: "cytryna", cat: "owoce", name: "Cytryny", emoji: "🍋", unit: "kg", price: 8.0 },
  { id: "jablka", cat: "owoce", name: "Jabłka", emoji: "🍎", unit: "kg", price: 3.5 },
  { id: "pomarancze", cat: "owoce", name: "Pomarańcze", emoji: "🍊", unit: "kg", price: 6.2 },
  { id: "winogrona", cat: "owoce", name: "Winogrona", emoji: "🍇", unit: "kg", price: 14.0 },
  { id: "miechunka", cat: "owoce", name: "Miechunka", emoji: "🟠", img: "../img/miechunka.webp", unit: "szt", price: 9.0 },

  // Sałaty i zioła
  { id: "salata-lod", cat: "salaty", name: "Sałata lodowa", emoji: "🥬", unit: "karton", price: 55.0 },
  { id: "rukola", cat: "salaty", name: "Rukola", emoji: "🌿", unit: "karton", price: 38.0 },
  { id: "jarmuz", cat: "salaty", name: "Jarmuż", emoji: "🥬", img: "../img/jarmuz.webp", unit: "kg", price: 16.0 },
  { id: "koper", cat: "salaty", name: "Koper", emoji: "🌿", unit: "kg", price: 18.0 },
  { id: "natka", cat: "salaty", name: "Natka pietruszki", emoji: "🌿", unit: "pęczek", price: 2.5 },
  { id: "bazylia", cat: "salaty", name: "Bazylia", emoji: "🌿", img: "../img/bazylia.webp", unit: "doniczka", price: 6.0 },
  { id: "mieta", cat: "salaty", name: "Mięta", emoji: "🌿", img: "../img/mieta.webp", unit: "doniczka", price: 6.0 },

  // Kiszonki
  { id: "kapusta-kisz", cat: "kiszonki", name: "Kapusta kiszona", emoji: "🥬", unit: "kg", price: 5.8 },
  { id: "ogorek-kisz", cat: "kiszonki", name: "Ogórki kiszone", emoji: "🥒", unit: "kg", price: 9.5 },
];

// Demo client – real accounts (with their own price lists) come with login.
window.CLIENT = { name: "Klient demo", priceFactor: 1 };
