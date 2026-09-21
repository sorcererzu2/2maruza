# server.py — gRPC server (4 xil chaqiruv turi)
import os, time, statistics
from concurrent import futures
import grpc
import talaba_pb2 as pb, talaba_pb2_grpc as pbg

PORT = os.environ.get("PORT", "50051")
# Sunʼiy kechikish (mustaqil topshiriq 4 uchun). Sukut boʻyicha 0.
KECHIKISH = float(os.environ.get("KECHIKISH_MS", "0")) / 1000

BAZA = {
    "1001": ("Alisher", 3, 4.5),
    "1002": ("Nodira",  3, 4.8),
    "1003": ("Sardor",  4, 3.9),
}

class Xizmat(pbg.TalabaXizmatiServicer):
    def Ol(self, sorov, ctx):                                  # unary
        if KECHIKISH:
            time.sleep(KECHIKISH)
        if not sorov.id:
            ctx.abort(grpc.StatusCode.INVALID_ARGUMENT, "id boʻsh boʻlmasligi kerak")
        if sorov.id not in BAZA:
            ctx.abort(grpc.StatusCode.NOT_FOUND, "talaba topilmadi")
        ism, kurs, r = BAZA[sorov.id]
        return pb.Talaba(id=sorov.id, ism=ism, kurs=kurs, reyting=r)

    def KursRoyxati(self, sorov, ctx):                         # server streaming
        for tid, (ism, kurs, r) in BAZA.items():
            if kurs == sorov.kurs:
                yield pb.Talaba(id=tid, ism=ism, kurs=kurs, reyting=r)
                time.sleep(0.2)   # oqimni koʻrsatish uchun

    def Yukla(self, oqim, ctx):                                # client streaming
        reytinglar = []
        for t in oqim:
            BAZA[t.id] = (t.ism, t.kurs, t.reyting)
            reytinglar.append(t.reyting)
        return pb.Statistika(soni=len(reytinglar),
                             ortacha_reyting=statistics.mean(reytinglar) if reytinglar else 0)

    def Kuzat(self, oqim, ctx):                                # bidirectional
        for s in oqim:
            if s.id in BAZA:
                ism, kurs, r = BAZA[s.id]
                yield pb.Talaba(id=s.id, ism=ism, kurs=kurs, reyting=r)

def main():
    srv = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pbg.add_TalabaXizmatiServicer_to_server(Xizmat(), srv)
    srv.add_insecure_port(f"[::]:{PORT}")
    srv.start()
    print(f"server {PORT} portda, kechikish {KECHIKISH * 1000:.0f} ms", flush=True)
    srv.wait_for_termination()

if __name__ == "__main__":
    main()
