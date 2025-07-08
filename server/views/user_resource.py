from flask import jsonify, make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from models import User
from extensions import db

class UserResource(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        role = current_user.get('role')

        # Check if the user has permission to view users
        if role != 'admin':
            return make_response({"error": "Not authorised to view users"}, 403)

        users=[user.to_dict() for user in User.query.all()]
        return make_response(jsonify(users),200)
    
    def post(self):
        data=request.get_json()

        #validate required fields
        if not all(k in data for k in("username","email", "password", "role")):
            return make_response({"error": "Missing required fields"}, 400)  
        
        new_user=User(
            username=data['username'],
            email=data['email'],
            role=data['role']
        )
        new_user.set_password(data['password'])

        db.session.add(new_user)
        db.session.commit()

        return make_response(new_user.to_dict(),201)
    
class UserByIDResource(Resource):
    @jwt_required()
    def get(self, id):
        current_user = get_jwt_identity()
        role = current_user.get('role')
        user_id = current_user.get('id')

        # Check if the user has permission to view user details
        if role != 'admin' and user_id != id:
            return make_response({"error": "Not authorised to view user details"}, 403)
        

        user = User.query.filter_by(id=id).first()
        if not user:
            return make_response({"error": "User not found"}, 404)
        return make_response(jsonify(user.to_dict()), 200)
    
    @jwt_required()
    def patch(self, id):
        current_user = get_jwt_identity()
        role = current_user.get('role')
        user_id = current_user.get('id')

        # only logged in user or admin can update user details
        if role != 'admin' and user_id != id:
            return make_response({"error": "Not authorised to update user"}, 403)
        

        user = User.query.filter(User.id == id).first()
        if not user:
            return make_response({"error": "User not found"}, 404)

        data = request.get_json()

        #only admin can update role
        if role != 'admin' and 'role' in data:
            return make_response({"error": "Not authorised to update role"}, 403)
        
        for attr in data:
            if hasattr(user, attr):
                setattr(user, attr, data[attr])

        db.session.commit()

        response_dict = user.to_dict()
        return make_response(response_dict, 200)
    
    @jwt_required()
    def delete(self, id):
        current_user = get_jwt_identity()
        role = current_user.get('role')
        user_id = current_user.get('id')

        #only admin or the user themselves can delete their account
        if role != 'admin' and user_id != id:
            return make_response({"error": "Not authorised to delete user"}, 403)
        
        user = User.query.get(id)
        if not user:
            return make_response({"error": "User not found"}, 404)

        db.session.delete(user)
        db.session.commit()

        return make_response('', 204)