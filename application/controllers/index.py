from flask import Blueprint, render_template, url_for, redirect, jsonify, send_file
import os
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
            posts=Post.query.order_by(Post.dt.desc()).all())

@bp.get('/b/<board>')
def board_posts(board: str):
    return render_template('board.jinja2',
            title=board,
            board=board,
            pf=PostForm(),
            cf=CommentForm(),
            posts=Post.query.filter_by(board=board).order_by(Post.dt.desc()))

@bp.get('/p/<post>')
def post(post: str):
    return render_template('board.jinja2',
            title=post,
            cf=CommentForm(),
            posts=Post.query.filter_by(uid=post).all())

@bp.get('/p/<post>/image')
def post_image(post: str):
    post: Post = Post.query.filter_by(uid=post).first()
    return send_file(
        os.path.join('..', post.image_path),
        download_name=post.image_filename,
        mimetype=post.image_mimetype
    )

@bp.get('/p/<post>/comments')
def post_replies(post: str):
    post = Post.query.filter_by(uid=post).first()
    return jsonify({
        "comments": [comment.body for comment in sorted(post.comments, key=lambda c: c.dt, reverse=True)]
    })

app.register_blueprint(bp)
