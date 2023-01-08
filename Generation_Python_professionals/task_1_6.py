def check_int(n: float) -> bool:
    return n == int(n)


if __name__ == '__main__':
    number = int(input())
    count = int(number ** (1 / 2)) + int(number ** (1 / 3)) - int(number ** (1 / 6))
    print(count)
