from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError
from flaskblog.models import User, News


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField('Content', validators = [DataRequired()])
    picture = FileField("Choose a picture", validators=[FileAllowed(['jpg', 'png'])])
    # file_name = StringField("File name", validators=[DataRequired()])
    submit = SubmitField('Post')

    def validate_title(self, title):
        title = News.query.filter_by(title=title.data).first()
        if title:
            raise ValidationError("This title is taken.")


class UpdatePostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    picture = FileField("Choose a picture", validators=[FileAllowed(['jpg', 'png'])])
    # file_name = StringField("File name", validators=[DataRequired()])
    submit = SubmitField('Update')

    def validate_title(self, title):
        title = News.query.filter_by(title=title.data).all()
        if len(title) > 1:
            raise ValidationError("This title is taken.")
