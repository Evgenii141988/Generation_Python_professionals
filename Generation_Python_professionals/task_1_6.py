from string import ascii_lowercase

if __name__ == '__main__':
    alphabet = {lit: i for i, lit in enumerate(ascii_lowercase, 1)}
    print(alphabet)