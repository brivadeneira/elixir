"""
main module
"""
from fastapi import FastAPI

from app.routers.beer import router as beer_router
from app.routers.cocktail import router as cocktail_router
from app.routers.home import router as home_router
from app.routers.suggestion import router as suggestion_router

app = FastAPI()

app.include_router(home_router)
app.include_router(beer_router)
app.include_router(cocktail_router)
app.include_router(suggestion_router)
