from datetime import date


if __name__ == '__main__':
    n = int(input())
    dates = [date.fromisoformat(input()) for _ in range(n)]
    dates.sort()
    for d in dates:
        print(d.strftime('%d/%m/%Y'))
