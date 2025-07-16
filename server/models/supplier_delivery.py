from extensions import db
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

class SupplierDelivery(db.Model, SerializerMixin):
    __tablename__ = 'supplier_deliveries'
    serialize_rules = ('-supplier_order','-supplier_order.supplier')

    id = db.Column(db.Integer, primary_key=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'), nullable=False)
    supplier_order_id = db.Column(db.Integer, db.ForeignKey('supplier_orders.id'), nullable=False)
    delivery_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False, default='pending')  # 'pending', 'in_transit', 'delivered', 'cancelled'

    supplier = db.relationship('Supplier', back_populates='deliveries', lazy=True)
    supplier_order = db.relationship('SupplierOrder', back_populates='delivery', lazy=True,)

    def __repr__(self):
        return f"<SupplierDelivery {self.id}, Supplier ID: {self.supplier_id}, Status: {self.status}>"