# Amaliy mashgʻulot 2. gRPC xizmatini ishlab chiqish

**Fan:** Taqsimlangan tizimlar · **Bogʻliq maʼruza:** M3 · **Ajratilgan vaqt:** 4 soat · **Ball:** 3

Toʻliq nazariya, sxemalar va izohlar — `Amaliy_02_Qollanma.docx` faylida.

---

## 0. Ishni boshlash

1. Shu sahifada **Use this template** → **Create a new repository**. Nomi: `dt-a2-familiyangiz`, **Public**.
2. Oʻz repozitoriyingizda **Code** → **Codespaces** → **Create codespace on main**.
3. 3–5 daqiqa kuting. Terminal oxirida `---- tayyor ----` va versiyalar chiqadi:

```
grpcio 1.84.0
grpcurl v1.9.4
Docker version ...
```

Chiqmagan boʻlsa, qoʻlda ishga tushiring: `bash .devcontainer/setup.sh`

---

## 1. Kodni generatsiya qilish

```bash
./gen.sh
```

Natija: `talaba_pb2.py` (xabarlar) va `talaba_pb2_grpc.py` (server va mijoz qismi). Bu fayllarni **qoʻlda tahrirlamang** — `talaba.proto` oʻzgarsa, `./gen.sh` ni qayta bajaring.

---

## 2. Serverni ishga tushirish — 1-terminal

```bash
python server.py
```

Chiqishi kerak: `server 50051 portda, kechikish 0 ms`. Bu terminalni yopmang.

---

## 3. Mijozni ishga tushirish — 2-terminal

Yangi terminal oching (terminal panelidagi **+** belgisi):

```bash
python mijoz.py | tee natijalar/01-mijoz.txt
```

Mijoz toʻrt chaqiruv turini, ikki xil xatolikni va qisqa deadline ni koʻrsatadi.

---

## 4. grpcurl bilan qoʻlda sinash

```bash
grpcurl -plaintext -proto talaba.proto -d '{"id":"1001"}' localhost:50051 talaba.TalabaXizmati/Ol
grpcurl -plaintext -proto talaba.proto -d '{"id":"9999"}' localhost:50051 talaba.TalabaXizmati/Ol
grpcurl -plaintext -proto talaba.proto -d '{"kurs":3}'    localhost:50051 talaba.TalabaXizmati/KursRoyxati
```

---

## 5. Deadline sinovi

1-terminalda serverni `Ctrl+C` bilan toʻxtating va sunʼiy kechikish bilan qayta ishga tushiring:

```bash
KECHIKISH_MS=300 python server.py
```

2-terminalda:

```bash
python deadline_sinov.py | tee natijalar/02-deadline.txt
python deadline_sinov.py 0.1 0.29 0.31 1 | tee natijalar/02-deadline-chegara.txt
```

---

## 6. Konteynerga joylash

Avval 1-terminaldagi serverni toʻxtating (`Ctrl+C`), keyin:

```bash
docker compose up -d --build grpc-server
docker compose ps
docker compose run --rm grpc-mijoz
docker compose down
```

Mijoz konteyneri serverga `grpc-server:50051` nomi orqali ulanadi — manzil `compose.yaml` dagi `SERVER` oʻzgaruvchisidan olinadi, kodga yozilmagan.

---

## 7. gRPC va HTTP/JSON qiyosi (mustaqil topshiriq 6)

1-terminal: `python server.py` · 2-terminal: `python qiyos/http_server.py` · 3-terminal:

```bash
python qiyos/solishtir.py 500 | tee natijalar/06-qiyos.txt
```

---

## Mustaqil topshiriq

Variantingizni oʻqituvchidan oling.

| Variant | Predmet sohasi | Qoʻshimcha metod |
|---|---|---|
| 1 | Kutubxona (kitob, oʻquvchi) | Kitobni band qilish |
| 2 | Ombor (mahsulot, qoldiq) | Qoldiqni kamaytirish |
| 3 | Transport (reys, chipta) | Boʻsh oʻrinlar oqimi |
| 4 | Tibbiyot (qabul, navbat) | Navbat holatini kuzatish |

1. `.proto` faylga oʻz sohangizga mos xabar va kamida bitta yangi metod qoʻshing.
2. Toʻrt chaqiruv turining hammasini ishlaydigan holga keltiring va har biri uchun mijoz kodini yozing.
3. NOT_FOUND, INVALID_ARGUMENT va DEADLINE_EXCEEDED holatlarini alohida koʻrsating.
4. Deadline qiymatlari 0.05, 0.5 va 5 s bilan natijani qayd eting.
5. Sxema evolyutsiyasini sinang: yangi maydon qoʻshing, eski mijoz bilan yangi serverni va aksincha sinab koʻring.
6. gRPC va HTTP/JSON orqali bir xil maʼlumotni 500 marta uzating; kechikish va bayt hajmini solishtiring.

---

## Topshirish

1. `hisobot.md` ni toʻldiring, natijalarni `natijalar/` papkasiga saqlang.
2. Saqlang va yuklang:

```bash
git add .
git commit -m "Amaliy 2 bajarildi"
git push
```

3. Oʻqituvchiga repozitoriy havolasini yuboring.
4. **Codespace ni toʻxtating:** pastki chap burchak → **Stop Current Codespace**.

---

## Tez-tez uchraydigan xatolar

| Xato | Sababi | Yechimi |
|---|---|---|
| `ModuleNotFoundError: talaba_pb2` | Kod generatsiya qilinmagan | `./gen.sh` |
| `Server topilmadi: localhost:50051` | Server ishlamayapti | 1-terminalda `python server.py` |
| `address already in use` | Server allaqachon ishlab turibdi | Eski terminalda `Ctrl+C` |
| `ModuleNotFoundError: grpc` | Paketlar oʻrnatilmagan | `bash .devcontainer/setup.sh` |
| `grpcurl: command not found` | Sozlash tugamagan | `bash .devcontainer/setup.sh` |
| `.proto` oʻzgardi, lekin natija eski | Kod qayta generatsiya qilinmagan | `./gen.sh`, keyin serverni qayta ishga tushiring |
