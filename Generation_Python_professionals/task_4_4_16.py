import json

if __name__ == '__main__':
    types = {}
    with open('food_services.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    for elem in data:
        type_obj = elem['TypeObject']
        name = elem['Name']
        seats = elem['SeatsCount']
        types[type_obj] = types.get(type_obj, []) + [(name, seats)]
    keys = sorted(types)
    for elm in keys:
        largest = max(types[elm], key=lambda x: x[1])
        print(f'{elm}: {largest[0]}, {largest[1]}')