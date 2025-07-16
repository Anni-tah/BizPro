from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from models.users import User
from extensions import db

class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            return {"message": "Invalid email or password"}, 401

        # ✅ Ensure identity is a string
        access_token = create_access_token(
            identity=str(user.id),  # <- fixed here
            additional_claims={
                "role": user.role,
                "email": user.email
            }
        )

        return jsonify({
            "message": "Login successful",
            "access_token": access_token,
            "user": user.to_dict()
        })


class LogoutResource(Resource):
    def post(self):
        return {"message": "Logout successful"}, 200
