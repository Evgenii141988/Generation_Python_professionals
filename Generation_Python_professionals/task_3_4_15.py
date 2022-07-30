from datetime import datetime, timedelta

if __name__ == '__main__':
    hours, minutes, seconds = (int(i) for i in input().split(':'))
    delta = timedelta(hours=hours, minutes=minutes, seconds=seconds).total_seconds()
    print(int(delta))