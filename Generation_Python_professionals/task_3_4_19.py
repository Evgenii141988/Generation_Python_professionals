from datetime import datetime, timedelta

if __name__ == '__main__':
    pattern = '%d.%m.%Y'
    date_list = [datetime.strptime(d, pattern) for d in input().split()]
    n = len(date_list)
    result = [abs((date_list[i + 1] - date_list[i]).days) for i in range(n - 1)]
    print(result)
