from flask_restful import Api
from views.login_resource import LoginResource, LogoutResource
from views.user_resource import UserResource, UserByIDResource
from views.supplier_resource import SupplierResource, SupplierByIDResource
from views.product_resource import ProductResource, ProductByIDResource
from views.sale_resource import SaleResource, SaleByIDResource
from views.saleitem_resource import SaleItemResource, SaleItemByIDResource


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

    
