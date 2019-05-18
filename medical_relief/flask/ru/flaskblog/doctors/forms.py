from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flaskblog.models import Doctors


class DoctorForm(FlaskForm):
    name = StringField("Name of the doctor", validators=[DataRequired()])
    sex = SelectField("Choose field of treatment", choices=[('male', 'Мужчина'), ('female', 'женщина')])
    specialization = StringField("What specialization does it have?", validators=[DataRequired()])
    academic_degree = StringField("What academic degree does it have?")
    employer = StringField("Where does it works currently")
    position = StringField("What position does it take?")
    city = StringField("In which city it working right now?")
    age = StringField("How old is it?")
    biography = TextAreaField('Content of treatment')
    picture = FileField("Choose a picture", validators=[FileAllowed(['jpg', 'png'])])
    file_name = StringField("File name", validators=[DataRequired()])
    submit = SubmitField('Add the doctor')


class UpdateDoctorForm(FlaskForm):
    name = StringField("Name of the doctor", validators=[DataRequired()])
    sex = SelectField("Choose field of treatment", choices=[('male', 'Мужчина'), ('female', 'женщина')])
    specialization = StringField("What specialization does it have?", validators=[DataRequired()])
    academic_degree = StringField("What academic degree does it have?")
    employer = StringField("Where does it works currently")
    position = StringField("What position does it take?")
    city = StringField("In which city it working right now?")
    age = StringField("How old is it?")
    biography = TextAreaField('Content of treatment')
    picture = FileField("Choose a picture", validators=[FileAllowed(['jpg', 'png'])])
    file_name = StringField("File name", validators=[DataRequired()])
    submit = SubmitField('Update')

    def validate_name(self, name):
        if name != name.data:
            name = Doctors.query.filter_by(name=name.data).first()

    def validate_sex(self, sex):
        if sex != sex.data:
            sex = Doctors.query.filter_by(sex=sex.data).first()

    def validate_specialization(self, specialization):
        if specialization != specialization.data:
            specialization = Doctors.query.filter_by(specialization=specialization.data).first()

    def validate_academic_degree(self, academic_degree):
        if academic_degree != academic_degree.data:
            academic_degree = Doctors.query.filter_by(academic_degree=academic_degree.data).first()

    def validate_employer(self, employer):
        if employer != employer.data:
            employer = Doctors.query.filter_by(employer=employer.data).first()

    def validate_position(self, position):
        if position != position.data:
            position = Doctors.query.filter_by(position=position.data).first()

    def validate_city(self, city):
        if city != city.data:
            city = Doctors.query.filter_by(city=city.data).first()

    def validate_age(self, age):
        if age != age.data:
            age = Doctors.query.filter_by(age=age.data).first()

    def validate_picture(self, picture):
        if picture != picture.data:
            picture = Doctors.query.filter_by(image_file=picture.data).first()
