from repositories.shopping_list_repository import ShoppingListRepository
from repositories.recipe_repository import RecipeRepository
from models.shopping_list import ShoppingList
from models.recipe_ingredient import RecipeIngredient
from models.ingredient import Ingredient

class ShoppingListService:
    @staticmethod
    def add_to_shopping_list(user_id, recipe_id):
        shopping_list = ShoppingList(user_id=user_id, recipe_id=recipe_id)
        ShoppingListRepository.add_to_shopping_list(shopping_list)
        return shopping_list


    @staticmethod
    def delete_from_shopping_list(user_id, recipe_id):
        shopping_list = ShoppingList.query.filter_by(user_id=user_id, recipe_id=recipe_id).first()
        ShoppingListRepository.delete_from_shopping_list(shopping_list)
        return shopping_list

    @staticmethod
    def get_aggregated_ingredients(user_id):
        shopping_list = ShoppingListRepository.get_shopping_list_by_user_id(user_id)
        ingredient_quantities = {}
        recipes = []

        for item in shopping_list:
            recipe_ingredients = RecipeIngredient.query.filter_by(recipe_id=item.recipe_id).all()
            recipe = RecipeRepository.get_recipe_by_id(item.recipe_id)
            recipes.append(recipe)
            for ri in recipe_ingredients:
                ingredient = Ingredient.query.get(ri.ingredient_id)
                if ingredient.name in ingredient_quantities:
                    ingredient_quantities[ingredient.name]["quantity"] += int(ri.quantity)
                else:
                    ingredient_quantities[ingredient.name] = {
                        "quantity": int(ri.quantity),
                        "unit": ingredient.measure_unit
                    }

        results = {
            "recipes": [recipe.to_dict() for recipe in recipes],
            "ingredients": ingredient_quantities
        }
        return results

    def is_in_shopping_list(user_id, recipe_id):
        return ShoppingListRepository.get_shopping_list_by_ids(user_id, recipe_id) is not None