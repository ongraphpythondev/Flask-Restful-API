# Flask Import
from marshmallow import fields, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()  # Object to serialization/deserialization
db = SQLAlchemy()  # Object to database


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, name, category_id):
        self.name = name
        self.category_id = category_id

# Serialization/Deserialization
class CategorySchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=False)


class ProductSchema(ma.Schema):
    id = fields.Integer()
    category_id = fields.Integer(required=False)
    name = fields.String(required=False, validate=validate.Length(1))
