from datetime import datetime, timedelta

if __name__ == '__main__':
    dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)

    print(dt.strftime('%d.%m.%Y %H:%M:%S'))
