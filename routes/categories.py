from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db
from models.category import Category

categories_bp = Blueprint(
    "categories",
    __name__,
    url_prefix="/categories"
)


@categories_bp.route("/")
def index():
    categories = Category.query.all()
    return render_template(
        "categories/index.html",
        categories=categories
    )


@categories_bp.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]

        category = Category(name=name)

        db.session.add(category)
        db.session.commit()

        return redirect(url_for("categories.index"))

    return render_template("categories/add.html")


@categories_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    category = Category.query.get_or_404(id)

    if request.method == "POST":
        category.name = request.form["name"]

        db.session.commit()

        return redirect(url_for("categories.index"))

    return render_template(
        "categories/edit.html",
        category=category
    )


@categories_bp.route("/delete/<int:id>")
def delete(id):
    category = Category.query.get_or_404(id)

    db.session.delete(category)
    db.session.commit()

    return redirect(url_for("categories.index"))
