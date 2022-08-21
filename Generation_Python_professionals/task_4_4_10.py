import json

if __name__ == '__main__':
    with open('countries.json', 'r', encoding='utf-8') as file:
        countries = json.load(file)
        religions = {}
        for country in countries:
            religions[country['religion']] = religions.get(country['religion'], []) + [country['country']]
    with open('religion.json', 'w', encoding='utf-8') as file:
        json.dump(religions, file, indent='   ')