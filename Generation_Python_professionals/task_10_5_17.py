def reverse(sequence):
    sequence = list(sequence)
    while True:
        if not sequence:
            return
        yield sequence.pop()


def reverse1(sequence):
    for i in reversed(sequence):
        yield i


if __name__ == '__main__':
    print(*reverse([1, 2, 3, 4, 5]))

    generator = reverse1('beegeek')

    print(type(generator))
    print(*generator)
