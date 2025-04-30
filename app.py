# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        print("Received data:", data)  # For debugging (visible in Azure logs)
        return jsonify({"message": "Data received successfully"}), 200
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
