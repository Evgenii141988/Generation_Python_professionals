from itertools import combinations

if __name__ == '__main__':
    wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
    counter = 0
    for i in range(1, len(wallet) + 1):
        for elm in set(combinations(wallet, r=i)):
            if sum(elm) == 100:
                counter += 1
    print(counter)
