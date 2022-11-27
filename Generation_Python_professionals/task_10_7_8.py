from datetime import date, timedelta


def years_days(year: int):
    start = date(year, 1, 1)
    end = date(year, 12, 31)
    while start <= end:
        yield start
        start += timedelta(hours=24)


if __name__ == '__main__':
    dates = years_days(2022)

    print(next(dates))
    print(next(dates))
    print(next(dates))
    print(next(dates))
