import json
import csv
from collections import Counter


if __name__ == '__main__':
    result = Counter()
    total = 0
    for n in range(1, 5):
        products_dict = Counter()
        with open(f'quarter{n}.csv', encoding='utf-8') as csv_file:
            products = list(csv.reader(csv_file))[1:]
            for product in products:
                products_dict[product[0]] = sum([int(num) for num in product[1:]])
        result += products_dict
    with open('prices.json', encoding='utf-8') as file:
        data = json.load(file)
        for key, value in data.items():
            total += (result[key] * value)
    print(total)

