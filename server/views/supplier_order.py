from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from extensions import db
from models import SupplierOrderItem, SupplierOrder, Product, Supplier

class SupplierOrderResource(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        role = get_jwt().get('role')

        if role == 'admin':
            orders = SupplierOrder.query.all()
        elif role == 'storekeeper':
            orders = SupplierOrder.query.filter_by(storekeeper_id=user_id).all()
        elif role == 'supplier':
            orders = SupplierOrder.query.filter_by(supplier_id=user_id).all()
        else:
            return make_response({"error": "Not authorised to view supplier orders"}, 403)

        order_data = [order.to_dict(rules=('items', 'items.product')) for order in orders]
        return make_response(jsonify(order_data), 200)

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        role = get_jwt().get('role')

        if role != 'storekeeper':
            return make_response({"error": "Only storekeepers can create supplier orders"}, 403)

        data = request.get_json()

        if not all(k in data for k in ("supplier_id", "items")):
            return make_response({"error": "Missing required fields: supplier_id and items"}, 400)

        supplier = Supplier.query.get(data['supplier_id'])
        if not supplier:
            return make_response({"error": "Supplier not found"}, 404)

        total_amount = 0
        new_order = SupplierOrder(
            storekeeper_id=user_id,
            supplier_id=data['supplier_id'],
            total_amount=0  # placeholder, updated after items
        )
        db.session.add(new_order)
        db.session.flush()  # Get new_order.id before commit

        for item in data['items']:
            product = Product.query.get(item['product_id'])
            if not product:
                return make_response({"error": f"Product {item['product_id']} not found"}, 404)

            quantity = item.get('quantity', 0)
            unit_price = product.price
            total_price = quantity * unit_price
            total_amount += total_price

            order_item = SupplierOrderItem(
                supplier_order_id=new_order.id,
                product_id=item['product_id'],
                quantity=quantity,
                unit_price=unit_price,
                total_price=total_price
            )
            db.session.add(order_item)

        new_order.total_amount = total_amount
        db.session.commit()

        return make_response(new_order.to_dict(rules=('items', 'items.product')), 201)


class SupplierOrderByIDResource(Resource):
    @jwt_required()
    def get(self, id):
        user_id = get_jwt_identity()
        role = get_jwt().get('role')

        order = SupplierOrder.query.get(id)
        if not order:
            return make_response({"error": "Supplier order not found"}, 404)

        if role == 'admin' or \
           (role == 'storekeeper' and order.storekeeper_id == user_id) or \
           (role == 'supplier' and order.supplier_id == user_id):
            return make_response(order.to_dict(rules=('items', 'items.product')), 200)

        return make_response({"error": "Not authorized to view this order"}, 403)

    @jwt_required()
    def patch(self, id):
        user_id = get_jwt_identity()
        role = get_jwt().get('role')

        order = SupplierOrder.query.get(id)
        if not order:
            return make_response({"error": "Supplier order not found"}, 404)

        if role != 'admin' and (role != 'storekeeper' or order.storekeeper_id != user_id):
            return make_response({"error": "Not authorized to update this order"}, 403)

        data = request.get_json()
        if 'status' in data:
            order.status = data['status']

        db.session.commit()
        return make_response(order.to_dict(rules=('items', 'items.product')), 200)

    @jwt_required()
    def delete(self, id):
        role = get_jwt().get('role')

        if role != 'admin':
            return make_response({"error": "Only admin can delete supplier orders"}, 403)

        order = SupplierOrder.query.get(id)
        if not order:
            return make_response({"error": "Supplier order not found"}, 404)

        db.session.delete(order)
        db.session.commit()
        return make_response({"message": "Supplier order deleted successfully"}, 200)
