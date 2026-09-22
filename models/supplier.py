from extensions import db

class Supplier(db.Model):
    __tablename__ = "suppliers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(30))
    address = db.Column(db.String(255))

    def __repr__(self):
        return f"<Supplier {self.name}>"
