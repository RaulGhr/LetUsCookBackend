from extensions import db


class RecipeIngredient(db.Model):
    __tablename__ = 'RecipeIngredient'

    recipe_id = db.Column(db.Integer, db.ForeignKey('Recipe.id'), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('Ingredient.id'), primary_key=True)
    quantity = db.Column(db.Float, nullable=False)

    recipe = db.relationship(
        'Recipe',
        back_populates='recipe_ingredients',
        overlaps="ingredients,recipes"
    )
    ingredient = db.relationship(
        'Ingredient',
        back_populates='recipe_ingredients',
        overlaps="recipes,ingredients"
    )
