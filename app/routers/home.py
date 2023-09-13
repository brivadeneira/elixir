"""
Home endpoint definitions
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def welcome():
    """
    :return:
    """
    return "Welcome to whiskycito! 🥃"
