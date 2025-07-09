from app import app
from extensions import db

from models.users import User
from models.product import Product
from models.sale import Sale
from models.saleItem import SaleItem
from models.supplier import Supplier
from models.supplier_delivery import SupplierDelivery
from models.supplierOrder import SupplierOrder
from models.supplier_order_item import SupplierOrderItem
from models.inventory import Inventory


with app.app_context():
    db.drop_all()
    db.create_all()
    print("✅ Tables created in bizpro_db.")
