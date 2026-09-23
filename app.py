from flask import Flask, render_template
from config import Config
from extensions import db

app = Flask(__name__)
app.config.from_object(Config)


db.init_app(app)

from models.category import Category
from models.product import Product
from models.customer import Customer
from models.supplier import Supplier

from routes.categories import categories_bp
from routes.products import products_bp
from routes.customers import customers_bp
from routes.suppliers import suppliers_bp

@app.route("/")
def home():

    from models.category import Category
    from models.product import Product
    from models.customer import Customer
    from models.supplier import Supplier

    categories_count = Category.query.count()
    products_count = Product.query.count()
    customers_count = Customer.query.count()
    suppliers_count = Supplier.query.count()

    return render_template(
        "dashboard.html",
        categories_count=categories_count,
        products_count=products_count,
        customers_count=customers_count,
        suppliers_count=suppliers_count
    )


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
