from flask import send_from_directory
import os

def add_production_routes(app):
    print("[DEBUG] add_production_routes called in production.py")
    print("[DEBUG] Existing endpoints before registration:", list(app.view_functions.keys()))

    if 'prod_index' not in app.view_functions and 'catchall' not in app.view_functions:
        print("[DEBUG] Registering prod_index and catchall")
        @app.route('/', defaults={'path': ''}, endpoint='prod_index')
        @app.route('/<path:path>', endpoint='catchall')
        def serve_react(path):
            if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
                return send_from_directory(app.static_folder, path)
            return send_from_directory(app.static_folder, 'index.html')

    else:
        if 'prod_index' in app.view_functions:
            print("[DEBUG] prod_index already registered!")
        if 'catchall' in app.view_functions:
            print("[DEBUG] catchall already registered!")

    print("[DEBUG] Existing endpoints after registration:", list(app.view_functions.keys()))
