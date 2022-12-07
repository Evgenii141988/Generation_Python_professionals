from itertools import combinations_with_replacement

if __name__ == '__main__':
    wallet = [100, 50, 20, 10, 5]
    counter = 0
    for i in range(1, 21):
        for elm in set(combinations_with_replacement(wallet, r=i)):
            if sum(elm) == 100:
                print(elm)
                counter += 1
    print(counter)
