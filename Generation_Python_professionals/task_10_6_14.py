def cubes_of_odds(iterable):
    return (number ** 3 for number in iterable if number % 2)


if __name__ == '__main__':
    print(*cubes_of_odds([1, 2, 3, 4, 5]))

    evens = [2, 4, 6, 8, 10]

    print(list(cubes_of_odds(evens)))
