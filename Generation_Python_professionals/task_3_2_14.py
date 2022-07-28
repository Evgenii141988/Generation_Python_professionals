from datetime import date


def is_correct(day: int, month: int, year: int) -> bool:
    try:
        d = date(year, month, day)
        return True
    except:
        return False


if __name__ == '__main__':
    count = 0
    while True:
        d = input()
        if d == 'end':
            break
        day, month, year = [int(i) for i in d.split('.')]
        if is_correct(day, month, year):
            print('Корректная')
            count += 1
        else:
            print('Некорректная')
    print(count)
