#!/usr/bin/python3
"""
this script shows states in route one
and cities of a state in route two
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def sates():
    """
    Displays all states in HTML page
    """
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route("/states/<id>")
def all_states(id):
    """
    displays states in html page
    """
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template("9-states.html", states=state)

    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exception):
    """
    cleaning all the current Session and request context
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
