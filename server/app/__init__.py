# contains create_app()
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()  # This loads .env file variables into environment

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')

    if os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object('server.config.ProductionConfig')
    else:
        app.config.from_object('server.config.DevelopmentConfig')

    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from .main import main_bp
    app.register_blueprint(main_bp)

    from .production import add_production_routes
    add_production_routes(app)


    return app
