from flask import jsonify, make_response, request
from flask_restful import Resource
from models import User, db

class UserResource(Resource):
    def get(self):
        users=[user.to_dict() for user in User.query.all()]
        return make_response(jsonify(users),200)
    
    def post(self):
        data=request.get_json()

        #validate required fields
        if not all(k in data for k in("username","email", "password_hash", "role")):
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
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return make_response({"error": "User not found"}, 404)
        return make_response(jsonify(user.to_dict()), 200)

    def patch(self, id):
        user = User.query.filter(User.id == id).first()
        if not user:
            return make_response({"error": "User not found"}, 404)

        data = request.get_json()
        for attr in data:
            if hasattr(user, attr):
                setattr(user, attr, data[attr])

        db.session.commit()

        response_dict = user.to_dict()
        return make_response(response_dict, 200)

    def delete(self, id):
        user = User.query.get(id)
        if not user:
            return make_response({"error": "User not found"}, 404)

        db.session.delete(user)
        db.session.commit()

        return make_response('', 204)