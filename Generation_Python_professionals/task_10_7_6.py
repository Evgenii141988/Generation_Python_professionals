def filter_names(names: list[str], ignore_char: str, max_names: int):
    new_names = (name for name in names if name[0] not in (ignore_char.lower(), ignore_char.upper()) and name.isalpha())
    for _ in range(max_names):
        try:
            yield next(new_names)
        except StopIteration:
            return


if __name__ == '__main__':
    data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

    print(*filter_names(data, 'D', 3))

    data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

    print(*filter_names(data, 't', 20))

    data = ['Di6ma', 'Ti4mur', 'Ar5thur', 'Anri7620', 'Ar3453ina', '345German', 'Ruslan543', 'Soslanfsdf123',
            'Geo000000r']

    print(*filter_names(data, 'A', 100))
