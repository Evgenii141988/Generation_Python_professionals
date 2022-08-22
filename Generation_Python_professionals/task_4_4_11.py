import json
import csv

if __name__ == '__main__':
    with open('playgrounds.csv', 'r', encoding='utf-8') as file:
        rows = csv.DictReader(file, delimiter=';')
        json_obj = {}
        for row in rows:
            # print(row)
            if row['AdmArea'] not in json_obj:
                json_obj[row['AdmArea']] = {row['District']: [row['Address']]}
            else:
                json_obj[row['AdmArea']][row['District']] = json_obj[row['AdmArea']].get(row['District'], []) + [row['Address']]
    with open('addresses.json', 'w', encoding='utf-8') as file:
        json.dump(json_obj, file, indent='   ')