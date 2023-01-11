if __name__ == '__main__':
    a = int(input())
    b = int(input())
    minimum, maximum = (a, b) if a < b else (b, a)
    print(minimum, maximum, sep=' ')
