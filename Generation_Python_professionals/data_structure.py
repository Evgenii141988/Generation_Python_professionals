if __name__ == '__main__':
    lst_in = list(map(str.strip, input().split()))
    cities = lst_in[:]
    if "Пермь" in cities:
        cities.remove("Пермь")
    print("n")
