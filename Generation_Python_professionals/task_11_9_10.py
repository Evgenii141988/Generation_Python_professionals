import re


if __name__ == '__main__':
    string = input()
    print(*re.split(r'\s*(?:\||&|and|or)\s*', string), sep=', ')