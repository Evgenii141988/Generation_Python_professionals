def get_weekday(number: int) -> str:
    days = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда', 4: 'Четверг', 5: 'Пятница', 6: 'Суббота', 7: 'Воскресенье'}
    if type(number) == int:
        try:
            return days[number]
        except KeyError:
            raise ValueError('Аргумент не принадлежит требуемому диапазону')
    else:
        raise TypeError('Аргумент не является целым числом')


if __name__ == '__main__':
    print(get_weekday(1))

    try:
        print(get_weekday('hello'))
    except Exception as err:
        print(err)
        print(type(err))

    try:
        print(get_weekday(8))
    except ValueError as err:
        print(err)
        print(type(err))