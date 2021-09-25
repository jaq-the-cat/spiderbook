from flask import Blueprint, render_template

from application import app
from application.models import Post, Board
from application.forms import PostForm

bp = Blueprint('index', __name__)

@bp.get('/')
def index():
    return render_template('board.jinja2',
            title="All",
            pf=PostForm(),
            posts=Post.query.all())

@bp.get('/b/<board>')
def board_posts(board: str):
    return render_template('board.jinja2',
            title=board,
            pf=PostForm(),
            posts=Post.query.filter_by(board=board))

@bp.get('/p/<post>')
def post(post: str):
    print(Board.query.all())
    post = Post.query.filter_by(uid=post).first()
    return render_template('post.jinja2',
            title=post.title,
            post=post)

app.register_blueprint(bp)
