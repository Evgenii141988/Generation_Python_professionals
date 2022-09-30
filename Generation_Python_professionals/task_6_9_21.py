import json
from collections import ChainMap


if __name__ == '__main__':
    total = 0
    with open('zoo.json') as file:
        zoo = ChainMap(*json.load(file))
        for elm in zoo.values():
            total += elm
        print(total)