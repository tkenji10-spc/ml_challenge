from scapy.all import AsyncSniffer
from scapy.layers.inet import IP, ICMP

from models import Packet
from database import SessionLocal

# Controla a captura em execução
sniffer = None


def process_packet(packet):
    if not packet.haslayer(IP):
        return

    if packet.haslayer("TCP"):
        protocol = "TCP"
    elif packet.haslayer("UDP"):
        protocol = "UDP"
    elif packet.haslayer(ICMP):
        protocol = "ICMP"
    else:
        protocol = "OTHER"

    item = Packet(
        src_ip=packet[IP].src,
        dst_ip=packet[IP].dst,
        protocol=protocol,
        packet_size=len(packet)
    )

    session = SessionLocal()

    try:
        session.add(item)
        session.commit()
    finally:
        session.close()


def start_capture(interface):
    global sniffer

    if sniffer is not None:
        print("[!] Captura já está em execução.")
        return

    print(
        f"[*] Iniciando captura de pacotes na interface: {interface}...",
        flush=True
    )

    sniffer = AsyncSniffer(
        iface=interface,
        prn=process_packet,
        store=False
    )

    sniffer.start()

    print("[*] Captura iniciada com sucesso.")


def stop_capture():
    global sniffer

    if sniffer is None:
        print("[!] Nenhuma captura em execução.")
        return

    sniffer.stop()
    sniffer = None

    print("[*] Captura encerrada.")


def is_capturing():
    return sniffer is not None