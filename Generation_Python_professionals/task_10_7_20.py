def pairwise(iterable):
    try:
        iterator = iter(iterable)
        a = next(iterator)
        for b in iterator:
            yield a, b
            a, b = b, a
        yield a, None
    except StopIteration:
        return
    return


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    print(*pairwise(numbers))

    iterator = iter('stepik')
    print(*pairwise(iterator))

    print(list(pairwise([])))