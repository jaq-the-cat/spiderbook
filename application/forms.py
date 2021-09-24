from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.fields.core import SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(256)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me?', default=False)

class SignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(32)])
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(256)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me?', default=False)

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(128)])
    body = TextAreaField('Body', validators=[Length(1024)])
    board = SelectField('Board', validators=[DataRequired()],
            choices=['board-a', 'board-b'])
