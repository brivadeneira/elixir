"""
Cocktail endpoint definitions
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/cocktail")
async def get_random_cocktail():
    """
    :return:
    """
    return
