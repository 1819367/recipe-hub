from app import app
from flask import jsonify   # better to use jsonify for JSON responses

@app.route('/api/test')
def test():
    return jsonify({"message": "Flask backend is working!"})