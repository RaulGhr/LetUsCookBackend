from models.recipe import Recipe
from app import db

class RecipeRepository:
    @staticmethod
    def add_recipe(recipe):
        db.session.add(recipe)
        db.session.commit()

    @staticmethod
    def get_recipe_by_id(recipe_id):
        return Recipe.query.get(recipe_id)

    @staticmethod
    def get_recipes_by_user(user_id):
        return Recipe.query.filter_by(user_id=user_id).all()
