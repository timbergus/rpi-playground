#!/usr/bin/python3.4
"""Example 01"""

from flask import Flask

APP = Flask(__name__)


@APP.route('/')
def hello():
    """Main route."""
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=3000)
