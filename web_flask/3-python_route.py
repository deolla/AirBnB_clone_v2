#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
        """/: display Hello HBNB!"""
        return 'Hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
        """/hbnb: display HBNB"""
        return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
        """/c/<text>: display followed by the value of the text variable
            (replace underscore _ symbols with a space
        """
        text = text.replace('_', ' ')
        return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
        """Display Python, followed by the value of the text variable
           (replace underscore _ symbols with a space)
            The default value of text is cool
        """
        text = text.replace('_', ' ')
        return "Python {}".format(text)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
