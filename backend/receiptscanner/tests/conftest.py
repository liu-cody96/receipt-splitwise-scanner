import pytest

from receiptscanner.app import main_app


@pytest.fixture(scope='session')
def main_app():
    """
    Setup our flask test app, this only gets executed once.

    :return: Flask app
    """

    _app = main_app

    main_app.config.update({
        "DEBUG": False,
        "TESTING": True,
    })
    # other setup can go here
    yield _app
    # clean up / reset resources here


@pytest.fixture(scope='function') # scope = function ensures every test is independent
def client(app):
    return app.test_client()