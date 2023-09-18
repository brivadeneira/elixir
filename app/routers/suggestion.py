"""
Suggestion endpoint definitions
"""
from dataclasses import asdict
from typing import Annotated

from fastapi import APIRouter, Depends

from app.factories import BeerFactory, CocktailFactory
from app.models import User
from app.routers.utils import get_random_user, is_daytime

router = APIRouter()


@router.get("/suggestion")
async def get_custom_suggestion(current_user: Annotated[User, Depends(get_random_user)]):
    """
    Return a random beer (if it is daytime)
    or a cocktail (otherwise) using their model factories,

    :return: (dict) with the attributes of a beer/cocktail
    """
    user_timezone = current_user.timezone
    if is_daytime(user_timezone):
        beer = BeerFactory()
        return asdict(beer)

    cocktail = CocktailFactory()
    # demo patch to force the name of the cocktail
    cocktail.name = f"{current_user.name[0]}{cocktail.name[1:]}"
    return asdict(cocktail)
