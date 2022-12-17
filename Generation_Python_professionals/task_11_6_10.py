import sys
from re import fullmatch

if __name__ == '__main__':
    words = [string.strip() for string in sys.stdin]
    for word in words:
        match1 = fullmatch(r'\b(\w{2,})\1\b', word)
        if match1:
            print(word)