import sys
from datetime import datetime

from freezegun import freeze_time

import atdate


def test_at_date_has_parse_attribute():
    assert hasattr(atdate, 'parse')


def test_at_date_has_atdateparser_attribute():
    assert hasattr(atdate, 'AtDateParser')


def test_parse_return_datetime_object():
    test_string = 'noon'
    result = atdate.parse(test_string)
    assert isinstance(result, datetime)


@freeze_time('2000-01-02 03:04:05')
def test_at_now():
    test_string = 'now'
    result = atdate.parse(test_string)
    assert result == datetime(2000, 1, 2, 3, 4, 5, 0)


@freeze_time('2000-01-02 03:04:05')
def test_at_noon_before_noon():
    test_string = 'noon'
    result = atdate.parse(test_string)
    assert result == datetime(2000, 1, 2, 12, 0, 0, 0)


@freeze_time('2000-01-02 13:04:05')
def test_at_noon_after_noon():
    test_string = 'noon'
    result = atdate.parse(test_string)
    assert result == datetime(2000, 1, 3, 12, 0, 0, 0)


@freeze_time('2000-01-31 13:04:05')
def test_at_noon_month_change():
    test_string = 'noon'
    result = atdate.parse(test_string)
    assert result == datetime(2000, 2, 1, 12, 0, 0, 0)


@freeze_time('2000-12-31 13:04:05')
def test_at_noon_year_change():
    test_string = 'noon'
    result = atdate.parse(test_string)
    assert result == datetime(2001, 1, 1, 12, 0, 0, 0)
