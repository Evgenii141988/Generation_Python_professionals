def get_num_sum(n: int) -> int:
    if n < 10:
        return n
    else:
        return n % 10 + get_num_sum(n // 10)


if __name__ == '__main__':
    print(get_num_sum(int(input())))
