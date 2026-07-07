from flask import Flask, jsonify
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from GitHub Actions Practice!",
        "hostname": socket.gethostname(),
        "time": str(datetime.datetime.now())
    })

@app.route("/health")
def health():
    return "Healthy", 200

@app.route("/version")
def version():
    return jsonify({
        "version": "1.0.0"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)