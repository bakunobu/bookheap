from app import app
from flask import render_template
from app.forms import LoginForm
import datetime as dt


@app.route('/')
@app.route('/index')
def index():
  user = {'username': 'Sergei Vakunov'}
  posts = [
    {
    'username': 'Sergei Vakunov',
    'login': 'bakunobu',
    'date': dt.datetime.now(),
    'author': 'В. Ян',
    'title': 'Юность полководца'
    },

    {
    'username': 'Sergei Vakunov',
    'login': 'bakunobu',
    'date': dt.datetime.now(),
    'author': 'Р. Адамс',
    'title': 'Обитатели холмов'
    },

       {
    'username': 'Sergei Vakunov',
    'login': 'bakunobu',
    'date': dt.datetime.now(),
    'author': 'Р. Хайнлайн',
    'title': 'Дверь в лето'
    }
  ]
    
  return render_template('index.html',
                         title='Home',
                         user=user,
                         posts=posts)


@app.route('/login')
def login():
  form = LoginForm()
  return render_template('login.html', title='Sign In', form=form)