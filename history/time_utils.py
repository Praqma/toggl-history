import calendar

from datetime import date


def get_previous_month(given_day = date.today()):
    """
    Returns the first day of the previous month for the given day

    >>> get_previous_month(date(1991, 1, 31))
    datetime.date(1990, 12, 1)
    """
    month, year = -1, -1
    if (given_day.month == 1):
        month = 12
        year = given_day.year -1
    else:
        month = given_day.month - 1
        year = given_day.year
    return date(year, month, 1)

def get_month_day_range(day_in_month):
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