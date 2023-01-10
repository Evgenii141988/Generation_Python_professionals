def Set(func):
    global new_func
    new_func = func


def Compute(string):
    return new_func(string)


if __name__ == '__main__':
    print([num for num in map(int, input().split()) if num not in (3, 5, 7, 9)])
