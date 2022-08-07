import calendar

if __name__ == '__main__':
    year_str, month = input().split()
    year = int(year_str)
    n = list(calendar.month_name).index(month)
    print(calendar.monthrange(year, n)[1])