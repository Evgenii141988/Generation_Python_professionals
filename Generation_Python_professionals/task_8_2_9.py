def triangle(h):
    if h > 1:
        triangle(h - 1)
    print('*' * h)


if __name__ == '__main__':
    triangle(5)