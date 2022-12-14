import re

if __name__ == '__main__':
    string = 'An acle, a Ancle, A antarktida, an Any'

    shablon = r'\b[Aa]n?\b'
    regex = r'^[MDE]r\.[A-Za-z]+$|^Mr?s\.[A-Za-z]+$'
    reg = '((bee)(geek)+)+'

    numbers = re.findall(shablon, string)
    for number in numbers:
        print(number)

    result = re.findall(regex, 'Mr.Guev')
    for elm in result:
        print(elm)

    new_result = re.findall(reg, 'Correct name is beegeekbeegeek hello beegeek_cyber_school beebeegeekgeekgeekbee')
    for elm in new_result:
        print(elm)