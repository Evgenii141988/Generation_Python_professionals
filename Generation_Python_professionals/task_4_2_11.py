import csv

if __name__ == '__main__':
    with open('sales.csv', 'r', encoding='utf-8', newline='') as file:
        rows = csv.DictReader(file, delimiter=';')
        rows_lst = list(filter(lambda x: int(x['old_price']) > int(x['new_price']), rows))
        for row in rows_lst:
            print(row['name'])
