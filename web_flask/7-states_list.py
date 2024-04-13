#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    all_states = list(storage.all(State).values())
    all_states.sort(key=lambda x: x.name)

    return render_template('7-states_list.html', states=all_states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
