if __name__ == '__main__':
    sign = input()
    match sign:
        case 'Овен' | 'Лев' | 'Стрелец':
            print('Огненный')
        case 'Телец' | 'Дева' | 'Козерог':
            print('Земной')
        case 'Близнецы' | 'Весы' | 'Водолей':
            print('Воздушный')
        case _:
            print('Водный')
