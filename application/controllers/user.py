from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required

from application import app, db
from application.forms import PostForm
from application.models import Post, Comment

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.get('/profile')
def profile():
    return ''

@bp.post('/post')
@login_required
def post():
    pf = PostForm()
    if pf.validate_on_submit():
        db.session.add(Post(
            current_user.get_id(),
            pf.board.data,
            pf.title.data,
            pf.body.data
        ))
        db.session.commit()
        return redirect(url_for('index.index'))
    return redirect(url_for('index.index'))

@bp.post('/comment')
def comment():
    cf = PostForm()
    if cf.validate_on_submit():
        db.session.add(Comment(
            current_user.get_id(),
            cf.post_uid.data,
            cf.body.data
        ))
        db.session.commit()
        return redirect(url_for('index.index'))
    return redirect(url_for('index.index'))

app.register_blueprint(bp)
