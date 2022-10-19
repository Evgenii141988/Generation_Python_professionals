def to_binary(number: int) -> str:
    if number == 0:
        return '0'
    if number == 1:
        return '1'
    else:
        return to_binary(number // 2) + str(number % 2)


if __name__ == '__main__':
    print(to_binary(15))
    print(to_binary(0))
    print(to_binary(1))
    print(to_binary(2))
    print(to_binary(3))
    print(to_binary(12))
    print(to_binary(5))
