"""
Cocktail endpoint definitions
"""
from dataclasses import asdict

from fastapi import APIRouter

from app.factories import CocktailFactory

router = APIRouter()


@router.get("/cocktail")
async def get_random_cocktail():
    """
    Return a random cocktail using its model factory
    :return: (dict) with the attributes of a cocktail
    e.g. { "name": "baby",
           "tagline": "Dark model light page conference away or inside.",
           "abv": 0.78,
           "ibu": 173,
           "food_pairing": ["Burger", "Pasta", "Pizza"]
         }
    """
    cocktail = CocktailFactory()
    return asdict(cocktail)
