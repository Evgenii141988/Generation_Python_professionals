from datetime import datetime, timedelta

if __name__ == '__main__':
    pattern = '%d.%m.%Y'
    start_date = datetime.strptime(input(), pattern)
    print(start_date.strftime(pattern))
    for n in range(2, 11):
        start_date += timedelta(days=n)
        print(start_date.strftime(pattern))

