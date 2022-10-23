def get_value(nested_dicts: dict, key):
    if key in nested_dicts:
        return nested_dicts[key]
    for k, v in nested_dicts.items():
        if type(v) == dict:
            value = get_value(v, key)
            if value is not None:
                return value


if __name__ == '__main__':
    data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993},
            'address': {'streetAddress': 'Часовая 25, кв. 127',
                        'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'},
                        'postalCode': '125315'}}

    print(get_value(data, 'cityName'))
    print(get_value({'a': 1, 'b': {'c': 5}, 'd': {'e': 10}}, 'c'))
    data = {'first_name': 'Alyson', 'last_name': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}

    print(get_value(data, 'birthday'))