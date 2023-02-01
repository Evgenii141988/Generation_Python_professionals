from collections import Counter


def shift_letter(letter: str, shift: int) -> str:
    """Функция сдвигает символ letter на shift позиций"""
    n = (ord(letter) - 97 + shift) % 26 + 97
    return chr(n)


if __name__ == '__main__':
    print(shift_letter('z', 5))
    print(shift_letter('w', 28))
    print(shift_letter('w', -26))