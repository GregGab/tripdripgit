# trip_blogs/form.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

class TripBlogForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    city_country = StringField('City', validators=[DataRequired()])
    stayed_where = StringField('Hotel', validators=[DataRequired()])
    went_where = StringField('Visited', validators=[DataRequired()])
    trip_image = FileField('Add Trip Photos', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Post")
