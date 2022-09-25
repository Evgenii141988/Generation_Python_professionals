from collections import Counter


if __name__ == '__main__':
    words_len = Counter([len(word) for word in input().lower().split()])
    for key, value in sorted(words_len.most_common(), key=lambda x: x[1]):
        print(f'Слов длины {key}: {value}')
