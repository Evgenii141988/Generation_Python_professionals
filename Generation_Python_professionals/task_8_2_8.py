def triangle(h):
    if h > 0:
        print('*' * h)
        triangle(h - 1)


if __name__ == '__main__':
    triangle(3)