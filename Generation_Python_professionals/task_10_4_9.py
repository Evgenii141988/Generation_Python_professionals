class Fibonacci:
    def __init__(self):
        self.first = 0
        self.second = 1
        self.third = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.third = self.first + self.second
        self.first, self.second = self.second, self.third
        return self.first


if __name__ == '__main__':
    fibonacci = Fibonacci()

    print(next(fibonacci))
    print(next(fibonacci))
    print(next(fibonacci))
    print(next(fibonacci))
    print(next(fibonacci))
    print(next(fibonacci))
    print(next(fibonacci))
