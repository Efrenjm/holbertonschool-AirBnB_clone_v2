#!/usr/bin/python3
"""Start a Flask web application"""
from models import storage
from models.place import Place
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template


app = Flask(__name__, template_folder='./templates')


@app.teardown_appcontext
def teardown(exception):
    """Close the SQLAlchemy session"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def load_filters():
    """Load State, City, Place and Amenity filters if found"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template('100-hbnb.html', states=states, amenities=amenities, places=places)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
