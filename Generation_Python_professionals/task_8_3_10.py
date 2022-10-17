def get_fast_pow(a: int, n: int) -> int:
    if n == 0:
        return 1
    else:
        if n % 2 != 0:
            return a * get_fast_pow(a, n - 1)
        return get_fast_pow(a * a, n // 2)


if __name__ == '__main__':
    print(get_fast_pow(2, 10))
    print(get_fast_pow(2, 3))
    print(get_fast_pow(5, 2))
    print(get_fast_pow(2, 100))