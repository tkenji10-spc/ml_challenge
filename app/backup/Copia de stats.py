from collections import Counter
from models import Packet
from database import SessionLocal

def generate_stats():

    session = SessionLocal()

    packets = session.query(Packet).all()

    print("\n===== ESTATÍSTICAS =====")

    print(f"Total de pacotes: {len(packets)}")

    protocol_counter = Counter()

    source_counter = Counter()

    destination_counter = Counter()

    for p in packets:

        protocol_counter[p.protocol] += 1

        source_counter[p.src_ip] += 1

        destination_counter[p.dst_ip] += 1

    print("\nPacotes por protocolo:")

    for proto, count in protocol_counter.items():
        print(proto, count)

    print("\nTop 5 IPs Origem")

    for ip, count in source_counter.most_common(5):
        print(ip, count)

    print("\nTop 5 IPs Destino")

    for ip, count in destination_counter.most_common(5):
        print(ip, count)

    session.close()
