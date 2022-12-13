import re

if __name__ == '__main__':
    string = 'An acle, a Ancle, A antarktida, an Any'


    shablon = r'\b[Aa]n?\b'

    numbers = re.findall(shablon, string)
    for number in numbers:
        print(number)