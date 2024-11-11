from repositories.ingredient_repository import IngredientRepository
from models.ingredient import Ingredient

class IngredientService:
    @staticmethod
    def add_ingredient(name, measure_unit=None):
        ingredient = Ingredient(name=name, measure_unit=measure_unit)
        IngredientRepository.add_ingredient(ingredient)
        return ingredient

    @staticmethod
    def get_all_ingredients():
        return IngredientRepository.get_all_ingredients()
