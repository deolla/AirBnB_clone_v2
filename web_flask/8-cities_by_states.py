#!/usr/bin/python3
"""Starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Routes:
            /: display Hello HBNB!
            /hbnb: display HBNB
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Routes:
            /: display Hello HBNB!
            /hbnb: display HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """c/<text>: display followed by the value of text
            (replace underscore _ symbols with a space
    """
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ Display Python, followed by the value of the text variable
            (replace underscore _ symbols with a space)
    """
    return 'Python {}'.format(text.replace("_", " "))


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
    if n % 2 == 0:
        p = 'even'
    else:
        p = 'odd'
    return render_template('6-number_odd_or_even.html', number=n, parity=p)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """state  storage"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(e):
    """Remove the current SQLAlchemy"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    """/cities_by_states: display a HTML page"""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
