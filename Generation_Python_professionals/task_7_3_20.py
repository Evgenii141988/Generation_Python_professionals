from calendar import month_name

if __name__ == '__main__':
    months = {i: month for i, month in enumerate(list(month_name)) if i != 0}
    try:
        number = int(input())
        print(months[number])
    except ValueError:
        print('Введено некорректное значение')
    except KeyError:
        print('Введено число из недопустимого диапазона')