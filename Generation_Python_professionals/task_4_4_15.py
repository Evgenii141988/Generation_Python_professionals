import json

if __name__ == '__main__':
    districts = {}
    names = {}
    with open('food_services.json', 'r', encoding='utf-8') as file:
        data_gen = (elem for elem in json.load(file))
    for data in data_gen:
        district = data['District']
        name = data['OperatingCompany']
        districts[district] = districts.get(district, 0) + 1
        if data['IsNetObject'] == 'да':
            names[name] = names.get(name, 0) + 1
    res_name = max(names, key=lambda x: names[x])
    res_district = max(districts, key=lambda x: districts[x])
    print(f'{res_district}: {districts[res_district]}')
    print(f'{res_name}: {names[res_name]}')
