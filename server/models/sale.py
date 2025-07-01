
from sqlalchemy_serializer import SerializerMixin
from extensions import db
from datetime import datetime

class Sale(db.Model):
    __tablename__ = 'sales'
    serialize_rules=('-items')

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    sale_date = db.Column(db.DateTime, default=datetime.utcnow)

    items = db.relationship('SaleItem', back_populates='sale', lazy=True)

    def __repr__(self):
        return f"<Sale ID: {self.id}, User ID: {self.user_id}, Total: {self.total_amount}>"
