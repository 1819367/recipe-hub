from flask import send_from_directory
import os

def add_production_routes(app):
    if 'prod_index' not in app.view_functions:
        @app.route('/', defaults={'path': ''}, endpoint='prod_index')
        def index():
            return send_from_directory(app.static_folder, 'index.html')

    if 'catchall' not in app.view_functions:
        @app.route('/<path:path>', endpoint='catchall')
        def catch_all(path):
            if os.path.exists(os.path.join(app.static_folder, path)):
                return send_from_directory(app.static_folder, path)
            return send_from_directory(app.static_folder, 'index.html')
