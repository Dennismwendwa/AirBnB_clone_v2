#!/usr/bin/python3
"""THis page displays all states"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def all_states():
    """
    this route disply all cities in an ahtml page
    """
    states = storage.all(State)
    states = sorted(states.values(), key=lambda s: s.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """
    this method closes all current request section and SQLALchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
