def traffic(n: int):
    if n > 0:
        print('Не парковаться')
        traffic(n - 1)


if __name__ == '__main__':
    traffic(10)
