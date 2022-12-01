from itertools import zip_longest


def roundrobin(*args):
    for elm in zip_longest(*args, fillvalue='python'):
        for i in elm:
            if i != 'python':
                yield i


if __name__ == '__main__':
    print(*roundrobin('abc', 'd', 'ef'))

    numbers = [1, 2, 3]
    letters = iter('beegeek')
    print(*roundrobin(numbers, letters))

    print(list(roundrobin()))

    numbers = iter([1, 2, 3])
    nones = iter([None, None, None, None])

    print(*roundrobin(numbers, nones))