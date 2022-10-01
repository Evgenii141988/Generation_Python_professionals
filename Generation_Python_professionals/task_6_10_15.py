from collections import ChainMap


def get_value(chainmap: ChainMap, key, from_left: bool = True):
    if key not in chainmap:
        return None
    chainmap.maps = chainmap.maps if from_left else chainmap.maps[::-1]
    for elem in chainmap.maps:
        if key in elem:
            return elem[key]


if __name__ == '__main__':
    chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

    print(get_value(chainmap, 'name'))

    chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

    print(get_value(chainmap, 'name', False))

    chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

    print(get_value(chainmap, 'age'))