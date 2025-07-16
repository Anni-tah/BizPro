from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from models import Payment
from extensions import db

class PaymentResource(Resource):
    @jwt_required()
    def get(self):
        role = get_jwt().get('role')
        user_id = get_jwt_identity()

        if role == 'admin':
            payments = Payment.query.all()
        else:
            payments = Payment.query.filter_by(user_id=user_id).all()

        return make_response(jsonify([p.to_dict() for p in payments]), 200)

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()

        data = request.get_json()
        required_fields = ['amount', 'payment_method']

        if not all(field in data for field in required_fields):
            return make_response({"error": "Missing required fields"}, 400)

        payment = Payment(
            user_id=user_id,
            customer_order_id=data.get('customer_order_id'),
            supplier_order_id=data.get('supplier_order_id'),
            amount=data['amount'],
            payment_method=data['payment_method'],
            status=data.get('status', 'pending')
        )

        db.session.add(payment)
        db.session.commit()

        return make_response(payment.to_dict(), 201)

class PaymentByIDResource(Resource):
    @jwt_required()
    def get(self, id):
        role = get_jwt().get('role')
        user_id = get_jwt_identity()

        payment = Payment.query.filter_by(id=id).first()
        if not payment:
            return make_response({"error": "Payment not found"}, 404)

        if role != 'admin' and payment.user_id != user_id:
            return make_response({"error": "Not authorised to view this payment"}, 403)

        return make_response(jsonify(payment.to_dict()), 200)

    @jwt_required()
    def patch(self, id):
        role = get_jwt().get('role')
        user_id = get_jwt_identity()

        payment = Payment.query.filter_by(id=id).first()
        if not payment:
            return make_response({"error": "Payment not found"}, 404)

        if role != 'admin' and payment.user_id != user_id:
            return make_response({"error": "Not authorised to update this payment"}, 403)

        data = request.get_json()
        for key, value in data.items():
            setattr(payment, key, value)

        db.session.commit()

        return make_response(payment.to_dict(), 200)
    
    @jwt_required()
    def delete(self, id):
        role = get_jwt().get('role')
        user_id = get_jwt_identity()

        payment = Payment.query.filter_by(id=id).first()
        if not payment:
            return make_response({"error": "Payment not found"}, 404)

        if role != 'admin' and payment.user_id != user_id:
            return make_response({"error": "Not authorised to delete this payment"}, 403)

        db.session.delete(payment)
        db.session.commit()

        return make_response({"message": "Payment deleted successfully"}, 200)
