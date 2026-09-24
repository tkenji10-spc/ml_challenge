from collections import Counter

from app.models import Packet
from app.database import SessionLocal


def get_stats_data():
    session = SessionLocal()

    try:
        packets = session.query(Packet).all()

        protocol_counter = Counter()
        source_counter = Counter()
        destination_counter = Counter()

        for p in packets:
            protocol_counter[p.protocol] += 1
            source_counter[p.src_ip] += 1
            destination_counter[p.dst_ip] += 1

        return {
            "total_packets": len(packets),
            "protocols": dict(protocol_counter),
            "top_sources": source_counter.most_common(5),
            "top_destinations": destination_counter.most_common(5)
        }

    finally:
        session.close()


def generate_stats():
    stats = get_stats_data()

    print("\n===== ESTATÍSTICAS =====")

    print(f"Total de pacotes: {stats['total_packets']}")

    print("\nPacotes por protocolo:")

    for proto, count in stats["protocols"].items():
        print(f"{proto}: {count}")

    print("\nTop 5 IPs Origem")

    for ip, count in stats["top_sources"]:
        print(f"{ip}: {count}")

    print("\nTop 5 IPs Destino")

    for ip, count in stats["top_destinations"]:
        print(f"{ip}: {count}")