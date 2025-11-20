from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))  

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# Database config (we'll add SQLAlchemy later when it works)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
if os.environ.get('DATABASE_URL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Import routes AFTER app is created
from routes import *

# PRODUCTION: Serve React on Render
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)