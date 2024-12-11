from app import db
from models.recipe_ingredient import RecipeIngredient
from repositories.ingredient_repository import IngredientRepository
from repositories.recipe_repository import RecipeRepository
from models.recipe import Recipe
from repositories.user_repository import UserRepository
from services.service_result import ServiceResult

class RecipeService:
    @staticmethod
    def add_recipe(user_id, title, images, description, instructions, servings, prep_time, cook_time, ingredients_req):
        user = UserRepository.get_user_by_id(user_id)
        if user is None:
            return ServiceResult(
                success=False,
                error_message='User does not exist',
                status_code=400,
                error_code='user_not_found'
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
        )

        for ingredient_req in ingredients_req:
            ingredient_id = ingredient_req['id']
            quantity = ingredient_req['quantity']
            ingredient = IngredientRepository.get_ingredient_by_id(ingredient_id)
            if ingredient is None:
                return ServiceResult(
                    success=False,
                    error_message='Some ingredients do not exist',
                    status_code=400,
                    error_code='ingredient_not_found'
                )

            recipe_ingredient = RecipeIngredient(recipe=recipe, ingredient=ingredient, quantity=quantity)
            db.session.add(recipe_ingredient)

        db.session.add(recipe)
        db.session.commit()

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