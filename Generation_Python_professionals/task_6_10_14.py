from collections import ChainMap


def deep_update(chainmap: ChainMap, key, value) -> None:
    if key in chainmap:
        for elem in chainmap.maps:
            if key in elem:
                elem[key] = value
    else:
        chainmap[key] = value


if __name__ == '__main__':
    chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Arthur'}, {'name': 'Timur'})
    deep_update(chainmap, 'name', 'Dima')

    print(chainmap)

    chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
    deep_update(chainmap, 'age', 20)

    print(chainmap)