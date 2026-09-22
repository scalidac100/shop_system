from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db
from models.customer import Customer

customers_bp = Blueprint(
    "customers",
    __name__,
    url_prefix="/customers"
)


@customers_bp.route("/")
def index():
    customers = Customer.query.all()

    return render_template(
        "customers/index.html",
        customers=customers
    )


@customers_bp.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        customer = Customer(
            name=request.form["name"],
            phone=request.form["phone"],
            address=request.form["address"]
        )

        db.session.add(customer)
        db.session.commit()

        return redirect(url_for("customers.index"))

    return render_template("customers/add.html")


@customers_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    customer = Customer.query.get_or_404(id)

    if request.method == "POST":

        customer.name = request.form["name"]
        customer.phone = request.form["phone"]
        customer.address = request.form["address"]

        db.session.commit()

        return redirect(url_for("customers.index"))

    return render_template(
        "customers/edit.html",
        customer=customer
    )


@customers_bp.route("/delete/<int:id>")
def delete(id):

    customer = Customer.query.get_or_404(id)

    db.session.delete(customer)
    db.session.commit()

    return redirect(url_for("customers.index"))
