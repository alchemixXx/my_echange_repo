import os

MYSQL_DATABASE_HOST = '127.0.0.1'
MYSQL_DATABASE_PORT = '3306'
MYSQL_DATABASE_USER = 'root'
MYSQL_DATABASE_PASSWORD = 'root'
MYSQL_DATABASE_DB = 'medical_relief_db'
MYSQL_DATABASE_CHARSET = 'utf-8'

class Config:
    SECRET_KEY = 'd6a7dd5539ce23fc722be0e5190a1526'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # setting location to db
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_DATABASE_USER}:{MYSQL_DATABASE_PASSWORD}@{MYSQL_DATABASE_HOST}/{MYSQL_DATABASE_DB}'
    SQLALCHEMY_ECHO = True
    MAIL_SERVER = 'smpt.yahoo.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 'True'
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASS")

    # app.config['MYSQL_HOST'] = 'localhost'
    # app.config['MYSQL_USER'] = 'root'
    # app.config['MYSQL_PASSWORD'] = 'root'
    # app.config['MYSQL_DB'] = 'MyDB'
    #

