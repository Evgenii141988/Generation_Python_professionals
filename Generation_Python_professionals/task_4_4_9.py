import json

if __name__ == '__main__':
    with open('people.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        full_key = list(max(data, key=len))
    for elem in data:
        for key in full_key:
            elem.setdefault(key, None)
    with open('updated_people.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent='   ')