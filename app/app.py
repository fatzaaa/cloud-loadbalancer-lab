import os
import socket
import time

from flask import Flask, jsonify

app = Flask(__name__)
HOSTNAME = socket.gethostname()


@app.route("/")
def index():
    return jsonify(
        message="Halo dari ICN load balancer lab",
        hostname=HOSTNAME,
        pid=os.getpid(),
    )


@app.route("/health")
def health():
    return jsonify(status="ok", hostname=HOSTNAME)


@app.route("/work")
def work():
    # Simulasi beban CPU, supaya beda 1 vs 3 replika kelihatan saat load test
    start = time.time()
    total = 0
    for i in range(2_000_000):
        total += i * i
    return jsonify(
        hostname=HOSTNAME,
        result=total,
        took_ms=round((time.time() - start) * 1000, 2),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)