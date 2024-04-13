#!/Users/efrenjimenez/Cursos/Holberton/holbieEnv/bin/python
#!/usr/bin/python3
"""
A simple Flask web application.
"""
from flask import Flask, render_template

from models import storage
from models.amenity import Amenity
from models.state import State


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    '''The hbnb_filters page.'''
    all_states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    all_states.sort(key=lambda x: x.name)
    amenities.sort(key=lambda x: x.name)
    for state in all_states:
        state.cities.sort(key=lambda x: x.name)

    return render_template('10-hbnb_filters.html',
                           states=all_states, amenities=amenities)


@app.teardown_appcontext
def flask_teardown(exc):
    '''The Flask app/request context end event listener.'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
