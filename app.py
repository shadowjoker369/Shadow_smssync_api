from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 👉 এটিই CORS সমস্যা সমাধান করবে

@app.route("/", methods=["POST"])
def receive_sms():
    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "message": "No JSON payload received"}), 400

    sender = data.get("number")
    message = data.get("message")

    print(f"📩 Send request to {sender}: {message}")

    return jsonify({"status": "success", "message": "Message received"}), 200

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "ok", "message": "Shadow SMS Sync API is live"}), 200
