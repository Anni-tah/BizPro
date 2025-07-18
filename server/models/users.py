
from sqlalchemy_serializer import SerializerMixin
from extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from .supplier import Supplier
from .sale import Sale
from .customer_deliveries import Delivery

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    serialize_rules=('-sales.user','-supplier.user','-password_hash','-customer_orders.customer','-supplier_orders.storekeeper','-deliveries_as_shopkeeper.shopkeeper','-deliveries_as_customer.customer')


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='customer', index=True)       # 'admin', 'storekeeper', 'customer','supplier' default='customer') 
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    

    sales = db.relationship('Sale', back_populates='user', lazy=True)
    supplier = db.relationship('Supplier', back_populates='user', uselist=False, lazy=True)
    customer_orders = db.relationship('CustomerOrder', back_populates='customer', lazy=True, cascade='all, delete-orphan')
    supplier_orders = db.relationship('SupplierOrder', back_populates='storekeeper', lazy=True, cascade='all, delete-orphan')
    payments = db.relationship('Payment', back_populates='user', lazy=True, cascade='all, delete-orphan')

    deliveries_as_shopkeeper = db.relationship('Delivery', back_populates='shopkeeper', foreign_keys='Delivery.shopkeeper_id', lazy=True, cascade='all, delete-orphan')
    deliveries_as_customer = db.relationship('Delivery', back_populates='customer', foreign_keys='Delivery.customer_id', lazy=True, cascade='all, delete-orphan')


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"<User {self.username}, Role: {self.role}>"
