import re


def normalize_whitespace(string: str) -> str:
    return re.sub(r' {2,}', r' ', string)


if __name__ == '__main__':
    print(normalize_whitespace('AAAA                A                AAAA'))
    print(normalize_whitespace('Тут нет лишних пробелов'))
    print(normalize_whitespace('Тут   н   е   т     л   и     шних пробелов     '))
