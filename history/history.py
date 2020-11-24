import calendar

from history.time_utils import get_previous_month
from history.time_utils import get_month_day_range

def store(client, monthCount):
    day_in_month = get_previous_month()

    for i in range(monthCount):
        from_date, to_date = get_month_day_range(day_in_month)

        print(f"Requesting month: {calendar.month_name[day_in_month.month]}")
        print(f"  from: {from_date}")
        print(f"  to: {to_date}")

        day_in_month = get_previous_month(day_in_month)
