#!/usr/bin/python3
"""Start a Flask web application"""

from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def filters():
    """Render template with states"""
    pop = '10-hbnb_filters.html'
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template(pop, states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(e):
    """Remove database"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
