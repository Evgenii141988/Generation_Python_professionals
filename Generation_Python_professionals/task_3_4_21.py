from datetime import datetime, timedelta


if __name__ == '__main__':
    pattern = '%H:%M'
    start = datetime.strptime(input(), pattern)
    end = datetime.strptime(input(), pattern)
    while start + timedelta(minutes=45) <= end:
        s = start
        e = start + timedelta(minutes=45)
        print(f'{s.strftime(pattern)} - {e.strftime(pattern)}')
        start += timedelta(minutes=55)
