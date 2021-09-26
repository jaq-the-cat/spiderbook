from flask import Blueprint, render_template, url_for, redirect, jsonify

from application import app
from application.models import Post
from application.forms import PostForm, CommentForm

bp = Blueprint('index', __name__)

@bp.get('/')
def index():
    return render_template('board.jinja2',
            title="All",
            pf=PostForm(),
            cf=CommentForm(),
            posts=Post.query.all())

@bp.get('/b/<board>')
def board_posts(board: str):
    return render_template('board.jinja2',
            title=board,
            pf=PostForm(),
            cf=CommentForm(),
            posts=Post.query.filter_by(board=board))

@bp.get('/p/<post>')
def post(post: str):
    return redirect(url_for('index.index'))

@bp.get('/p/<post>/comments')
def post_replies(post: str):
    post = Post.query.filter_by(uid=post).first()
    return jsonify({
        "comments": [comment.body for comment in post.comments]
    })

app.register_blueprint(bp)
