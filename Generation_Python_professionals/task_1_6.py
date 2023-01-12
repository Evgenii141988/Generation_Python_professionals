if __name__ == '__main__':
    n = int(input())
    match n:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            print(31)
        case 4 | 6 | 9 | 11:
            print(30)
        case 2:
            print(28)
        case _:
            print('Неизвестный месяц')
