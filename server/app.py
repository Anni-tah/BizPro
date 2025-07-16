from flask import Flask, jsonify
from config import Config
from extensions import db, migrate, jwt
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

from models.customer_deliveries import Delivery
from models.customerOrder import CustomerOrder
from models.inventory import Inventory
from models.payments import Payment
from models.product import Product
from models.sale import Sale
from models.saleItem import SaleItem
from models.supplier_delivery import SupplierDelivery
from models.supplier_order_item import SupplierOrderItem
from models.supplierOrder import SupplierOrder
from models.supplier import Supplier
from models.users import User

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Initialize extensions
db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)

# Register API routes
api = Api(app)
from routes import create_routes
create_routes(api)

# JWT error handlers
@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({"message": "Missing or invalid token"}), 401

@jwt.expired_token_loader
def expired_token_response(jwt_header, jwt_payload):
    return jsonify({"message": "Token has expired"}), 401

@jwt.invalid_token_loader
def invalid_token_response(callback):
    print("🧠 INVALID TOKEN - Reason:", callback)
    return jsonify({"message": "Invalid token"}), 401

@app.route("/test-token")
@jwt_required()
def test_token():
    identity = get_jwt_identity()
    print("🧠 TOKEN DECODED AS:", identity)
    return jsonify({"identity": identity})


# Admin summary route (JWT-protected)
@app.route('/admin/summary')
@jwt_required()
def admin_summary():
    identity = get_jwt_identity()  # just user_id
    claims = get_jwt()             # contains 'role', etc.

    if claims.get('role') != 'admin':
        return jsonify({"message": "Access denied. Admins only."}), 403

    return jsonify({
        "users": User.query.count(),
        "products": Product.query.count(),
        "sales": Sale.query.count(),
        "suppliers": Supplier.query.count(),
        "orders": CustomerOrder.query.count()
    })
    

if __name__ == "__main__":
    app.run(debug=True)
