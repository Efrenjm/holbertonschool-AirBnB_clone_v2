#!/usr/bin/python3
"""
Starts a flask web app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_c(text):
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python(text):
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    return "{} is a number".format(n)


@app.route('number_template(<int:n>)', strict_slashes=False)
def show_template(n):
    if isinstance(n, int):
        return render_template('number_template.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)