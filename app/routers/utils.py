"""
Utils for routers
"""
import os
from datetime import datetime

import pytz
import requests
from dotenv import load_dotenv
from pytz.exceptions import UnknownTimeZoneError
from requests import HTTPError, Timeout, TooManyRedirects

from app.factories import UserFactory

load_dotenv()

RAND_USER_URL = "https://randomuser.me/api/"


def get_random_user() -> UserFactory:
    """
    Build a random user from data
    :return: (User)
    """
    try:
        rand_user_resp = requests.get(RAND_USER_URL, timeout=30)
        rand_user = rand_user_resp.json()["results"][0]
        user_name, user_timezone = (
            rand_user["name"]["first"],
            rand_user["location"]["timezone"]["description"],
        )
        return UserFactory(name=user_name, timezone=user_timezone)
    except (ConnectionError, HTTPError, Timeout, TooManyRedirects, KeyError):
        return UserFactory(timezone=get_local_timezone())


def get_local_timezone():
    """
    Self-explanatory
    """
    return datetime.now().astimezone().tzinfo


def get_time_now(timezone):
    """
    Get the time right now
    :param timezone: (timezone)
    :return:
    """
    return datetime.now(timezone).time()


def is_daytime(str_timezone: str = None, str_sunset_time: str = None) -> bool:
    """
    Return a bool according to the time for the given timezone compared with the given sunset time,
    if not timezone given, the local one is going to be used.
    in case of not sunset time given, the env var SUNSET_TIME is going to be used.
    :param str_sunset_time: (str) with '%H:%M' format, e.g. 19:30
    :param str_timezone: (str) e.g. 'Europe/Lisbon'
    :return: (bool) self-explanatory
    """

    if not str_sunset_time:
        str_sunset_time = os.getenv("SUNSET_TIME")

    sunset_time = datetime.strptime(str_sunset_time, "%H:%M").time()

    timezone = None

    if str_timezone:
        try:
            timezone = pytz.timezone(str_timezone)
        except UnknownTimeZoneError:
            pass

    if not timezone:
        timezone = get_local_timezone()

    time_now = get_time_now(timezone)

    return time_now < sunset_time
