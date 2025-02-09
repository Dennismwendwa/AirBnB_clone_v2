#!/usr/bin/python3
"""this is flask application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return f"Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def rout_hbnb():
    return f"HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fan(text):
    formatted_t = text.replace("_", " ")
    return f"C {formatted_t}"


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text):
    formatted_t = text.replace("_", " ")
    return f"Python {formatted_t}"


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def template_num(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_or_old(n):
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
