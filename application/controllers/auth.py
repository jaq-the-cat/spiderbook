from flask import Blueprint, redirect, render_template, request, url_for

from application import app, db
from application.forms import LoginForm, SignupForm
from application.models import User
from application.util import hashpw

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    login_form = LoginForm()
    if request.method.lower() == 'get':
        return render_template('signin.jinja2', title='Sign In', lf=login_form)
    if login_form.validate_on_submit():
        res = User.query.filter_by(
            email=login_form.email.data,
            password=hashpw(login_form.password.data)
        ).all()
        if len(res) != 0:
            res[0].signin(login_form.remember_me)
        return redirect(url_for('index.index'))
    return redirect(url_for('auth.auth'))

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_form = SignupForm()
    if request.method.lower() == 'get':
        return render_template('signup.jinja2', title='Sign Up', sf=signup_form)
    if signup_form.validate_on_submit():
        print(vars(signup_form.email))
        db.session.add(User(
            signup_form.name.data,
            signup_form.email.data,
            signup_form.password.data
        ))
        db.session.commit()
        return redirect(url_for('index.index'))
    return redirect(url_for('auth.auth'))

app.register_blueprint(bp)
