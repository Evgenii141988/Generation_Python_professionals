import sys
import re

if __name__ == '__main__':
    strings = [string.strip() for string in sys.stdin]
    tags = {}
    for string in strings:
        url_match = re.finditer(r'<(\w+)\b.*?>', string)
        for url in url_match:
            key = url.group(1)
            value = re.findall(r'(\b[a-z\-]*)=', url.group())
            tags[key] = tags.get(key, []) + value
    for key in sorted(tags):
        print(f'{key}: {", ".join(sorted(set(tags[key])))}')