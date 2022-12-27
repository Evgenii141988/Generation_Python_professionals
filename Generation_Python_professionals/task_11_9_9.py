import re


if __name__ == '__main__':
    string = input()
    print(*re.split(r'\s*[,.;]\s*', string), sep=' ')