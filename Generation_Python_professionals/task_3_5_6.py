from datetime import timedelta, datetime

if __name__ == '__main__':
    n = int(input())
    pattern = '%d.%m.%Y'
    employees = {}
    max_date = []
    for _ in range(n):
        name, lastname, birthday = input().split()
        birthday = datetime.strptime(birthday, pattern)
        employees[birthday] = employees.get(birthday, 0) + 1
    max_date = max((v for v in employees.values()))
    max_dates = sorted((k for k, v in employees.items() if v == max_date))
    print(*[d.strftime(pattern) for d in max_dates], sep='\n')

