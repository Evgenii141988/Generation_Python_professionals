if __name__ == '__main__':
    numbers = [int(i) for i in input().split()]
    res = set(i for i in numbers if numbers.count(i) > 1)
    print(*sorted(res))