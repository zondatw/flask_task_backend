import logging

import pytest

from backend.app import create_app


@pytest.fixture()
def app():
    """Create application for the tests."""
    _app = create_app()
    _app.logger.setLevel(logging.DEBUG)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()