from app import app
from extensions import db
from models import User, Supplier, Product, Sale, SaleItem
from werkzeug.security import generate_password_hash
from datetime import datetime

def seed():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # --- Create Users ---
        admin = User(
            username='admin',
            email='admin@example.com',
            password_hash=generate_password_hash('admin123'),
            role='admin'
        )

        supplier_user_1 = User(
            username='supplier1',
            email='supplier1@example.com',
            password_hash=generate_password_hash('supplier123'),
            role='supplier'
        )

        supplier_user_2 = User(
            username='supplier2',
            email='supplier2@example.com',
            password_hash=generate_password_hash('supplier123'),
            role='supplier'
        )

        customer_user = User(
            username='customer1',
            email='customer1@example.com',
            password_hash=generate_password_hash('customer123'),
            role='customer'
        )

        db.session.add_all([admin, supplier_user_1, supplier_user_2, customer_user])
        db.session.commit()

        # --- Create Suppliers ---
        supplier_a = Supplier(
            id=supplier_user_1.id,  # ForeignKey to users.id
            name='Supplier A',
            contact_person='John Doe',
            phone_number='0712345678',
            email='contact@supplierA.com',
            address='123 Market Street'
        )

        supplier_b = Supplier(
            id=supplier_user_2.id,
            name='Supplier B',
            contact_person='Jane Smith',
            phone_number='0798765432',
            email='contact@supplierB.com',
            address='456 Commerce Avenue'
        )

        db.session.add_all([supplier_a, supplier_b])
        db.session.commit()

        # --- Create Products ---
        product_a = Product(
            name='Product A',
            description='High quality product A',
            price=10.99,
            quantity=100,
            status='approved',
            supplier_id=supplier_a.id
        )

        product_b = Product(
            name='Product B',
            description='Durable and affordable product B',
            price=20.99,
            quantity=200,
            status='approved',
            supplier_id=supplier_b.id
        )

        db.session.add_all([product_a, product_b])
        db.session.commit()

        # --- Create Sale ---
        sale = Sale(
            user_id=customer_user.id,
            total_amount=42.97,
            status='completed',
            payment_method='cash',
            sale_date=datetime.utcnow()
        )

        db.session.add(sale)
        db.session.commit()

        # --- Create SaleItems ---
        item1 = SaleItem(
            sale_id=sale.id,
            product_id=product_a.id,
            quantity=2,
            unit_price=10.99
        )

        item2 = SaleItem(
            sale_id=sale.id,
            product_id=product_b.id,
            quantity=1,
            unit_price=20.99
        )

        db.session.add_all([item1, item2])
        db.session.commit()

        print("✅ Database seeded successfully!")

if __name__ == "__main__":
    seed()
