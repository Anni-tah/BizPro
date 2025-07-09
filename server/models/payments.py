from extensions import db
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin


class Payment(db.Model, SerializerMixin):
    __tablename__ = 'payments'
    serialize_rules = ('-customer_order', '-supplier_order')

    id = db.Column(db.Integer, primary_key=True)
    customer_order_id = db.Column(db.Integer, db.ForeignKey('customer_orders.id'), nullable=True)
    supplier_order_id = db.Column(db.Integer, db.ForeignKey('supplier_orders.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # User who made the payment
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)  # e.g., 'credit_card', 'paypal', 'bank_transfer'
    payment_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False, default='pending')  # 'pending', 'completed', 'failed'

    customer_order = db.relationship('CustomerOrder', back_populates='payments', lazy=True)
    supplier_order = db.relationship('SupplierOrder', back_populates='payments', lazy=True)
    user = db.relationship('User', back_populates='payments', lazy=True)


    def __repr__(self):
        return f"<Payment {self.id}, User: {self.user_id}, Amount: {self.amount}, Status: {self.status}>"