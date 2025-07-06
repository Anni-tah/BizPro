
from sqlalchemy_serializer import SerializerMixin
from extensions import db
from datetime import datetime
class Sale(db.Model, SerializerMixin):
    __tablename__ = 'sales'
    serialize_rules=('-items', '-user.sales')

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    sale_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), nullable=False, default='completed') # 'completed', 'pending', 'cancelled'
    payment_method = db.Column(db.String(50), nullable=False, default='cash') # 'cash', 'credit_card', 'Mpesa'

    # Relationships
    items = db.relationship('SaleItem', back_populates='sale', lazy=True)
    user = db.relationship('User', back_populates='sales', lazy=True)


    def __repr__(self):
        return f"<Sale ID: {self.id}, User ID: {self.user_id}, Total: {self.total_amount}>"
