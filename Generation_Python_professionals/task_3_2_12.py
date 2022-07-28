from datetime import date


def print_good_dates(dates: list):
    if dates:
        dates.sort()
        for d in dates:
            day, month, year = int(d.day), int(d.month), int(d.year)
            if year == 1992 and day + month == 29:
                print(d.strftime('%B %d, %Y'))


if __name__ == '__main__':
    dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
    print_good_dates(dates)
