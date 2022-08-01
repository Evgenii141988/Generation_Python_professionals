from datetime import date, time, datetime, timedelta


if __name__ == '__main__':
    week_days_num = {}
    start = date(day=1, month=1, year=1)
    while start < date(day=31, month=12, year=9999):
        if start.day == 13:
            week_days_num[start.weekday()] = week_days_num.get(start.weekday(), 0) + 1
        start += timedelta(days=1)
    for i in range(7):
        print(week_days_num[i])