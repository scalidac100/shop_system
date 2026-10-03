from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

from models.user import User
from extensions import db


users_bp = Blueprint(
    "users",
    __name__,
    url_prefix="/users"
)


@users_bp.route("/")
def index():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if session.get("role") != "admin":
        return redirect(url_for("home"))

    users = User.query.all()

    return render_template(
        "users/index.html",
        users=users
    )


@users_bp.route("/add", methods=["GET", "POST"])
def add():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if session.get("role") != "admin":
        return redirect(url_for("home"))

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]
        role = request.form["role"]

        existing_user = User.query.filter_by(
            username=username
        ).first()

        if existing_user:
            flash(
                "Username tayari ipo.",
                "danger"
            )

            return redirect(
                url_for("users.add")
            )

        user = User(
            username=username,
            role=role
        )

        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash(
            "User ameongezwa successfully.",
            "success"
        )

        return redirect(
            url_for("users.index")
        )

    return render_template(
        "users/add.html"
    )

