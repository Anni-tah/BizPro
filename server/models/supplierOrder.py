from extensions import db
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

class SupplierOrder(db.Model, SerializerMixin):
    __tablename__ = 'supplier_orders'
    serialize_rules = ('-items', '-storekeeper', '-supplier', '-delivery', '-payments')

    id = db.Column(db.Integer, primary_key=True)
    storekeeper_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'), nullable=False)
    
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_amount = db.Column(db.Float, nullable=False)

    status = db.Column(db.String(20), nullable=False, default='pending')  # 'pending', 'accepted', 'rejected'

    storekeeper = db.relationship('User', back_populates='supplier_orders', lazy=True)
    supplier = db.relationship('Supplier', back_populates='supplier_orders', lazy=True)
    delivery = db.relationship('SupplierDelivery', back_populates='supplier_order', lazy=True, uselist=False, cascade='all, delete-orphan')
    payments = db.relationship('Payment', back_populates='supplier_order', lazy=True, cascade='all, delete-orphan')



    def __repr__(self): return f"<SupplierOrder {self.id}, Storekeeper: {self.storekeeper_id}, Status: {self.status}>"
