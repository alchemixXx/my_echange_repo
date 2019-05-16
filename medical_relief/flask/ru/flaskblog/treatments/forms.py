from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flaskblog.models import User, News, Treatment

class TreatmentForm(FlaskForm):
    title = StringField("Title of treatment", validators=[DataRequired()])
    content = TextAreaField('Content of treatment', validators = [DataRequired()])
    direction = SelectField("Choose field of treatment",
                            choices = [('sys1', 'Дыхательная система'), ('sys2', 'Пищеварительная система'),
                                       ('sys3', 'Мочевыделительная система'),('sys4', 'Опорно-двигательный аппарат'),
                                       ('sys5', 'Циркуляторная система'), ('sys6', 'Нервная система'),
                                       ('sys7', 'Сенсорная система'),('sys8', 'Покровная система'),
                                       ('sys9', 'Эндокринная система'),('sys10', 'Органы кроветворения и иммунной системы'),])
    picture = FileField("Choose a picture", validators=[FileAllowed(['jpg', 'png'])])
    file_name = StringField("File name", validators=[DataRequired()])
    submit = SubmitField('Publicate')



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