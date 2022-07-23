if __name__ == '__main__':
    n = int(input())
    num_dict = {}
    for i in range(1, n + 1):
        n = sum((int(j) for j in str(i)))
        num_dict[n] = num_dict.get(n, tuple()) + (i, )
    print(len(max((value for value in num_dict.values()), key=len)))
