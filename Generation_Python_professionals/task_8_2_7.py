def func():
    n = int(input())
    if n != 0:
        func()
    print(n)


if __name__ == '__main__':
    func()
