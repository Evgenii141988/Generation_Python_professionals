import pprint

if __name__ == '__main__':
    new_set = set()
    for _ in range(int(input())):
        new_set.update(map(int, input().split()))
    print(len(new_set))

