from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError
from flaskblog.models import Team


class TeamForm(FlaskForm):
    name = StringField("Name of the teammate", validators=[DataRequired()])
    education = StringField("What education does it have?", validators=[DataRequired()])
    position = StringField("What position does it take in this Organization?")
    employer = StringField("Where does it works currently")
    work = StringField("Where else does it works")
    work_position = StringField("What position does it take?")
    social_link = StringField("Link to the social networks")
    biography = TextAreaField('More about person, biography')
    picture = FileField("Choose a picture", validators=[FileAllowed(['jpg', 'png'])])
    # file_name = StringField("File name", validators=[DataRequired()])
    submit = SubmitField('Add the doctor')

    def validate_name(self, name):
        name = Team.query.filter_by(name=name.data).first()
        if name:
            raise ValidationError("This name is taken.")


class UpdateTeamForm(FlaskForm):
    name = StringField("Name of the teammate", validators=[DataRequired()])
    education = StringField("What education does it have?")
    position = StringField("What position does it take in this Organization")
    employer = StringField("Where does it works currently")
    work = StringField("Where else does it works")
    work_position = StringField("What position does it take?")
    social_link = StringField("Link to the social networks")
    biography = TextAreaField('More about person, biography')
    picture = FileField("Choose a picture", validators=[FileAllowed(['jpg', 'png'])])
    # file_name = StringField("File name", validators=[DataRequired()])
    submit = SubmitField('Update')

    def validate_name(self, name):
        name = Team.query.filter_by(name=name.data).all()
        if len(name) > 1:
            raise ValidationError("This name is taken.")
