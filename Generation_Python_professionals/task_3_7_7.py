import calendar

if __name__ == '__main__':
    year_str, month = (i for i in input().split())
    year = int(year_str)
    num_month = list(calendar.month_abbr).index(month)
    print(calendar.month(year, num_month))
