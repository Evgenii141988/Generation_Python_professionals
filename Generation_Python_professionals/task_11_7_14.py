import re


def abbreviate(phrase: str) -> str:
    return "".join(re.findall(r'\b[A-Za-z]|\B[A-Z]', phrase)).upper()


if __name__ == '__main__':
    print(abbreviate('javaScript object notation'))
    print(abbreviate('frequently asked questions'))
    print(abbreviate('JS game sec'))
