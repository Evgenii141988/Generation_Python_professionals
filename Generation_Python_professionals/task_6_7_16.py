from collections import Counter


def count_occurences(word: str, words: str) -> int:
    return Counter(words.lower().split())[word.lower()]


if __name__ == '__main__':
    word = 'python'
    words = 'Python Conferences python training python events'
    print(count_occurences(word, words))
