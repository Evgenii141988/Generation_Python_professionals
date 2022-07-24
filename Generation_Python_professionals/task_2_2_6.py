if __name__ == '__main__':
    n = int(input())
    my_set = set(s for s in input().split(', '))
    for _ in range(n - 1):
        new_set = set(s for s in input().split(', '))
        my_set = my_set & new_set
    if my_set:
        print(*sorted(my_set), sep=', ')
    else:
        print('Сериал снять не удастся')

