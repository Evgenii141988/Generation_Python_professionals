import json

if __name__ == '__main__':
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    # print(data)
    new_data = []
    for elem in data:
        if isinstance(elem, str):
            new_data.append(elem + '!')
        elif type(elem) in (int, float):
            new_data.append(elem + 1)
        elif type(elem) == bool:
            new_data.append(not elem)
        elif isinstance(elem, list):
            new_data.append(elem * 2)
        elif isinstance(elem, dict):
            elem["newkey"] = None
            new_data.append(elem)
    with open('updated_data.json', 'w', encoding='utf-8') as file:
        json.dump(new_data, file)

