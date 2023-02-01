from collections import Counter


def first_repeated_word(string: str) -> str | bool:
    """Находит первый дубль в строке"""
    words = []
    for word in string.split():
        if word in words:
            return word
        words.append(word)


if __name__ == '__main__':
    print(first_repeated_word('hello hi hello'))
    print(first_repeated_word('hello hi Hello'))
