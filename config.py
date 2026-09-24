import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:Kilimanjaro100@localhost/shop_db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
