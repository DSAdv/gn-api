import os

from flask import render_template, flash, redirect, url_for
from flask import send_from_directory
from flask_login import login_user, current_user, logout_user

from app import app
from src.forms import LoginForm
from src.models import User


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'David Ikkes'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]

    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        # todo: add logging message after user login
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template("login.html",
                           title="Sign In",
                           form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
