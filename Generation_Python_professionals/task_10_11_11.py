from itertools import groupby

if __name__ == '__main__':
    words = groupby(sorted(input().split(), key=lambda x: (len(x), x)), key=len)
    for n, group in words:
        print(f"{n} -> {', '.join(list(group))}")