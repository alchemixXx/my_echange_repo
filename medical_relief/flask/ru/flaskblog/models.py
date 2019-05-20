from flaskblog import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"News('{self.title}', '{self.pub_date}')"


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config["SECRET_KEY"], expires_sec)
        return s.dumps({{'user_id':self.id}}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f'User("{self.username}", "{self.email}", "{self.image_file}")'


class Treatment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    direction = db.Column(db.String(256), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"Treatment('{self.title}', '{self.direction}')"


class Doctors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    sex = db.Column(db.String(256), nullable=False, default='Nothing')
    specialization = db.Column(db.String(256), nullable=True, default='Nothing')
    academic_degree = db.Column(db.String(256), nullable=True, default='Nothing')
    employer = db.Column(db.String(256), nullable=True, default='Nothing')
    position = db.Column(db.String(256), nullable=True, default='Nothing')
    city = db.Column(db.String(256), nullable=True, default='Nothing')
    age = db.Column(db.Integer, nullable=True, default='Nothing')
    biography = db.Column(db.Text, nullable=True, default='Nothing')
    image_file = db.Column(db.String(50), nullable=False, default='no_photo.png')

    def __str__(self):
        return f"This Doctor has attributes('{self.name}', '{self.sex}', '{self.specialization}', '{self.academic_degree}'," \
            f" '{self.employer}','{self.position}', '{self.city}', '{self.age}' )"

    def __repr__(self):
        return f"Doctors({self.__class__.__name__, self.__dict__})"


class Partners(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    address = db.Column(db.String(256), nullable=True)
    link = db.Column(db.String(256), nullable=True)
    specialization = db.Column(db.String(256), nullable=False)
    city = db.Column(db.String(256), nullable=True)
    country = db.Column(db.String(256), nullable=True)
    content = db.Column(db.Text, nullable=True)
    image_file = db.Column(db.String(50), nullable=False, default='no_image.jpg')

    def __str__(self):
        return f"This Partner has attributes('{self.title}', '{self.specialization}', '{self.link}'," \
            f" '{self.address}', '{self.city}', '{self.country}' )"

    def __repr__(self):
        return f"Doctors({self.__class__.__name__, self.__dict__})"


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    position = db.Column(db.String(256), nullable=False)
    education = db.Column(db.String(256), nullable=False)
    work = db.Column(db.String(256), nullable=False)
    work_position = db.Column(db.String(256), nullable=False)
    social_link = db.Column(db.String(256), nullable=False)
    biography = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(50), nullable=False, default='default.jpg')

    def __str__(self):
        return f"This Partner has attributes('{self.name}', '{self.position}', '{self.social_link}'," \
            f" '{self.education}', '{self.work}', '{self.work_position}' )"

    def __repr__(self):
        return f"Doctors({self.__class__.__name__, self.__dict__})"
