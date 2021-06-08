# 重定向跳转
# 跳转回上一个页面（通过两种方式实现）
# 安全问题，对url进行验证
import os
from urllib.parse import urlparse

from flask import Flask, url_for, request
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'lisa123456')


@app.route('/hello')
def hello():
    return 'hello!'


@app.route('/foo')
def foo():
    return '<h1>Foo page</h1><a href="%s">Do something</a>' % url_for('do_something', next=request.full_path)


@app.route('/bar')
def bar():
    return '<h1>Bar page</h1><a href="%s">Do something</a>' % url_for('do_something', next=request.full_path)


@app.route('/do_something')
def do_something():
    # return redirect(url_for('hello'))
    # return redirect(request.referrer or url_for('hello'))
    # return redirect(request.args.get('next', url_for('hello')))
    return redirect_bak()


def redirect_bak(default='hello', **kwargs):
    for target in request.args.get('next'), request.referrer:
        # if target:
        #    return redirect(target)
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default, **kwargs))


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(target)
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


if __name__ == '__main__':
    app.run()
