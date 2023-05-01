def solution():
    x = input().split()
    n = 0
    for i in range(1, len(x)):
        if x[i].isalpha() and x[i - 1].isalpha():
            print(x[i - 1], x[i])
            n += 1
    if n == 0:
        print("Мало слов!")


if __name__ == '__main__':
    solution()
