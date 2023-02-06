from collections import Counter


def replace(text: str, old: str, new: str = "") -> str:
    return text.replace(old, new)


if __name__ == '__main__':
    print(replace('Нет', 'т'))
    print(replace('Bella Ciao', 'a'))
    print(replace('nobody; i myself farewell analysis', 'l', 'z'))
    print(replace('commend me to my kind lord meaning', 'M', 'w'))
