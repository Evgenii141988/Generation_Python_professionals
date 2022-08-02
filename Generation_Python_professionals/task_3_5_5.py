from datetime import datetime

if __name__ == '__main__':
    n = int(input())
    pattern = '%d.%m.%Y'
    employees = []
    for _ in range(n):
        name, lastname, date_birthday = input().split()
        employees.append((name, lastname, datetime.strptime(date_birthday, pattern)))
    oldest_employee = min(employees, key=lambda x: x[2])
    oldest_employees = [employee for employee in employees if employee[2] == oldest_employee[2]]
    if len(oldest_employees) == 1:
        print(oldest_employee[2].strftime(pattern), oldest_employee[0], oldest_employee[1])
    else:
        print(oldest_employee[2].strftime(pattern), len(oldest_employees))