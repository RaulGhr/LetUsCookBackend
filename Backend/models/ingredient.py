from app import db

class Ingredient(db.Model):
    __tablename__ = 'Ingredient'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    measure_unit = db.Column(db.String(50))
