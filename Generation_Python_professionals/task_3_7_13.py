import calendar
from datetime import date, timedelta


def get_third_thursday(year: int) -> list:
    pattern = '%d.%m.%Y'
    thursday_days = []
    for month in range(1, 13):
        start = date(year, month, 1)
        count = 0
        while start.month == month:
            if start.weekday() == 3:
                count += 1
                if count == 3:
                    thursday_days.append(start.strftime(pattern))
                    count = 0
                start += timedelta(days=7)
            else:
                start += timedelta(days=1)
    return thursday_days


if __name__ == '__main__':
    year = int(input())
    print(*get_third_thursday(year), sep='\n')