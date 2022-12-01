from itertools import cycle, count
from string import ascii_uppercase


def alnum_sequence():
    for a, b in zip(cycle(range(1, 27)), cycle(ascii_uppercase)):
        yield a
        yield b


if __name__ == '__main__':
    alnum = alnum_sequence()

    print(*(next(alnum) for _ in range(55)))