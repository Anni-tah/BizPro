from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from models import SupplierOrderItem, SupplierOrder, Product

class SupplierOrderItemResource(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        role = current_user.get('role')
        user_id = current_user.get('id')

        if role == 'admin':
            items = [item.to_dict() for item in SupplierOrderItem.query.all()]
        else:
            items = SupplierOrderItem.query.join(SupplierOrder).filter(SupplierOrder.storekeeper_id == user_id).all()
            items = [item.to_dict() for item in items]

        return make_response(jsonify(items), 200)

    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        role = current_user.get('role')
        user_id = current_user.get('id')

        data = request.get_json()

        if not all(k in data for k in ("supplier_order_id", "product_id", "quantity", "unit_price")):
            return make_response({"error": "Missing required fields"}, 400)

        order = SupplierOrder.query.get(data['supplier_order_id'])
        if not order:
            return make_response({"error": "Supplier order not found"}, 404)

        if role != 'admin' and order.storekeeper_id != user_id:
            return make_response({"error": "Not authorized to add item to this order"}, 403)

        product = Product.query.get(data['product_id'])
        if not product:
            return make_response({"error": "Product not found"}, 404)

        total_price = data['quantity'] * data['unit_price']

        new_item = SupplierOrderItem(
            supplier_order_id=data['supplier_order_id'],
            product_id=data['product_id'],
            quantity=data['quantity'],
            unit_price=data['unit_price'],
            total_price=total_price
        )

        db.session.add(new_item)
        db.session.commit()

        return make_response(new_item.to_dict(), 201)


class SupplierOrderItemByIDResource(Resource):
    @jwt_required()
    def get(self, id):
        item = SupplierOrderItem.query.get(id)
        if not item:
            return make_response({"error": "Supplier order item not found"}, 404)
        return make_response(item.to_dict(), 200)

    @jwt_required()
    def patch(self, id):
        current_user = get_jwt_identity()
        role = current_user.get('role')
        user_id = current_user.get('id')

        item = SupplierOrderItem.query.get(id)
        if not item:
            return make_response({"error": "Supplier order item not found"}, 404)

        order = SupplierOrder.query.get(item.supplier_order_id)
        if not order or (role != 'admin' and order.storekeeper_id != user_id):
            return make_response({"error": "Not authorized to edit this item"}, 403)

        data = request.get_json()

        if 'quantity' in data:
            item.quantity = data['quantity']
        if 'unit_price' in data:
            item.unit_price = data['unit_price']

        item.total_price = item.quantity * item.unit_price

        db.session.commit()
        return make_response(item.to_dict(), 200)

    @jwt_required()
    def delete(self, id):
        current_user = get_jwt_identity()
        role = current_user.get('role')
        user_id = current_user.get('id')

        item = SupplierOrderItem.query.get(id)
        if not item:
            return make_response({"error": "Supplier order item not found"}, 404)

        order = SupplierOrder.query.get(item.supplier_order_id)
        if not order or (role != 'admin' and order.storekeeper_id != user_id):
            return make_response({"error": "Not authorized to delete this item"}, 403)

        db.session.delete(item)
        db.session.commit()

        return make_response({"message": "Supplier order item deleted successfully"}, 200)
