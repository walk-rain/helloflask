import json
import os

import click
from flask import Flask, request, redirect, url_for, make_response, session
from markupsafe import escape
from werkzeug.exceptions import abort

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'yard123456')


@app.route('/')
def hello_world():
    # return 'Hello World!', 302, {'Location': 'http://www.baidu.com'}
    # return redirect('http://www.baidu.com')
    return redirect(url_for('hello'))


@app.route('/hello')
def hello():
    # name = request.args.get('name', 'Flask')
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name', 'Human')  # 从cookie中获取
    response = '<h1>Hello, %s!</h1>' % escape(name)
    if 'logged_in' in session:
        response += '[Authenticated]'
    else:
        response += '[Not Authenticated]'
    return response
    # for name in request.args.get('name'), request.cookies.get('name', 'Human'):
    #     if name is None:
    #         continue
    #     response = '<h1>Hello, %s!</h1>' % name
    #     if 'logged_in' in session:
    #         response += '[Authenticated]'
    #     else:
    #         response += '[Not Authenticated]'
    #     return response
    # return 'hello!'


@app.route('/foo')
def foo():
    # response = make_response('Hello')
    # response.mimetype = 'text/plain'
    # return response
    data = {
        'name': 'yard',
        'gender': 'male'
    }
    response = make_response(json.dumps(data))
    response.mimetype = 'application/json'
    return response
    # return jsonify({'name': 'yard','gender': 'male'})


@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name)
    return response


@app.route('/login')
def login():
    session['logged_in'] = True
    return redirect(url_for('hello'))


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
    return redirect(url_for('hello'))


@app.route('/admin')
def admin():
    if 'logged_in' not in session:
        abort(403)
    else:
        return 'Welcome to admin page!'


@app.cli.command()
def hello():
    click.echo('hello World!')


if __name__ == '__main__':
    app.run()
