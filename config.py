import os


class Config:

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "shop-system-secret-key"
    )

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:Kilimanjaro100@localhost/shop_db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
