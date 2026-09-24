import argparse

from scapy.all import get_working_if

from models import Base
from database import engine

from capture import start_capture
from stats import generate_stats

Base.metadata.create_all(bind=engine)

parser = argparse.ArgumentParser()

parser.add_argument(
    "--interface",
    required=False
)

parser.add_argument(
    "--stats",
    action="store_true"
)

args = parser.parse_args()

if args.stats:
    generate_stats()
else:

    interface = args.interface

    if interface is None:
        interface = str(get_working_if())

    print(f"Interface detectada: {interface}")

    start_capture(interface)
