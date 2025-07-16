from flask import jsonify, make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from flask_restful import Resource
from models import User
from extensions import db

class UserResource(Resource):
    @jwt_required()
    def get(self):
        claims = get_jwt()
        role = claims.get('role')

        if role != 'admin':
            return make_response({"error": "Not authorised to view users"}, 403)

        users = [user.to_dict() for user in User.query.all()]
        return make_response(jsonify(users), 200)

    def post(self):
        data = request.get_json()

        if not all(k in data for k in ("username", "email", "password", "role")):
            return make_response({"error": "Missing required fields"}, 400)

        new_user = User(
            username=data['username'],
            email=data['email'],
            role=data['role']
        )
        new_user.set_password(data['password'])

        db.session.add(new_user)
        db.session.commit()

        return make_response(new_user.to_dict(), 201)


class UserByIDResource(Resource):
    @jwt_required()
    def get(self, id):
        claims = get_jwt()
        current_user_id = get_jwt_identity()
        role = claims.get("role")

        if role != 'admin' and current_user_id != id:
            return make_response({"error": "Not authorised to view user details"}, 403)

        user = User.query.get(id)
        if not user:
            return make_response({"error": "User not found"}, 404)
        return make_response(jsonify(user.to_dict()), 200)

    @jwt_required()
    def patch(self, id):
        claims = get_jwt()
        current_user_id = get_jwt_identity()
        role = claims.get("role")

        if role != 'admin' and current_user_id != id:
            return make_response({"error": "Not authorised to update user"}, 403)

        user = User.query.get(id)
        if not user:
            return make_response({"error": "User not found"}, 404)

        data = request.get_json()

        if role != 'admin' and 'role' in data:
            return make_response({"error": "Not authorised to update role"}, 403)

        for attr in data:
            if hasattr(user, attr):
                setattr(user, attr, data[attr])

        db.session.commit()
        return make_response(user.to_dict(), 200)

    @jwt_required()
    def delete(self, id):
        claims = get_jwt()
        current_user_id = get_jwt_identity()
        role = claims.get("role")

        if role != 'admin' and current_user_id != id:
            return make_response({"error": "Not authorised to delete user"}, 403)

        user = User.query.get(id)
        if not user:
            return make_response({"error": "User not found"}, 404)

        db.session.delete(user)
        db.session.commit()

        return make_response('', 204)
