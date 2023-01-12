if __name__ == '__main__':
    n = int(input())
    match n:
        case 1:
            print('Совсем еще зеленый студентик')
        case 2:
            print('Джун-студент')
        case 3:
            print('Мидл-студент')
        case 4:
            print('Сеньер-студент')
        case 5:
            print('Босс качалки')
        case _:
            print('Неизвестный курс')
