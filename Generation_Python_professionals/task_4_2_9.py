import csv


if __name__ == '__main__':
    with open('grades.csv', encoding='utf-8') as csv_file:
        rows = csv.reader(csv_file, delimiter=';')
        for row in rows:
            print(row)