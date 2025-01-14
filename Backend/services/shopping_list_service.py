from repositories.shopping_list_repository import ShoppingListRepository
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
    def get_aggregated_ingredients(user_id):
        shopping_list = ShoppingListRepository.get_shopping_list_by_user_id(user_id)
        ingredient_quantities = {}

        for item in shopping_list:
            recipe_ingredients = RecipeIngredient.query.filter_by(recipe_id=item.recipe_id).all()
            for ri in recipe_ingredients:
                ingredient = Ingredient.query.get(ri.ingredient_id)
                if ingredient.name in ingredient_quantities:
                    ingredient_quantities[ingredient.name] += ri.quantity
                else:
                    ingredient_quantities[ingredient.name] = ri.quantity

        return ingredient_quantities