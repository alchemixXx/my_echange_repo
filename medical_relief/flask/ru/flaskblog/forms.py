from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User, News

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max = 20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("This username is taken.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("This email is taken.")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('LogIn')



class UpdateAccountForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max = 20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    picture = FileField("Update Profile Picture", validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("This username is taken.")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("This email is taken.")


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


