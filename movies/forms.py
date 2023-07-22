from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    username = StringField('username', validators = [DataRequired()])
    email = StringField('email', validators = [DataRequired(), Email()])
    password = PasswordField('password', validators = [DataRequired()])
    submit_button = SubmitField()


class MovieForm(FlaskForm):
    name = StringField('name')
    description = StringField('description')
    price = DecimalField('price', places=2)
    release = StringField('release')
    director = StringField('director')
    sequel = StringField('sequel')
    based_on = StringField('based_on')
    box_office = StringField('box_office')    
    series = StringField('series')
    dad_joke = StringField('dad joke')
    submit_button = SubmitField()
    

