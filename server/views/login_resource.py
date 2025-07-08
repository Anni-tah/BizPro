from flask import request, jsonify
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from models.users import User
from extensions import db

class LoginResource(Resource):
    def post(self):
       data= request.get_json()

       email=data.get('email')
       password=data.get('password')

       user = User.query.filter_by(email=email).first()
       if not user or not user.check_password(password):
          return {"message": "Invalid username or password"}, 401
       
       #jwt token creation
       identity = {
              "id": user.id,
              "email": user.email,
              "role": user.role
         }
       access_token = create_access_token(identity=identity)
       return jsonify({
              "message": "Login successful",
              "access_token": access_token,
              "user": user.to_dict()
         })
    
class LogoutResource(Resource):
    def post(self):
        # Invalidate the JWT token by not returning it
        return {"message": "Logout successful"}, 200
    

       
       
