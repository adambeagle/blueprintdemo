from flask import Blueprint, jsonify, request, url_for
from .. import models


bp = Blueprint('api.soda', __name__)


@bp.route('/create', methods=['POST'])
def create():
    soda = models.Soda(**{k:request.form.get(k) for k in request.form if request.form.get(k)})
    try:
        soda.add_object()
    except:
        return jsonify(success=False, err='Database error')
    return jsonify(success=True, result=soda.serialize())


@bp.route('/delete', methods=['POST'])
def delete():
    soda = models.Soda.query.filter_by(soda_id=request.form.get('soda_id')).first_or_404()
    try:
        soda.delete_object()
    except:
        return jsonify(success=False, err='Database error')
    return jsonify(success=True, redirect=url_for('soda.index'))


@bp.route('/get', methods=['POST'])
def get():
    soda = models.Soda.query.filter_by(soda_id=request.form.get('soda_id')).first_or_404()
    return jsonify(success=True, result=soda.serialize())


@bp.route('/update', methods=['POST'])
def update():
    soda = models.Soda.query.filter_by(soda_id=request.form.get('soda_id')).first_or_404()
    for key in request.form:
        setattr(soda, key, request.form.get(key))
    try:
        soda.update_object()
    except Exception as e:
        print(e)
        return jsonify(success=False, err='Database error')
    return jsonify(success=True, result=soda.serialize())
