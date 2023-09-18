"""
Test routers utils
"""
from datetime import datetime
from unittest import mock

import pytest

from app.routers import utils


@pytest.mark.parametrize(
    "str_timezone,str_sunset_time,now_time,expected",
    [
        ("America/Denver", "19:00", "16:45", True),
        (None, "20:45", "23:30", False),
        ("Pacific/Truk", None, "19:00", True),
    ],
)
def test_is_daytime(str_timezone, str_sunset_time, now_time, expected):
    """
    Should return the expected bool according to mocked times
    """
    now_time_obj = datetime.strptime(now_time, "%H:%M").time()

    with mock.patch.object(utils, "get_time_now", return_value=now_time_obj):
        assert expected == utils.is_daytime(str_timezone, str_sunset_time)
