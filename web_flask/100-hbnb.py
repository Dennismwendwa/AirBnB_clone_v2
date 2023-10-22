#!/usr/bin/python3
"""this app list all states with teir cities"""
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models import storage

app = Flask(__name__, static_url_path='/static')


@app.route("/hbnb", strict_slashes=False)
def hbnb_filters():
    """this route filter cities by states"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)

    return render_template("100-hbnb.html",
                           states=states,
                           amenities=amenities,
                           places=places)


@app.teardown_appcontext
def app_teardown(exception):
    """cleaning all current request and Session resources"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
