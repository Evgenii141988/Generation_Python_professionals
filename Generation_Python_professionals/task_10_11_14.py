from itertools import pairwise, groupby


def ranges(numbers: list[int]) -> list[tuple]:
    result = []
    elm = [numbers[0]]
    for i, n in enumerate(numbers[:-1]):
        if numbers[i + 1] - n == 1:
            elm.append(numbers[i + 1])
        else:
            result.append(elm)
            elm = [numbers[i + 1]]
    result.append(elm)
    return [(elm[0], elm[-1]) for elm in result]


def ranges1(numbers):
    result = []
    for _, group in groupby(numbers, key=lambda n: n - numbers.index(n)):
        group = tuple(group)
        group = group[0], group[-1]
        result.append(group)
    return result


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 7, 8, 10]
    # numbers = [1, 3, 5, 7]
    # numbers = [1, 2, 3, 4, 5, 6, 7]

    for group in ranges1(numbers):
        print(group)
