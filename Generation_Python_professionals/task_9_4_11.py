def numbers_sum(elems: list):
    """Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет."""
    return sum(filter(lambda x: type(x) in (int, float), elems))


if __name__ == '__main__':
    print(numbers_sum([1, '2', 3, 4, 'five']))
    print(numbers_sum(['beegeek', 'stepik', '100']))
    print(numbers_sum.__doc__)
