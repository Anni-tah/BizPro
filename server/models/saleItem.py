from extensions import db
from sqlalchemy_serializer import SerializerMixin

class SaleItem(db.Model, SerializerMixin):
    __tablename__ = 'sale_items'
    serialize_rules = ('-sale.items', '-product.items')

    id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('sales.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)

    sale = db.relationship('Sale', back_populates='items', lazy=True)
    product = db.relationship('Product', back_populates='items', lazy=True)


    def __repr__(self):
        return f"<SaleItem Sale ID: {self.sale_id}, Product ID: {self.product_id}, Quantity: {self.quantity}>"
