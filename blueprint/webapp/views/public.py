from flask import Blueprint, render_template


# Instantiate a blueprint object.
# This object is imported by the module containing the application factory, and registered with a Flask application object
#
# We call it 'bp' by convention, to make registration consistent and predictable
bp = Blueprint('public', __name__)


@bp.route('/', strict_slashes=False)
def landing():
    return render_template('public/landing.html')

