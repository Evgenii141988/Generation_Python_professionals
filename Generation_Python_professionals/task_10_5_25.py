def flatten(nested_list):
    for elm in nested_list:
        if type(elm) == int:
            yield elm
        else:
            yield from flatten(elm)


if __name__ == '__main__':
    generator = flatten([[1, 2], [[3]], [[4], 5]])

    print(*generator)

    generator = flatten([1, 2, 3, 4, 5, 6, 7])

    print(*generator)
