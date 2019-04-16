from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# from flask_admin import Admin
# from flask_admim.contrib.sqla import ModelView

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\01_personal_documents\02_coding\medical_relief\flask\ru\news.db'


# DB settings
app.config['SECRET_KEY'] = 'v1g5x7a1u0h8m3p6j3b1z9h7u3k6f4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'  # setting location to db
db = SQLAlchemy(app)  # connection with DB sqlite

from flaskblog import routes