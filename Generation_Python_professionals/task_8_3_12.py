def is_power(number: int) -> bool:
    if number == 1:
        return True
    if number % 2 != 0:
        return False
    else:
        return is_power(number // 2)


if __name__ == '__main__':
    print(is_power(512))
    print(is_power(15))
    print(is_power(1))
