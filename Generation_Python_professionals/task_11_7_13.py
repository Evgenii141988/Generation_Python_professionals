import re

if __name__ == '__main__':
    word = input()
    text = input()
    print(len(re.findall(fr'\b{word[:-3]}ou?r\b', text, flags=re.I)))