from repositories.recipe_repository import RecipeRepository
from models.recipe import Recipe

class RecipeService:
    @staticmethod
    def add_recipe(user_id, title, images, description, instructions, servings, prep_time, cook_time):
        recipe = Recipe(
            user_id=user_id,
            title=title,
            images=images,
            description=description,
            instructions=instructions,
            servings=servings,
            prep_time=prep_time,
            cook_time=cook_time
        )
        RecipeRepository.add_recipe(recipe)
        return recipe

    @staticmethod
    def get_all_recipes():
        return RecipeRepository.get_all_recipes()