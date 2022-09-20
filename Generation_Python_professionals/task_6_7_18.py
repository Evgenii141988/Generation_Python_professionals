from collections import Counter


def get_price(product: str) -> int:
    return sum([ord(lit) for lit in product if lit != ' '])


if __name__ == '__main__':
    products = Counter(input().split(','))
    max_len_key = len(max(products, key=lambda x: len(x)))
    for key in sorted(products):
        print(f'{key}{(max_len_key - len(key)) * " "}: {get_price(key)} UC x {products[key]} = {get_price(key) * products[key]} UC')
