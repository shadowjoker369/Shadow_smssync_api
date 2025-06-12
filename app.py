from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def receive_sms():
    if request.method == "POST":
        data = request.get_json()

        if not data:
            return jsonify({"status": "error", "message": "No JSON payload received"}), 400

        sender = data.get("from")
        message = data.get("message")
        timestamp = data.get("sent_timestamp")

        print(f"📩 New SMS from {sender} at {timestamp}: {message}")

        return jsonify({"status": "success", "message": "SMS received"}), 200

    else:  # For GET request
        return jsonify({"status": "ok", "message": "Shadow SMS Sync API is live"}), 200

if __name__ == "__main__":
    app.run(debug=True)
