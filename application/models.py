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
        return not User.query.filter_by(uid=uid).first().suspended

    def is_anonymous(self) -> bool:
        return False

    def get_id(self) -> str:
        return self.uid

class Post(db.Model):
    __tablename__ = 'posts'
    uid = db.Column(db.String(36), primary_key=True, nullable=False)
    user_uid = db.Column(db.String(36), db.ForeignKey('users.uid'), nullable=False)
    board = db.Column(db.String(36))
    comments = db.relationship('Comment', backref='post')
    title = db.Column(db.String(128), nullable=False)
    body = db.Column(db.String(1024), nullable=False)
    image_filename = db.Column(db.String(512), nullable=True)
    image_path = db.Column(db.String(512), nullable=True)
    image_mimetype = db.Column(db.String(64), nullable=True)

    def __repr__(self):
        return f'Post<{self.title[:30]} : {self.body[:30]} by {self.user_uid}>'

    def __init__(self, user_uid: str, board: str, title: str, body: str,
            image_filename: str=None, image_path: str=None, image_mimetype: str=None):
        self.uid = str(uuid4())
        self.user_uid = user_uid
        self.board = board
        self.title = title
        self.body = body
        self.image_filename = image_filename
        self.image_path = image_path
        self.image_mimetype = image_mimetype

class Comment(db.Model):
    __tablename__ = 'comments'
    uid = db.Column(db.String(36), primary_key=True, nullable=False)
    user_uid = db.Column(db.String(36), db.ForeignKey('users.uid'), nullable=False)
    post_uid = db.Column(db.String(36), db.ForeignKey('posts.uid'), nullable=False)
    body = db.Column(db.String(512), nullable=False)
    image_filename = db.Column(db.String(512), nullable=True)
    image_path = db.Column(db.String(512), nullable=True)
    image_mimetype = db.Column(db.String(64), nullable=True)

    def __repr__(self):
        return f'Comment<{self.body[:30]} by {self.user_uid}>'

    def __init__(self, user_uid: str, post_uid: str, body: str,
            image_filename: str=None, image_path: str=None, image_mimetype: str=None):
        self.uid = str(uuid4())
        self.user_uid = user_uid
        self.post_uid = post_uid
        self.body = body
        self.image_filename = image_filename
        self.image_path = image_path
        self.image_mimetype = image_mimetype
