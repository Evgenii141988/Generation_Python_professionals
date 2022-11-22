def primes(left: int, right: int):
    while True:
        counter = 0
        if left > right:
            return
        for i in range(2, left // 2 + 1):
            if left % i == 0:
                counter += 1
        if counter == 0 and left != 1:
            yield left
        left += 1


if __name__ == '__main__':
    generator = primes(1, 15)

    print(*generator)

    generator = primes(6, 36)

    print(next(generator))
    print(next(generator))
