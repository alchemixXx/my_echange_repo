from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# from flask_admin import Admin
# from flask_admim.contrib.sqla import ModelView

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\01_personal_documents\02_coding\medical_relief\flask\ru\news.db'


# DB settings
app.config['SECRET_KEY'] = 'd6a7dd5539ce23fc722be0e5190a1526'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # setting location to db
db = SQLAlchemy(app)  # connection with DB sqlite

bcrypt = Bcrypt(app)  # for hashing the passwords
login_manager = LoginManager(app)

from flaskblog import routes