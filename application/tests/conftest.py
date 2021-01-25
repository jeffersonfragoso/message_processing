import os
import pytest
from application.app import create_app

app = create_app()

@pytest.yield_fixture(autouse=True)
def application():
    """application with context."""

    ctx = app.app_context()
    ctx.push()

    yield app

    ctx.pop()


@pytest.yield_fixture()
def request_context(application):
    with application.test_request_context():
        yield


@pytest.fixture(scope='module')
def client():

    # celery config
    os.environ['RABBIT_URL'] = 'rabbitmq'

    with app.test_client() as client:
        with app.app_context():
            yield client
