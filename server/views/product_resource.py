from flask import jsonify, make_response, request
from flask_restful import Resource
from models import Product
from extensions import db
from models import Supplier
from flask_jwt_extended import jwt_required, get_jwt_identity

class ProductResource(Resource):  
    def get(self):
        products = [prod.to_dict() for prod in Product.query.all()]
        return make_response(jsonify(products), 200)
    
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        role= current_user.get('role')
        
        # Check if the user has permission to add products
        if role not in ['admin', 'supplier']:
            return make_response({"error": "Not authorised to add products"}, 403)
        
        data = request.get_json()

        #get supplier_id from current user if supplier
        if role == 'supplier':
            data['supplier_id'] = current_user.get('id')

        # Validate required fields
        if not all(k in data for k in ("name", "description", "price", "quantity","supplier_id")):
            return make_response({"error": "Missing required fields"}, 400)
        
        #set status
        if role=='admin':
           status=data.get('status', 'approved')
        else:
            status = data.get('status', 'pending')
    

        new_product =Product(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            quantity=data['quantity'],
            status=status,
            supplier_id=data['supplier_id']
        )

        db.session.add(new_product)
        db.session.commit()

        return make_response(new_product.to_dict(), 201)
    
class ProductByIDResource(Resource):
    def get(self, id):
        prod = Product.query.filter_by(id=id).first()
        if not prod:
            return make_response({"error": "Product not found"}, 404)
        return make_response(jsonify(prod.to_dict()), 200)
    
    @jwt_required()
    def patch(self, id):
        current_user = get_jwt_identity()
        role = current_user.get('role')

        prod = Product.query.filter(Product.id == id).first()
        if not prod:
            return make_response({"error": "Product not found"}, 404)
        data = request.get_json()

        #only admin can edit status
        if role != 'admin':
            return make_response({"error": "Only admin can update status"}, 403)
        prod.status=data['status'] 

        #update other allowed fields
        allowed_fields = ['name', 'description', 'price', 'quantity', 'supplier_id']

        # Check if all required fields are present
        if not all(k in data for k in allowed_fields):
            return make_response({"error": "Missing required fields"}, 400)
      
        for attr in data:
            if hasattr(prod, attr):
                setattr(prod, attr, data[attr])

        db.session.commit()
        response_dict = prod.to_dict()
        return make_response(response_dict, 200)

    @jwt_required()
    def delete(self, id):
        current_user = get_jwt_identity()
        role = current_user.get('role')
        user_id = current_user.get('id')

        prod = Product.query.get(id)
        if not prod:
            return make_response({"error": "Product not found"}, 404)
        
        # Only admin or supplier can delete products
        if role not in ['admin', 'supplier']:
            return make_response({"error": "Not authorised to delete products"}, 403)
        
        # Suppliers can only delete their own products
        if role == 'supplier' and prod.supplier_id != user_id:
            return make_response({"error": "Not authorised to delete this product"}, 403)
    

        db.session.delete(prod)
        db.session.commit()

        return make_response('', 204)
