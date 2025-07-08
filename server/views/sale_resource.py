from flask import jsonify, make_response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Sale
from extensions import db

class SaleResource(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        role = current_user.get('role')
        user_id = current_user.get('id')

    #admin to view all sales and users to view their own sales
        if role == 'admin':
            sales = [sale_item.to_dict() for sale_item in Sale.query.all()]
        else:
            sales = [sale_item.to_dict() for sale_item in Sale.query.filter_by(user_id=user_id).all()]

        return make_response(jsonify(sales), 200)


    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        user_id = current_user.get('id')

        data = request.get_json()

        # Validate required fields
        if not all(k in data for k in ( "total_amount","status", "payment_method")):
            return make_response({"error": "Missing required fields"}, 400)

        new_sale = Sale(
            user_id=user_id,  
            total_amount=data['total_amount'],
            status=data.get('status', 'completed'),  # Default to 'completed' if not provided
            payment_method=data.get('payment_method', 'cash')  # Default to 'cash' if not provided
        )

        db.session.add(new_sale)
        db.session.commit()

        return make_response(new_sale.to_dict(), 201)
    
class SaleByIDResource(Resource):
    @jwt_required()
    def get(self, id):
        current_user = get_jwt_identity()
        role = current_user.get('role')
        user_id = current_user.get('id')

        sale_item = Sale.query.filter_by(id=id).first()
        if not sale_item:
            return make_response({"error": "Sale not found"}, 404)
        
        if role != 'admin' and sale_item.user_id != user_id:
            return make_response({"error": "Not authorised to view this sale"}, 403)
        
        return make_response(jsonify(sale_item.to_dict()), 200)
    
    @jwt_required()
    def patch(self, id):
        current_user = get_jwt_identity()
        role = current_user.get('role')
        user_id = current_user.get('id')

        sale_item = Sale.query.filter(Sale.id == id).first()
        if not sale_item:
            return make_response({"error": "Sale not found"}, 404)
        
        # Only admin can update sales or the user who made the sale
        if role != 'admin' and sale_item.user_id != user_id:
            return make_response({"error": "Not authorised to update this sale"}, 403)
        

        data = request.get_json()
        for attr in data:
            if hasattr(sale_item, attr):
                setattr(sale_item, attr, data[attr])

        db.session.commit()

        response_dict = sale_item.to_dict()
        return make_response(response_dict, 200)
    
    @jwt_required()
    def delete(self, id):
        current_user = get_jwt_identity()
        role = current_user.get('role')
        user_id = current_user.get('id')

        sale_item = Sale.query.get(id)
        if not sale_item:
            return make_response({"error": "Sale not found"}, 404)

        # Only admin or the user who made the sale can delete it
        if role !='admin' and sale_item.user_id != user_id:
            return make_response({"error": "Not authorised to delete this sale"}, 403)

        db.session.delete(sale_item)
        db.session.commit()

        return make_response({"message": "Sale deleted successfully"}, 204)
   