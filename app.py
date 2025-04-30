from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Data endpoint
@app.route('/api/data', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        print("Received data:", data)
        return jsonify({"message": "Data received successfully"}), 200
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500

# Optional: Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(debug=True)
