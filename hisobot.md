# Amaliy mashgʻulot 2 — Hisobot

**Talaba:** ______________________  **Guruh:** __________  **Variant:** ____  **Sana:** __________

---

## 1. `.proto` fayli va sxema tanlovi

Oʻz variantingiz uchun yozilgan `.proto` faylining toʻliq matni:

```proto
// shu yerga joylang
```

**Sxema tanlovi izohi:** _(qaysi xabarlar va metodlar nima uchun kerak; qaysi metod qaysi chaqiruv turida va nega)_

---

## 2. Server va mijoz kodining asosiy qismlari

_(toʻliq kod repozitoriyda; bu yerga eng muhim 20–40 qatorni izoh bilan keltiring)_

---

## 3. Toʻrt chaqiruv turining natijasi

| Chaqiruv turi | Metod | Terminal chiqishi (qisqacha) |
|---|---|---|
| Unary | | |
| Server streaming | | |
| Client streaming | | |
| Bidirectional | | |

---

## 4. Xatolik holatlari

| Holat | Qaytgan status kodi | Qayta urinish maʼnoga egami | Nima uchun |
|---|---|---|---|
| Mavjud boʻlmagan yozuv | | | |
| Notoʻgʻri kiritilgan maʼlumot | | | |
| Deadline tugadi | | | |
| Server ishlamayapti | | | |

---

## 5. Deadline natijalari

Server sunʼiy kechikishi: ______ ms

| Deadline, s | Natija | Javob vaqti, ms |
|---|---|---|
| 0.05 | | |
| 0.5 | | |
| 5 | | |

**Tahlil:** _(nega deadline 5 s boʻlganda javob 5 soniya emas, tezroq keldi? Chegara qiymat qayerda?)_

---

## 6. Sxema evolyutsiyasi

Qoʻshilgan maydon: `______________ = __;`

| Tajriba | Natija |
|---|---|
| Yangi server → eski mijoz | |
| Eski server → yangi mijoz | |
| Teg raqami oʻzgartirilgan server → eski mijoz | |

**Izoh:** _(qaysi oʻzgarish xavfsiz, qaysi biri xavfli va nima uchun; xatolik chiqdimi yoki maʼlumot jimgina buzildimi?)_

---

## 7. gRPC va HTTP/JSON qiyosi

| | p50, ms | p95, ms | Javob tanasi, bayt |
|---|---|---|---|
| gRPC | | | |
| HTTP/JSON | | | |

**Xulosa:** _(qaysi biri tezroq, qaysi biri ixchamroq chiqdi? Natija kutganingizga mos keldimi? Oʻlchov bitta kompyuter ichida olinganini hisobga oling: real tarmoqda farq qanday oʻzgarishi mumkin?)_

---

## 8. Nazorat savollariga javoblar

1. gRPC qaysi transport va qaysi seriyalash formatidan foydalanadi?
2. Protocol Buffers da teg raqami nima uchun oʻzgartirilmasligi kerak?
3. Sxema evolyutsiyasining asosiy qoidalarini sanang.
4. Toʻrt chaqiruv turini tavsiflang va har biriga qoʻllanish misolini keltiring.
5. Deadline timeout dan nima bilan farq qiladi? U nima uchun zanjir boʻylab tarqatiladi?
6. Qaysi gRPC status kodlarida qayta urinish maʼnoga ega, qaysilarida yoʻq?
7. Nima uchun server manzilini kodga qattiq yozish tavsiya etilmaydi?
8. Oʻlchovlaringizga koʻra gRPC HTTP/JSON bilan solishtirganda tezlik va hajm jihatidan qanday natija berdi?
9. Qaysi holatlarda REST ni gRPC dan afzal koʻrgan boʻlardingiz?
