from flask import Flask, jsonify, request, send_file
import os

app = Flask(__name__)

# Dashboard route
@app.route('/', methods=['GET'])
def dashboard():
    """Serve the dashboard HTML"""
    try:
        with open('dashboard.html', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return jsonify({"error": "Dashboard not found"}), 404

# Health check route
@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        "status": "online",
        "bot_name": "ELTHRANY FF",
        "message": "البوت شغّال 🟢"
    })

# API endpoint for bot status
@app.route('/api/status', methods=['GET'])
def bot_status():
    return jsonify({
        "online": True,
        "bot_name": "ELTHRANY FF",
        "region": "ME",
        "commands_available": ["emote", "squad", "status"]
    })

# Catch-all for undefined routes
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint not found", "message": "الـ route هذا غير موجود"}), 404

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
