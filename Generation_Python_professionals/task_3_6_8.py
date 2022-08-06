import time


def calculate_it(func, *args):
    start = time.monotonic()
    result = func(*args)
    end = time.monotonic()
    return result, end - start


def func(a, b, c):
    time.sleep(3)
    return a + b + c


if __name__ == '__main__':
    print(calculate_it(func, 1, 2, 3))
