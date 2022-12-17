import sys
from re import search

if __name__ == '__main__':
    strings = [string.strip() for string in sys.stdin]
    print(len([string for string in strings if search(r'(.*bee.*).*\1', string)]))
    print(len([string for string in strings if search(r'\bgeek\b', string)]))