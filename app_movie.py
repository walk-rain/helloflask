from flask import Flask, render_template

app = Flask(__name__)

user = {
    'username': 'yard',
    'bio': 'A boy who love movies'
}
movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'}
]


@app.route('/index')
def index():
    return 'hello!'


@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user, movies=movies)


if __name__ == '__main__':
    app.run()
