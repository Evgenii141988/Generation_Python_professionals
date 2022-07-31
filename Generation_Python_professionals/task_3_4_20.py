from datetime import datetime, timedelta


def fill_up_missing_dates(dates: list):
    pattern = '%d.%m.%Y'
    my_dates = [datetime.strptime(dt, pattern) for dt in dates]
    start = min(my_dates)
    end = max(my_dates)
    result = []
    while start <= end:
        result.append(start.strftime(pattern))
        start += timedelta(days=1)
    return result


if __name__ == '__main__':
    dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']

    print(fill_up_missing_dates(dates))
