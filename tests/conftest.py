from blogexample.app import create_app,db
import pytest

@pytest.fixture
def app():
    app=create_app()
    app.config.update({
        "SQLALCHEMY_DATABASE_URI":'sqlite://',
        'WTF_CSRF_ENABLED':False,
    })
    with app.app_context():
        db.create_all()
    yield app


@pytest.fixture
def client(app):
    return app.test_client()