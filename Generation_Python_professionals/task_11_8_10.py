import re
import keyword


def get_keyword(match_obj) -> str:
    string = match_obj.group(0)
    if string.lower() in [word.lower() for word in keyword.kwlist]:
        return '<kw>'
    return string


if __name__ == '__main__':
    string = input()
    print(re.sub(r'\b\w+\b', get_keyword, string))
