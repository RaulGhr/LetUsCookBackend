from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.recipe_service import RecipeService
from services.recipe_like_service import RecipeLikeService
from services.favorite_recipe_service import FavoriteRecipeService
from services.shopping_list_service import ShoppingListService
from services.user_service import UserService

recipe_bp = Blueprint('recipe_bp', __name__)

@recipe_bp.route('/create', methods=['POST'])
@jwt_required()
def create_recipe():
    data = request.get_json()
    user_id = get_jwt_identity()
    title = data.get('title')
    images = data.get('img')
    description = data.get('description')
    instructions = data.get('instructions')
    servings = data.get('servings')
    prep_time = data.get('preptime')
    cook_time = data.get('cooktime')
    ingredients = data.get('ingredients')

    service_result = RecipeService.add_recipe(user_id, title, images, description, instructions, servings, prep_time, cook_time, ingredients)
    if not service_result.success:
        return jsonify(service_result.get_error_map()), service_result.status_code

    return jsonify(service_result.data.to_dict()), service_result.status_code

@recipe_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_recipes():
    user_id = get_jwt_identity()
    query_params = request.args
    title = query_params.get('title')
    recipe_id = query_params.get('recipe_id')

    recipes = [RecipeService.get_recipe_by_id(recipe_id)] if recipe_id else RecipeService.get_all_recipes(title)
    favorites = [fav.to_dict()['recipe_id'] for fav in FavoriteRecipeService.get_favorite_recipe_by_user_id(user_id)]
    recipes_json = [recipe.to_dict() for recipe in recipes]
    for recipe in recipes_json:
        recipe['isFavorite'] = recipe['id'] in favorites
        recipe['numberOfLikes'] = RecipeLikeService.get_recipe_like_count(recipe['id'])
        recipe['isLiked'] = RecipeLikeService.is_recipe_liked_by_user(user_id, recipe['id'])
        recipe['isInShoppingList'] = ShoppingListService.is_in_shopping_list(user_id, recipe['id'])



    return jsonify(recipes_json), 200

@recipe_bp.route('/getAllForCurrentUser', methods=['GET'])
@jwt_required()
def get_all_recipes_for_user():
    user_id = get_jwt_identity()
    recipes = RecipeService.get_recipes_by_user_id(user_id)
    favorites = [fav.to_dict()['recipe_id'] for fav in FavoriteRecipeService.get_favorite_recipe_by_user_id(user_id)]
    recipes_json = [recipe.to_dict() for recipe in recipes]
    for recipe in recipes_json:
        recipe['isFavorite'] = recipe['id'] in favorites
        recipe['numberOfLikes'] = RecipeLikeService.get_recipe_like_count(recipe['id'])
        recipe['isLiked'] = RecipeLikeService.is_recipe_liked_by_user(user_id, recipe['id'])
        recipe['isInShoppingList'] = ShoppingListService.is_in_shopping_list(user_id, recipe['id'])
    return jsonify(recipes_json), 200

@recipe_bp.route('/getAllById', methods=['GET'])
@jwt_required()
def get_all_recipes_by_username():
    selected_user_id = request.args.get('user_id')
    user_id = get_jwt_identity()
    recipes = RecipeService.get_recipes_by_user_id(selected_user_id)
    favorites = [fav.to_dict()['recipe_id'] for fav in FavoriteRecipeService.get_favorite_recipe_by_user_id(user_id)]
    recipes_json = [recipe.to_dict() for recipe in recipes]
    for recipe in recipes_json:
        recipe['isFavorite'] = recipe['id'] in favorites
        recipe['numberOfLikes'] = RecipeLikeService.get_recipe_like_count(recipe['id'])
        recipe['isLiked'] = RecipeLikeService.is_recipe_liked_by_user(user_id, recipe['id'])
        recipe['isInShoppingList'] = ShoppingListService.is_in_shopping_list(user_id, recipe['id'])

    return jsonify(recipes_json), 200

@recipe_bp.route('/like', methods=['POST'])
@jwt_required()
def like_recipe():
    data = request.get_json()
    recipe_id = data.get('recipe_id')
    user_id = get_jwt_identity()
    if RecipeLikeService.is_recipe_liked_by_user(user_id, recipe_id):
        return '', 200
    RecipeLikeService.add_like(user_id, recipe_id)
    return '', 200

@recipe_bp.route('/dislike', methods=['POST'])
@jwt_required()
def dislike_recipe():
    data = request.get_json()
    recipe_id = data.get('recipe_id')
    user_id = get_jwt_identity()
    if RecipeLikeService.is_recipe_liked_by_user(user_id, recipe_id) is False:
        return '', 200
    RecipeLikeService.delete_like(user_id, recipe_id)
    return '', 200

@recipe_bp.route('/favorite', methods=['GET'])
@jwt_required()
def get_favorite_recipes():
    user_id = get_jwt_identity()
    favorite_recipes = [fav.to_dict() for fav in FavoriteRecipeService.get_favorite_recipe_by_user_id(user_id)]
    # print(favorite_recipes)
    result = []
    for fav in favorite_recipes:
        recipe = RecipeService.get_recipe_by_id(fav['recipe_id'])
        recipe_dict = recipe.to_dict()
        recipe_dict['isFavorite'] = True
        result.append(recipe_dict)

    return jsonify(result), 200

@recipe_bp.route('/getFollowingUsersRecipes', methods=['GET'])
@jwt_required()
def get_followed_users_recipes():
    user_id = get_jwt_identity()
    recipes = RecipeService.get_recipes_by_followed_users(user_id)

    recipes_sorted = sorted(recipes, key=lambda x: x.created_at, reverse=True)
    recipes_json = [recipe.to_dict() for recipe in recipes_sorted]

    # return jsonify(recipes_json), 200

    favorites = [fav.to_dict()['recipe_id'] for fav in FavoriteRecipeService.get_favorite_recipe_by_user_id(user_id)]
    # recipes_json = [recipe.to_dict() for recipe in recipes]
    for recipe in recipes_json:
        recipe['isFavorite'] = recipe['id'] in favorites
        recipe['numberOfLikes'] = RecipeLikeService.get_recipe_like_count(recipe['id'])
        recipe['isLiked'] = RecipeLikeService.is_recipe_liked_by_user(user_id, recipe['id'])
        recipe['isInShoppingList'] = ShoppingListService.is_in_shopping_list(user_id, recipe['id'])

    return jsonify(recipes_json), 200

