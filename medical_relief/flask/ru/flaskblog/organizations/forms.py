from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired
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
    file_name = StringField("File name", validators=[DataRequired()])
    submit = SubmitField('Add the organization')


class UpdateOrganiztionForm(FlaskForm):
    title = StringField("Name of the organization", validators=[DataRequired()])
    address = StringField("What address does it have?", validators=[DataRequired()])
    link = StringField("Please enter a website address")
    specialization = StringField("What specialization does it have?")
    city = StringField("In which city it located?")
    country = StringField("In which city it located?")
    content = TextAreaField('Description of work of the organization')
    picture = FileField("Choose a picture", validators=[FileAllowed(['jpg', 'png'])])
    file_name = StringField("File name", validators=[DataRequired()])
    submit = SubmitField('Update')

    def validate_title(self, title):
        if title != title.data:
            title = Partners.query.filter_by(title=title.data).first()

    def validate_address(self, address):
        if address != address.data:
            address = Partners.query.filter_by(address=address.data).first()

    def validate_link(self, link):
        if link != link.data:
            link = Partners.query.filter_by(link=link.data).first()

    def validate_specialization(self, specialization):
        if specialization != specialization.data:
            specialization = Partners.query.filter_by(specialization=specialization.data).first()

    def validate_city(self, city):
        if city != city.data:
            city = Partners.query.filter_by(city=city.data).first()

    def validate_country(self, country):
        if country != country.data:
            country = Partners.query.filter_by(country=country.data).first()

    def validate_content(self, content):
        if content != content.data:
            content = Partners.query.filter_by(content=content.data).first()

    def validate_picture(self, picture):
        if picture != picture.data:
            picture = Partners.query.filter_by(image_file=picture.data).first()
