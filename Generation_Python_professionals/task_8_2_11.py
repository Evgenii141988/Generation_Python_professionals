def print_digits(number: int):
    print(number % 10)
    if number // 10:
        print_digits(number // 10)


if __name__ == '__main__':
    print_digits(12345)