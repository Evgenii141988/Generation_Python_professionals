import calendar

if __name__ == '__main__':
    year, month = (int(i) for i in input().split())
    print(calendar.monthrange(year, month)[1])