from re import search, match
import sys

if __name__ == '__main__':
    numbers = [string.strip() for string in sys.stdin]
    # numbers = ['1 877 2638277', '91-011-23413627']
    reg = r'(?P<country>\d{1,3})([\s-])(?P<city>\d{1,3})\2(?P<number>\d{4,10})'
    for num in numbers:
        match1 = match(reg, num)
        if match:
            print(f'Код страны: {match1.group("country")}, Код города: {match1.group("city")}, Номер: {match1.group("number")}')
