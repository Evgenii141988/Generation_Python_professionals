from collections import namedtuple
from itertools import combinations

if __name__ == '__main__':
    bag_mass = int(input())
    Item = namedtuple('Item', ['name', 'mass', 'price'])

    items = [Item('Обручальное кольцо', 7, 49_000),
             Item('Мобильный телефон', 200, 110_000),
             Item('Ноутбук', 2000, 150_000),
             Item('Ручка Паркер', 20, 37_000),
             Item('Статуэтка Оскар', 4000, 28_000),
             Item('Наушники', 150, 11_000),
             Item('Гитара', 1500, 32_000),
             Item('Золотая монета', 8, 140_000),
             Item('Фотоаппарат', 720, 79_000),
             Item('Лимитированные кроссовки', 300, 80_000)]

    items.sort(key=lambda x: x.mass)
    result = []
    for i in range(1, len([elm.mass for elm in items if elm.mass <= bag_mass]) + 1):
        for elm in set(combinations((elm for elm in items if elm.mass <= bag_mass), r=i)):
            if sum(e.mass for e in elm) <= bag_mass:
                result.append(elm)

    try:
        for elm in sorted(max(result, key=lambda x: sum(i.price for i in x)), key=lambda y: y.name):
            print(elm.name)
    except ValueError:
        print('Рюкзак собрать не удастся')

