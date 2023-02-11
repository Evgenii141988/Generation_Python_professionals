def double_fact(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return double_fact(n - 2) * n


if __name__ == '__main__':
    print(double_fact(7))
