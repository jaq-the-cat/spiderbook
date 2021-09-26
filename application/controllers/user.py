import os
from uuid import uuid4

from flask import Blueprint, jsonify, redirect, render_template, url_for, request
from flask_login import current_user, login_required
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

from application import app, db
from application.forms import CommentForm, PostForm
from application.models import Comment, Post

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.get('/profile')
def profile():
    return ''

@bp.post('/post')
@login_required
def post():
    board = request.args.get('board')
    r = url_for('index.board_posts', board=board)\
        if board is not None\
        else url_for('index.index')
    pf = PostForm()
    if pf.validate_on_submit():
        image: FileStorage = pf.image.data
        path = os.path.join(
            os.getenv('UPLOAD_PATH', 'storage/'),
            f"{uuid4()}{image.filename.split('.')[-1]}")
        mt = image.mimetype
        image.save(path),
        db.session.add(Post(
            current_user.get_id(),
            pf.board.data,
            pf.title.data,
            pf.body.data,
            secure_filename(image.filename),
            path,
            mt,
        ))
        db.session.commit()
        return redirect(r)
    else:
        print(pf.errors)
    return redirect(r)

@bp.post('/comment')
@login_required
def comment():
    cf = CommentForm()
    if cf.validate_on_submit():
        image: FileStorage = cf.image.data
        path = os.path.join(
            os.getenv('UPLOAD_PATH', 'storage/'),
            f"{uuid4()}{image.filename.split('.')[-1]}")
        mt = image.mimetype
        image.save(path),
        db.session.add(Comment(
            current_user.get_id(),
            cf.post_uid.data,
            cf.body.data,
            secure_filename(image.filename.split('/')[-1]),
            path,
            mt,
        ))
        db.session.commit()
        return jsonify({'succ': True})
    else:
        print(cf.errors)
    return jsonify({'succ': False})

app.register_blueprint(bp)
