"""
Suggestion endpoint definitions
"""
from dataclasses import asdict

from fastapi import APIRouter

from app.factories import BeerFactory, CocktailFactory
from app.routers.utils import is_daytime

router = APIRouter()


@router.get("/suggestion")
async def get_custom_suggestion():
    """
    Return a random beer (if it is daytime)
    or a cocktail (otherwise) using their model factories,

    :return: (dict) with the attributes of a beer/cocktail
    """
    if is_daytime():
        beer = BeerFactory()
        return asdict(beer)

    cocktail = CocktailFactory()
    return asdict(cocktail)
