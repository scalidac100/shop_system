import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://shopuser:Shop%4012345@localhost/shop_management"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
