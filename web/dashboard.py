import sys
from pathlib import Path

# Adiciona a raiz do projeto ao PYTHONPATH
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from flask import Flask, render_template, jsonify
from scapy.all import get_working_if

from app.capture import (
    start_capture,
    stop_capture,
    is_capturing
)

from app.stats import (
    get_stats_data,
    clear_packets
)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start")
def start():

    if not is_capturing():

        # Limpa os registros da captura anterior
        clear_packets()

        interface = str(get_working_if())

        print(
            f"Interface detectada: {interface}",
            flush=True
        )

        start_capture(interface)

    return jsonify({
        "status": "capturando"
    })


@app.route("/stop")
def stop():

    stop_capture()

    return jsonify({
        "status": "parado"
    })


@app.route("/api/stats")
def stats():

    return jsonify(
        get_stats_data()
    )


@app.route("/api/status")
def status():

    return jsonify({
        "capturando": is_capturing()
    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5001,
        debug=False
    )