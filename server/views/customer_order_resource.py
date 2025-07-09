from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import CustomerOrder
from extensions import db

class CustomerOrderResource(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        role = current_user.get('role')
        user_id = current_user.get('id')

        # Admins and shopkeepers can view all customer orders
        if role in ['admin', 'storekeeper']:
            orders = CustomerOrder.query.all()
        else:
            # Customers see only their own orders
            orders = CustomerOrder.query.filter_by(customer_id=user_id).all()

        return make_response(jsonify([order.to_dict() for order in orders]), 200)

    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        user_id = current_user.get('id')

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
        current_user = get_jwt_identity()
        role = current_user.get('role')
        user_id = current_user.get('id')

        order = CustomerOrder.query.get(id)
        if not order:
            return make_response({"error": "Customer order not found"}, 404)

        # Admin and shopkeeper can view all orders
        if role not in ['admin', 'storekeeper'] and order.customer_id != user_id:
            return make_response({"error": "Unauthorized access"}, 403)

        return make_response(order.to_dict(), 200)

    @jwt_required()
    def patch(self, id):
        current_user = get_jwt_identity()
        role = current_user.get('role')
        user_id = current_user.get('id')

        order = CustomerOrder.query.get(id)
        if not order:
            return make_response({"error": "Customer order not found"}, 404)

        if role not in ['admin'] and order.customer_id != user_id:
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
        current_user = get_jwt_identity()
        role = current_user.get('role')
        user_id = current_user.get('id')

        order = CustomerOrder.query.get(id)
        if not order:
            return make_response({"error": "Customer order not found"}, 404)

        if role != 'admin' and order.customer_id != user_id:
            return make_response({"error": "Unauthorized delete attempt"}, 403)

        db.session.delete(order)
        db.session.commit()
        return make_response({"message": "Customer order deleted successfully"}, 200)
