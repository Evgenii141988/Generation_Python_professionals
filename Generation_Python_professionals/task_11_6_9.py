import sys
from re import fullmatch

if __name__ == '__main__':
    logins = [string.strip() for string in sys.stdin]
    for login in logins:
        print(True if fullmatch(r'_\d+[A-Za-z]*_?', login) else False)

