import json
import csv


if __name__ == '__main__':
    columns = ['name', 'phone']
    with open('students.json', 'r', encoding='utf-8') as file:
        data = sorted([[elem['name'], elem['phone']] for elem in json.load(file) if elem['age'] >= 18 and elem['progress'] >= 75], key=lambda x: x[0])

    with open('data.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerows(data)



