def number_of_frogs(year: int) -> int:
    if year == 1:
        return 77
    else:
        return 3 * (number_of_frogs(year - 1) - 30)


if __name__ == '__main__':
    print(number_of_frogs(2))
    print(number_of_frogs(10))
    print(number_of_frogs(1))