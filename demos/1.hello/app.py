# -*- coding: utf-8 -*-
"""
    第一章的例子
"""

import click
from flask import Flask

app = Flask(__name__)   # Web app 启动项


# the minimal Flask application
@app.route('/')
def index():
    return '<h1>Hello, Mad World!</h1>'


# bind multiple URL for one view function
@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello, Flask!</h1>'


# dynamic route, URL variable default
@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name


# custom flask cli command
@app.cli.command()
def hello():
    """Just say hello."""
    click.echo('Hello, Human!')
