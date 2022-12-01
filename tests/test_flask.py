
import pytest
from shop_app import create_app

@pytest.fixture()
def app():
    a = create_app()
    a.config.update({
        "TESTING": True,
    })
    yield a

@pytest.fixture()
def client(app):
    return app.test_client()

def test_request_example(client):
    response = client.get("/")
    assert isinstance(response.text, str)
