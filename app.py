from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Cross-origin এর জন্য দরকার হতে পারে

@app.route('/', methods=['POST'])  # ❗ এখানে POST স্পষ্ট করে বলা আছে
def receive_sms():
    data = request.get_json()
    number = data.get("number")
    message = data.get("message")

    print("Number:", number)
    print("Message:", message)

    return jsonify({"status": "success", "number": number, "message": message})

if __name__ == '__main__':
    app.run()
