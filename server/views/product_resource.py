from flask import jsonify, make_response, request
from flask_restful import Resource
from models import product, db
from models import supplier

class ProductResource(Resource):
    def get(self):
        products = [prod.to_dict() for prod in product.Product.query.all()]
        return make_response(jsonify(products), 200)

    def post(self):
        data = request.get_json()

        # Validate required fields
        if not all(k in data for k in ("name", "description", "price", "quantity","supplier_id")):
            return make_response({"error": "Missing required fields"}, 400)
        
        # Validate supplier_id exists
        if not supplier.Supplier.query.get(data['supplier_id']):
            return make_response({"error": "Supplier not found"}, 404)

        new_product = product.Product(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            quantity=data['quantity'],
            supplier_id=data['supplier_id']
        )

        db.session.add(new_product)
        db.session.commit()

        return make_response(new_product.to_dict(), 201)
    
class ProductByIDResource(Resource):
    def get(self, id):
        prod = product.Product.query.filter_by(id=id).first()
        if not prod:
            return make_response({"error": "Product not found"}, 404)
        return make_response(jsonify(prod.to_dict()), 200)

    def patch(self, id):
        prod = product.Product.query.filter(product.Product.id == id).first()
        if not prod:
            return make_response({"error": "Product not found"}, 404)

        data = request.get_json()
        for attr in data:
            if hasattr(prod, attr):
                setattr(prod, attr, data[attr])

        db.session.commit()

        response_dict = prod.to_dict()
        return make_response(response_dict, 200)

    def delete(self, id):
        prod = product.Product.query.get(id)
        if not prod:
            return make_response({"error": "Product not found"}, 404)

        db.session.delete(prod)
        db.session.commit()

        return make_response('', 204)
