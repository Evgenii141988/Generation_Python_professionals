import calendar
from datetime import date, timedelta


def get_all_mondays(year: int) -> list:
    mondey_days = []
    start = date(year, 1, 1)
    while start.year == year:
        if start.weekday() == 0:
            mondey_days.append(start)
            start += timedelta(days=7)
        else:
            start += timedelta(days=1)
    return mondey_days


if __name__ == '__main__':
   print(get_all_mondays(2021))