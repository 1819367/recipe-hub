from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db, Recipe  # Import models
import os

app = Flask(__name__)
CORS(app)

# DB config
db_uri = 'sqlite:///recipes_local.db'
if os.environ.get('DATABASE_URL'):
    db_uri = os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://")

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)  

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask!"})

@app.route("/api/recipes", methods=['GET', 'POST'])  # ← ONE ROUTE, BOTH METHODS
def recipes():
    if request.method == 'GET':
        recipes = Recipe.query.all()
        return jsonify([recipe.to_dict() for recipe in recipes])
    
    if request.method == 'POST':
        data = request.get_json()
        required_fields = ['title', 'ingredients', 'instructions', 'servings', 'description', 'image_url']
        
        for field in required_fields:
            if field not in data or data[field] == "":
                return jsonify({'error': f"Missing required field: '{field}'"}), 400
        
        new_recipe = Recipe(
            title=data['title'],
            ingredients=data['ingredients'],
            instructions=data['instructions'],
            servings=data['servings'],
            description=data['description'],
            image_url=data['image_url']
        )
        
        db.session.add(new_recipe)
        db.session.commit()
        
        return jsonify({
            'message': 'Recipe added successfully', 
            'recipe': new_recipe.to_dict()
        }), 201

# @app.route("/api/seed")
# def seed_data():
#     """Add sample recipes to database (run ONCE)"""
#     # Check if data exists to avoid duplicates
#     if Recipe.query.count() == 0:
#         sample_recipes = [
#             Recipe(
#                 title="Chocolate Cake",
#                 ingredients="flour, sugar, cocoa, eggs, butter",
#                 instructions="Mix, bake at 350°F for 30 min",
#                 servings=8
#             ),
#             Recipe(
#                 title="Pasta Carbonara",
#                 ingredients="pasta, eggs, pancetta, parmesan",
#                 instructions="Boil pasta, mix with egg sauce",
#                 servings=4
#             )
#         ]
        
#         for recipe in sample_recipes:
#             db.session.add(recipe)
        
#         db.session.commit()
#         return jsonify({"message": f"Seeded {len(sample_recipes)} recipes!"})
#     else:
#         return jsonify({"message": "Database already has data!"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

