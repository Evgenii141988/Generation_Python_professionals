from collections import Counter


if __name__ == '__main__':
    words = [word.lower() for word in input().split()]
    print(Counter(words).most_common()[0][0])