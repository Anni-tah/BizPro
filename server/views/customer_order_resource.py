from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from models import CustomerOrder
from extensions import db

class CustomerOrderResource(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        role = get_jwt().get('role')

        if role in ['admin', 'storekeeper']:
            orders = CustomerOrder.query.all()
        else:
            orders = CustomerOrder.query.filter_by(customer_id=user_id).all()

        return make_response(jsonify([order.to_dict() for order in orders]), 200)

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        data = request.get_json()

        if 'total_amount' not in data:
            return make_response({"error": "Total amount is required"}, 400)

        new_order = CustomerOrder(
            customer_id=user_id,
            total_amount=data['total_amount'],
            status=data.get('status', 'pending')
        )

        db.session.add(new_order)
        db.session.commit()

        return make_response(new_order.to_dict(), 201)


class CustomerOrderByIDResource(Resource):
    @jwt_required()
    def get(self, id):
        user_id = get_jwt_identity()
        role = get_jwt().get('role')

        order = CustomerOrder.query.get(id)
        if not order:
            return make_response({"error": "Customer order not found"}, 404)

        if role not in ['admin', 'storekeeper'] and order.customer_id != user_id:
            return make_response({"error": "Unauthorized access"}, 403)

        return make_response(order.to_dict(), 200)

    @jwt_required()
    def patch(self, id):
        user_id = get_jwt_identity()
        role = get_jwt().get('role')

        order = CustomerOrder.query.get(id)
        if not order:
            return make_response({"error": "Customer order not found"}, 404)

        if role != 'admin' and order.customer_id != user_id:
            return make_response({"error": "Unauthorized update attempt"}, 403)

        data = request.get_json()
        if 'total_amount' in data:
            order.total_amount = data['total_amount']
        if 'status' in data:
            order.status = data['status']

        db.session.commit()
        return make_response(order.to_dict(), 200)

    @jwt_required()
    def delete(self, id):
        user_id = get_jwt_identity()
        role = get_jwt().get('role')

        order = CustomerOrder.query.get(id)
        if not order:
            return make_response({"error": "Customer order not found"}, 404)

        if role != 'admin' and order.customer_id != user_id:
            return make_response({"error": "Unauthorized delete attempt"}, 403)

        db.session.delete(order)
        db.session.commit()
        return make_response({"message": "Customer order deleted successfully"}, 200)
