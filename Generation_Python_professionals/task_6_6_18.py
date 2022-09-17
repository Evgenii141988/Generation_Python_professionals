from collections import OrderedDict

if __name__ == '__main__':
    data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                        'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                        'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
    keys = list(data)
    n = len(keys) // 2
    keys1 = keys[:n]
    keys2 = keys[n:][::-1]
    new_data = OrderedDict()
    for i in range(n):
        new_data[keys1[i]] = data[keys1[i]]
        new_data[keys2[i]] = data[keys2[i]]
    print(new_data)
