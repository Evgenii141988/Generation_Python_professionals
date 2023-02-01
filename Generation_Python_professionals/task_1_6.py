from collections import Counter


def shift_letter(letter: str, shift: int) -> str:
    """Функция сдвигает символ letter на shift позиций"""
    n = (ord(letter) - 97 + shift) % 26 + 97
    return chr(n)


def caesar_cipher(string: str, shift: int) -> str:
    """Шифр цезаря"""
    return ''.join([shift_letter(letter, shift) if letter.isalpha() else letter for letter in string])


if __name__ == '__main__':
    print(caesar_cipher('lost in the echo', 27))
    # print(shift_letter('w', 28))
    # print(shift_letter('w', -26))
