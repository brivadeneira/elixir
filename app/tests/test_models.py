"""
Tests for models using factories
"""
import unittest

from pydantic import ValidationError

from app.factories import BeerFactory, CocktailFactory, DrinkFactory, UserFactory


class TestUser(unittest.TestCase):
    def test_valid_user(self):
        """
        Should be a valid user
        """
        user = UserFactory()
        self.assertIsInstance(user.name, str)
        self.assertIsInstance(user.timezone, str)

    def test_wrong_types(self):
        """
        Test validation for name and tagline as numbers
        """
        with self.assertRaises(ValidationError):
            UserFactory(name=-200)

        with self.assertRaises(ValidationError):
            UserFactory(timezone=-200)


class TestDrink(unittest.TestCase):
    def test_valid_drink(self):
        """
        Should be a valid drink
        """
        drink = DrinkFactory()
        self.assertIsInstance(drink.name, str)
        self.assertIsInstance(drink.tagline, str)

    def test_wrong_types(self):
        """
        Test validation for name and tagline as numbers
        """
        with self.assertRaises(ValidationError):
            DrinkFactory(name=-200)

        with self.assertRaises(ValidationError):
            DrinkFactory(tagline=-200)


class TestBeer(unittest.TestCase):
    def test_valid_beer(self):
        """
        Should be a valid beer
        """
        beer = BeerFactory()

        self.assertIsInstance(beer.name, str)
        self.assertIsInstance(beer.tagline, str)
        self.assertIsInstance(beer.abv, float)
        self.assertIsInstance(beer.ibu, int)
        self.assertIsInstance(beer.food_pairing, list)
        self.assertTrue(all(isinstance(food, str) for food in beer.food_pairing))

    def test_wrong_abv(self):
        """
        Test ABV validation with invalid types and values
        """
        with self.assertRaises(ValidationError):
            BeerFactory(abv="fake abv")
        with self.assertRaises(ValueError):
            BeerFactory(abv=-200)

    def test_wrong_ibu(self):
        """
        Test IBU validation with invalid types and values
        """
        with self.assertRaises(ValidationError):
            BeerFactory(ibu="fake ibu")
        with self.assertRaises(ValueError):
            BeerFactory(ibu=2000)


class TestCocktail(unittest.TestCase):
    def test_valid_cocktail(self):
        """
        Should be a valid cocktail
        """
        cocktail = CocktailFactory()

        self.assertIsInstance(cocktail.name, str)
        self.assertIsInstance(cocktail.tagline, str)
        self.assertIsInstance(cocktail.instructions, str)
        self.assertIsInstance(cocktail.ingredients, list)
        self.assertTrue(all(isinstance(ing, str) for ing in cocktail.ingredients))

    def test_wrong_types(self):
        """
        Test validation with invalid types for ingredients and instructions
        """
        with self.assertRaises(ValueError):
            CocktailFactory(instructions=-200)
        with self.assertRaises(ValueError):
            CocktailFactory(ingredients=-200)
