import logging

import pytest

from backend.app import create_app
from backend.database import db as _db


@pytest.fixture()
def app():
    """app

    Create application for the tests
    """
    _app = create_app("tests.settings")
    _app.logger.setLevel(logging.DEBUG)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()

@pytest.fixture()
def db(app):
    """db

    Create database for the tests
    """
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    # Explicitly close DB connection
    _db.session.close()
    _db.drop_all()

@pytest.fixture()
def client():
    """client

    Create client for the tests
    """
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client