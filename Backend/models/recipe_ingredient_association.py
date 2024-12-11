from extensions import db

class RecipeIngredient(db.Model):
    __tablename__ = 'RecipeIngredient'
    recipe_id = db.Column(db.Integer, db.ForeignKey('Recipe.id'), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('Ingredient.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
