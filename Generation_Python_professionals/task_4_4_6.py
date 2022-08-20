import json
import sys

if __name__ == '__main__':
    data = json.load(sys.stdin)
    for k, v in data.items():
        if type(v) == list:
            print(f'{k}: {", ".join([str(el) for el in v])}')
        else:
            print(f'{k}: {v}')