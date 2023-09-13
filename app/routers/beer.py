"""
Beer endpoint definitions
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/beer")
async def get_random_beer():
    """
    :return:
    """
    return
