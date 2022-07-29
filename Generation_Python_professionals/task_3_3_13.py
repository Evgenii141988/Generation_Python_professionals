from datetime import datetime


if __name__ == '__main__':
    seconds = 2483228800
    dt = datetime(2011, 11, 4)

    print(datetime.fromtimestamp(seconds))
    print(dt.timestamp())

