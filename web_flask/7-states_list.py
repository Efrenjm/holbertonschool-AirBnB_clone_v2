#!/usr/bin/python3
"""Start a Flask web application"""
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__, template_folder='./templates')


@app.teardown_appcontext
def remove_current_session(exception):
    """Close the SQLAlchemy session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Get the list of all states"""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
