from itertools import groupby


def group_anagrams(words: list[str]) -> list[tuple]:
    return (tuple(group) for name, group in groupby(sorted(words, key=lambda x: sorted(x)), key=lambda x: sorted(x)))


if __name__ == '__main__':
    groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])
    print(*groups)

    groups = group_anagrams(['evil', 'father', 'book', 'stepik', 'beegeek'])
    print(*groups)

    groups = group_anagrams(['крона', 'сеточка', 'тесачок', 'лучик', 'стоечка', 'норка', 'чулки'])
    print(*groups)
