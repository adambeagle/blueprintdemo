from flask import Flask, g, jsonify, render_template, request, url_for
from pathlib import Path

from . import models


app = Flask(__name__, root_path=Path(__file__).parent.parent)
models.db.init_app(app)
with app.app_context():
    models.db.create_all()
app.jinja_env.globals['models'] = models


"""
REQUEST HOOKS
"""


@app.before_request
def before_request():
    g.branding = "Monolith Example"


"""
ERROR HANDLERS
"""


@app.errorhandler(404)
def errorhandler_404(err):
    return "I still haven't found what I'm looking for. -Bono"


"""
SETUP VIEWS
"""


@app.route('/setup/init-db')
def init_db():
    models.db.create_all()
    return 'SUCCESS'


"""
VIEWS
"""


@app.route('/')
def index():
    return render_template('landing.html')


@app.route('/pops')
@app.route('/sodas')
def sodas_list():
    sodas = models.Soda.query.order_by(models.Soda.name).all()
    return render_template('sodas_list.html', sodas=sodas)


@app.route('/pops/<int:soda_id>')
@app.route('/sodas/<int:soda_id>')
def soda_detail(soda_id):
    soda = models.Soda.query.filter_by(soda_id=soda_id).first_or_404()
    return render_template('soda.html', soda=soda)


"""
SODAS API
"""


@app.route('/api/soda/create', methods=['POST'])
def api_soda_create():
    soda = models.Soda(**{k:request.form.get(k) for k in request.form if request.form.get(k)})
    try:
        soda.add_object()
    except:
        return jsonify(success=False, err='Database error')
    return jsonify(success=True, result=soda.serialize())


@app.route('/api/soda/delete', methods=['POST'])
def api_soda_delete():
    soda = models.Soda.query.filter_by(soda_id=request.form.get('soda_id')).first_or_404()
    try:
        soda.delete_object()
    except:
        return jsonify(success=False, err='Database error')
    return jsonify(success=True, redirect=url_for('sodas_list'))


@app.route('/api/soda/get', methods=['POST'])
def api_soda_get():
    soda = models.Soda.query.filter_by(soda_id=request.form.get('soda_id')).first_or_404()
    return jsonify(success=True, result=soda.serialize())


@app.route('/api/soda/update', methods=['POST'])
def api_soda_update():
    soda = models.Soda.query.filter_by(soda_id=request.form.get('soda_id')).first_or_404()
    for key in request.form:
        setattr(soda, key, request.form.get(key))
    try:
        soda.update_object()
    except Exception as e:
        print(e)
        return jsonify(success=False, err='Database error')
    return jsonify(success=True, result=soda.serialize())

