"""
Beer endpoint definitions
"""
from dataclasses import asdict

from fastapi import APIRouter

from app.factories import BeerFactory

router = APIRouter()


@router.get("/beer")
async def get_random_beer():
    """
    Return a random Beer using its model factory
    :return: (dict) with the attributes of a beer
    e.g. { "name": "worker",
           "tagline": "Need prove difference note power first.",
           "abv": 0.35,
           "ibu": 338,
           "food_pairing": ["Sushi", "Pizza", "Sushi"]
          }
    """
    beer = BeerFactory()
    return asdict(beer)
