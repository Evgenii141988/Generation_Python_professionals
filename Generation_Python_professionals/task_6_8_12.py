from collections import Counter


if __name__ == '__main__':
    words = Counter(input().lower().split())
    n = words.most_common()[-1][1]
    print(*sorted([elem[0] for elem in words.most_common() if elem[1] == n]), sep=', ')