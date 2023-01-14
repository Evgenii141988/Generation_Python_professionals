if __name__ == '__main__':
    words = input().split()
    new_words = []
    words_lower = []
    for word in words:
        if word.lower() not in words_lower:
            new_words.append(word)
            words_lower.append(word.lower())
    print(' '.join(new_words))
