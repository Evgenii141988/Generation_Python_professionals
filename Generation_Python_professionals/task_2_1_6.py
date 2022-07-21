def filter_anagrams(word: str, words: list) -> list:
    return [s for s in words if sorted(s) == sorted(word)]


if __name__ == '__main__':
    word = 'abba'
    anagrams = ['aabb', 'abcd', 'bbaa', 'dada']

    print(filter_anagrams(word, anagrams))
    print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))
    print(filter_anagrams('tommarvoloriddle',
                          ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))
    print(filter_anagrams('стекло', []))