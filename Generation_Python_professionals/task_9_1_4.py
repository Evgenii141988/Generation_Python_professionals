def convert(number: int) -> tuple:
    return bin(number).replace('0b', ''), oct(number).replace('0o', ''), hex(number).replace('0x', '').upper()


def convert1(n):
    return f'{n:b}', f'{n:o}', f'{n:X}'


if __name__ == '__main__':
    print(convert(15))
    print(convert(-24))
