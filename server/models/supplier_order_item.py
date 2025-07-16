from extensions import db
from sqlalchemy_serializer import SerializerMixin

class SupplierOrderItem(db.Model, SerializerMixin):
    __tablename__ = 'supplier_order_items'
    serialize_rules = ('-supplier_order', '-product.supplier_order_items', '-product.items', '-product.inventory', '-product.order_items')

    id = db.Column(db.Integer, primary_key=True)
    supplier_order_id = db.Column(db.Integer, db.ForeignKey('supplier_orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    total_price = db.Column(db.Float, nullable=False)

    supplier_order = db.relationship('SupplierOrder', back_populates='items')  # ✅ Add this line
    product = db.relationship('Product', back_populates='supplier_order_items')
