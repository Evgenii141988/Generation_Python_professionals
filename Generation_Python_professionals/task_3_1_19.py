from datetime import date


def get_min_max(dates: list) -> tuple:
    if dates:
        return min(dates), max(dates)
    return ()


if __name__ == '__main__':
    dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
    print(get_min_max(dates))
    print(get_min_max([]))
    dates = [date(2021, 10, 5), date(2021, 10, 5), date(2021, 10, 5), date(2021, 10, 5)]

    print(get_min_max(dates))
