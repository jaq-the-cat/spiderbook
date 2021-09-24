from flask import render_template, Blueprint

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.get('/profile')
def profile():
    return ''

@bp.post('/post')
def post():
    return ''

@bp.post('/comment')
def comment():
    return ''
