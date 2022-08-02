from datetime import timedelta, datetime

if __name__ == '__main__':
    pattern = '%d.%m.%Y'
    start = datetime.strptime(input(), pattern)
    end = datetime.strptime(input(), pattern)
    while True:
        if (start.day + start.month) % 2 == 0:
            start += timedelta(days=1)
        else:
            break
    while True:
        if start.weekday() not in (0, 3):
            print(start.strftime(pattern))
        start += timedelta(days=3)
        if start > end:
            break

