from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Importa si inregistreaza rutele
# from routes.user_routes import user_bp
# from routes.ingredient_routes import ingredient_bp
# from routes.recipe_routes import recipe_bp

# app.register_blueprint(user_bp, url_prefix='/users')
# app.register_blueprint(ingredient_bp, url_prefix='/ingredients')
# app.register_blueprint(recipe_bp, url_prefix='/recipes')

if __name__ == "__main__":
    app.run(debug=True)
