from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_lag', methods=['POST'])
def send_lag():
    uid = request.json.get('uid')
    if not uid:
        return jsonify({"status": "error", "message": "UID is required"}), 400
    
    # API Endpoint
    api_url = f"https://uidlag.onrender.com/lag?uid={uid}"
    
    try:
        response = requests.get(api_url, timeout=15)
        return jsonify({"status": "success", "message": "COMPLETE LAG"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
