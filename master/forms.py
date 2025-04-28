from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField , PasswordField , SelectField ,SelectMultipleField,widgets,DateField
from wtforms.validators import InputRequired 

class LoginForm(FlaskForm):
    username = StringField("username" , validators=[InputRequired()])
    
    submit = SubmitField("submit")
