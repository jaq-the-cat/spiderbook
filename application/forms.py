from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, TextAreaField
from wtforms.fields.core import SelectField
from wtforms.fields.html5 import EmailField
from wtforms.fields.simple import HiddenField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(5, 256)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me?', default=False)

class SignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(4, 32)])
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(1, 256)])
    password = PasswordField('Password', validators=[DataRequired()])

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 128)])
    body = TextAreaField('Body', validators=[Length(1, 1024)])
    board = SelectField('Board', validators=[DataRequired()], choices=[
        ('board-a', 'board-a'),('board-b', 'board-b'), ('board-c', 'board-c')])

class CommentForm(FlaskForm):
    post_uid = HiddenField('post_uid', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[Length(1, 512)])
