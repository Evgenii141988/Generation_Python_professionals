import sys
from datetime import datetime

if __name__ == '__main__':
    pattern = '%Y-%m-%d'
    dates = [datetime.strptime(date.strip(), pattern) for date in sys.stdin]
    print((max(dates) - min(dates)).days)
