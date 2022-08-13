import csv


def get_index_upper_lit(string: str) -> int:
    for lit in string:
        if lit.isupper():
            return string.find(lit)


if __name__ == '__main__':
    districts = {}
    with open('wifi.csv', 'r', encoding='utf-8') as file:
        rows = csv.DictReader(file, delimiter=';')
        for row in rows:
            districts[row['district']] = districts.get(row['district'], 0) + int(row['number_of_access_points'])
    districts_sort = sorted(districts, key=lambda x: (-districts[x], get_index_upper_lit(x)))
    for key in districts_sort:
        print(f'{key}: {districts[key]}')
