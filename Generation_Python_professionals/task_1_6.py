

def Set(func):
    global new_func
    new_func = func


def Compute(string):
    return new_func(string)


if __name__ == '__main__':
    Set(len)
    print(Compute('Hello'))  # 5
    print(Compute('129'))  # 3
    Set(max)
    print(Compute('129'))  # 9
