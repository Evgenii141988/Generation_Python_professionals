def count_strings(*args):
    return len(list(elm for elm in args if isinstance(elm, str)))


if __name__ == '__main__':
    print(count_strings(1, 2, 'hello', [2, 3, 4], True))
    print(count_strings('am', 'world', 'hello', 'is'))
    print(count_strings())
    print(count_strings(True, False))