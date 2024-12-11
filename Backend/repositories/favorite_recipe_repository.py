from extensions import db
from models.favorite_recipe import FavoriteRecipe

class FavoriteRecipeRepository():
    @staticmethod
    def add_favorite_recipe(favorite_recipe):
        db.session.add(favorite_recipe)
        db.session.commit()

    @staticmethod
    def get_favorite_recipe_by_id(favorite_recipe_id):
        return FavoriteRecipe.query.get(favorite_recipe_id)

    @staticmethod
    def get_favorite_recipes_by_user_id(user_id):
        return FavoriteRecipe.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_all_favorite_recipes():
        return FavoriteRecipe.query.all()