from flask import jsonify, make_response, request
from flask_restful import Resource
from models import saleItem, db

class SaleItemResource(Resource):
    def get(self):
        sale_items = [item.to_dict() for item in saleItem.SaleItem.query.all()]
        return make_response(jsonify(sale_items), 200)

    def post(self):
        data = request.get_json()

        # Validate required fields
        if not all(k in data for k in ("sale_id", "product_id", "quantity", "price")):
            return make_response({"error": "Missing required fields"}, 400)

        new_sale_item = saleItem.SaleItem(
            sale_id=data['sale_id'],
            product_id=data['product_id'],
            quantity=data['quantity'],
            price=data['price']
        )

        db.session.add(new_sale_item)
        db.session.commit()

        return make_response(new_sale_item.to_dict(), 201)
    
class SaleItemByIDResource(Resource):
    def get(self, id):
        item = saleItem.SaleItem.query.filter_by(id=id).first()
        if not item:
            return make_response({"error": "Sale Item not found"}, 404)
        return make_response(jsonify(item.to_dict()), 200)

    def patch(self, id):
        item = saleItem.SaleItem.query.filter(saleItem.SaleItem.id == id).first()
        if not item:
            return make_response({"error": "Sale Item not found"}, 404)

        data = request.get_json()
        for attr in data:
            if hasattr(item, attr):
                setattr(item, attr, data[attr])

        db.session.commit()

        response_dict = item.to_dict()
        return make_response(response_dict, 200)

    def delete(self, id):
        item = saleItem.SaleItem.query.get(id)
        if not item:
            return make_response({"error": "Sale Item not found"}, 404)

        db.session.delete(item)
        db.session.commit()

        return make_response('', 204)
