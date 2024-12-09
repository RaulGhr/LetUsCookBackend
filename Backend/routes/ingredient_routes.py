from flask import Blueprint, request, jsonify

from services.ingredient_service import IngredientService

ingredient_bp = Blueprint('ingredient_bp', __name__)

@ingredient_bp.route('/create', methods=['POST'])
def create_ingredient():
    body = request.get_json()
    name = body['name']
    measure_unit = body['measureunit']

    ingredient = IngredientService.add_ingredient(name, measure_unit)
    return jsonify({"message": "Ingredient created successfully", "ingredient": ingredient.id}), 201

@ingredient_bp.route('/getAll', methods=['GET'])
def get_all_ingredients():
    ingredients = IngredientService.get_all_ingredients()
    return jsonify([ingredient.to_dict() for ingredient in ingredients]), 200