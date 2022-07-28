from datetime import date


if __name__ == '__main__':
    date1 = date.fromisoformat(input())
    date2 = date.fromisoformat(input())
    min_date = min((date1, date2))
    print(min_date.strftime('%d-%m (%Y)'))