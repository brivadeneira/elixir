"""
Suggestion endpoint definitions
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/suggestion")
async def get_custom_suggestion():
    """
    :return:
    """
    return
