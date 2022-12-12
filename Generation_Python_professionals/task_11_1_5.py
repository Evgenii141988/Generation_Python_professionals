import re

if __name__ == '__main__':
    string = 'The PAN (or PAN number) is a ten-character long alpha-numeric unique identifier. Example: AAAPZ1234C first number is ABCD EZZPA1234ZaPMQ0000O, check thusEZZPA1234ZAPMQ0000O, '

    shablon = r'[A-Z]{5}\d{4}[A-Z]'

    numbers = re.findall(shablon, string)
    for number in numbers:
        print(number)
