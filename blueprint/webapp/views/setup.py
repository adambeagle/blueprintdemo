from flask import Blueprint
from .. import models


bp = Blueprint('setup', __name__)


@bp.route('/init-db')
def init_db():
    models.db.create_all()
    return 'SUCCESS'
