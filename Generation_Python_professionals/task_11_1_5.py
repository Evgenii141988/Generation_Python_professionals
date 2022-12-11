import re

if __name__ == '__main__':
    string = input()

    shablon = r'8-\d{3}-\d{4}-\d{4}|7-\d{3}-\d{3}-\d{2}-\d{2}'

    numbers = re.findall(shablon, string)
    for number in numbers:
        print(number)

