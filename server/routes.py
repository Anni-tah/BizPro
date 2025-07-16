from flask_restful import Api
from views.login_resource import LoginResource, LogoutResource
from views.user_resource import UserResource, UserByIDResource
from views.supplier_resource import SupplierResource, SupplierByIDResource
from views.product_resource import ProductResource, ProductByIDResource
from views.sale_resource import SaleResource, SaleByIDResource
from views.saleitem_resource import SaleItemResource, SaleItemByIDResource
from views.customer_order_resource import CustomerOrderResource, CustomerOrderByIDResource
from views.customer_delivery_resource import CustomerDeliveryResource, CustomerDeliveryByIDResource
from views.inventory_resource import InventoryResource, InventoryByIDResource
from views.payment_resource import PaymentResource, PaymentByIDResource
from views.supplier_order import SupplierOrderResource, SupplierOrderByIDResource
from views.supplierorderItem import SupplierOrderItemResource, SupplierOrderItemByIDResource




def create_routes(api: Api):
    # Authentication routes
    api.add_resource(LoginResource, '/login')
    api.add_resource(LogoutResource, '/logout')

    # User routes
    api.add_resource(UserResource, '/users')
    api.add_resource(UserByIDResource, '/users/<int:id>')

    # Supplier routes
    api.add_resource(SupplierResource, '/suppliers')
    api.add_resource(SupplierByIDResource, '/suppliers/<int:id>')

    # Product routes
    api.add_resource(ProductResource, '/products')
    api.add_resource(ProductByIDResource, '/products/<int:id>')

    # Sale routes
    api.add_resource(SaleResource, '/sales')
    api.add_resource(SaleByIDResource, '/sales/<int:id>')

    # SaleItem routes
    api.add_resource(SaleItemResource, '/saleitems')
    api.add_resource(SaleItemByIDResource, '/saleitems/<int:id>')

    # CustomerOrder routes
    api.add_resource(CustomerOrderResource, '/customer_orders')
    api.add_resource(CustomerOrderByIDResource, '/customer_orders/<int:id>')

    # Delivery routes
    api.add_resource(CustomerDeliveryResource, '/customer_deliveries')
    api.add_resource(CustomerDeliveryByIDResource, '/customer_deliveries/<int:id>')

    # Inventory routes
    api.add_resource(InventoryResource, '/inventories')
    api.add_resource(InventoryByIDResource, '/inventories/<int:id>')

    # Payment routes
    api.add_resource(PaymentResource, '/payments')
    api.add_resource(PaymentByIDResource, '/payments/<int:id>')

    # SupplierOrder routes
    api.add_resource(SupplierOrderResource, '/supplier_orders')
    api.add_resource(SupplierOrderByIDResource, '/supplier_orders/<int:id>')

    # SupplierOrderItem routes
    api.add_resource(SupplierOrderItemResource, '/supplier_order_items')
    api.add_resource(SupplierOrderItemByIDResource, '/supplier_order_items/<int:id>')

    