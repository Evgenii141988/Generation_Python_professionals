counter = -1


def calls_num():
    global counter
    counter += 1
    return counter


if __name__ == '__main__':
    print(calls_num())
    print(calls_num())
    print(calls_num())
    print(calls_num())
