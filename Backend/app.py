# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Importă și înregistrează rutele
from routes.user_routes import user_bp
# from routes.ingredient_routes import ingredient_bp
from routes.recipe_routes import recipe_bp

app.register_blueprint(user_bp, url_prefix='/users')
# app.register_blueprint(ingredient_bp, url_prefix='/ingredients')
app.register_blueprint(recipe_bp, url_prefix='/recipes')

with app.app_context(): db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
