from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
import datetime as dt
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
import sqlalchemy as sa
from app import db
from app.models import User
from flask import request
from urllib.parse import urlsplit

posts = None

@app.route('/')
@app.route('/index')
@login_required
def index():   
  return render_template('index.html',
                         title='Home page',
                         posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form = LoginForm()
  if form.validate_on_submit():
      user = db.session.scalar(
          sa.select(User).where(User.username == form.username.data))
      if user is None or not user.check_password(form.password.data):
          flash('Invalid username or password')
          return redirect(url_for('login'))
      login_user(user, remember=form.remember_me.data)
      next_page = request.args.get('next')
      if not next_page or urlsplit(next_page).netloc != '':
          next_page = url_for('index')
      return redirect(next_page)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))