from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flaskblog.models import User, News

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField('Content', validators = [DataRequired()])
    picture = FileField("Choose a picture", validators=[FileAllowed(['jpg', 'png'])])
    file_name = StringField("File name", validators=[DataRequired()])
    submit = SubmitField('Post')



class UpdatePostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
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