from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Local SQLite OR Render Postgres
db_uri = 'sqlite:///recipes_local.db'  # default for local dev

database_url = os.environ.get('DATABASE_URL')
if database_url:
    # Render sets DATABASE_URL in the Environment tab
    db_uri = database_url.replace("postgres://", "postgresql://")

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask with DB!"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Auto-creates tables in SQLite or Postgres
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

