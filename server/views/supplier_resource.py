from flask import jsonify, make_response, request
from flask_restful import Resource
from models import supplier, db

class SupplierResource(Resource):
    def get(self):
        suppliers = [s.to_dict() for s in supplier.Supplier.query.all()]
        return make_response(jsonify(suppliers), 200)

    def post(self):
        data = request.get_json()

        # Validate required fields
        if not all(k in data for k in ("name", "contact_person", "phone_number", "email", "address")):
            return make_response({"error": "Missing required fields"}, 400)

        new_supplier = supplier.Supplier(
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
    def get(self, id):
        sup = supplier.Supplier.query.filter_by(id=id).first()
        if not sup:
            return make_response({"error": "Supplier not found"}, 404)
        return make_response(jsonify(sup.to_dict()), 200)

    def patch(self, id):
        sup = supplier.Supplier.query.filter(supplier.Supplier.id == id).first()
        if not sup:
            return make_response({"error": "Supplier not found"}, 404)

        data = request.get_json()
        for attr in data:
            if hasattr(sup, attr):
                setattr(sup, attr, data[attr])

        db.session.commit()

        response_dict = sup.to_dict()
        return make_response(response_dict, 200)

    def delete(self, id):
        sup = supplier.Supplier.query.get(id)
        if not sup:
            return make_response({"error": "Supplier not found"}, 404)

        db.session.delete(sup)
        db.session.commit()

        return make_response({"message": "Supplier deleted successfully"}, 204)