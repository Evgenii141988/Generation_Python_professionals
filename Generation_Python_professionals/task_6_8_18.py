from collections import Counter


def scrabble(symbols: str, word: str) -> bool:
    return all([Counter(symbols.lower())[key] >= value for key, value in Counter(word.lower()).items()])
    # return Counter(word.lower()) <= Counter(symbols.lower())


if __name__ == '__main__':
    print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))
    print(scrabble('begk', 'beegeek'))
    print(scrabble('beegeek', 'beegeek'))
