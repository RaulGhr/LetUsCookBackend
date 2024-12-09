from app import db
from models.recipe import Recipe
from models.user import User


class FavoriteRecipe(db.Model):
    __tablename__ = 'FavoriteRecipe'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    recipe_id = db.Column(db.Integer, db.ForeignKey(Recipe.id))

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "recipe_id": self.recipe_id
        }