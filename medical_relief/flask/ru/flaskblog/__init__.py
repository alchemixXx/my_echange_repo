from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm



# from flask_admin import Admin
# from flask_admim.contrib.sqla import ModelView

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\01_personal_documents\02_coding\medical_relief\flask\ru\news.db'


# DB settings
app.config['SECRET_KEY'] = 'd6a7dd5539ce23fc722be0e5190a1526'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'  # setting location to db
db = SQLAlchemy(app)  # connection with DB sqlite

from flaskblog import routes