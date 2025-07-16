from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from models import Delivery
from extensions import db

class CustomerDeliveryResource(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        claims = get_jwt()
        role = claims.get('role')

        if role == 'supplier':
            return make_response({"error": "Access denied"}, 403)

        if role == 'admin':
            deliveries = Delivery.query.all()
        elif role == 'customer':
            deliveries = Delivery.query.filter_by(customer_id=user_id).all()
        elif role == 'storekeeper':
            deliveries = Delivery.query.filter_by(shopkeeper_id=user_id).all()
        else:
            return make_response({"error": "Invalid role"}, 400)

        return make_response(jsonify([d.to_dict() for d in deliveries]), 200)

    @jwt_required()
    def post(self):
        data = request.get_json()
        user_id = get_jwt_identity()
        claims = get_jwt()
        role = claims.get('role')

        if role not in ['admin', 'storekeeper']:
            return make_response({"error": "Access denied"}, 403)

        required_fields = ['customer_order_id', 'shopkeeper_id', 'customer_id', 'delivery_date', 'status']
        if not all(field in data for field in required_fields):
            return make_response({"error": "Missing required fields"}, 400)

        try:
            new_delivery = Delivery(
                customer_order_id=data['customer_order_id'],
                shopkeeper_id=data['shopkeeper_id'],
                customer_id=data['customer_id'],
                delivery_date=data['delivery_date'],
                status=data.get('status', 'pending')
            )

            db.session.add(new_delivery)
            db.session.commit()
            return make_response(new_delivery.to_dict(), 201)

        except Exception as e:
            db.session.rollback()
            return make_response({"error": str(e)}, 500)
class CustomerDeliveryByIDResource(Resource):
    @jwt_required()
    def get(self, id):
        user_id = get_jwt_identity()
        role = get_jwt().get('role')

        delivery = Delivery.query.get(id)
        if not delivery:
            return make_response({"error": "Delivery not found"}, 404)

        if role == 'admin' or (role == 'customer' and delivery.customer_id == user_id) or (role == 'storekeeper' and delivery.shopkeeper_id == user_id):
            return make_response(jsonify(delivery.to_dict()), 200)
        else:
            return make_response({"error": "Not authorised to view this delivery"}, 403)

    @jwt_required()
    def patch(self, id):
        user_id = get_jwt_identity()
        role = get_jwt().get('role')

        delivery = Delivery.query.get(id)
        if not delivery:
            return make_response({"error": "Delivery not found"}, 404)

        if role not in ['admin', 'storekeeper']:
            return make_response({"error": "Access denied"}, 403)

        data = request.get_json()
        if 'status' in data:
            delivery.status = data['status']

        db.session.commit()
        return make_response(delivery.to_dict(), 200)

    @jwt_required()
    def delete(self, id):
        user_id = get_jwt_identity()
        role = get_jwt().get('role')

        if role not in ['admin', 'storekeeper']:
            return make_response({"error": "Access denied"}, 403)

        delivery = Delivery.query.get(id)
        if not delivery:
            return make_response({"error": "Delivery not found"}, 404)

        db.session.delete(delivery)
        db.session.commit()
        return make_response({"message": "Delivery deleted successfully"}, 204)
