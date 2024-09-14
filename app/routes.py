from app import app
import datetime as dt
@app.route('/')
@app.route('/index')
def index():
  user = {
    'username': 'Sergei Vakunov',
    'login': 'bakunobu',
    'date': dt.datetime.now(),
    'author': 'Р. Адамс',
    'title': 'Обитатели холмов'
    }
  return f'''
    <html>
      <head>
        <title>Home Page - Microblog</title>
      </head>
      <body>
        <h1>{user.get('username')} @{user.get('login')}</h1>
        <h2>Прочитано: {user.get('author')}.{user.get('title')}.</h2>
        <h2>{user.get('date')}</h2>
      </body>
    </html>'''