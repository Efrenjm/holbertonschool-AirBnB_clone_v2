#!/usr/bin/python3
"""Start a Flask web application"""
from flask import Flask, render_template
app = Flask(__name__, template_folder='./templates')


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace("_", " ")
    return f'C {text}'


@app.route('/python', strict_slashes=False, defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    text = text.replace("_", " ")
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def python_number(n):
    try:
        return f'{n} is a number'
    except TypeError:
        return f'{n} must be an integer'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    try:
        return render_template('5-number.html', n=n)
    except TypeError:
        return f'{n} must be an integer'


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    try:
        is_even = n % 2 == 0
        return render_template('6-number_odd_or_even.html',
                               n=n, is_even=is_even)
    except TypeError:
        return f'{n} must be an integer'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
