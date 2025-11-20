from flask import send_from_directory
import os

def add_production_routes(app):
    @app.route('/', defaults={'path': ''})
    def index():
        return send_from_directory(app.static_folder, 'index.html')

    @app.route('/<path:path>', endpoint='catchall')  # <-- different endpoint name
    def catch_all(path):
        if os.path.exists(os.path.join(app.static_folder, path)):
            return send_from_directory(app.static_folder, path)
        return send_from_directory(app.static_folder, 'index.html')