def zip_longest(*args, fill=None):
    max_len = max([len(lst) for lst in args])
    return [elm for elm in zip(*[lst + [fill] * (max_len - len(lst)) for lst in args])]


if __name__ == '__main__':
    print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))
    data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
    print(zip_longest(*data))
    data = [[1, 2, 3, 4, 5], ['one', 'two', 'three', 'four', 'five'], ['I', 'II', 'III', 'IV', 'V']]
    print(zip_longest(*data))
