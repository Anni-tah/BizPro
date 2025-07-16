from extensions import db
from datetime import datetime 
from sqlalchemy_serializer import SerializerMixin  

class Supplier(db.Model, SerializerMixin):
    __tablename__ = 'suppliers'
    serialize_rules = ('-products', '-user')
    
    id = db.Column(db.Integer, db.ForeignKey('users.id'),primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    contact_person = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    address = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    products= db.relationship('Product', back_populates='supplier', lazy=True)
    user = db.relationship('User', back_populates='supplier', lazy=True)
    deliveries = db.relationship('SupplierDelivery', back_populates='supplier', lazy=True, cascade='all, delete-orphan')
    supplier_orders = db.relationship('SupplierOrder', back_populates='supplier', lazy=True, cascade='all, delete-orphan')

    
    def __repr__(self):
        return f"<Supplier {self.name}>"
