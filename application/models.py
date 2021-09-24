# type: ignore
from uuid import uuid4

from flask_login import login_user, logout_user

from application import db
from application.util import hashpw

class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    suspended = db.Column(db.Boolean, nullable=False)
    posts = db.relationship('Post', backref='user')

    def __init__(self, name: str, email: str, password: str):
        self.uid = str(uuid4())
        self.name = name
        self.email = email
        self.password = hashpw(password)
        self.suspended = False

    def signin(self, rember: bool):
        login_user(self, remember=rember)

    def __repr__(self):
        return f'User<{self.email} : {self.name}>'

    def is_authenticated(self) -> bool:
        return True

    def is_active(self) -> bool:
        return not self.suspended

    def is_anonymous(self) -> bool:
        return False

    def get_id(self) -> str:
        return self.uid

class Board(db.Model):
    __tablename__ = 'boards'
    uid = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(128), unique=True)

    def __init__(self, name: str):
        self.uid = str(uuid4())
        self.name = name

class Post(db.Model):
    __tablename__ = 'posts'
    uid = db.Column(db.String(36), primary_key=True)
    user_uid = db.Column(db.String(36), db.ForeignKey('users.uid'))
    board_uid = db.Column(db.String(36), db.ForeignKey('boards.uid'))
    title = db.Column(db.String(128))
    body = db.Column(db.String(1024))

    def __init__(self, user_uid: str, board_name: str, title: str, body: str):
        self.uid = str(uuid4())
        self.user_uid = user_uid
        self.board_uid = Board.query.filter_by(name=board_name).first().uid
        self.title = title
        self.body = body
