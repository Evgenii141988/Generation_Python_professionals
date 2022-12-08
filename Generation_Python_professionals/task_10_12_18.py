from string import ascii_lowercase
from itertools import product


if __name__ == '__main__':
    letters = ascii_lowercase[:8]
    digits = [1, 2, 3, 4, 5, 6, 7, 8]
    print(*(elm[0] + str(elm[1]) for elm in sorted(product(letters, digits))))