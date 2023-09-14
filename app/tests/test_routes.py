"""
Test GET method for all the routes using TestClient
"""
from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_read_main():
    """
    Should be a welcome message
    :return: None
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Welcome to whiskycito! 🥃"


def test_get_beer():
    """
    Should be a random beer
    :return: None
    """
    response = client.get("/beer")
    assert response.status_code == 200


def test_get_cocktail():
    """
    Should be a random cocktail
    :return: None
    """
    response = client.get("/cocktail")
    assert response.status_code == 200


def test_get_suggestion():
    """
    Should be a custom suggestion
    :return: None
    """
    response = client.get("/suggestion")
    assert response.status_code == 200
