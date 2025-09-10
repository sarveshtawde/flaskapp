from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

# Get absolute path of data.json relative to app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")

@app.route('/api', methods=['GET'])
def get_data():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
