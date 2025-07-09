from extensions import db
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'
    serialize_rules = ('-items', '-supplier.products')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False, default='pending')  # 'pending', 'approved', 'rejected'
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'), nullable=False)

    supplier = db.relationship('Supplier', back_populates='products', lazy=True)
    items = db.relationship('SaleItem', back_populates='product', lazy=True, cascade='all, delete-orphan')
    inventory = db.relationship('Inventory', back_populates='product', lazy=True, cascade='all, delete-orphan')
    order_items = db.relationship('SupplierOrderItem', back_populates='product', lazy=True, cascade='all, delete-orphan')

    




    def __repr__(self): return f"<Product {self.name}, Price: {self.price}, Stock: {self.quantity}>"
