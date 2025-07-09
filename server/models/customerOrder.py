from extensions import db
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

class CustomerOrder(db.Model, SerializerMixin):
    __tablename__ = 'customer_orders'
    serialize_rules = ('-items', '-payments', '-deliveries', '-customer.customer_orders')
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')  # 'pending', 'completed', 'cancelled'

    customer = db.relationship('User', back_populates='customer_orders', lazy=True)
    items = db.relationship('SaleItem', back_populates='customer_order', lazy=True, cascade='all, delete-orphan')
    payments = db.relationship('Payment', back_populates='customer_order', lazy=True, cascade='all, delete-orphan')
    deliveries = db.relationship('Delivery', back_populates='customer_order', lazy=True, cascade='all, delete-orphan')


    def __repr__(self): return f"<CustomerOrder {self.id}, Status: {self.status}, Total: {self.total_amount}>"