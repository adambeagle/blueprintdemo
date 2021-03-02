from flask import Flask, g
from pathlib import Path
from . import api, models, views


def create_app():
    app = Flask(__name__, root_path=Path(__file__).parent.parent)
    models.db.init_app(app)
    
    # (This is only here because this app uses the default in-memory sqllite database for simplicity)
    with app.app_context():
        models.db.create_all()

    # This line registers the blueprint with the application.
    # I.e. the /, /login, and /contact routes are now part of the application's URL schema
    app.register_blueprint(views.public.bp)

    app.register_blueprint(views.setup.bp, url_prefix='/setup')

    # This blueprint is registered twice, with two different prefixes
    # Note the first registered prefix takes precedence when using url_for
    app.register_blueprint(views.soda.bp, url_prefix='/sodas')
    app.register_blueprint(views.soda.bp, url_prefix='/pops')

    # API blueprints are registered the same way as view blueprints
    # By convention they should always start with `/api/<endpoint>` where 
    app.register_blueprint(api.soda.bp, url_prefix='/api/soda')

    app.before_request(before_request)
    app.register_error_handler(404, views.errorhandling.on_404)
    app.jinja_env.globals['models'] = models
    return app


def before_request():
    g.branding = 'Blueprint Demo'
