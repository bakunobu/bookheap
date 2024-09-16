from app import app
from flask import render_template
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
    'title': 'Юность полководца'},

    {
    'username': 'Sergei Vakunov',
    'login': 'bakunobu',
    'date': dt.datetime.now(),
    'author': 'Р. Адамс',
    'title': 'Обитатели холмов'
    }
  ]
    
  return render_template('index.html',
                         title='Home',
                         user=user,
                         posts=posts)