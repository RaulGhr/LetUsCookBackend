from models.ingredient import Ingredient
from app import db

class IngredientRepository:
    @staticmethod
    def add_ingredient(ingredient):
        db.session.add(ingredient)
        db.session.commit()

    @staticmethod
    def get_ingredient_by_id(ingredient_id):
        return Ingredient.query.get(ingredient_id)

    @staticmethod
    def get_all_ingredients():
        return Ingredient.query.all()
