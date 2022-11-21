def alternating_sequence(count=None):
    counter = 0
    while True:
        if counter == count:
            return
        counter += 1
        yield -counter if counter % 2 == 0 else counter


if __name__ == '__main__':
    generator = alternating_sequence()

    print(next(generator))
    print(next(generator))

    generator = alternating_sequence(10)

    print(*generator)

