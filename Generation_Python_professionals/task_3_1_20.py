from datetime import date


def get_date_range(start: date, end: date) -> list:
    if end >= start:
        return [date.fromordinal(day) for day in range(start.toordinal(), end.toordinal() + 1)]
    return []


if __name__ == '__main__':
    date1 = date(2021, 10, 1)
    date2 = date(2021, 10, 5)

    print(*get_date_range(date1, date2), sep='\n')