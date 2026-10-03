from app import app
from extensions import db
from models.user import User

with app.app_context():

    admin = User(
        username="admin",
        role="admin"
    )

    admin.set_password("admin123")

    db.session.add(admin)
    db.session.commit()

    print("Admin created successfully!")
