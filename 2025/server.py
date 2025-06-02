from flask import Flask, request, jsonify, send_from_directory, render_template_string
from datetime import datetime
import uuid
import os

app = Flask(__name__, static_folder='static')
valid_password = os.environ.get("CHALLENGE_PASSWORD", "gr33n4zubi")
issued_codes = {}  # { code: timestamp }

@app.route("/2025/")
def serve_challenge_page():
    with open(os.path.join(app.static_folder, "index.html")) as f:
        html = f.read()
    return render_template_string(html, password_hex=valid_password.encode().hex())

@app.route("/2025/code", methods=["POST"])
def get_code():
    data = request.json
    if not data or data.get("password") != valid_password:
        return jsonify({"error": "Invalid password"}), 403

    code = f"AZU2025-{uuid.uuid4().hex[:4]}"
    timestamp = datetime.utcnow().isoformat()
    issued_codes[code] = timestamp
    return jsonify({"code": code, "timestamp": timestamp})

@app.route("/2025/verify", methods=["POST"])
def verify_code():
    data = request.json
    code = data.get("code")
    ts = data.get("timestamp")
    if issued_codes.get(code) == ts:
        return jsonify({"result": "OK", "message": "Challenge bestanden! ✨"})
    return jsonify({"result": "FAIL", "message": "Ungültiger Code oder Timestamp."}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
