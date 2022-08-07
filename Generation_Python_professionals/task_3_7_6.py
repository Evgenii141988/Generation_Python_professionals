import calendar

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        year = int(input())
        print(calendar.isleap(year))