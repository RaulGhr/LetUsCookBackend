# app.py
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from extensions import db, bcrypt, jwt
from config import Config
from routes.middlewares.normalize_request_json import normalize_request_json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

from routes.user_routes import user_bp
from routes.ingredient_routes import ingredient_bp
from routes.recipe_routes import recipe_bp
from routes.user_follow_routes import user_follow_bp
from routes.favorite_recipe_routes import favorite_recipe_bp
from routes.review_routes import review_bp
from routes.shopping_list_routes import shopping_list_bp

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(ingredient_bp, url_prefix='/ingredients')
app.register_blueprint(recipe_bp, url_prefix='/recipes')
app.register_blueprint(user_follow_bp, url_prefix='/user_follows')
app.register_blueprint(favorite_recipe_bp, url_prefix='/favorite_recipes')
app.register_blueprint(review_bp, url_prefix='/reviews')

app.register_blueprint(shopping_list_bp, url_prefix='/shopping_list')

app.before_request(normalize_request_json)

with app.app_context(): db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
