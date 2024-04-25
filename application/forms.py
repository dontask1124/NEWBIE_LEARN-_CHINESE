from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from application.models import user

class LoginForm(FlaskForm):
    userName = StringField("Username", validators=[DataRequired()])
    passWord = PasswordField("Password", validators=[DataRequired(),Length(min =6, max = 15)])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Login")
    
