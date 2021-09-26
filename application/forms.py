from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, TextAreaField, FileField
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms.fields.core import SelectField
from wtforms.fields.html5 import EmailField
from wtforms.fields.simple import HiddenField
from wtforms.validators import DataRequired, Email, Length

with open('boards.txt') as b:
    boards = [(b[:-1], b[:-1]) for b in b.readlines()]

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
    board = SelectField('Board', validators=[DataRequired()], choices=boards)
    image = FileField('Image', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'bmp'], 'Images only')])

class CommentForm(FlaskForm):
    post_uid = HiddenField('post_uid', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[Length(1, 512)])
    image = FileField('Image', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'bmp'], 'Images only')])
