from models.recipe import Recipe
from extensions import db

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

    @staticmethod
    def get_all_recipes(title=None):
        if title:
            return Recipe.query.filter(Recipe.title.startswith(title)).all()

        return Recipe.query.all()

    @staticmethod
    def get_recipes_by_followed_users(user_ids):
        return Recipe.query.filter(Recipe.user_id.in_(user_ids)).order_by(Recipe.created_at.desc()).all()

    @staticmethod
    def commit():
        db.session.commit()