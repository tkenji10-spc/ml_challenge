from scapy.all import sniff
from scapy.layers.inet import IP, ICMP
from models import Packet
from database import SessionLocal

def process_packet(packet):
    if not packet.haslayer(IP):
        return

    protocol = ""

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
    session.add(item)
    session.commit()
    session.close()

def start_capture(interface):
    print(f"[*] Iniciando captura de pacotes na interface: {interface}...", flush=True)
    sniff(
        iface=interface,
        prn=process_packet,
        store=False
    )