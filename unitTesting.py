import pytest
import webserver


@pytest.fixture
def client():
    app = webserver.app
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def testMainPage(client):
    result = client.get("/")

    assert 200 == result.status_code

def testPizza(client):
    result = client.get("/pizza")
    assert 200 == result.status_code

def testBread(client):
    result = client.get("/bread")
    assert 200 == result.status_code

def test404(client):
    result = client.get('/test')
    assert 404 == result.status_code

def testMaintenance(client):
    result = client.get("/maintenance")
    assert 503 == result.status_code
    result = client.get("/")
    assert '503 SERVICE UNAVAILABLE' == result.status
