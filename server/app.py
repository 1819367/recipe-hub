from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))  

os.environ['PYTHONHASHSEED'] = '0'  

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

# PRODUCTION: Serve React build on Render
try:
    from production import add_production_routes
    add_production_routes(app)
except ImportError:
    pass  # Local dev — no problem

if __name__ == '__main__':
    app.run(debug=True)