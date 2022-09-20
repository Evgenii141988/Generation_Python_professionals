from collections import Counter

if __name__ == '__main__':
    products = input().split(',')
    products_count = Counter(products)
    for key in sorted(products_count):
        print(f'{key}: {products_count[key]}')