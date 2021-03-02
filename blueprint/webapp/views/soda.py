from flask import Blueprint, render_template
from .. import models


bp = Blueprint('soda', __name__)


@bp.route('/', strict_slashes=False)
def index():
    sodas = models.Soda.query.order_by(models.Soda.name).all()
    return render_template('soda/index.html', sodas=sodas)


@bp.route('/<int:soda_id>')
def detail(soda_id):
    soda = models.Soda.query.filter_by(soda_id=soda_id).first_or_404()
    return render_template('soda/detail.html', soda=soda)
