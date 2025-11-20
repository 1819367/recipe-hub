from flask import send_from_directory
import os

def add_production_routes(app):
    print("[DEBUG] add_production_routes called in production.py")
    print("[DEBUG] Existing endpoints before registration:", list(app.view_functions.keys()))

    if 'prod_index' not in app.view_functions:
        print("[DEBUG] Registering prod_index")
        @app.route('/', defaults={'path': ''}, endpoint='prod_index')
        def index():
            return send_from_directory(app.static_folder, 'index.html')
    else:
        print("[DEBUG] prod_index already registered!")

    if 'catchall' not in app.view_functions:
        print("[DEBUG] Registering catchall")
        @app.route('/<path:path>', endpoint='catchall')
        def catch_all(path):
            if os.path.exists(os.path.join(app.static_folder, path)):
                return send_from_directory(app.static_folder, path)
            return send_from_directory(app.static_folder, 'index.html')
    else:
        print("[DEBUG] catchall already registered!")

    print("[DEBUG] Existing endpoints after registration:", list(app.view_functions.keys()))

