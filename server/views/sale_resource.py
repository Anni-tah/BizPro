from flask import jsonify, make_response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from models import Sale
from extensions import db

class SaleResource(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        claims = get_jwt()
        role = claims.get('role')

        if role == 'admin':
            sales = Sale.query.all()
        else:
            sales = Sale.query.filter_by(user_id=user_id).all()

        return make_response(jsonify([sale.to_dict() for sale in sales]), 200)

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()

        data = request.get_json()

        if not all(k in data for k in ("total_amount", "status", "payment_method")):
            return make_response({"error": "Missing required fields"}, 400)

        new_sale = Sale(
            user_id=user_id,
            total_amount=data['total_amount'],
            status=data.get('status', 'completed'),
            payment_method=data.get('payment_method', 'cash')
        )

        db.session.add(new_sale)
        db.session.commit()

        return make_response(new_sale.to_dict(), 201)

class SaleByIDResource(Resource):
    @jwt_required()
    def get(self, id):
        user_id = get_jwt_identity()
        claims = get_jwt()
        role = claims.get('role')

        sale_item = Sale.query.get(id)
        if not sale_item:
            return make_response({"error": "Sale not found"}, 404)

        if role != 'admin' and sale_item.user_id != user_id:
            return make_response({"error": "Not authorised to view this sale"}, 403)

        return make_response(sale_item.to_dict(), 200)

    @jwt_required()
    def patch(self, id):
        user_id = get_jwt_identity()
        claims = get_jwt()
        role = claims.get('role')

        sale_item = Sale.query.get(id)
        if not sale_item:
            return make_response({"error": "Sale not found"}, 404)

        if role != 'admin' and sale_item.user_id != user_id:
            return make_response({"error": "Not authorised to update this sale"}, 403)

        data = request.get_json()
        for attr in data:
            if hasattr(sale_item, attr):
                setattr(sale_item, attr, data[attr])

        db.session.commit()
        return make_response(sale_item.to_dict(), 200)

    @jwt_required()
    def delete(self, id):
        user_id = get_jwt_identity()
        claims = get_jwt()
        role = claims.get('role')

        sale_item = Sale.query.get(id)
        if not sale_item:
            return make_response({"error": "Sale not found"}, 404)

        if role != 'admin' and sale_item.user_id != user_id:
            return make_response({"error": "Not authorised to delete this sale"}, 403)

        db.session.delete(sale_item)
        db.session.commit()
        return make_response({"message": "Sale deleted successfully"}, 204)
