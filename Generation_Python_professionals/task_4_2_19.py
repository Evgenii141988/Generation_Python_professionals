import csv


def condense_csv(filename: str, id_name: str):
    with open(filename, 'r', encoding='utf-8') as file:
        rows = list(csv.reader(file))
        columns = [id_name]
        data = []
        properties = [rows[0][0]]
    for row in rows:
        if row[0] not in properties:
            data.append(properties)
            properties = [row[0]]
        if row[1] not in columns:
            columns.append(row[1])
        properties.append(row[2])
    data.append(properties)
    with open('condensed.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerows(data)


if __name__ == '__main__':
    condense_csv('my_test_file.csv', 'object')
