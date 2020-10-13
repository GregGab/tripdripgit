# trip_blogs/form.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class TripBlogForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    city_country = StringField('City', validators=[DataRequired()])
    stayed_where = StringField('Hotel', validators=[DataRequired()])
    went_where = StringField('visited', validators=[DataRequired()])
    trip_image = FileField('Add Trip Photos', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Post")
