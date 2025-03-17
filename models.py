from db import db

class TajPalace(db.Model):
    dish_id = db.Column(db.Integer, primary_key=True)
    dish_name = db.Column(db.String(100), nullable=False)
    dish_price = db.Column(db.Float, nullable=False)
    dish_image = db.Column(db.String(100), nullable=False)
    dish_description = db.Column(db.String(100), nullable=False)
    dish_category = db.Column(db.String(100), nullable=False)
    dish_rating = db.Column(db.Float, nullable=False)

class SarwaanaBhawan(db.Model):
    dish_id = db.Column(db.Integer, primary_key=True)
    dish_name = db.Column(db.String(100), nullable=False)
    dish_price = db.Column(db.Float, nullable=False)
    dish_image = db.Column(db.String(100), nullable=False)
    dish_description = db.Column(db.String(100), nullable=False)
    dish_category = db.Column(db.String(100), nullable=False)
    dish_rating = db.Column(db.Float, nullable=False)

class PunjabGrill(db.Model):
    dish_id = db.Column(db.Integer, primary_key=True)
    dish_name = db.Column(db.String(100), nullable=False)
    dish_price = db.Column(db.Float, nullable=False)
    dish_image = db.Column(db.String(100), nullable=False)
    dish_description = db.Column(db.String(100), nullable=False)
    dish_category = db.Column(db.String(100), nullable=False)
    dish_rating = db.Column(db.Float, nullable=False)

class DosaPlaza(db.Model):
    dish_id = db.Column(db.Integer, primary_key=True)
    dish_name = db.Column(db.String(100), nullable=False)
    dish_price = db.Column(db.Float, nullable=False)
    dish_image = db.Column(db.String(100), nullable=False)
    dish_description = db.Column(db.String(100), nullable=False)
    dish_category = db.Column(db.String(100), nullable=False)
    dish_rating = db.Column(db.Float, nullable=False)

class BiryaniHouse(db.Model):
    dish_id = db.Column(db.Integer, primary_key=True)
    dish_name = db.Column(db.String(100), nullable=False)
    dish_price = db.Column(db.Float, nullable=False)
    dish_image = db.Column(db.String(100), nullable=False)
    dish_description = db.Column(db.String(100), nullable=False)
    dish_category = db.Column(db.String(100), nullable=False)
    dish_rating = db.Column(db.Float, nullable=False)

class Baarista(db.Model):
    dish_id = db.Column(db.Integer, primary_key=True)
    dish_name = db.Column(db.String(100), nullable=False)
    dish_price = db.Column(db.Float, nullable=False)
    dish_image = db.Column(db.String(100), nullable=False)
    dish_description = db.Column(db.String(100), nullable=False)
    dish_category = db.Column(db.String(100), nullable=False)
    dish_rating = db.Column(db.Float, nullable=False)

class MughalsKitchen(db.Model):
    dish_id = db.Column(db.Integer, primary_key=True)
    dish_name = db.Column(db.String(100), nullable=False)
    dish_price = db.Column(db.Float, nullable=False)
    dish_image = db.Column(db.String(100), nullable=False)
    dish_description = db.Column(db.String(100), nullable=False)
    dish_category = db.Column(db.String(100), nullable=False)
    dish_rating = db.Column(db.Float, nullable=False)