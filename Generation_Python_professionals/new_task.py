from typing import Generator


def gen_squares(n: int) -> Generator[int, int, None]:
    for i in range(1, n + 1):
        yield i ** 2


if __name__ == '__main__':
    for i in gen_squares(3):
        print(i)
