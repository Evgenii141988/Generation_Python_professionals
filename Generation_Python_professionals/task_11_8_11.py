import re


if __name__ == '__main__':
    string = input()
    print(re.sub(r'\b(\w)(\w)(\w*)\b', r'\2\1\3', string))
