from itertools import pairwise


def max_pair(iterable):
    return max(a + b for a, b in pairwise(iterable))


if __name__ == '__main__':
    print(max_pair([1, 8, 2, 4, 3]))

    iterator = iter([1, 2, 3, 4, 5])
    print(max_pair(iterator))

    iterator = iter([0, 0, 0, 0, 0, 0, 0, 0, 0])

    print(max_pair(iterator))