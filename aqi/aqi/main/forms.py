from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class GetCity(FlaskForm):
  city = StringField("Enter city name", validators=[DataRequired()])
  submit = SubmitField("Go")