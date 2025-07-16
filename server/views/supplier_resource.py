from flask import jsonify, make_response, request
from flask_jwt_extended import get_jwt_identity, get_jwt, jwt_required
from flask_restful import Resource
from models import Supplier
from extensions import db

class SupplierResource(Resource):
    @jwt_required()
    def get(self):
        role = get_jwt().get('role')

        if role != 'admin':
            return make_response({"error": "Not authorised to view suppliers"}, 403)

        suppliers = [s.to_dict() for s in Supplier.query.all()]
        return make_response(jsonify(suppliers), 200)

    def post(self):
        data = request.get_json()

        if not all(k in data for k in ("name", "contact_person", "phone_number", "email", "address")):
            return make_response({"error": "Missing required fields"}, 400)

        new_supplier = Supplier(
            name=data['name'],
            contact_person=data['contact_person'],
            phone_number=data['phone_number'],
            email=data['email'],
            address=data['address']
        )

        db.session.add(new_supplier)
        db.session.commit()

        return make_response(new_supplier.to_dict(), 201)

class SupplierByIDResource(Resource):
    @jwt_required()
    def get(self, id):
        role = get_jwt().get('role')
        user_id = get_jwt_identity()

        sup = Supplier.query.get(id)
        if not sup:
            return make_response({"error": "Supplier not found"}, 404)

        if role != 'admin' and sup.id != user_id:
            return make_response({"error": "Not authorised to view this supplier"}, 403)

        return make_response(jsonify(sup.to_dict()), 200)

    @jwt_required()
    def patch(self, id):
        role = get_jwt().get('role')
        user_id = get_jwt_identity()

        sup = Supplier.query.get(id)
        if not sup:
            return make_response({"error": "Supplier not found"}, 404)

        if role != 'admin' and sup.id != user_id:
            return make_response({"error": "Not authorised to update this supplier"}, 403)

        data = request.get_json()
        for attr in data:
            if hasattr(sup, attr):
                setattr(sup, attr, data[attr])

        db.session.commit()
        return make_response(sup.to_dict(), 200)

    @jwt_required()
    def delete(self, id):
        role = get_jwt().get('role')
        user_id = get_jwt_identity()

        sup = Supplier.query.get(id)
        if not sup:
            return make_response({"error": "Supplier not found"}, 404)

        if role != 'admin' and sup.id != user_id:
            return make_response({"error": "Not authorised to delete this supplier"}, 403)

        db.session.delete(sup)
        db.session.commit()

        return make_response({"message": "Supplier deleted successfully"}, 204)
