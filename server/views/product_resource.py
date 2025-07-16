from flask import jsonify, make_response, request
from flask_restful import Resource
from models import Product
from extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

class ProductResource(Resource):
    def get(self):
        products = [prod.to_dict() for prod in Product.query.all()]
        return make_response(jsonify(products), 200)

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        claims = get_jwt()
        role = claims.get('role')

        if role not in ['admin', 'supplier']:
            return make_response({"error": "Not authorised to add products"}, 403)

        data = request.get_json()

        # Supplier auto-assigns their own supplier_id
        if role == 'supplier':
            data['supplier_id'] = user_id

        required_fields = ("name", "description", "price", "quantity", "supplier_id")
        if not all(k in data for k in required_fields):
            return make_response({"error": "Missing required fields"}, 400)

        # Only admin can set 'approved' directly
        status = data.get('status', 'approved' if role == 'admin' else 'pending')

        new_product = Product(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            quantity=data['quantity'],
            status=status,
            supplier_id=data['supplier_id']
        )

        db.session.add(new_product)
        db.session.commit()

        return make_response(new_product.to_dict(), 201)

class ProductByIDResource(Resource):
    def get(self, id):
        prod = Product.query.get(id)
        if not prod:
            return make_response({"error": "Product not found"}, 404)
        return make_response(prod.to_dict(), 200)

    @jwt_required()
    def patch(self, id):
        claims = get_jwt()
        role = claims.get('role')

        prod = Product.query.get(id)
        if not prod:
            return make_response({"error": "Product not found"}, 404)

        data = request.get_json()

        # Only admin can update 'status'
        if 'status' in data and role != 'admin':
            return make_response({"error": "Only admin can update status"}, 403)

        # Allowed fields to update
        allowed_fields = ['name', 'description', 'price', 'quantity', 'supplier_id', 'status']

        for attr in data:
            if attr in allowed_fields and hasattr(prod, attr):
                setattr(prod, attr, data[attr])

        db.session.commit()
        return make_response(prod.to_dict(), 200)

    @jwt_required()
    def delete(self, id):
        user_id = get_jwt_identity()
        claims = get_jwt()
        role = claims.get('role')

        prod = Product.query.get(id)
        if not prod:
            return make_response({"error": "Product not found"}, 404)

        if role == 'supplier' and prod.supplier_id != user_id:
            return make_response({"error": "Not authorised to delete this product"}, 403)

        if role not in ['admin', 'supplier']:
            return make_response({"error": "Not authorised to delete products"}, 403)

        db.session.delete(prod)
        db.session.commit()

        return make_response('', 204)
