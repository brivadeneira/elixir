"""
Beer and Cocktail factories
"""
import random

import factory
import pytz

from app.models import Beer, Cocktail, Drink, User

food_names = [
    "Pizza",
    "Burger",
    "Sushi",
    "Pasta",
    "Salad",
    "Steak",
    "Tacos",
    "Ice Cream",
    "Fries",
    "Soup",
]


class UserFactory(factory.Factory):
    """
    For creating fake users
    """

    class Meta:
        model = User

    name = factory.Faker("name")
    timezone = random.choice(pytz.all_timezones)


class DrinkFactory(factory.Factory):
    """
    For creating fake drinks
    """

    class Meta:
        model = Drink

    name = factory.Faker("word")
    tagline = factory.Faker("sentence")


class BeerFactory(factory.Factory):
    """
    For creating fake beers
    """

    class Meta:
        model = Beer

    name = factory.Faker("word")
    tagline = factory.Faker("sentence")
    abv = factory.Faker("pyfloat", min_value=0, max_value=1)
    ibu = factory.Faker("pyint", min_value=0, max_value=1000)
    food_pairing = random.sample(food_names, 3)  # TODO: sublist is not changing with new requests


class CocktailFactory(factory.Factory):
    """
    For creating fake cocktails
    """

    class Meta:
        model = Cocktail

    name = factory.Faker("word")
    tagline = factory.Faker("sentence")
    ingredients = factory.List([factory.Faker("word") for _ in range(3)])
    instructions = factory.Faker("text")
