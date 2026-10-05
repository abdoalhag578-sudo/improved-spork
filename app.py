from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
  return "Flask API is running successfully!"


@app.route("/api", methods=["POST", "GET"])
def api():
  # يمكنك استقبال البيانات هنا وإرسال رد لـ AppSheet
  return jsonify({"status": "success", "message": "Connected to AppSheet!"})


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
