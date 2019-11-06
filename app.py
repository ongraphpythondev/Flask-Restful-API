# Flask Import
from flask import Blueprint
from flask_restful import Api
# Project Import
from resources.Category import CategoryResources, CategoryResource
from resources.Product import ProductResources, ProductResource

# App Initialization
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
api.add_resource(CategoryResources, '/category/', methods=['GET', 'POST'])
api.add_resource(CategoryResource, '/category/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
api.add_resource(ProductResources, '/product/', methods=['GET', 'POST'])
api.add_resource(ProductResource, '/product/<int:id>/', methods=['GET', 'PUT', 'DELETE'])