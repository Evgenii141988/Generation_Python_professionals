def find_unic_words(file_name: str) -> int:
    words = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        for word in [word.upper() for word in file.read().split()]:
            words[word] = words.get(word, 0) + 1
        return words


if __name__ == '__main__':
    print(find_unic_words('lorem.txt'))