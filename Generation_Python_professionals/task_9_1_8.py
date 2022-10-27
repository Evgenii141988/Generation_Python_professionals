def custom_isinstance(objects: list, typeinfo):
    return len([obj for obj in objects if isinstance(obj, typeinfo)])


if __name__ == '__main__':
    numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
    print(custom_isinstance(numbers, list))

    numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
    print(custom_isinstance(numbers, (int, float)))

    numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
    print(custom_isinstance(numbers, int))