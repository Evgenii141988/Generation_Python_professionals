import calendar
from datetime import date


def get_days_in_month(year: int, month: str) -> list:
    n_month = list(calendar.month_name).index(month)
    n_days = calendar.monthrange(year, n_month)[1]
    return [date(year, n_month, day) for day in range(1, n_days + 1)]


if __name__ == '__main__':
    print(get_days_in_month(2021, 'December'))
