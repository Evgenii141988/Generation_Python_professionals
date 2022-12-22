import sys
import re

if __name__ == '__main__':
    strings = [string.strip() for string in sys.stdin]
    for string in strings:
        url_match = re.finditer(r'<a href=\"(.+)\">(.+)</a>', string)
        for url in url_match:
            print(f'{url.group(1)}, {url.group(2)}')
