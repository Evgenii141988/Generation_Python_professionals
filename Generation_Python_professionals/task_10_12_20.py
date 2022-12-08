from itertools import product


if __name__ == '__main__':
    n = int(input())
    m = int(input())

    for elm in product(range(n) if n < 11 else '0123456789ABCDEF'[:n], repeat=m):
        print(*elm, sep='', end=' ')