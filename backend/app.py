from flask import Flask

from backend.task import views as task_views
from backend.extensions import db, migrate
from backend import commands


def create_app(config_object="config.settings"):
    """create_app
    
    Create application factory
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app


def register_extensions(app):
    """register_extensions

    Register Flask extensions
    """
    db.init_app(app)
    migrate.init_app(app, db)
    return None


def register_blueprints(app):
    """register_blueprints

    Register Flask blueprints
    """
    app.register_blueprint(task_views.blueprint)
    return None


def register_commands(app):
    """register_commands
    
    Register Click commands
    """
    app.cli.add_command(commands.test)