from flask import jsonify, request
from flask_restful import Resource
from Model import db, Product, Category, ProductSchema

products_schema = ProductSchema(many=True)
product_schema = ProductSchema()


class ProductResources(Resource):
    def get(self):
        products = Product.query.all()
        products = products_schema.dump(products)
        return {"status":"success", "data":products}, 200

    def post(self):
        json_data = request.get_json(force=True)
        data = product_schema.load(json_data)
        category_id = Category.query.filter_by(id=data['category_id']).first()
        if not category_id:
            return {'status': 'error', 'message': 'product category not found'}, 400
        product = Product(category_id=data['category_id'], name=data['name'])
        db.session.add(product)
        db.session.commit()
        result = product_schema.dump(product)
        return {'status': "success", 'data': result}, 201


class ProductResource(Resource):
    def get(self, id):
        product = Product.query.filter_by(id=id)
        if product.count() > 0:
            product = products_schema.dump(product)
            return {'status': 'success', 'data': product}, 200
        else:
            return {'message': 'Product does not exist'}, 400

    def put(self, id):
        json_data = request.get_json(force=True)
        data = product_schema.load(json_data)
        product = Product.query.filter_by(id=id)
        if product.count() > 0:
            product = product.first()
            product.name = data['name']
            product.category_id = data['category_id']
            db.session.commit()
            result = product_schema.dump(product)
            return {"status": 'success', 'data': result}, 200
        else:
            return {'message': 'Product does not exist'}, 400

    def delete(self, id):
        product = Product.query.filter_by(id=id)
        if product.count() > 0:
            product.delete()
            db.session.commit()
            return { "status": 'success'}, 200
        else:
            return {'message': 'Product does not exist'}, 400

