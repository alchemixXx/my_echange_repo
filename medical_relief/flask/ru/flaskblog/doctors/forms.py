from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError
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
    # file_name = StringField("File name", validators=[DataRequired()])
    submit = SubmitField('Add the doctor')

    def validate_name(self, name):
        name = Doctors.query.filter_by(name=name.data).first()
        if name:
            raise ValidationError("This name is taken.")


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
    # file_name = StringField("File name", validators=[DataRequired()])
    submit = SubmitField('Update')

    def validate_name(self, name):
        name = Doctors.query.filter_by(name=name.data).all()
        if len(name) > 1:
            raise ValidationError("This name is taken.")
