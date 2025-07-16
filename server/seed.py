from faker import Faker
import random
from datetime import datetime
from extensions import db
from app import app

from models.users import User
from models.product import Product
from models.sale import Sale
from models.saleItem import SaleItem
from models.payments import Payment
from models.supplier import Supplier
from models.supplierOrder import SupplierOrder
from models.supplier_order_item import SupplierOrderItem
from models.supplier_delivery import SupplierDelivery
from models.customerOrder import CustomerOrder
from models.customer_deliveries import Delivery
from models.inventory import Inventory

fake = Faker()

def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # USERS
        admin = User(username="admin", email="admin@example.com", role="admin")
        admin.set_password("admin123")

        storekeeper = User(username="storekeeper", email="store@example.com", role="storekeeper")
        storekeeper.set_password("store123")

        suppliers = []
        for _ in range(2):
            s = User(username=fake.user_name(), email=fake.email(), role="supplier")
            s.set_password("supplier123")
            suppliers.append(s)

        customers = []
        for _ in range(5):
            c = User(username=fake.user_name(), email=fake.email(), role="customer")
            c.set_password("customer123")
            customers.append(c)

        db.session.add_all([admin, storekeeper] + suppliers + customers)
        db.session.commit()

        # SUPPLIER PROFILES
        supplier_profiles = []
        for s in suppliers:
            profile = Supplier(
                id=s.id,
                name=s.username.capitalize() + " Ltd",
                contact_person=fake.name(),
                phone_number=fake.phone_number(),
                email=s.email,
                address=fake.address()
            )
            supplier_profiles.append(profile)

        db.session.add_all(supplier_profiles)
        db.session.commit()

        # PRODUCTS
        products = []
        for sup in supplier_profiles:
            for _ in range(3):
                product = Product(
                    name=fake.word().capitalize() + " Water",
                    description=fake.sentence(),
                    price=round(random.uniform(50, 200), 2),
                    quantity=random.randint(10, 50),
                    status="approved",
                    supplier_id=sup.id
                )
                products.append(product)

        db.session.add_all(products)
        db.session.commit()

        # INVENTORY
        inventory = [Inventory(product_id=prod.id, quantity=prod.quantity) for prod in products]
        db.session.add_all(inventory)
        db.session.commit()

        # SALES + SALE ITEMS
        for cust in customers:
            sale = Sale(
                user_id=cust.id,
                total_amount=0,
                payment_method="Mpesa"
            )
            db.session.add(sale)
            db.session.commit()

            total = 0
            for _ in range(2):
                prod = random.choice(products)
                qty = random.randint(1, 3)
                item = SaleItem(
                    sale_id=sale.id,
                    product_id=prod.id,
                    quantity=qty,
                    unit_price=prod.price
                )
                total += qty * prod.price
                db.session.add(item)

            sale.total_amount = round(total, 2)
            db.session.commit()

        # CUSTOMER ORDERS + DELIVERIES
        for cust in customers:
            order = CustomerOrder(
                customer_id=cust.id,
                total_amount=random.uniform(300, 1000),
                status=random.choice(["pending", "completed"])
            )
            db.session.add(order)
            db.session.commit()

            delivery = Delivery(
                customer_order_id=order.id,
                shopkeeper_id=storekeeper.id,
                customer_id=cust.id,
                status=random.choice(["pending", "in_transit", "delivered"])
            )
            db.session.add(delivery)

        db.session.commit()

        # SUPPLIER ORDERS + ITEMS + DELIVERIES
        for sup in supplier_profiles:
            s_order = SupplierOrder(
                storekeeper_id=storekeeper.id,
                supplier_id=sup.id,
                total_amount=0,
                status="pending"
            )
            db.session.add(s_order)
            db.session.commit()

            total = 0
            for _ in range(2):
                prod = random.choice([p for p in products if p.supplier_id == sup.id])
                qty = random.randint(5, 10)
                item = SupplierOrderItem(
                    supplier_order_id=s_order.id,
                    product_id=prod.id,
                    quantity=qty,
                    unit_price=prod.price,
                    total_price=qty * prod.price
                )
                total += item.total_price
                db.session.add(item)

            s_order.total_amount = round(total, 2)
            db.session.commit()

            s_delivery = SupplierDelivery(
                supplier_id=sup.id,
                supplier_order_id=s_order.id,
                status="delivered"
            )
            db.session.add(s_delivery)

        db.session.commit()

        # PAYMENTS
        for _ in range(10):
            payment = Payment(
                user_id=random.choice(customers).id,
                amount=random.uniform(300, 1500),
                payment_method=random.choice(["Mpesa", "Bank", "Cash"]),
                status=random.choice(["completed", "pending"])
            )
            db.session.add(payment)

        db.session.commit()

        print("✅ Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
