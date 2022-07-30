from datetime import date, timedelta


if __name__ == '__main__':
    day, month, year = (int(i) for i in input().split('.'))
    my_date = date(year, month, day)
    print((my_date - timedelta(days=1)).strftime('%d.%m.%Y'))
    print((my_date + timedelta(days=1)).strftime('%d.%m.%Y'))
