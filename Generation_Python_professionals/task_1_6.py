from collections import Counter


def get_word_indices(strings: list[str]) -> dict[str]:
    result = {}
    for i, string in enumerate(strings):
        for word in (elm.lower() for elm in string.split()):
            result[word] = result.get(word, []) + [i]
    return result


if __name__ == '__main__':
    print(get_word_indices(['This is a string',
                            'test String',
                            'test',
                            'string']))
    print(get_word_indices(['Look at my horse',
                            'my horse',
                            'is amazing']))
    print(get_word_indices([]))
    print(get_word_indices(['Avada Kedavra',
                            'avada kedavra',
                            'AVADA KEDAVRA']))