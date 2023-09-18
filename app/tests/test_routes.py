"""
Test GET method for all the routes using TestClient
"""
from unittest import mock

import pytest
from fastapi.testclient import TestClient

from ..main import app
from ..routers import utils

client = TestClient(app)


def test_read_main():
    """
    Should be a welcome message
    :return: None
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Welcome to elixir! 🥃"


def assert_beer(response):
    """
    Test keys and values types for a beer expected response
    :param response: Response
    :return: None (or assert errors)
    """
    expected_keys = ["name", "tagline", "abv", "ibu", "food_pairing"]
    assert all(k in response.json() for k in expected_keys)
    assert isinstance(response.json()["name"], str)
    assert isinstance(response.json()["tagline"], str)
    assert isinstance(response.json()["abv"], float)
    assert isinstance(response.json()["ibu"], int)
    assert isinstance(response.json()["food_pairing"], list)


def assert_cocktail(response):
    """
    Test keys and values types for a cocktail expected response
    :param response: Response
    :return: None (or assert errors)
    """
    expected_keys = ["name", "tagline", "ingredients", "instructions"]
    assert all(k in response.json() for k in expected_keys)
    assert isinstance(response.json()["name"], str)
    assert isinstance(response.json()["tagline"], str)
    assert isinstance(response.json()["ingredients"], list)
    assert isinstance(response.json()["instructions"], str)


def test_get_beer():
    """
    Should be a random beer
    :return: None
    """

    response = client.get("/beer")
    assert response.status_code == 200
    assert_beer(response)


def test_get_cocktail():
    """
    Should be a random cocktail
    :return: None
    """

    response = client.get("/cocktail")
    assert response.status_code == 200
    assert_cocktail(response)


@pytest.mark.parametrize(
    "is_daytime_value",
    [True, False],
)
def test_get_suggestion(is_daytime_value):
    """
    Should be a custom suggestion
    :return: None
    """
    with mock.patch.object(utils, "is_daytime", return_value=is_daytime_value):
        # TODO: fix patch
        response = client.get("/suggestion")
        assert response.status_code == 200
        if is_daytime_value:
            assert_beer(response)
        else:
            assert_cocktail(response)
