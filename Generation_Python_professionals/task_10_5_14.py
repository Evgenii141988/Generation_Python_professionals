def simple_sequence():
    number = 1
    while True:
        for _ in range(number):
            yield number
        number += 1


if __name__ == '__main__':
    generator = simple_sequence()

    print(next(generator))
    print(next(generator))

    generator = simple_sequence()
    numbers = [next(generator) for _ in range(10)]

    print(*numbers)
