def get_combin(n: int, k: int) -> int:
    if k == 0 or k == n:
        return 1
    return get_combin(n - 1, k) + get_combin(n - 1, k - 1)


if __name__ == '__main__':
    print(get_combin(5, 5))
    print(get_combin(5, 2))
