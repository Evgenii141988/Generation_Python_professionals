from itertools import permutations

if __name__ == '__main__':
    string = input()
    for elm in sorted(set(permutations(string))):
        print(''.join(list(elm)))


