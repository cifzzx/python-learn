#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>hello world!!!</h1>'


@app.route('/sigin', methods=['GET'])
def signin_form():
    return '''<form action="/sigin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/sigin', methods=['POST'])
def sigin():
    if request.form['username'] == 'ljm' and request.form['password'] == '123':
        return '<h1>welcome!!!</h1>'

    return '<h1>username or password error</h1>'


@app.route('/sigin/get', methods=['GET'])
def sigin_get():
    if request.args.get('username') == 'ljm' and request.args.get('password') == '123':
        return '<h1>welcome!!!,login get</h1>'

    return '<h1>username or password error</h1>'


if __name__ == '__main__':
    app.run()
