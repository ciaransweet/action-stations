from datetime import datetime

from assertpy import assert_that
from freezegun import freeze_time

from src.get_datetime import get_the_datetime


@freeze_time("2021-01-01 23:49:49")
def test_that_datetime_returned_correctly():
    the_frozen_time = get_the_datetime()
    assert_that(the_frozen_time).is_equal_to(datetime.now())
