import sys
from re import search

if __name__ == '__main__':
    strings = (string.strip() for string in sys.stdin)
    counter = 0
    for string in strings:
        if search(r'^(beegeek).*\1$', string):
            counter += 3
        elif search(r'^(beegeek)|(beegeek)$', string):
            counter += 2
        elif search(r'.+beegeek.+', string):
            counter += 1
    print(counter)