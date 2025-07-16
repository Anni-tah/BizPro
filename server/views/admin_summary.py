from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from flask import jsonify, make_response
from models import User, Product, Sale

class AdminSummaryResource(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        claims = get_jwt()
        role = claims.get("role")

        if role != "admin":
            return make_response({"error": "Not authorised"}, 403)

        summary = {
            "total_users": User.query.count(),
            "total_suppliers": User.query.filter_by(role='supplier').count(),
            "total_products": Product.query.count(),
            "total_sales": Sale.query.count()
        }

        return make_response(jsonify(summary), 200)
