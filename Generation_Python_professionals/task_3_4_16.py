from datetime import datetime, timedelta

if __name__ == '__main__':
    pattern = '%H:%M:%S'
    dt = datetime.strptime(input(), pattern)
    n = int(input())
    print((dt + timedelta(seconds=n)).strftime(pattern))
