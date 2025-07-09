from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Inventory, Product
from extensions import db

class InventoryResource(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        role = current_user.get('role')

        if role in ['admin', 'storekeeper']:
            inventories = Inventory.query.all()
            return make_response(jsonify([i.to_dict() for i in inventories]), 200)
        else:
            return make_response({"error": "Unauthorized to view inventory"}, 403)

    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        role = current_user.get('role')

        if role not in ['admin', 'storekeeper']:
            return make_response({"error": "Only admin or storekeeper can add inventory"}, 403)

        data = request.get_json()
        if not all(k in data for k in ("product_id", "quantity")):
            return make_response({"error": "Missing product_id or quantity"}, 400)

        product = Product.query.get(data['product_id'])
        if not product:
            return make_response({"error": "Product not found"}, 404)

        new_inventory = Inventory(
            product_id=data['product_id'],
            quantity=data['quantity']
        )

        db.session.add(new_inventory)
        db.session.commit()

        return make_response(new_inventory.to_dict(), 201)

class InventoryByIDResource(Resource):
    @jwt_required()
    def get(self, id):
        current_user = get_jwt_identity()
        role = current_user.get('role')

        inventory = Inventory.query.get(id)
        if not inventory:
            return make_response({"error": "Inventory not found"}, 404)

        if role not in ['admin', 'storekeeper']:
            return make_response({"error": "Unauthorized to view inventory item"}, 403)

        return make_response(inventory.to_dict(), 200)

    @jwt_required()
    def patch(self, id):
        current_user = get_jwt_identity()
        role = current_user.get('role')

        if role not in ['admin', 'storekeeper']:
            return make_response({"error": "Unauthorized to update inventory"}, 403)

        inventory = Inventory.query.get(id)
        if not inventory:
            return make_response({"error": "Inventory not found"}, 404)

        data = request.get_json()
        if 'quantity' in data:
            inventory.quantity = data['quantity']

        db.session.commit()
        return make_response(inventory.to_dict(), 200)

    @jwt_required()
    def delete(self, id):
        current_user = get_jwt_identity()
        role = current_user.get('role')

        if role != 'admin':
            return make_response({"error": "Only admin can delete inventory"}, 403)

        inventory = Inventory.query.get(id)
        if not inventory:
            return make_response({"error": "Inventory not found"}, 404)

        db.session.delete(inventory)
        db.session.commit()
        return make_response({"message": "Inventory deleted"}, 200)
