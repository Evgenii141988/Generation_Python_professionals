import sys
from datetime import datetime

if __name__ == '__main__':
    pattern = '%d.%m.%Y'
    dates = [datetime.strptime(date_str.strip(), pattern) for date_str in sys.stdin]
    n = len(dates)
    asc = all((dates[i + 1] > dates[i] for i in range(n - 1)))
    desc = all((dates[i + 1] < dates[i] for i in range(n - 1)))
    if asc:
        print('ASC')
    elif desc:
        print('DESC')
    else:
        print('MIX')