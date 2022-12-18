import sys
import re

if __name__ == '__main__':
    strings = (string.strip() for string in sys.stdin)
    print(sum(1 for string in strings if re.search(r'beegeek', string, flags=re.IGNORECASE)))
