import os

class Config:
    SECRET_KEY = 'd6a7dd5539ce23fc722be0e5190a1526'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # setting location to db
    MAIL_SERVER = 'smpt.yahoo.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 'True'
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASS")