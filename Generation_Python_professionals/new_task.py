def find_unic_words(file_name: str) -> int:
    with open(file_name, 'r', encoding='utf-8') as file:
        words = set([word.lower() for word in file.read().split()])
        return len(words)


if __name__ == '__main__':
    print(find_unic_words('lorem.txt'))