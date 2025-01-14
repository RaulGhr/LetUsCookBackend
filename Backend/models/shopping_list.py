from extensions import db

class ShoppingList(db.Model):
    __tablename__ = 'ShoppingList'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('Recipe.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "recipe_id": self.recipe_id
        }