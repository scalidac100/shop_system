from app import app
from extensions import db
from models.user import User

with app.app_context():

    # Create all database tables
    db.create_all()

    # Check if admin already exists
    admin = User.query.filter_by(
        username="admin"
    ).first()

    if admin:
        print("Admin already exists!")

    else:
        admin = User(
            username="admin",
            role="admin"
        )

        admin.set_password("admin123")

        db.session.add(admin)
        db.session.commit()

        print("Admin created successfully!")
