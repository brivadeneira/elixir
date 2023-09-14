"""
Models for drinks
"""
from pydantic import field_validator
from pydantic.dataclasses import dataclass


@dataclass
class Drink:
    """
    Base drink model to be inherited by every needed one
    """

    name: str
    tagline: str

    def __str__(self) -> str:
        return f"{self.name}: '{self.tagline}'"


@dataclass
class Beer(Drink):
    """
    Model for beer
    NOTE: abv and ibu should be fields with metadata
    """

    abv: float  # Alcohol by volume
    ibu: int  # International Bitterness Unit
    food_pairing: list[str]

    @field_validator("abv")
    def validate_abv(self, abv: float) -> float:
        """
        ABV (Alcohol by volume) represents a percentage,
        and its value must be between 0% and 100% -> 0, 1
        """
        if abv < 0 or abv > 1:
            raise ValueError(f"ABV must be a value between 0 and 1, not {abv}")
        return abv

    @field_validator("ibu")
    def validate_ibu(self, ibu: float) -> float:
        """
        IBU (International Bitterness Unit),
        the maximum "bitterness" value that can be detected by humans is 100 (120 exceptionally),
        however some beers put higher units in their indications, even 1000.
        """
        if ibu < 0 or ibu > 1000:
            raise ValueError(f"IBU must be a value between 0 and 1000, not {ibu}")
        return ibu


@dataclass
class Cocktail(Drink):
    """
    Model for cocktail
    """

    ingredients: list[str]
    instructions: str
