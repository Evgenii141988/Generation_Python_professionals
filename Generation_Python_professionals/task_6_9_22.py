from collections import ChainMap, Counter

if __name__ == '__main__':
    products = Counter(input().split(','))
    bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
    meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
    sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
    vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
    toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}
    ingredients = ChainMap(bread, meat, sauce, vegetables, toppings)
    max_len_order = len(max(products, key=len))
    max_product_len = 0
    total = 0
    for product in sorted(products):
        string = f'{product}{" " * (max_len_order - len(product))} x {products[product]}'
        print(string)
        max_product_len = len(string) if len(string) > max_product_len else max_product_len
        total += ingredients[product] * products[product]
    result = f'ИТОГ: {total}р'
    print('-' * max((max_product_len, len(result))))
    print(result)


