from extensions import db
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

class Product(db.Model):
    __tablename__ = 'products'
    serialize_rules=('-sale_items')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    sale_items = db.relationship('SaleItem', back_populates='product', lazy=True)
    def __repr__(self):
        return f"<Product {self.name}, Price: {self.price}, Stock: {self.stock}>"
