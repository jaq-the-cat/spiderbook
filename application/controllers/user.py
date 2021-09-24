from application.forms import PostForm
from flask import render_template, Blueprint, redirect
from flask_login import login_required, current_user
from application import app, db
from application.models import Post

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
        return redirect(url_for('index.index'))
    return redirect(url_for('index.index'))

app.register_blueprint(bp)
