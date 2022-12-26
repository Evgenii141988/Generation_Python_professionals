import re


def get_string(math_obj) -> str:
    return int(math_obj.group(1)) * math_obj.group(2)


if __name__ == '__main__':
    string = input()
    while '(' in string:
        string = re.sub(r'(\d+)\((\w+)\)', get_string, string)

    print(string)