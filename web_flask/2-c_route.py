#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
        """display Hello HBNB"""
        return 'Hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
        """display HBNB"""
        return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def custom_text(text):
        """Replace underscores with spaces"""
        text = text.replace('_', ' ')
        return "C {}".format(text)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
