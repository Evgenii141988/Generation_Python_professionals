from collections import Counter

if __name__ == '__main__':
    words = Counter(input().lower().split())
    max_value = words.most_common()[0][1]
    print(sorted([word for word, value in words.most_common() if value == max_value])[-1])