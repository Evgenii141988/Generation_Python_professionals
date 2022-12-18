import re

if __name__ == '__main__':
    string = input()
    reg = r'^(Здравствуйте|Доброе утро|Добрый день|Добрый вечер)'
    print(bool(re.search(reg, string, flags=re.IGNORECASE)))

