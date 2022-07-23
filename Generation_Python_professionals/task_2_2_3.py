if __name__ == '__main__':
    n, x, y, a, b = (int(i) for i in input().split())
    numbers = list(range(n + 1))
    numbers = numbers[:x] + numbers[x: y + 1][::-1] + numbers[y + 1:]
    numbers = numbers[1:a] + numbers[a: b + 1][::-1] + numbers[b + 1:]
    print(*numbers)
