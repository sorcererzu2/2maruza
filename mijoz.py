# mijoz.py — toʻrt chaqiruv turi, xatoliklar va deadline
import os, time
import grpc
import talaba_pb2 as pb, talaba_pb2_grpc as pbg

# Manzil kodga qattiq yozilmaydi — muhit oʻzgaruvchisidan olinadi
SERVER = os.environ.get("SERVER", "localhost:50051")

kanal = grpc.insecure_channel(SERVER)
# Server hali koʻtarilmagan boʻlishi mumkin — ulanishni 10 soniyagacha kutamiz
try:
    grpc.channel_ready_future(kanal).result(timeout=10)
except grpc.FutureTimeoutError:
    raise SystemExit(f"Server topilmadi: {SERVER}. Server ishga tushganini va manzil toʻgʻriligini tekshiring.")
x = pbg.TalabaXizmatiStub(kanal)
print(f"ulanish: {SERVER}\n")

print("1) Unary — bitta soʻrov, bitta javob")
try:
    t = x.Ol(pb.IdSorovi(id="1001"), timeout=2.0)
    print(f"   {t.id}: {t.ism}, {t.kurs}-kurs, reyting {t.reyting}")
except grpc.RpcError as e:
    print("   XATO:", e.code(), e.details())

print("\n2) Xatolik holatlari")
for tid, izoh in [("9999", "mavjud boʻlmagan id"), ("", "boʻsh id")]:
    try:
        x.Ol(pb.IdSorovi(id=tid), timeout=2.0)
    except grpc.RpcError as e:
        print(f"   {izoh:22} -> {e.code().name}: {e.details()}")

print("\n3) Server streaming — bitta soʻrov, bir nechta javob")
for t in x.KursRoyxati(pb.KursSorovi(kurs=3), timeout=5.0):
    print(f"   oqimdan: {t.ism}")

print("\n4) Client streaming — bir nechta soʻrov, bitta javob")
yangi = [pb.Talaba(id="2001", ism="Dilnoza", kurs=2, reyting=4.2),
         pb.Talaba(id="2002", ism="Jasur",   kurs=2, reyting=3.6)]
st = x.Yukla(iter(yangi), timeout=5.0)
print(f"   yuklandi: {st.soni} ta, oʻrtacha reyting {st.ortacha_reyting:.2f}")

print("\n5) Bidirectional — ikki tomonlama oqim")
idlar = (pb.IdSorovi(id=i) for i in ["1002", "2001", "1003"])
for t in x.Kuzat(idlar, timeout=5.0):
    print(f"   javob: {t.id} -> {t.ism}")

print("\n6) Qisqa deadline — oqim 0,1 s ichida tugay olmaydi")
t0 = time.perf_counter()
try:
    list(x.KursRoyxati(pb.KursSorovi(kurs=3), timeout=0.1))
except grpc.RpcError as e:
    print(f"   {e.code().name}, {1000 * (time.perf_counter() - t0):.0f} ms dan keyin")
