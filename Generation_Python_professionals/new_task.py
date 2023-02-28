if __name__ == '__main__':
    litters = input().split()
    new_litters = list(map(lambda x: (x.upper(), x.lower()), litters))
    print(new_litters)
