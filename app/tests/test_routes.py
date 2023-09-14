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
    expected_keys = ["name", "tagline", "abv", "ibu", "food_pairing"]

    response = client.get("/beer")
    assert response.status_code == 200
    assert all(k in response.json() for k in expected_keys)
    assert isinstance(response.json()["name"], str)
    assert isinstance(response.json()["tagline"], str)
    assert isinstance(response.json()["abv"], float)
    assert isinstance(response.json()["ibu"], int)
    assert isinstance(response.json()["food_pairing"], list)


def test_get_cocktail():
    """
    Should be a random cocktail
    :return: None
    """
    expected_keys = ["name", "tagline", "ingredients", "instructions"]

    response = client.get("/cocktail")
    assert response.status_code == 200
    assert all(k in response.json() for k in expected_keys)
    assert isinstance(response.json()["name"], str)
    assert isinstance(response.json()["tagline"], str)
    assert isinstance(response.json()["ingredients"], list)
    assert isinstance(response.json()["instructions"], str)


def test_get_suggestion():
    """
    Should be a custom suggestion
    :return: None
    """
    response = client.get("/suggestion")
    assert response.status_code == 200
