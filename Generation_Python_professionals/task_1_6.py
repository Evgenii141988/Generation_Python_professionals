import sys


def fib(n):
    count = 2
    a, b = 1, 1
    while count < n:
        a += b
        a, b = b, a
        count += 1
    return b


if __name__ == '__main__':
    # number = int(input())
    number = 10 ** 5
    print(fib(number) % 1000000007)
    # print(fib(number))
