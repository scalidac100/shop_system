from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db
from models.supplier import Supplier

suppliers_bp = Blueprint(
    "suppliers",
    __name__,
    url_prefix="/suppliers"
)


@suppliers_bp.route("/")
def index():
    suppliers = Supplier.query.all()

    return render_template(
        "suppliers/index.html",
        suppliers=suppliers
    )


@suppliers_bp.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        supplier = Supplier(
            name=request.form["name"],
            phone=request.form["phone"],
            address=request.form["address"]
        )

        db.session.add(supplier)
        db.session.commit()

        return redirect(url_for("suppliers.index"))

    return render_template("suppliers/add.html")


@suppliers_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    supplier = Supplier.query.get_or_404(id)

    if request.method == "POST":

        supplier.name = request.form["name"]
        supplier.phone = request.form["phone"]
        supplier.address = request.form["address"]

        db.session.commit()

        return redirect(url_for("suppliers.index"))

    return render_template(
        "suppliers/edit.html",
        supplier=supplier
    )


@suppliers_bp.route("/delete/<int:id>")
def delete(id):

    supplier = Supplier.query.get_or_404(id)

    db.session.delete(supplier)
    db.session.commit()

    return redirect(url_for("suppliers.index"))
