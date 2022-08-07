import calendar


if __name__ == '__main__':
    year, month, day = (int(i) for i in input().split('-'))
    n = calendar.weekday(year, month, day)
    print(list(calendar.day_name)[n])
