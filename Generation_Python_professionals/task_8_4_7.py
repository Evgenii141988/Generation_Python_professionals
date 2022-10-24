def dict_travel(nested_dicts: dict):
    def rec(dicts, string=''):
        results = []
        for k, v in dicts.items():
            if type(v) != dict:
                results.append(string + f'{k}: {v}')
            else:
                string += f'{k}.'
                results.extend(rec(v, string))
                string = '.'.join(string.split('.')[:-2]) + '.' if len(string.split('.')) > 2 else ''
        return results

    res = rec(nested_dicts)
    print(*sorted(res), sep='\n')


def dict_travel1(nestd):
    for k, v in sorted(nestd.items()):
        if type(v) == dict:
            dict_travel({f'{k}.{i}': v[i] for i in v})
        else:
            print(f'{k}: {v}')


if __name__ == '__main__':
    data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

    dict_travel(data)
    # print(dict_travel(data))
    print()

    data = {'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}

    dict_travel(data)
    print()
    # print(dict_travel(data))

    data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}

    dict_travel(data)
    # print(dict_travel(data))
    print()

    data = {'firstname': 'Тимур', 'lastname': 'Гуев', 'birthdate': {'day': 10, 'month': 'October', 'year': 1993},
            'address': {'streetaddress': 'Часовая 25, кв. 127',
                        'city': {'region': 'Московская область', 'type': 'город', 'cityname': 'Москва'},
                        'postalcode': '125315'}}

    dict_travel(data)
