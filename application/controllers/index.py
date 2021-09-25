from flask import Blueprint, render_template

from application import app
from application.models import Post, Board
from application.forms import PostForm

bp = Blueprint('index', __name__)

@bp.get('/')
def index():
    return render_template('index.jinja2', title='Title')

@bp.get('/b/<board>')
def board_posts(board: str):
    print(Board.query.all())
    return render_template('board.jinja2',
            title=board,
            pf=PostForm(),
            posts=Post.query.all())

app.register_blueprint(bp)
