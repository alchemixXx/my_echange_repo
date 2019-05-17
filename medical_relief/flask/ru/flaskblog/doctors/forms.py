from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flaskblog.models import Doctors

class DoctorForm(FlaskForm):
    name = StringField("Name of the doctor", validators=[DataRequired()])
    sex = SelectField("Choose field of treatment", choices = [('male', 'Мужчина'), ('female', 'женщина')])
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



class UpdateTreatmentForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    direction = SelectField("Choose field of treatment", validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    picture = FileField("Choose a picture", validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_title(self, title):
        if title != title.data:
            title = News.query.filter_by(title=title.data).first()


    def validate_content(self, content):
        if content != content.data:
            content = News.query.filter_by(content=content.data).first()

    def validate_picture(self, picture):
        if picture != picture.data:
            picture = News.query.filter_by(image_file=picture.data).first()

    def validate_direction(self, direction):
        if direction != direction.data:
            direction = Treatment.query.filter_by(direction=direction.data).first()