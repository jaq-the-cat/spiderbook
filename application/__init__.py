import os
from typing import Callable

import dotenv
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

dotenv.load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

@app.before_first_request
def before_first_request():
    db.create_all()
    db.session.commit()

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Initialize Flask-Limiter
limiter = Limiter(
    app,
    key_func=get_remote_address
)

from application.models import User
@login_manager.user_loader
def load_user(uid: str):
    return User.query.get(uid)

# Register views
import application.controllers.auth
import application.controllers.index
import application.controllers.user
