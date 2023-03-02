def find_keys(**kwargs):
    return sorted((key for key, value in kwargs.items() if isinstance(value, (list, tuple))), key=str.lower)


if __name__ == '__main__':
    print(find_keys(t=[4, 5], W=[5, 3], A=(3, 2), a={2, 3}, b=[4]))

    print(find_keys(name='Bruce', surname='Wayne'))

    print(find_keys(marks=[4, 5], name='ashle', surname='Brown', age=20, Also=(1, 2)))