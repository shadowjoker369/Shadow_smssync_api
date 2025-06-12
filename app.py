from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def receive_sms():
    data = request.get_json()
    sender = data.get("from")
    message = data.get("message")
    timestamp = data.get("sent_timestamp")

    print(f"📩 New SMS from {sender} at {timestamp}: {message}")

    # You can add more processing here or forward to Telegram/DB

    return jsonify({"status": "success", "message": "SMS received"}), 200

if __name__ == "__main__":
    app.run(debug=True)
