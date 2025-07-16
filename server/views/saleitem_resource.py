from flask import jsonify, make_response, request
from flask_jwt_extended import get_jwt_identity, get_jwt, jwt_required
from flask_restful import Resource
from models import SaleItem
from extensions import db

class SaleItemResource(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        role = get_jwt().get('role')

        if role == 'admin':
            sale_items = [si.to_dict() for si in SaleItem.query.all()]
        else:
            sale_items = [si.to_dict() for si in SaleItem.query.filter_by(user_id=user_id).all()]
        
        return make_response(jsonify(sale_items), 200)

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()

        data = request.get_json()
        if not all(k in data for k in ("sale_id", "product_id", "quantity", "unit_price")):
            return make_response({"error": "Missing required fields"}, 400)

        new_sale_item = SaleItem(
            sale_id=data['sale_id'],
            product_id=data['product_id'],
            quantity=data['quantity'],
            unit_price=data['unit_price'],
            user_id=user_id  # Associate with user
        )

        db.session.add(new_sale_item)
        db.session.commit()

        return make_response(new_sale_item.to_dict(), 201)
    
class SaleItemByIDResource(Resource):
    @jwt_required()
    def get(self, id):
        user_id = get_jwt_identity()
        role = get_jwt().get('role')

        sale_item = SaleItem.query.get(id)
        if not sale_item:
            return make_response({"error": "Sale item not found"}, 404)

        if role != 'admin' and sale_item.user_id != user_id:
            return make_response({"error": "Not authorised to view this sale item"}, 403)
        
        return make_response(jsonify(sale_item.to_dict()), 200)

    @jwt_required()
    def patch(self, id):
        user_id = get_jwt_identity()
        role = get_jwt().get('role')

        sale_item = SaleItem.query.get(id)
        if not sale_item:
            return make_response({"error": "Sale item not found"}, 404)

        if role != 'admin' and sale_item.user_id != user_id:
            return make_response({"error": "Not authorised to update this sale item"}, 403)

        data = request.get_json()
        for attr in data:
            if hasattr(sale_item, attr):
                setattr(sale_item, attr, data[attr])

        db.session.commit()
        return make_response(sale_item.to_dict(), 200)

    @jwt_required()
    def delete(self, id):
        user_id = get_jwt_identity()
        role = get_jwt().get('role')

        sale_item = SaleItem.query.get(id)
        if not sale_item:
            return make_response({"error": "Sale item not found"}, 404)

        if role != 'admin' and sale_item.user_id != user_id:
            return make_response({"error": "Not authorised to delete this sale item"}, 403)

        db.session.delete(sale_item)
        db.session.commit()

        return make_response({"message": "Sale item deleted successfully"}, 204)
