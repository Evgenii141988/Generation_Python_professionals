def is_prime(number: int):
    if number == 1:
        return False
    return all(number % i != 0 for i in range(2, number // 2 + 1))


if __name__ == '__main__':
    print(is_prime(7))

    print(is_prime(8))

    print(is_prime(1))
