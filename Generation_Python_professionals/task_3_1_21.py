from datetime import date


def saturdays_between_two_dates(start: date, end: date) -> int:
    if end < start:
        start, end = end, start
    return len([date.fromordinal(day) for day in range(start.toordinal(), end.toordinal() + 1) if
                date.fromordinal(day).weekday() == 5])


if __name__ == '__main__':
    date1 = date(2021, 11, 1)
    date2 = date(2021, 11, 22)

    print(saturdays_between_two_dates(date1, date2))
