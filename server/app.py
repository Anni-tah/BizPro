from flask import Flask
from config import Config
from extensions import db, migrate, jwt
from flask_restful import Api
from flask_cors import CORS

from models.users import User
from models.product import Product
from models.sale import Sale
from models.saleItem import SaleItem
from models.supplier import Supplier


app = Flask(__name__)
app.config.from_object(Config)
CORS(app)


db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)


api = Api(app)

from routes import create_routes
create_routes(api)

#handles custom error responses

@jwt.unauthorized_loader
def unauthorized_response(callback):
    return {"message": "Missing or invalid token"}, 401

@jwt.expired_token_loader
def expired_token_response(callback):
    return {"message": "Token has expired"}, 401

@jwt.invalid_token_loader
def invalid_token_response(callback):
    return {"message": "Invalid token"}, 401

if __name__ == "__main__":
    app.run(debug=True)
