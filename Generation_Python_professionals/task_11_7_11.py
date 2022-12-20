import re

if __name__ == '__main__':
    string = input()
    word = input()
    print(len(re.findall(fr'\b{word}\b', string)))