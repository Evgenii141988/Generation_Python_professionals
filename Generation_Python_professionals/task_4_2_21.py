import csv

if __name__ == '__main__':
    min_products = []
    with open('prices.csv', 'r', encoding='utf-8') as file:
        rows = csv.DictReader(file, delimiter=';')
        for row in rows:
            products = rows.fieldnames[1:]
            min_product = min(products, key=lambda x: int(row[x]))
            min_products.append((row['Магазин'], min_product, int(row[min_product])))
    result = min(min_products, key=lambda x: (x[2], x[1], x[0]))
    print(f'{result[1]}: {result[0]}')
