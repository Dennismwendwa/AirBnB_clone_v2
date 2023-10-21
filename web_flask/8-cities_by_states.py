#!/usr/bin/python3
"""this app lists all cities with places"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def all_cities_by_state():
    """
    this route display all states and their cities
    """
    all_states = storage.all(State)
    return render_template("8-cities_by_states.html", all_states=all_states)


@app.teardown_appcontext
def teardown(exception):
    """cleaning all currect Session context"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
