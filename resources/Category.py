from flask import request
from flask_restful import Resource
from Model import db, Category, CategorySchema

categories_schema = CategorySchema(many=True)
category_schema = CategorySchema()


class CategoryResources(Resource):
    def get(self):
        categories = Category.query.all()
        categories = categories_schema.dump(categories)
        return {'status': 'success', 'data': categories}, 200

    def post(self):
        json_data = request.get_json(force=True)
        data = category_schema.load(json_data)
        category = Category.query.filter_by(name=data['name']).first()
        if category:
            return {'message': 'Category already exists'}, 400
        category = Category(name=json_data['name'])
        db.session.add(category)
        db.session.commit()
        result = category_schema.dump(category)
        return { "status": 'success', 'data': result }, 201


class CategoryResource(Resource):
    def get(self, id):
        category = Category.query.filter_by(id=id)
        if category.count() > 0:
            category = categories_schema.dump(category)
            return {'status': 'success', 'data': category}, 200
        else:
            return {'message': 'Category does not exist'}, 400

    def put(self, id):
        json_data = request.get_json(force=True)
        data = category_schema.load(json_data)
        category = Category.query.filter_by(id=id)
        if category.count() > 0:
            category = category.first()
            category.name = data['name']
            db.session.commit()
            result = category_schema.dump(category)
            return { "status": 'success', 'data': result }, 200
        else:
            return {'message': 'Category does not exist'}, 400

    def delete(self, id):
        category = Category.query.filter_by(id=id)
        if category.count() > 0:
            category.delete()
            db.session.commit()
            return {'status': 'success'}, 200
        else:
            return {'message': 'Category does not exist'}, 400