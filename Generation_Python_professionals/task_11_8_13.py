import re


def get_string(math_obj) -> str:
    return math_obj.group(1) + math_obj.group(2)


if __name__ == '__main__':
    string = input()
    n = 1
    while n:
        string, n = re.subn(r'\b(\W*)(\w+)(\W*)\b(\W*)\b\2\b', get_string, string)
        print(string)

    pattern = r'(\b\w+\b)(\W+\1\b)+'

    print(re.sub(pattern, r'\1', input()))