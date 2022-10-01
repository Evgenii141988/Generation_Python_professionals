from collections import ChainMap


def get_all_values(chainmap: ChainMap, key) -> set:
    return {elem[key] for elem in chainmap.maps if key in elem}


if __name__ == '__main__':
    chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
    result = get_all_values(chainmap, 'name')

    print(*sorted(result))

    chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
    result = get_all_values(chainmap, 'age')

    print(result)
