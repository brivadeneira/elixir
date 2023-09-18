"""
Utils for routers
"""
import os
from datetime import datetime

import pytz
from dotenv import load_dotenv
from pytz.exceptions import UnknownTimeZoneError

load_dotenv()


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
        timezone = datetime.now().astimezone().tzinfo

    time_now = get_time_now(timezone)

    return time_now < sunset_time
