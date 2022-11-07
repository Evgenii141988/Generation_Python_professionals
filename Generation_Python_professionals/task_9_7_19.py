def sandwich(func):
    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        result = func(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return result

    return wrapper


@sandwich
def add_ingredients(ingredients):
    print(' | '.join(ingredients))


@sandwich
def beegeek():
    return 'beegeek'


if __name__ == '__main__':
    add_ingredients(['томат', 'салат', 'сыр', 'бекон'])
    print(beegeek())
