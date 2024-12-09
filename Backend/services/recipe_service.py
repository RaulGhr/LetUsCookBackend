from models.ingredient import Ingredient
from repositories.ingredient_repository import IngredientRepository
from repositories.recipe_repository import RecipeRepository
from models.recipe import Recipe
from repositories.user_repository import UserRepository
from services.service_result import ServiceResult

class RecipeService:
    @staticmethod
    def add_recipe(user_id, title, images, description, instructions, servings, prep_time, cook_time, ingredients_ids):
        user = UserRepository.get_user_by_id(user_id)
        if user is None:
            return ServiceResult(
                success=False,
                error_message='User does not exist',
                status_code=400,
                error_code='user_not_found'
            )

        ingredients = IngredientRepository.get_all_ingredients(Ingredient.id.in_(ingredients_ids))
        if len(ingredients) != len(ingredients_ids):
            return ServiceResult(
                success=False,
                error_message='Some ingredients do not exist',
                status_code=400,
                error_code='ingredient_not_found'
            )

        recipe = Recipe(
            user_id=user_id,
            title=title,
            images=images,
            description=description,
            instructions=instructions,
            servings=servings,
            prep_time=prep_time,
            cook_time=cook_time,
            number_of_likes=0,
            ingredients=ingredients
        )
        RecipeRepository.add_recipe(recipe)
        return ServiceResult(success=True, data=recipe, status_code=201)

    @staticmethod
    def get_all_recipes(title=None):
        return RecipeRepository.get_all_recipes(title)

    @staticmethod
    def get_recipes_by_user_id(user_id):
        return RecipeRepository.get_recipes_by_user(user_id)

    @staticmethod
    def like_recipe(recipe_id):
        return RecipeService.update_recipe(recipe_id, Recipe.like)

    @staticmethod
    def dislike_recipe(recipe_id):
        return RecipeService.update_recipe(recipe_id, Recipe.dislike)

    @staticmethod
    def update_recipe(recipe_id, update_method):
        recipe = RecipeRepository.get_recipe_by_id(recipe_id)
        if recipe is None:
            return ServiceResult(
                success=False,
                error_message='Recipe does not exist',
                status_code=404,
                error_code='recipe_not_found'
            )

        update_method(recipe)
        RecipeRepository.commit()

        return ServiceResult(success=True, data=recipe, status_code=200)