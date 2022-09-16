from collections import defaultdict


def flip_dict(dict_of_lists: dict):
    result = defaultdict(list)
    for k, v in dict_of_lists.items():
        for elm in v:
            result[elm].append(k)
    return result


if __name__ == '__main__':
    print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))
