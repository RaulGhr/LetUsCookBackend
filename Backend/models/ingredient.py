from app import db

class Ingredient(db.Model):
    __tablename__ = 'Ingredient'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    measure_unit = db.Column(db.String(50))
    recipes = db.relationship('Recipe', secondary='RecipeIngredient', back_populates='ingredients')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "measureUnit": self.measure_unit,
        }
