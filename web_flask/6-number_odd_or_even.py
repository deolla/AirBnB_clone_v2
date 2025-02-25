#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
        """/: display Hello HBNB!"""
        return 'Hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
        """/hbnb: display HBNB"""
        return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
        """/c/<text>: display followed by the value of text
            (replace underscore _ symbols with a space
        """
        text = text.replace('_', ' ')
        return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
        """Display Python, followed by the value of the text variable
            (replace underscore _ symbols with a space)
            The default value of text is \is cool
        """
        text = text.replace('_', ' ')
        return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
        """/number/<n>: display is a number only if n is an integer"""
        return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_number_html(n):
        """/number_template/<n>: display a HTML page only if n is an integer"""
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
        """/number_odd_or_even/<n>: display a HTML page only if n is integer"""
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
