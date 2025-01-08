from repositories.favorite_recipe_repository import FavoriteRecipeRepository
from models.favorite_recipe import FavoriteRecipe

class FavoriteRecipeService:
    @staticmethod
    def add_favorite_recipe(user_id, recipe_id):
        favorite_recipe = FavoriteRecipe(user_id=user_id, recipe_id=recipe_id)
        FavoriteRecipeRepository.add_favorite_recipe(favorite_recipe)
        return favorite_recipe

    @staticmethod
    def delete_favorite_recipe(user_id, recipe_id):
        favorites_recipes = FavoriteRecipeRepository.get_favorite_recipes_by_user_id(user_id)
        favorite_recipe = None
        for favorite in favorites_recipes:
            if favorite.recipe_id == recipe_id:
                favorite_recipe = favorite
                break
        FavoriteRecipeRepository.delete_favorite_recipe(favorite_recipe)
        return favorite_recipe

    @staticmethod
    def get_all_favorite_recipes():
        return FavoriteRecipeRepository.get_all_favorite_recipes()

    @staticmethod
    def get_favorite_recipe_by_user_id(user_id):
        return FavoriteRecipeRepository.get_favorite_recipes_by_user_id(user_id)