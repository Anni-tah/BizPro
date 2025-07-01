from flask import Flask
from config import Config
from extensions import db, migrate, jwt

app = Flask(__name__)
app.config.from_object(Config)


db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)

if __name__ == "__main__":

    from models.users import User
    from models.product import Product
    from models.sale import Sale
    from models.saleItem import SaleItem
    app.run(debug=True)
