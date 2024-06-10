#!/usr/bin/python3
"""Start a Flask web application"""
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template


app = Flask(__name__, template_folder='./templates')


@app.teardown_appcontext
def remove_current_session(exception):
    """Close the SQLAlchemy session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def load_filters():
    """Load State, City and Amenity filters if found"""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda z: z.name)
    for state in states:
        cities = sorted(state.cities, key=lambda y: y.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
