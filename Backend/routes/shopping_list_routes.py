from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.shopping_list_service import ShoppingListService

shopping_list_bp = Blueprint('shopping_list_bp', __name__)

@shopping_list_bp.route('/add', methods=['POST'])
@jwt_required()
def add_to_shopping_list():
    data = request.get_json()
    user_id = get_jwt_identity()
    recipe_id = data.get('recipe_id')

    if ShoppingListService.is_in_shopping_list(user_id, recipe_id):
        return jsonify({"message": "Recipe already in shopping list"}), 400

    shopping_list = ShoppingListService.add_to_shopping_list(user_id, recipe_id)
    return jsonify({"message": "Recipe added to shopping list successfully", "shopping_list": shopping_list.to_dict()}), 201

@shopping_list_bp.route('/delete/<int:recipe_id>', methods=['DELETE'])
@jwt_required()
def delete_from_shopping_list(recipe_id):
    # data = request.get_json()
    user_id = get_jwt_identity()
    # recipe_id = data.get('recipe_id')

    if not ShoppingListService.is_in_shopping_list(user_id, recipe_id):
        return jsonify({"message": "Recipe not in shopping list"}), 400

    shopping_list = ShoppingListService.delete_from_shopping_list(user_id, recipe_id)
    return jsonify({"message": "Recipe deleted from shopping list successfully", "shopping_list": shopping_list.to_dict()}), 200

@shopping_list_bp.route('/get', methods=['GET'])
@jwt_required()
def get_shopping_list():
    user_id = get_jwt_identity()
    ingredients = ShoppingListService.get_aggregated_ingredients(user_id)
    return jsonify(ingredients), 200