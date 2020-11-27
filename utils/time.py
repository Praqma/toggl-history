import calendar

from datetime import date, datetime
from typing import Tuple


def format_ms_as_hhmmss(miliseconds: int):
    """
    Formats given miliseconds (int) as a string: hh:mm:ss

    >>> format_ms_as_hhmmss(115123456)
    '31:58:43'
    """
    seconds = int(miliseconds/1000)
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return f'{h:d}:{m:02d}:{s:02d}'

def get_month_range(start: Tuple[int, int], until: Tuple[int, int]):
    """
    Returns a range of months between the given dates

    >>> get_month_range((1991, 1), (1991, 1))
    []

    >>> get_month_range((1991, 1), (1991, 2))
    [datetime.date(1991, 1, 1)]

    >>> get_month_range((1991, 1), (1991, 3))
    [datetime.date(1991, 1, 1), datetime.date(1991, 2, 1)]

    >>> get_month_range((1991, 12), (1992, 2))
    [datetime.date(1991, 12, 1), datetime.date(1992, 1, 1)]

    >>> len(get_month_range((1991, 12), (1993, 2)))
    14
    """
    start_year, start_month = start
    until_year, until_month = until
    if start_year == until_year:
        return [
            date(start_year, month, 1)
            for month in range(start_month, until_month)
        ]
    else:
        first_year = [
            date(start_year, month, 1)
            for month in range(start_month, 13)
        ]
        in_between_years = [
            date(year, month, 1)
            for year in range(start_year + 1, until_year)
            for month in range(1, 13)
        ]
        final_year = [
            date(until_year, month, 1)
            for month in range(1, until_month)
        ]
        return first_year + in_between_years + final_year

def get_month_day_range(day_in_month: date):
    """
    Returns the first and last day for the given day's month

    >>> get_month_day_range(date(2020, 2, 12))
    (datetime.date(2020, 2, 1), datetime.date(2020, 2, 29))
    """
    first_day = day_in_month.replace(day = 1)
    last_day = day_in_month.replace(day = calendar.monthrange(day_in_month.year, day_in_month.month)[1])
    return first_day, last_day

if __name__ == "__main__":
    import doctest
    doctest.testmod()
