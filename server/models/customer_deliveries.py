from extensions import db
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

class Delivery(db.Model, SerializerMixin):
    __tablename__ = 'deliveries'
    serialize_rules = ('-customer_order')

    id = db.Column(db.Integer, primary_key=True)
    customer_order_id = db.Column(db.Integer, db.ForeignKey('customer_orders.id'), nullable=False)
    delivery_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False, default='pending')  # 'pending', 'in_transit', 'delivered', 'cancelled'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


    customer_order = db.relationship('CustomerOrder', back_populates='deliveries')




    def __repr__(self): return f"<Delivery {self.id}, Order ID: {self.customer_order_id}, Status: {self.status}>"
