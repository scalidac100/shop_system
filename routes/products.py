from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db
from models.product import Product
from models.category import Category

products_bp = Blueprint(
    "products",
    __name__,
    url_prefix="/products"
)


@products_bp.route("/")
def index():
    products = Product.query.all()
    return render_template(
        "products/index.html",
        products=products
    )


@products_bp.route("/add", methods=["GET", "POST"])
def add():
    categories = Category.query.all()

    if request.method == "POST":
        product = Product(
            name=request.form["name"],
            category_id=request.form["category_id"],
            buying_price=request.form["buying_price"],
            selling_price=request.form["selling_price"],
            quantity=request.form["quantity"]
        )

        db.session.add(product)
        db.session.commit()

        return redirect(url_for("products.index"))

    return render_template(
        "products/add.html",
        categories=categories
    )


@products_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    product = Product.query.get_or_404(id)
    categories = Category.query.all()

    if request.method == "POST":
        product.name = request.form["name"]
        product.category_id = request.form["category_id"]
        product.buying_price = request.form["buying_price"]
        product.selling_price = request.form["selling_price"]
        product.quantity = request.form["quantity"]

        db.session.commit()

        return redirect(url_for("products.index"))

    return render_template(
        "products/edit.html",
        product=product,
        categories=categories
    )


@products_bp.route("/delete/<int:id>")
def delete(id):
    product = Product.query.get_or_404(id)

    db.session.delete(product)
    db.session.commit()

    return redirect(url_for("products.index"))
