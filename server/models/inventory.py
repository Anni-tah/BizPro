from extensions import db
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

class Inventory(db.Model, SerializerMixin):
    __tablename__ = 'inventories'
    serialize_rules = ('-product.inventory',)

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

    product = db.relationship('Product', back_populates='inventory', lazy=True)


    def __repr__(self):
        return f"<Inventory {self.id}, Product ID: {self.product_id}, Quantity: {self.quantity}>"