from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired
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
    file_name = StringField("File name", validators=[DataRequired()])
    submit = SubmitField('Add the doctor')


class UpdateTeamForm(FlaskForm):
    name = StringField("Name of the teammate", validators=[DataRequired()])
    education = StringField("What education does it have?")
    position = StringField("What position does it take in this Organization")
    # employer = StringField("Where does it works currently")
    work = StringField("Where else does it works")
    work_position = StringField("What position does it take?")
    social_link = StringField("Link to the social networks")
    biography = TextAreaField('More about person, biography')
    picture = FileField("Choose a picture", validators=[FileAllowed(['jpg', 'png'])])
    file_name = StringField("File name", validators=[DataRequired()])
    submit = SubmitField('Update')

    def validate_name(self, name):
        if name != name.data:
            name = Team.query.filter_by(name=name.data).first()

    def validate_position(self, position):
        if position != position.data:
            position = Team.query.filter_by(position=position.data).first()

    def validate_education(self, education):
        if education != education.data:
            education = Team.query.filter_by(education=education.data).first()

    def validate_work(self, work):
        if work != work.data:
            work = Team.query.filter_by(work=work.data).first()

    def validate_work_position(self, work_position):
        if work_position != work_position.data:
            work_position = Team.query.filter_by(work_position=work_position.data).first()

    def validate_social_link(self, social_link):
        if social_link != social_link.data:
            social_link = Team.query.filter_by(social_link=social_link.data).first()

    def validate_biography(self, biography):
        if biography != biography.data:
            biography = Team.query.filter_by(biography=biography.data).first()

    def validate_picture(self, file_name):
        if file_name != file_name.data:
            file_name = Team.query.filter_by(image_file=file_name.data).first()
