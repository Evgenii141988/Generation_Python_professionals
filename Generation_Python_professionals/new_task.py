def find_words(file_name: str) -> dict:
    words = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        for word in [word.upper() for word in file.read().split() if word.upper()[-2:] == 'ЕЯ']:
            words[word] = words.get(word, 0) + 1

    return sorted(words, key=lambda x: (len(x), x))


if __name__ == '__main__':
    print(*find_words('words.txt'), sep='\n')