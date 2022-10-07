from string import ascii_lowercase, ascii_uppercase


def get_id(names: list, name: str) -> int:
    if type(name) == str and name[0] in ascii_uppercase and all([lit in ascii_lowercase for lit in name[1:]]):
        names.append(name)
        return len(names)
    elif type(name) == str:
        raise ValueError('Имя не является корректным')
    else:
        raise TypeError('Имя не является строкой')


if __name__ == '__main__':
    # names = ['Timur', 'Anri', 'Dima']
    # name = 'Arthur'
    #
    # print(get_id(names, name))
    #
    # names = ['Timur', 'Anri', 'Dima', 'Arthur']
    # name = 'Ruslan1337'
    #
    # try:
    #     print(get_id(names, name))
    # except ValueError as e:
    #     print(e)

    names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
    name = ['E', 'd', 'u', 'a', 'r', 'd']

    try:
        print(get_id(names, name))
    except TypeError as e:
        print(e)
