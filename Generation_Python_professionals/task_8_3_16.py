def get_number(number: int):
    if number <= 0:
        print(number)
    else:
        print(number)
        get_number(number - 5)
        print(number)


if __name__ == '__main__':
    number = int(input())
    get_number(number)
    get_number(16)
    get_number(10)
    get_number(1)