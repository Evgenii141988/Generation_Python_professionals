import sys
from collections import Counter

if __name__ == '__main__':
    total = 0
    books = Counter(input().split())
    n = int(input())
    buyers = [tuple(buyer.strip().split()) for buyer in sys.stdin.readlines()]
    for buyer in buyers:
        book, price = buyer
        if books[book] > 0:
            total += int(price)
            books[book] -= 1
    print(total)