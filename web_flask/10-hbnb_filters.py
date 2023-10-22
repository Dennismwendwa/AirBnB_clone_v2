#!/usr/bin/python3
"""this app list all states with teir cities"""
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity
from models import storage

app = Flask(__name__, static_url_path='/static')


@app.route("/hbnb_filters", strict_slashes=False)
def states_filters():
    """this route filter cities by states"""
    state = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html",
    state=state, amenities=amenities)


@app.teardown_appcontext
def app_teardown(exception):
    """cleaning all current request and Session resources"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
