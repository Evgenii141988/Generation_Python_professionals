def get_clock(n, m):
    print(' ' * ((16 - m * 4) // 2) + str(n) * m * 4 + ' ' * ((16 - m * 4) // 2))
    if n < 4:
        get_clock(n + 1, m - 1)
    if n != 4:
        print(' ' * ((16 - m * 4) // 2) + str(n) * m * 4 + ' ' * ((16 - m * 4) // 2))


if __name__ == '__main__':
    get_clock(1, 4)
