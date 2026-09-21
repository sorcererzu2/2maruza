# deadline_sinov.py — turli deadline qiymatlarida Ol chaqiruvi (mustaqil topshiriq 4)
# Oldin serverni sunʼiy kechikish bilan ishga tushiring:
#   KECHIKISH_MS=300 python server.py
import os, sys, time
import grpc
import talaba_pb2 as pb, talaba_pb2_grpc as pbg

SERVER = os.environ.get("SERVER", "localhost:50051")
DEADLINES = [float(v) for v in sys.argv[1:]] or [0.05, 0.5, 5.0]

kanal = grpc.insecure_channel(SERVER)
try:
    grpc.channel_ready_future(kanal).result(timeout=10)
except grpc.FutureTimeoutError:
    raise SystemExit(f"Server topilmadi: {SERVER}. Server ishga tushganini va manzil toʻgʻriligini tekshiring.")
x = pbg.TalabaXizmatiStub(kanal)

print(f"{'deadline, s':>12}  {'natija':<20} {'vaqt, ms':>9}")
for d in DEADLINES:
    t0 = time.perf_counter()
    try:
        x.Ol(pb.IdSorovi(id="1001"), timeout=d)
        natija = "OK"
    except grpc.RpcError as e:
        natija = e.code().name
    print(f"{d:>12}  {natija:<20} {1000 * (time.perf_counter() - t0):>9.1f}")
