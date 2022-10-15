def get_count(n: int):
    numbers = []

    def rec_count(n: int):
        if n > 0:
            numbers.append(n % 10)
            rec_count(n // 10)

    rec_count(n)
    return len(numbers)


def get_count_num(n):
    if n < 10:
        return 1
    else:
        return 1 + get_count_num(n // 10)


if __name__ == '__main__':
    number = int(input())
    print(get_count(number))
    print(get_count_num(number))
