#!/usr/bin/python3
"""Starts a Flask web application"""
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb")
def filters():
    """Displays the list of all State objects sorted by name"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(e):
    """Close database"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
