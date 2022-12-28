import re


def multiple_split(string: str, delimiters: list[str]) -> list[str]:
    reg = "|".join([re.escape(elm) for elm in delimiters])
    return re.split(fr'{reg}', string)


if __name__ == '__main__':
    print(multiple_split('beegeek-python.stepik', ['.', '-']))
    print(multiple_split('Timur---Arthur+++Dima****Anri', ['---', '+++', '****']))
    print(multiple_split('timur.^[+arthur.^[+dima.^[+anri.^[+roma.^[+ruslan', ['.^[+']))