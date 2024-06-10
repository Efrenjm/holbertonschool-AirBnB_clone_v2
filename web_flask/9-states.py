#!/usr/bin/python3
"""Start a Flask web application"""
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__, template_folder='./templates')


@app.teardown_appcontext
def teardown(exception):
    """Close the SQLAlchemy session"""
    storage.close()


@app.route('/states', defaults={'id': None}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_id_found(id):
    """Get the list of cities related to the state id"""
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state, id=id)
    if id is None:
        return render_template('9-states.html', states=states, id=id)
    return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
