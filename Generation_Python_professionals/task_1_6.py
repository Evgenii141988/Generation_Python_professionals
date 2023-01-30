# объявление функции
def is_between(name, surname, middlename):
    print(surname <= name <= middlename or middlename <= name <= surname)


if __name__ == '__main__':
    # считываем данные
    a, b, c = map(int, input().split())

    # вызываем функцию
    is_between(a, b, c)
