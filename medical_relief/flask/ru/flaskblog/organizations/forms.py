from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError
from flaskblog.models import Partners


class OrganizationForm(FlaskForm):
    title = StringField("Name of the organization", validators=[DataRequired()])
    address = StringField("What address does it have?", validators=[DataRequired()])
    link = StringField("Please enter a website address")
    specialization = StringField("What specialization does it have?")
    city = StringField("In which city it located?")
    country = StringField("In which country it located?")
    content = TextAreaField('Description of work of the organization')
    picture = FileField("Choose a picture", validators=[FileAllowed(['jpg', 'png'])])
    # file_name = StringField("File name", validators=[DataRequired()])
    submit = SubmitField('Add the organization')


    def validate_title(self, title):
        title = Partners.query.filter_by(title=title.data).first()
        if title:
            raise ValidationError("This titlte is taken.")



class UpdateOrganiztionForm(FlaskForm):
    title = StringField("Name of the organization", validators=[DataRequired()])
    address = StringField("What address does it have?", validators=[DataRequired()])
    link = StringField("Please enter a website address")
    specialization = StringField("What specialization does it have?")
    city = StringField("In which city it located?")
    country = StringField("In which city it located?")
    content = TextAreaField('Description of work of the organization')
    picture = FileField("Choose a picture", validators=[FileAllowed(['jpg', 'png'])])
    # file_name = StringField("File name", validators=[DataRequired()])
    submit = SubmitField('Update')

    def validate_title(self, title):
        title = Partners.query.filter_by(title=title.data).all()
        if len(title) > 1:
            raise ValidationError("This title is taken.")
