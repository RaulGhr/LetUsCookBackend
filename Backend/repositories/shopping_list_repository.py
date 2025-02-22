from models.shopping_list import ShoppingList
from extensions import db

class ShoppingListRepository:
    @staticmethod
    def add_to_shopping_list(shopping_list):
        db.session.add(shopping_list)
        db.session.commit()

    @staticmethod
    def delete_from_shopping_list(shopping_list):
        db.session.delete(shopping_list)
        db.session.commit()

    @staticmethod
    def get_shopping_list_by_user_id(user_id):
        return ShoppingList.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_shopping_list_by_ids(user_id, recipe_id):
        return ShoppingList.query.filter_by(user_id=user_id, recipe_id=recipe_id).first()