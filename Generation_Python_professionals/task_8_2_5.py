def get_numbers(n):
    if n <= 100:
        print(n)
        get_numbers(n + 1)


if __name__ == '__main__':
    get_numbers(1)
