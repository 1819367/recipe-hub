#contains routes
from . import main_bp
from flask import jsonify

@main_bp.route('/api/test')
def test():
    return jsonify({"message": "Flask backend is working!"})
