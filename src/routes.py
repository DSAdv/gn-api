import os

from flask import render_template, flash, redirect
from flask import send_from_directory

from app import app
from src.forms import LoginForm


@app.route('/')
@app.route('/index')
def hello_world():
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
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login request for user -> {form.username.data}, remember_me={form.remember_me.data}")
        return redirect("/index")
    return render_template("login.html",
                           title="Sign In",
                           form=form)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
