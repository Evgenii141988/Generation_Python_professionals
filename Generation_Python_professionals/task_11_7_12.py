import re

if __name__ == '__main__':
    word = input()
    text = input()
    print(len(re.findall(fr'\b{word[:-2]}(se|ze)\b', text, flags=re.I | re.M)))
